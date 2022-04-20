import numpy

import cv2
from PIL import Image, ImageDraw
from PIL import ImageFile
ImageFile.LOAD_TRUNCATED_IMAGES = True
Image.MAX_IMAGE_PIXELS = None

#python 的标准库手册推荐在任何情况下尽量使用time.clock().
#只计算了程序运行CPU的时间，返回值是浮点数
# import time
# start =time.clock()

#image = cv2.imread("img/result_1.jpg")#读入图像
image=Image.open('image/medianBlur.png')
image=numpy.asarray(image)
print(image.shape)

#高斯模糊
image3= cv2.GaussianBlur(image,(3,3),0)
image9= cv2.GaussianBlur(image,(9,9),0)
image15= cv2.GaussianBlur(image,(15,15),0)
image27= cv2.GaussianBlur(image,(27,27),0)

#Canny
canny3=cv2.Canny(image3,50,150)
canny9=cv2.Canny(image9,50,150)
canny15=cv2.Canny(image15,50,150)
canny27=cv2.Canny(image27,50,150)

#颜色反转
# height,width=canny.shape
# dst=np.zeros((height,width,1),np.uint8)
# for i in range(height):
#     for j in range(width):
#         dst[i,j]=255-canny[i,j]


cv2.imwrite('image/canny_3x3.png',canny3)
cv2.imwrite('image/canny_9x9.png',canny9)
cv2.imwrite('image/canny_15x15.png',canny15)
cv2.imwrite('image/canny_27x27.png',canny27)

# end = time.clock()
# print('Running time: %s Seconds'%(end-start))
