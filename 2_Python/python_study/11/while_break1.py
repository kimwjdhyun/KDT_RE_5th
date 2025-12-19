while True: # 의도적으로 무한 반복을 하되, 반복문 내부에서 탈출 조건 만들기
	launch = input("오늘 점심 리스트('그만' 입력시 종료됨)? ")
	if launch == "그만":
		break # 반복문 흐름을 깨다 = 탈출	
	print(launch)
print("done")
