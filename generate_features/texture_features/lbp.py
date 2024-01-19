# -*- coding: utf-8 -*-
"""
Created on Wed May 10 20:42:02 2023

@author: DELL
# https://blog.csdn.net/matrix_space/article/details/50481641
"""

import os
import cv2
import sys
import numpy as np

from skimage.exposure import rescale_intensity
from skimage.feature import local_binary_pattern

sys.path.append("..")
from image_io.image_io import imwrite

def cal_lbp(image_gray, image_name, save_dir=""):
    
    image_name_without_suffix = ".".join(image_name.split(".")[:-1])
    
    # for radius in range(1,6):
    radius = 3
    # radius为计算LBP选取的区域的半径
    # n_points为区域内像素点的个数
    n_points = 8 * radius
    lbp = local_binary_pattern(image_gray, n_points, radius, method='uniform')
    
    lbp_norm = rescale_intensity(lbp, out_range=(0,1))

    save_path = os.path.join(save_dir+"/LBP", image_name)
    imwrite(save_path, lbp_norm)