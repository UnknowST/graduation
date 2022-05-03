# 利用Canny算子提取海岸线

import cv2
import numpy as np
from PIL import Image, ImageDraw
from PIL import ImageFile

ImageFile.LOAD_TRUNCATED_IMAGES = True
Image.MAX_IMAGE_PIXELS = None

import datetime

start =datetime.datetime.now()
# 载入提取MNDWI后的图片
img = Image.open('img/mndwi-0.24687930.jpg')

# 转为numpy 数组
img = np.asarray(img)

# 图像转为灰度图
#img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)


# 卷积核
kernel = cv2.getStructuringElement(cv2.MORPH_RECT, (7, 7))
# 开运算
opened = cv2.morphologyEx(img, cv2.MORPH_OPEN, kernel, iterations=17)



cv2.imwrite('img/opened1.png', opened)

opened = cv2.resize(opened, (0, 0), fx=0.1, fy=0.1, interpolation=cv2.INTER_AREA)

cv2.imwrite('img/opened2.png', opened)

end = datetime.datetime.now()
print ( 'Running time: %s Seconds' %(end-start).seconds)
img=0

# 填充图像
def filling(image, size, num):
    mask = np.zeros_like(image)
    print(np.shape(image))
    # 先利用二值化去除图片噪声
    ret, img = cv2.threshold(image, 127, 255, cv2.THRESH_BINARY)
    contours, _ = cv2.findContours(img, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)
    n = len(contours)  # 轮廓的个数
    print(n)
    cv_contours = []
    for contour in contours:
        area = cv2.contourArea(contour)
        if area <= size:
            cv_contours.append(contour)
        else:
            continue

    cv2.fillPoly(img, cv_contours, (num, num, num))
    return img




img1 = Image.open('img/opened2.png')
img1 = np.asarray(img1)
img1=cv2.cvtColor(img1,cv2.COLOR_BGR2GRAY)#将图像转化为灰度图像

img1 = filling(img1, 10000, 255)
cv2.imwrite('img/samall1.png', img1)  # 填充海水部分

#img1 = 0

# img2 = Image.open('image/samall1.png')
# img2 = np.asarray(img2)

img2 = filling(img1, 10000, 0)
cv2.imwrite('img/samall2.png', img2)  # 填充陆地部分

img1=0

# 中值滤波降噪
medianBlur = cv2.medianBlur(img2, 11)
cv2.imwrite('img/medianBlur.png',medianBlur)

# 高斯滤波
guass = cv2.GaussianBlur(medianBlur, (3, 3), 0)

medianBlur=0
# Canny算子
canny = cv2.Canny(guass, 50, 150)

cv2.imwrite('img/canny_3x3.png', canny)
end = datetime.datetime.now()
print ( 'Running time: %s Seconds' %(end-start).seconds)
# canny=0
# #图片叠加
#
# img2=cv2.imread('image/result_resize2.png')
# canny=cv2.imread('image/canny.png')
# #img3=cv2.add(img1,img2)
# add=cv2.addWeighted(canny,0.7,img2,0.3,0)
#
# cv2.imwrite('image/add.png',add)
