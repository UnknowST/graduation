import  cv2
img1=cv2.imread('img/canny_3x3.png')
img2=cv2.imread('img/result.png')

#img3=cv2.add(img1,img2)
img3=cv2.addWeighted(img1,0.7,img2,0.3,0)

cv2.imwrite('img/add.png',img3)
