# -*- coding: utf-8 -*-
"""
Created on Sun Apr 23 19:58:44 2023

@author: DELL
"""
import cv2
import numpy as np

from osgeo import gdal

def imread(image_path, xoff=0, yoff=0, data_width=0, data_height=0):
    '''
    Parameters
    ----------
    tif_path : string
        读取图像的路径.
    xoff : int
        读取数据的x方向偏移. The default is 0.
    yoff : int
        读取数据的y方向偏移. The default is 0.
    data_width : int
        读取数据的宽. The default is 0.
    data_height : int
        读取数据的高. The default is 0.

    Returns
    -------
    data : numpy
        图像像素矩阵.
    geotrans : tuple
        仿射变换矩阵六参数.
    proj : string
        坐标参考.
    '''
    dataset = gdal.Open(image_path)
    #  栅格矩阵的列数
    width = dataset.RasterXSize
    #  栅格矩阵的行数
    height = dataset.RasterYSize
    #  获取数据
    if (data_width == 0 and data_height == 0):
        data_width = width
        data_height = height
    data = dataset.ReadAsArray(xoff, yoff, data_width, data_height)
    #  获取仿射矩阵信息
    geotrans = dataset.GetGeoTransform()
    #  获取投影信息
    proj = dataset.GetProjection()
    return data, geotrans, proj

def imwrite(path, data, geotrans=(0,0,0,0,0,0), proj=""):
    '''
    Parameters
    ----------
    im_data : numpy
        图像像素矩阵.
    im_geotrans : tuple
        仿射变换矩阵.
    im_proj : string
        坐标参考.
    path : string
        图像保存路径.

    Returns
    -------
    None.

    '''
    if 'int8' in data.dtype.name:
        datatype = gdal.GDT_Byte
    elif 'int16' in data.dtype.name:
        datatype = gdal.GDT_UInt16
    else:
        datatype = gdal.GDT_Float32
    if len(data.shape) == 3:
        im_bands, im_height, im_width = data.shape
    elif len(data.shape) == 2:
        data = np.array([data])
        im_bands, im_height, im_width = data.shape

    # 创建文件
    driver = gdal.GetDriverByName("GTiff")
    dataset = driver.Create(path, int(im_width), int(im_height), int(im_bands), datatype)
    if (dataset != None):
        dataset.SetGeoTransform(geotrans)  # 写入仿射变换参数
        dataset.SetProjection(proj)  # 写入投影
    for i in range(im_bands):
        dataset.GetRasterBand(i + 1).WriteArray(data[i])
    del dataset
    
def cv_imwrite(save_path, image):
    """
    功能相当于cv2.imwrite
    :param filepath: 保存的图片地址（包含名字），如 "C:\\已处理图片\\宝马.jpg"
    :param img: 要保存的图片，三维数组
    """
    cv_imw = cv2.imencode('.png',image)[1].tofile(save_path)
    return cv_imw