import  cv2
img1=cv2.imread('image/canny.png')
img2=cv2.imread('image/result_resize2.png')

#img3=cv2.add(img1,img2)
img3=cv2.addWeighted(img1,0.7,img2,0.3,0)

cv2.imwrite('image/add2.png',img3)
