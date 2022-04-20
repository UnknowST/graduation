
#Sobel算子


import cv2
img = cv2.imread("image/medianBlur.png", 0)

# 高斯滤波
#guass = cv2.GaussianBlur(img, (3, 3), 0)

x = cv2.Sobel(img, cv2.CV_16S, 1, 0)
y = cv2.Sobel(img, cv2.CV_16S, 0, 1)

absX = cv2.convertScaleAbs(x) # 转回uint8
absY = cv2.convertScaleAbs(y)

dst = cv2.addWeighted(absX, 0.5, absY, 0.5, 0)

cv2.imwrite('image/Sobel1.png',dst)

