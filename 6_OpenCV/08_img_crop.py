import cv2

img = cv2.imread('image/image.png')

# 이미지 자르기
img_crop = img[100:200, 100:400]

cv2.imshow("turtle", img)
cv2.imshow("Image Croppped", img_crop)

cv2.waitKey(0)
cv2.destroyAllWindows()