
#图片填充

import cv2
import os
import numpy as np
from PIL import Image, ImageDraw
from PIL import ImageFile
ImageFile.LOAD_TRUNCATED_IMAGES = True
Image.MAX_IMAGE_PIXELS = None



#img = cv2.imread('image/opened2.png', 0)
img=Image.open('image/samall3.png')
img=np.asarray(img)

#img = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)#将图像转化为灰度图像
mask = np.zeros_like(img)
print(np.shape(img))

# 先利用二值化去除图片噪声
ret, img = cv2.threshold(img, 127, 255, cv2.THRESH_BINARY)

contours, _ = cv2.findContours(img, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)
n = len(contours)  # 轮廓的个数
print(n)
cv_contours = []
for contour in contours:
    area = cv2.contourArea(contour)
    if area <= 10000:    #面积小于多少时填充
        cv_contours.append(contour)

    else:
        continue

cv2.fillPoly(img, cv_contours, (0, 0,0))
cv2.imwrite('image/samall4.png', img)

