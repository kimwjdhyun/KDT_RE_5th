while True:
    launch = input("오늘 점심 후보? ")
    if launch == "그만":
	    break # 반복문 흐름을 깨다 = 탈출
    if len(launch) <= 3:
            print("그건 안돼")
            continue
    print(launch)
print("done")
