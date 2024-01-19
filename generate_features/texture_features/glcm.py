# -*- coding: utf-8 -*-
"""
Created on Sat May 13 11:08:39 2023

@author: DELL
"""
import os
import cv2
import sys
import tqdm
import numpy as np

from skimage.exposure import rescale_intensity
from skimage.feature import greycomatrix, greycoprops

sys.path.append("..")
from image_io.image_io import imwrite

def cal_glcm(image_gray, image_name, grey_levels=32, slide_window=7, save_dir=""):
    
    image_name_without_suffix = ".".join(image_name.split(".")[:-1])
    
    image_h, image_w = image_gray.shape
    
    # grey_levels = 32
    # slide_window = 7
    
    expand_size = int(slide_window/2)
    
    # 对比度、相异性、同质性、相关性、角二阶矩
    contrast, dissimilarity, homogeneity, correlation, asm = [], [], [], [], []
    
    # 压缩灰度范围：256 -> nbit
    bins = np.linspace(0, 256, grey_levels + 1)
    image = np.digitize(image_gray, bins) - 1
    
    image_tile = cv2.copyMakeBorder(image, 
                                    expand_size,
                                    expand_size,
                                    expand_size,
                                    expand_size,
                                    cv2.BORDER_REPLICATE
                                    )
    
    # for i in tqdm.tqdm(range(image_h)):
    for i in range(image_h):
        contrast_col, dissimilarity_col, homogeneity_col, correlation_col, asm_col = [], [], [], [], []
        for j in range(image_w):
            image_window = image_tile[i:i+slide_window, j:j+slide_window]
            glcm = greycomatrix(image_window, 
                                [2], # 像素对距离偏移list
                                [0, np.pi / 4, np.pi / 2, np.pi * 3 / 4], # 以弧度为单位的像素对角度list
                                grey_levels, # 灰度等级
                                )
            
            contrast_col.append(greycoprops(glcm, 'contrast'))
            dissimilarity_col.append(greycoprops(glcm, 'dissimilarity'))
            homogeneity_col.append(greycoprops(glcm, 'homogeneity'))
            correlation_col.append(greycoprops(glcm, 'correlation'))
            asm_col.append(greycoprops(glcm, 'ASM'))
            
        contrast.append(contrast_col)
        dissimilarity.append(dissimilarity_col)
        homogeneity.append(homogeneity_col)
        correlation.append(correlation_col)
        asm.append(asm_col)
        
    contrast = np.array(contrast)
    # 删除维度为1的维度
    contrast = contrast.squeeze()
    # 四个方向的均值
    contrast_mean = np.mean(contrast, -1)
    
    contrast_mean_norm = rescale_intensity(contrast_mean, out_range=(0,1))
    save_path = os.path.join(save_dir+"/Contrast", image_name)
    imwrite(save_path, contrast_mean_norm)
    
    
    dissimilarity = np.array(dissimilarity)
    # 删除维度为1的维度
    dissimilarity = dissimilarity.squeeze()
    # 四个方向的均值
    dissimilarity_mean = np.mean(dissimilarity, -1)
    
    dissimilarity_mean_norm = rescale_intensity(dissimilarity_mean, out_range=(0,1))

    save_path = os.path.join(save_dir+"/Dissimilarity", image_name)
    imwrite(save_path, dissimilarity_mean_norm)
    
    
    homogeneity = np.array(homogeneity)
    # 删除维度为1的维度
    homogeneity = homogeneity.squeeze()
    # 四个方向的均值
    homogeneity_mean = np.mean(homogeneity, -1)
    
    homogeneity_mean_norm = rescale_intensity(homogeneity_mean, out_range=(0,1))

    save_path = os.path.join(save_dir+"/Homogeneity", image_name)
    imwrite(save_path, homogeneity_mean_norm)
    
    
    correlation = np.array(correlation)
    # 删除维度为1的维度
    correlation = correlation.squeeze()
    # 四个方向的均值
    correlation_mean = np.mean(correlation, -1)
    
    correlation_mean_norm = rescale_intensity(correlation_mean, out_range=(0,1))

    save_path = os.path.join(save_dir+"/Correlation", image_name)
    imwrite(save_path, correlation_mean_norm)
    
    
    asm = np.array(asm)
    # 删除维度为1的维度
    asm = asm.squeeze()
    # 四个方向的均值
    asm_mean = np.mean(asm, -1)
    
    asm_mean_norm = rescale_intensity(asm_mean, out_range=(0,1))

    save_path = os.path.join(save_dir+"/ASM", image_name)
    imwrite(save_path, asm_mean_norm)
    
    
