import cv2

img = cv2.imread('image/image.png')

# 1. 고정 크기로 조정(가로 320, 세로 240)
dst_fixed = cv2.resize(img, (320, 240))

# 2. 비율로 조정(가로 0.5배, 세로 0.5배)
dst_ratio = cv2.resize(img, None, fx=0.5, fy=0.5)

cv2.imshow("Fixed Resize", dst_fixed)
cv2.imshow("Ratio Resize", dst_ratio)
cv2.waitKey(0)
cv2.destroyAllWindows()

import cv2

cap = cv2.VideoCapture('image/video.mp4')
fps = cap.get(cv2.CAP_PROP_FPS)

while True:
    ret, frame = cap.read()
    if not ret:
        break

    dst_ratio = cv2.resize(frame, None, fx=1.5, fy=1.5, interpolation=cv2.INTER_CUBIC)
    cv2.imshow("Ratio Resize", dst_ratio)
    
    if cv2.waitKey(int(1000/fps)) == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()
