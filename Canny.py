import cv2
import numpy as np
from PIL import Image, ImageDraw
from PIL import ImageFile
import  PIL.ImageOps
ImageFile.LOAD_TRUNCATED_IMAGES = True
Image.MAX_IMAGE_PIXELS = None

#载入提取MNDWI后的图片

img=Image.open('image/samall2.png')

#转为numpy 数组
img=np.asarray(img)
#高斯滤波
guass= cv2.GaussianBlur(img,(3,3),0)
guass=cv2.resize(guass,(0,0),fx=0.1,fy=0.1,interpolation=cv2.INTER_AREA)
#Canny算子
canny=cv2.Canny(guass,50,150)

# img1=Image.fromarray(canny)
# canny1=PIL.ImageOps.invert(img1)
# canny1=np.asarray(canny1)
cv2.imwrite('image/canny.png', canny)  #填充陆地部分

