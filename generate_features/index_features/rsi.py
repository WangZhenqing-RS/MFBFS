# -*- coding: utf-8 -*-
"""
Created on Thu May 11 09:39:02 2023

@author: DELL
"""
import os
import cv2
import sys
import numpy as np

from skimage.morphology import square, white_tophat
from skimage.transform import rotate
from skimage.exposure import rescale_intensity
from skimage.color import lab2lch, rgb2lab, rgb2ycbcr

sys.path.append("..")
from image_io.image_io import imwrite

def cal_ndvi(image_nir, image_r, image_name, save_dir=""):
    
    image_nir = image_nir.astype(np.float32)
    image_r = image_r.astype(np.float32)
    
    image_name_without_suffix = ".".join(image_name.split(".")[:-1])
    
    ndvi = (image_nir - image_r + 0.0001) / (image_nir + image_r + 0.0001)
    
    ndvi_norm = (ndvi - (-1))/(1 - (-1))

    save_path = os.path.join(save_dir+"/NDVI", image_name)
    imwrite(save_path, ndvi_norm)
    
def cal_ndwi(image_g, image_nir, image_name, save_dir=""):
    
    image_g = image_g.astype(np.float32)
    image_nir = image_nir.astype(np.float32)
    
    image_name_without_suffix = ".".join(image_name.split(".")[:-1])
    
    ndwi = (image_g - image_nir + 0.0001) / (image_g + image_nir + 0.0001)

    #[-1,1] -> [0,1]
    ndwi_norm = (ndwi - (-1))/(1 - (-1))

    save_path = os.path.join(save_dir+"/NDWI", image_name)
    imwrite(save_path, ndwi_norm)
    
def cal_si(image_bgr, image_name, save_dir=""):
    
    image_name_without_suffix = ".".join(image_name.split(".")[:-1])
    
    image_rgb = cv2.cvtColor(image_bgr,cv2.COLOR_BGR2RGB)
    # 从 RGB 模型到 CIELAB 模型的图像转换，以便从强度信息中分离颜色
    image_lab = rgb2lab(image_rgb)
    
    # 从 CIELAB 颜色空间转换为其极坐标表示 CIELCh，因此我们可以使用色调通道来利用阴影具有较大色调值的事实
    image_lch = np.float32(lab2lch(image_lab))
    
    # 平滑L和h通道，旨在减少图像噪声
    l = cv2.medianBlur(image_lch[:, :, 0], ksize=5)
    h = cv2.medianBlur(image_lch[:, :, 2], ksize=5)
    
    # 改进的光谱比SR计算，使用 CIELCh 而不是 HSI 色彩空间
    l_norm = rescale_intensity(l, out_range = (0, 1))
    h_norm = rescale_intensity(h, out_range = (0, 1))
    specthem_ratio = (h_norm + 1) / (l_norm + 1)
    
    specthem_ratio_norm = rescale_intensity(specthem_ratio, out_range=(0,1))

    save_path = os.path.join(save_dir+"/SI", image_name)
    imwrite(save_path, specthem_ratio_norm)
    
    
def cal_mbi(image_cwh, image_name, save_dir="", s_min=3, s_max=20, delta_s=1):
    
    image_name_without_suffix = ".".join(image_name.split(".")[:-1])
    
    #  多光谱带的最大值对应于具有高反射率的特征->取光谱带最大值作为后续计算数据
    gray = np.max(image_cwh, 0)
    #  为消除白帽边缘效应，进行边缘补零
    gray = np.pad(gray, ((s_min, s_min), (s_min, s_min)), 'constant', constant_values=(0, 0))
    #  形态学剖面集合
    mp_mbi_list = []
    #  差分形态学剖面dmp集合
    dmp_mbi_list = []
    
    #  计算形态学剖面
    for i in range(s_min, s_max + 1, 2 * delta_s):
        # print("s = ", i)
        #  大小为i×i的单位矩阵
        SE_intermediate = square(i)
        #  只保留中间一行为1,其他设置为0
        SE_intermediate[ : int((i - 1) / 2), :] = 0
        SE_intermediate[int(((i - 1) / 2) + 1) : , :] = 0
        
        #  SE_intermediate表示结构元素，用于设定局部区域的形状和大小
        #  旋转0 45 90 135°
        for angle in range(0, 180, 45):
            SE_intermediate = rotate(SE_intermediate, angle, order = 0, preserve_range = True).astype('uint8')
            #  多角度形态学白帽重构
            mp_mbi = white_tophat(gray, selem = SE_intermediate)
            mp_mbi_list.append(mp_mbi)
            
    #  计算差分形态学剖面dmp
    for j in range(4, len(mp_mbi_list), 1):
        #  差的绝对值
        dmp_mbi = np.absolute(mp_mbi_list[j] - mp_mbi_list[j - 4])
        dmp_mbi_list.append(dmp_mbi)
    
    #  计算mbi
    mbi = np.sum(dmp_mbi_list, axis = 0) / (4 * (((s_max - s_min) / delta_s) + 1))
    #  去除多余边缘结果
    mbi = mbi[s_min : mbi.shape[0] - s_min, s_min : mbi.shape[1] - s_min]
    
    mbi_norm = rescale_intensity(mbi, out_range=(0,1))
    
    save_path = os.path.join(save_dir+"/MBI", image_name)
    imwrite(save_path, mbi_norm)
    