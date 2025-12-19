# 파일 입출력
# - 저장장치에 저장된 파일을 읽어오거나 저장하는 작업
'''
# 파일열기와 닫기
# 파일열기 : open()
# open(파일경로, mode="r", encoding="원하는 인코딩 - utf-8")
# open으로 파일을 읽으면 '파일 객체'를 반환
f = open("example.txt", "w", encoding="utf-8")  # 쓰기 모드로 파일 열기

f.write("파이썬 파일 입출력 예제\n")              # 파일에 문자열 쓰기
f.write("파이썬 공부!")

# 파일 닫기 : close()
# 열린 파일을 닫아 시스템 자원을 해제함
f.close() 


# 파일 읽기
# read() : 전체 내용을 한번에 읽기
f = open("example.txt", "r", encoding="utf-8") # 읽기 모드로 파일 열기
content = f.read()                             # 파일 내용 전체 읽기
print(content)        # 파이썬 파일 입출력 예제
f.close()             #  파이썬 공부!    


# readline() : 한 줄씩 순차적으로 읽기
f = open("example.txt", "r", encoding="utf-8") # 읽기 모드로 파일 열기
line1 = f.readline()                           # 첫 번째 줄 읽기
line2 = f.readline()                           # 두 번째 줄 읽기

print("첫번째 줄 :", line1.strip())     # 첫번째 줄 : 파이썬 파일 입출력 예제
print("두번째 줄 :", line2)             # 두번째 줄 : 파이썬 공부!
f.close()

# for문으로 읽기
f = open("example.txt", "r", encoding="utf-8")
for line in f:
    print(line.strip()) # 파이썬 파일 입출력 예제
f.close()               # 파이썬 공부!

# readlines() : 모든 줄을 한번에 리스트로 읽기
f = open("example.txt", "r", encoding="utf-8")
content = f.readlines()
print(content)          # ['파이썬 파일 입출력 예제\n', '파이썬 공부!']
f.close()

# tell() : 현재 읽고 있는 위치(바이트)를 반환
f = open("example.txt", "r", encoding="utf-8")
print("처음 위치 : ", f.tell())             # 처음 위치 :  0
f.read(5)
print("5바이트 읽은 후 위치 : ", f.tell())   # 5바이트 읽은 후 위치 :  13
f.close()


# seek() : 파일 포인터 위치를 이동
f = open("example.txt", "r", encoding="utf-8")
print(f.read(10))       # 파이썬 파일 입출력(10바이트만큼 읽어옴)
f.seek(0)               # 파일의 맨 처음으로 이동
print(f.read())         # 파이썬 파일 입출력 예제
f.close()               # 파이썬 공부!

# a 모드 : 추가 쓰기
f = open("example.txt", "a", encoding="utf-8")
f.write("\n추가한 내용입니다.")
f.close()


# with 문
# 파일 입출력시에 자동으로 close()를 호출해주는 구문

# 파일 쓰기
with open("with_example.txt", "w", encoding="utf-8") as f1:
    f1.write("with문으로 작성한 파일이에요\n")
    f1.write("파일 입출력 완료")

# 예제 1. 파일에서 랜덤 추출
import random as r

with open("words.txt", "w", encoding="utf-8") as f1:
    words = [
      "apple", "banana", "orange", "grape", "lemon",
      "peach", "melon", "cherry", "plum", "pear",
      "school", "friend", "family", "flower", "garden",
      "window", "bottle", "pencil", "summer", "winter",
      "happy", "future", "travel", "animal", "market",
      "doctor", "planet", "energy", "nature", "memory"]
    
    for i in words:
        f1.write(i + "\n")

with open("words.txt", "r", encoding="utf-8") as f1:
    data = f1.readlines()
    for i in range(5):
        word = r.choice(data).split()
        print(word)

#['nature']
# ['market']
# ['grape']
# ['bottle']
# ['pear']

# 예제 2. 입력받아 파일 쓰기
with open("with_example.txt", "a", encoding="utf-8") as f1:
    while True:
        text = input("저장할 내용을 입력해주세요(종료 : z) : ")
        if text == "Z" or text == "z":
            break
        f1.write(text + "\n")

# 저장할 내용을 입력해주세요(종료 : z) : 안녕하세요
# 저장할 내용을 입력해주세요(종료 : z) : 반갑습니다
# 저장할 내용을 입력해주세요(종료 : z) : z

# 실습 1. 회원 명부 작성하기


# 문제 3. 로그인 성공 시 전화번호 저장하기

# 문제 1. 회원 명부 작성하기

users = []

for i in range(3):
    username = input(f"사용자 이름 {i+1} : ")
    password = input(f"비밀번호 {i+1} : ")
    users.append((username, password))

with open("member.txt", "a", encoding="utf-8") as f:
    for user, pw in users:
        f.write(user + "\n")
        f.write(pw + "\n")
with open("member.txt", "r", encoding="utf-8") as f:
    member = f.read().split()
    print(member)


["kimwjdhyun","12321", "wjdhyun", "123321", "kimhyun", "123123"]

# 문제 2. 회원 명부를 이용한 로그인 기능


users = {}
user_count = 0

with open("member.txt", "r", encoding="utf-8") as f:
    lines = f.read().splitlines()

    for i in range(0, len(lines), 2):
        username = lines[i]
        password = lines[i + 1]
        users[username] = password

while user_count < 3:
    login_user = input("사용자 이름을 입력하세요: ")
    login_pw = input("비밀번호를 입력하세요: ")

    if login_user in users and users[login_user] == login_pw:
        user_count += 1
        print("로그인 성공!")
    else:
        print("로그인 실패!")

# 사용자 이름을 입력하세요: kimwjdhyun
# 비밀번호를 입력하세요: 12321
# 로그인 성공!
# 사용자 이름을 입력하세요: wjdhyun
# 비밀번호를 입력하세요: 1231
# 로그인 실패!
# 사용자 이름을 입력하세요: wjdhyun
# 비밀번호를 입력하세요: 123321
# 로그인 성공!
# 사용자 이름을 입력하세요: kimhyun
# 비밀번호를 입력하세요: 123123
# 로그인 성공!

# 문제 3. 로그인 성공시 전화번호 저장하기

import os

users = {}
user_count = 0

with open("member.txt", "r", encoding="utf-8") as f:
    lines = f.read().splitlines()

    for i in range(0, len(lines), 2):
        username = lines[i]
        password = lines[i + 1]
        users[username] = password

while user_count < 3:
    login_user = input("사용자 이름을 입력하세요 : ")
    login_pw = input("비밀번호를 입력하세요 : ")

    if login_user in users and users[login_user] == login_pw:
        user_count += 1
        print("로그인 성공!")

        tel_exists = False
        tel_data = {}

        if os.path.exists("member_tel.txt"):
            with open("member_tel.txt", 'r', encoding="utf-8") as f:
                for line in f:
                    if ":" in line:
                        name, tel = line.strip().split(" : ")
                        tel_data[name] = tel

                        if name == login_user:
                            tel_exists = True

            if tel_exists:
                 print(f"기존 전화번호: {tel_data[login_user]}")
                 tel_num = input("새로운 전화번호를 입력하세요 (수정): ")
            else:
                 tel_num = input("전화번호를 입력하세요: ")
        
            tel_data[login_user] = tel_num
        
            with open("member_tel.txt", "w", encoding="utf-8") as f:
                for name, tel in tel_data.items():
                     f.write(f"{name} : {tel}\n")
                     
    else:
        print("로그인 실패!")



# 실습 1

import os
# ------------------------------------------
# 1. 회원 3명 입력하여 파일에 저장
# ------------------------------------------
if os.path.exists("member.txt"):
    print("member.txt가 이미 존재합니다. 회원 등록을 건너뜁니다.\n")
else:
    with open("member.txt", "w", encoding="utf-8") as f:
        for i in range(3):
            name = input(f"{i+1}번째 회원의 이름: ")
            password = input(f"{i+1}번째 회원의 비밀번호: ")
            f.write(f"{name},{password}\n")
        
print("\n[회원 명부 저장 완료]\n")


# ------------------------------------------
# 2. 로그인 과정
# ------------------------------------------
input_name = input("로그인 - 이름을 입력하세요: ")
input_password = input("로그인 - 비밀번호를 입력하세요: ")

login = False
with open("member.txt", "r", encoding="utf-8") as f:
    for line in f:
        name, password = line.strip().split(",")
        if input_name == name and input_password == password:
            login = True
            break
        

# ------------------------------------------
# 3. 로그인 성공 시 전화번호 등록/수정
# ------------------------------------------
if login:
    print("\n로그인 성공!")
    
    # 기존 전화번호 데이터 로드
    phone_data = {}
    
    if os.path.exists("member_tel.txt"):
        with open("member_tel.txt", "r", encoding="utf-8") as f:
            for line in f:
                name, phone = line.strip().split(",")
                phone_data[name] = phone
                
    # 전화번호 입력
    new_phone = input(f"{input_name}님의 전화번호를 입력하세요: ")
    
    # 추가 또는 수정
    if input_name in phone_data:
        print("기존 전화번호 수정")
    else:
        print("전화번호 새로 추가")
    
    phone_data[input_name] = new_phone
    
    # 전화번호 파일 갱신
    with open("member_tel.txt", "w", encoding="utf-8") as f:
        for name, phone in phone_data.items():
            f.write(f"{name},{phone}\n")
            
    print("전화번호 저장 완료!")
else:
    print("\n로그인 실패!")
'''


# 바이너리 파일 읽기

# import os

# print(os.getcwd())

# with open('./image/rabbit.jpg', 'rb') as f:
#     img = f.read()
#     print(img)

# # 바이너리 파일 쓰기
# with open("./image/output/rabbit_copy.jpg", "wb") as f:
#     f.write(img)


# pickle 모듈
# 객체의 형태를 유지하면서 파일에 저장하고 불러올 수 있음

import pickle as p

# 리스트, 딕셔너리 파일 저장
with open("pickle.txt", "wb") as f:
    li = ['dog', 'cat']
    dic = {1 : 'dog', 2 : 'cat'}

    p.dump(li, f)
    p.dump(dic, f)

# 읽기
with open("pickle.txt", "rb") as f:
    li = p.load(f)
    dic = p.load(f)

    print(li, dic)  # ['dog', 'cat'] {1: 'dog', 2: 'cat'}