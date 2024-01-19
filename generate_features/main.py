# -*- coding: utf-8 -*-
"""
Created on Wed May 10 19:58:15 2023

@author: DELL
"""
import os
import cv2
import glob
import tqdm_pathos
import numpy as np

from multiprocessing.pool import Pool

from index_features.rsi import cal_ndvi, cal_ndwi, cal_si, cal_mbi
from texture_features.lbp import cal_lbp
from texture_features.hog import cal_hog
from texture_features.glcm import cal_glcm
from edge_features.sobel import cal_sobel
from edge_features.canny import cal_canny
from image_io.image_io import imread, imwrite

def cal_features(image_path):
    
    feature_save_dir = "../features"
    image_name = os.path.basename(image_path)
    image_dir = os.path.dirname(image_path)
    
    image_cwh, geotrans, proj = imread(image_path)
    image_b, image_g, image_r, image_nir = image_cwh[0], image_cwh[1], image_cwh[2], image_cwh[3]
    
    # (c,w,h) -> (w,h,c)
    image_whc = image_cwh.transpose((1,2,0))
    # bgrnir -> rgb
    image_bgr = image_whc[:,:,:3]
    # 若图像最大值大于255,将其拉伸到[0,255]
    if image_bgr.max()>255:
        image_bgr = np.uint8(image_bgr/image_bgr.max()*255.0)
    # imwrite(image_path.replace(".tif", "_rgb.png"), image_bgr)
    
    image_gray = cv2.cvtColor(image_bgr, cv2.COLOR_BGR2GRAY)
    
    # 计算光谱特征
    image_b_norm = image_b / 255.0
    imwrite(feature_save_dir+"/Blue/"+image_name, image_b_norm)
    image_g_norm = image_g / 255.0
    imwrite(feature_save_dir+"/Green/"+image_name, image_g_norm)
    image_r_norm = image_r / 255.0
    imwrite(feature_save_dir+"/Red/"+image_name, image_r_norm)
    image_b_norm = image_b / 255.0
    imwrite(feature_save_dir+"/NIR/"+image_name, image_b_norm)
    
    # 计算纹理特征
    print(f"{image_name}正在计算纹理特征")
    cal_glcm(image_gray, image_name, grey_levels=8, slide_window=5, save_dir=feature_save_dir)
    print("glcm calculated.")
    cal_lbp(image_gray, image_name, save_dir=feature_save_dir)
    print("lbp calculated.")
    cal_hog(image_gray, image_name, save_dir=feature_save_dir)
    print("hog calculated.")
    
    # 计算边缘特征
    cal_sobel(image_gray, image_name, save_dir=feature_save_dir)
    print("sobel calculated.")
    cal_canny(image_gray, image_name, save_dir=feature_save_dir)
    print("canny calculated.")
    
    # 计算指数特征
    cal_mbi(image_cwh, image_name, save_dir=feature_save_dir)
    print("mbi calculated.")
    cal_si(image_bgr, image_name, save_dir=feature_save_dir)
    print("si calculated.")
    cal_ndvi(image_nir, image_r, image_name, save_dir=feature_save_dir)
    print("ndvi calculated.")
    cal_ndwi(image_g, image_nir, image_name, save_dir=feature_save_dir)
    print("ndwi calculated.")
    
if __name__ == '__main__':
    
    '''
    单进程运行单个图像
    '''
    # image_path = "../data/94.tif"
    # cal_features(image_path)
    
    
    '''
    多进程运行多个图像
    '''
    image_paths = glob.glob(r"E:\WangZhenQing\建筑物特征集\songbei_images/*.tif")
    # tqdm_pathos.map(cal_features, image_paths, n_cpus=os.cpu_count())
    tqdm_pathos.map(cal_features, image_paths, n_cpus=8)
    
    
    
    