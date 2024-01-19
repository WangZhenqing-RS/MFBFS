# -*- coding: utf-8 -*-
"""
Created on Wed May 10 21:27:52 2023

@author: DELL
"""
import os
import cv2
import sys
import numpy as np

from skimage.feature import hog
from skimage.exposure import rescale_intensity

sys.path.append("..")
from image_io.image_io import imwrite

def cal_hog(image_gray, image_name, save_dir=""):
    
    image_name_without_suffix = ".".join(image_name.split(".")[:-1])
    
    _, hog_image = hog(image_gray, orientations=9, pixels_per_cell=(8, 8), 
                       cells_per_block=(8, 8), block_norm='L2-Hys', visualize=True)
    hog_image_norm = rescale_intensity(hog_image, out_range=(0,1))

    save_path = os.path.join(save_dir+"/HOG", image_name)
    imwrite(save_path, hog_image_norm)