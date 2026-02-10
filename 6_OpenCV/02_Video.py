import cv2

# 비디오 파일 또는 웹캠 연결
cap = cv2.VideoCapture("6_OpenCV/image/video.mp4") # 웹캠은 0 입력

while cap.isOpened(): # 영상이 정상적으로 열려있는 동안 반복
    ret, frame = cap.read() # 프레임 읽기
    
    if not ret: # 더 이상 프레임이 없으면 종료
        break

    cv2.imshow("Video Player", frame)

    # 'q'키를 누르면 종료(33ms 대기 약 30fps 유지)
    if cv2.waitKey(33) == ord('q'):
        break

cap.release() # 자원 해제
cv2.destroyAllWindows()

capture = cv2.VideoCapture("6_OpenCV/image/video.mp4")
fps = capture.get(cv2.CAP_PROP_FPS)
total = capture.get(cv2.CAP_PROP_FRAME_COUNT)

while cv2.waitKey(int(10000.0//fps)) < 0:
    if capture.get(cv2.CAP_PROP_POS_FRAMES) == total - 1:
        capture.set(cv2.CAP_PROP_POS_FRAMES, 0)

    ret, frame = capture.read()
    cv2.imshow('Practice', frame)


capture.release()
cv2.destroyAllWindows()