#图片颜色反转

import cv2
import numpy as np
from PIL import Image, ImageDraw
from PIL import ImageFile

ImageFile.LOAD_TRUNCATED_IMAGES = True
Image.MAX_IMAGE_PIXELS = None

# 载入提取MNDWI后的图片
img = Image.open('img/canny_3x3.png')

# 转为numpy 数组
canny = np.asarray(img)
#颜色反转
height,width=canny.shape
dst=np.zeros((height,width,1),np.uint8)
for i in range(height):
    for j in range(width):
        dst[i,j]=255-canny[i,j]

cv2.imwrite('img/invCanny.png',dst)