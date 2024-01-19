# -*- coding: utf-8 -*-
"""
Created on Tue Oct 17 10:32:26 2023

@author: 126243
"""
import os
import cv2
import sys
import numpy as np
import matplotlib.pyplot as plt

from skimage.exposure import rescale_intensity

sys.path.append("..")
from image_io.image_io import imwrite

def cal_canny(image_gray, image_name, save_dir=""):
    image_name_without_suffix = ".".join(image_name.split(".")[:-1])
    # 高斯滤波
    kernel_size = 3
    sigma = 1.4
    grey_blur = cv2.GaussianBlur(image_gray, (kernel_size, kernel_size), sigma)
    
    # 计算梯度和方向
    sobel_x = cv2.Sobel(grey_blur, cv2.CV_64F, 1, 0, ksize=3)
    sobel_y = cv2.Sobel(grey_blur, cv2.CV_64F, 0, 1, ksize=3)
    grad_mag = np.sqrt(sobel_x ** 2 + sobel_y ** 2)
    grad_dir = np.arctan2(sobel_y, sobel_x)
    
    # 非极大值抑制
    grad_mag_max = np.zeros(grad_mag.shape)
    for i in range(1, grad_mag.shape[0] - 1):
        for j in range(1, grad_mag.shape[1] - 1):
            # 如果角度小于0，使其加上一个pi,量化至四个方向
            if grad_dir[i, j] < 0:
                grad_dir[i, j] += np.pi
            if np.pi / 8 <= grad_dir[i, j] < 3 * np.pi / 8:
                if grad_mag[i, j] > grad_mag[i - 1, j - 1] and grad_mag[i, j] > grad_mag[i + 1, j + 1]:
                    grad_mag_max[i, j] = grad_mag[i, j]
            elif 3 * np.pi / 8 <= grad_dir[i, j] < 5 * np.pi / 8:
                if grad_mag[i, j] > grad_mag[i - 1, j] and grad_mag[i, j] > grad_mag[i + 1, j]:
                    grad_mag_max[i, j] = grad_mag[i, j]
            elif 5 * np.pi / 8 <= grad_dir[i, j] < 7 * np.pi / 8:
                if grad_mag[i, j] > grad_mag[i - 1, j + 1] and grad_mag[i, j] > grad_mag[i + 1, j - 1]:
                    grad_mag_max[i, j] = grad_mag[i, j]
            else:
                if grad_mag[i, j] > grad_mag[i, j - 1] and grad_mag[i, j] > grad_mag[i, j + 1]:
                    grad_mag_max[i, j] = grad_mag[i, j]
                    
    
    image_sobel_norm = rescale_intensity(grad_mag_max, out_range=(0,1))
    
    save_path = os.path.join(save_dir+"/Canny", image_name)
    imwrite(save_path, image_sobel_norm)

