#不同边缘检测算子对比

import cv2
import numpy as np
import matplotlib.pyplot as plt


#以灰度图的方式读入图像
img = cv2.imread("img/lena.jpg", 0)

#sobel
x = cv2.Sobel(img,cv2.CV_16S,1,0)
y = cv2.Sobel(img,cv2.CV_16S,0,1)
absX = cv2.convertScaleAbs(x) # 转回uint8
absY = cv2.convertScaleAbs(y)
sobel = cv2.addWeighted(absX,0.5,absY,0.5,0)


#Canny
img = cv2.GaussianBlur(img,(3,3),0) #用高斯平滑处理原图像降噪。
canny = cv2.Canny(img, 65, 200) #最大最小阈值

#拉普拉斯边缘检测
lap = cv2.Laplacian(img,cv2.CV_64F)#拉普拉斯边缘检测
lap = np.uint8(np.absolute(lap))##对lap去绝对值


#显示图像
plt.rcParams['font.sans-serif'] = ['SimHei']
title = ['原图', 'Sobel算子', 'Laplacian算子','Canny算子']
image = [img, sobel, lap,canny]
for i in range(4):
    plt.subplot(2, 2, i+1)
    plt.title(title[i])
    plt.imshow(image[i], 'gray')
    plt.xticks([])
    plt.yticks([])
plt.tight_layout()
plt.show()