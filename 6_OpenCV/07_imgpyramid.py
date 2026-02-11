import cv2

img = cv2.imread('image/image.png')

# 2배 확대
img_up = cv2.pyrUp(img)
# 2배 축소
img_down = cv2.pyrDown(img)

cv2.imshow("UP", img_up)
cv2.imshow("DOWN", img_down)
cv2.waitKey(0)
cv2.destroyAllWindows()

