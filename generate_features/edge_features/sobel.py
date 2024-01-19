# -*- coding: utf-8 -*-
"""
Created on Wed May 10 22:16:36 2023

@author: DELL
"""

import os
import cv2
import sys
import numpy as np

from skimage.filters import sobel
from skimage.exposure import rescale_intensity

sys.path.append("..")
from image_io.image_io import imwrite

def cal_sobel(image_gray, image_name, save_dir=""):
    
    image_name_without_suffix = ".".join(image_name.split(".")[:-1])
    
    image_sobel = sobel(image_gray)
    
    image_sobel_norm = rescale_intensity(image_sobel, out_range=(0,1))
    
    save_path = os.path.join(save_dir+"/Sobel", image_name)
    imwrite(save_path, image_sobel_norm)