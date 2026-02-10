import cv2
import os

# 이미지 파일 경로를 스크립트 기준으로 안전하게 구성
img_path = os.path.join(os.path.dirname(__file__), "image", "image.png")
# 이미지 읽기
img = cv2.imread('6_OpenCV/image/image.png')
# 이미지 창에 표시
cv2.imshow("Image Window", img)
# # 키보드 입력 대기 (0은 무한 대기)
key = cv2.waitKey(0)
print("Pressed key code : ", key)
# # 모든 창 닫기
cv2.destroyAllWindows()

# # 채널 3(R, G, B)
img_default = cv2.imread(img_path, cv2.IMREAD_COLOR)
# # 채널 없음 (그레이스케일)
img_grayscale = cv2.imread(img_path, cv2.IMREAD_GRAYSCALE)

cv2.imshow("Default Image", img_default)
cv2.imshow("Grayscale", img_grayscale)
cv2.waitKey(0)
cv2.destroyAllWindows()

logo_path = os.path.join(os.path.dirname(__file__), "image", "logo.png")

# # # 채널 3(R, G, B)
logo_default = cv2.imread(logo_path, cv2.IMREAD_COLOR)
# # 채널 4 (Alpha 값 포함 - 배경 투명일 경우)
logo_unchanged = cv2.imread(logo_path, cv2.IMREAD_UNCHANGED)

cv2.imshow("Default Image", logo_default)
cv2.imshow("Unchanged", logo_unchanged)
print("logo shape(Unchanged) : ", logo_unchanged.shape)
cv2.waitKey(0)
cv2.destroyAllWindows()

practice_path = os.path.join(os.path.dirname(__file__), "image", "pexel_practice.png")

img_default = cv2.imread(practice_path, cv2.IMREAD_COLOR)
img_grayscale = cv2.imread(practice_path, cv2.IMREAD_GRAYSCALE)

cv2.imshow("Default Image", img_default)
cv2.imshow("Grayscale", img_grayscale)
cv2.waitKey(0)
cv2.destroyAllWindows()