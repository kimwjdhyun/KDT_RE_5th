import cv2

img = cv2.imread('image/image.png')

# 좌우반전
img_flip = cv2.flip(img, 1) # 0 보다 크면 y축 반전ㅂ
cv2.imshow("FLIP", img_flip)

cv2.waitKey(0)
cv2.destroyAllWindows()


# 실습. 이미지 조정
penguin = cv2.imread('image/penguin.png')

pr_penguin = cv2.resize(penguin, None, fx=0.5, fy=0.5)

pr_penguin_flip = cv2.flip(pr_penguin, 1)

h, w, _ = penguin.shape
h2, w2, _ = pr_penguin_flip.shape

x = w - w2
y = h - h2

penguin[y:y+h2, x:x+w2] = pr_penguin_flip

cv2.imshow("Practice", penguin)
cv2.waitKey(0)
cv2.destroyAllWindows()
