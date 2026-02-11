import cv2

cap = cv2.VideoCapture("6_OpenCV/image/video.mp4")

# 1. VideoWriter 설정을 위한 정보 획등
fourcc = cv2.VideoWriter_fourcc(*"H264") # 코덱 설정
fps = cap.get(cv2.CAP_PROP_FPS) # 원본 FPS 가져오기
width = round(cap.get(cv2.CAP_PROP_FRAME_WIDTH))
height = round(cap.get(cv2.CAP_PROP_FRAME_HEIGHT))

# 2. VideoWriter 객체 생성
out = cv2.VideoWriter("6_OpenCV/output/video.mp4", fourcc, fps, (width, height))

# 
while cap.isOpened():
    ret, frame = cap.read()

    if not ret:
        break
    
    # 3. 프레임 저장
    # 주의) 이 방식은 소리는 저장 x
    out.write(frame)
    cv2.imshow("Video", frame)

    # 'q'키를 누르면 종료
    if cv2.waitKey(int(1000/fps)) == ord('q'):
        cv2.imwrite('6_OpenCV/output/capture_video.jpg', frame)
        break

# 자원 해제
out.release()
cap.release()
cv2.destroyAllWindows()