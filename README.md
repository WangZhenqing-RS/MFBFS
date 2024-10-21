# MFBFS：高分辨率多光谱遥感影像细粒度建筑物特征集

## 1.特征生成代码已上传

详见generate_features文件夹。

## 2.特征可视化展示

### 2.1.光谱特征

![可见光影像](https://github.com/WangZhenqing-RS/MFBFS/blob/main/sample_data/94_rgb.png) | ![蓝波段光谱特征](https://github.com/WangZhenqing-RS/MFBFS/blob/main/sample_data/94_b.png) | ![绿波段光谱特征](https://github.com/WangZhenqing-RS/MFBFS/blob/main/sample_data/94_g.png) | ![红波段光谱特征](https://github.com/WangZhenqing-RS/MFBFS/blob/main/sample_data/94_r.png) | ![近红波段光谱特征](https://github.com/WangZhenqing-RS/MFBFS/blob/main/sample_data/94_nir.png)
:-------------------------:|:-------------------------:|:-------------------------:|:-------------------------:|:-------------------------:
*可见光影像* | *蓝波段光谱特征* | *绿波段光谱特征* | *红波段光谱特征* | *近红波段光谱特征*

光谱特征数据下载链接：[百度网盘](https://pan.baidu.com/s/1U2F-md4R3I3Rrcz3SWxk-g?pwd=2024)

### 2.2.纹理特征

![可见光影像](https://github.com/WangZhenqing-RS/MFBFS/blob/main/sample_data/94_rgb.png) | ![对比度](https://github.com/WangZhenqing-RS/MFBFS/blob/main/sample_data/94_contrast_mean.png) | ![相异性](https://github.com/WangZhenqing-RS/MFBFS/blob/main/sample_data/94_dissimilarity_mean.png) | ![同质度](https://github.com/WangZhenqing-RS/MFBFS/blob/main/sample_data/94_homogeneity_mean.png) | ![相关性](https://github.com/WangZhenqing-RS/MFBFS/blob/main/sample_data/94_correlation_mean.png) | ![角二阶矩](https://github.com/WangZhenqing-RS/MFBFS/blob/main/sample_data/94_asm_mean.png) | ![局部二值模式](https://github.com/WangZhenqing-RS/MFBFS/blob/main/sample_data/94_lbp.png) | ![方向梯度直方图](https://github.com/WangZhenqing-RS/MFBFS/blob/main/sample_data/94_hog.png)
:-------------------------:|:-------------------------:|:-------------------------:|:-------------------------:|:-------------------------:|:-------------------------:|:-------------------------:|:-------------------------:
*可见光* | *对比度* | *相异性* | *同质度* | *相关性* | *二阶矩* | *二值模* | *梯度图*

纹理特征数据下载链接：[百度网盘](https://pan.baidu.com/s/1K938L0U78eWlRX5QwKP6og?pwd=2024)

### 2.3.边缘特征

![可见光影像](https://github.com/WangZhenqing-RS/MFBFS/blob/main/sample_data/94_rgb.png) | ![Sobel边缘特征](https://github.com/WangZhenqing-RS/MFBFS/blob/main/sample_data/94_sobel.png) | ![Canny边缘特征](https://github.com/WangZhenqing-RS/MFBFS/blob/main/sample_data/94_canny.png)
:-------------------------:|:-------------------------:|:-------------------------:
*可见光影像* | *Sobel边缘特征* | *Canny边缘特征*

边缘特征数据下载链接：[百度网盘](https://pan.baidu.com/s/1ox7HoaCea9QQf19wrhMbPQ?pwd=2024)

### 2.4.指数特征

![可见光影像](https://github.com/WangZhenqing-RS/MFBFS/blob/main/sample_data/94_rgb.png) | ![建筑物指数特征](https://github.com/WangZhenqing-RS/MFBFS/blob/main/sample_data/94_mbi.png) | ![阴影特征](https://github.com/WangZhenqing-RS/MFBFS/blob/main/sample_data/94_si.png) | ![归一化植被指数特征](https://github.com/WangZhenqing-RS/MFBFS/blob/main/sample_data/94_ndvi.png) | ![归一化水体指数特征](https://github.com/WangZhenqing-RS/MFBFS/blob/main/sample_data/94_ndwi.png)
:-------------------------:|:-------------------------:|:-------------------------:|:-------------------------:|:-------------------------:
*可见光影像* | *建筑物指数特征* | *阴影特征* | *归一化植被指数特征* | *归一化水体指数特征*

指数特征数据下载链接：[百度网盘](https://pan.baidu.com/s/18-AA8P-cPhbShEs_ObiqTA?pwd=2024)

## 3.地面真实值可视化展示

![可见光影像1](https://github.com/WangZhenqing-RS/MFBFS/blob/main/sample_data/94_rgb.png) | ![可见光影像2](https://github.com/WangZhenqing-RS/MFBFS/blob/main/sample_data/577_rgb.png) | ![可见光影像3](https://github.com/WangZhenqing-RS/MFBFS/blob/main/sample_data/937_rgb.png)
:-------------------------:|:-------------------------:|:-------------------------:
![可见光影像1](https://github.com/WangZhenqing-RS/MFBFS/blob/main/sample_data/94_label.png) | ![可见光影像2](https://github.com/WangZhenqing-RS/MFBFS/blob/main/sample_data/577_label.png) | ![可见光影像3](https://github.com/WangZhenqing-RS/MFBFS/blob/main/sample_data/937_label.png)

注：红色代表钢及钢筋混凝土结构建筑物；绿色代表砌体结构建筑物；蓝色代表砖石及其他结构建筑物

地面真实值数据下载链接：[百度网盘](https://pan.baidu.com/s/1JVoNBi_5jFVI4jAUciJu1A?pwd=2024)

## 4.引用

王振庆，周艺，王福涛，王世新，高郭瑞，朱金峰，王平，胡凯龙.MFBFS：高分辨率多光谱遥感影像细粒度建筑物特征集.遥感学报，XX（XX）： 1-12 DOI: 10.11834/jrs.20243526.
WANG Zhenqing，ZHOU Yi，WANG Futao，WANG Shixin，GAO Guorui，ZHU Jinfeng，WANG Ping，HU Kailong. MFBFS： a fine-grained building feature set for high-resolution multispectral remote sensing images. National Remote Sensing Bulletin， XX（XX）：1-12 DOI: 10.11834/jrs.20243526.
