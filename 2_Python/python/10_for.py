# for 문
# - 이터러블(순회 가능한) 요소를 하나씩 꺼내서 실행 블록에 전달하는 반복문
'''
# 리스트 반복
fruits = ['apple', 'banana', 'cherry']
for fruit in fruits:
    print(f"I like {fruit}")
# I like apple
# I like banana
# I like cherry

# 문자열 반복
my_str = "codingon"
for cha in my_str:
    print(cha) # c o d i n g o n

# 튜플 반복
coords = [(1, 2), (10, 15), (-6, 8)]
#언패킹 (구조분해 가능)
for x, y in coords:
    print(f"x좌표 : {x}, y좌표는 {y}")
# x좌표 : 1, y좌표는 2
# x좌표 : 10, y좌표는 15
# x좌표 : -6, y좌표는 8

# dict 반복
person = {
    "name" : "kim", 
    "age" : 28, 
    "address" : "jeju"
}

# 기본
for key in person:
    print(f"key : {key}, value : {person[key]}")
# key : name, value : kim
# key : age, value : 28
# key : address, value : jeju

# value 만 가져오기
for value in person.values():
    print(f"value : {value}")
# value : kim
# value : 28
# value : jeju

# items : 모든 쌍(키, 값) 가져오기
for key, value in person.items():
    print(f"key : {key}, value : {value}")
# key : name, value : kim
# key : age, value : 28
# key : address, value : jeju

# set 반복
my_set = {1, 2, 3, 4}

for s in my_set:
    print(s) # 1, 2, 3, 4

# 실습 1. for문 기본 문법 문제
# 문제 1. 리스트의 값을 두 배로 변환하기
numbers = [3, 6, 1, 8, 4]
doubled = []
for num in numbers:
    doubled.append(num * 2)
    print(doubled)
# [6]
# [6, 12]
# [6, 12, 2]
# [6, 12, 2, 16]
# [6, 12, 2, 16, 8]

# 중요 !: 새로운 리스트 생성 후 진행 

# 문제 2. 문자열의 길이 구해서 새 리스트 만들기
words = ["apple", "banana", "kiwi", "grape"]
list = []
for word in words:
    list.append(len(word))
    print(list)
# [5]
# [5, 6]
# [5, 6, 4]
# [5, 6, 4, 5]

# 문제 3. 좌표 튜플에서 x, y 좌표 나누기
coordinates = [(1, 2), (3, 4), (5, 6), (7, 8)]

x_values = []
y_values = []

for x, y in coordinates:
    x_values.append(x)
    y_values.append(y)

print(f"x 좌표 :, {x_values}")
print(f"y 좌표 :, {y_values}")


# x 좌표 :, [1, 3, 5, 7]
# y 좌표 :, [2, 4, 6, 8]
'''

'''
# for 문과 range()
# range ()함수 : 지정된 범위의 정수 시퀀스 생성

# 기본 문법
# range(start, end, step) 
# - start : 생량 가능, 기본 값 = 0
# - end : end -1까지 생성
# - step : 생략 가능, 기본 값 = 1

range(1, 5)

for i in range(1, 5):
    print(i) # 1 2 3 4

for i in [1,2,3,4]:
    print(i) # 1 2 3 4

# start 생략
for i in range(5):
    print(i) # 0 2 3 6 8 10

# # 간격 (step) 지정
for i in range(0, 11, 2):
    print(i)
for i in range(11, 0, -2):
    print(i) # 11 9 7 5 3 1

# 실습 2. for 문과 range
# 문제 1. 입력 받은 수의 합 구하기

user_number = input("수를 입력하세요")
x = [user_number]

for user_number in x:
    range(1, int(user_number))
    x = sum(range(1, int(user_number)+1))
    print(x) # 100 / 4950

# #해설 
num = int(input("숫자를 입력하세요"))
sum = 0

for i in range(num+1):
    sum += 1
    print sum

# # 문제 2. 구구단 만들기
user_number = int(input("수를 입력하세요. :"))

for i in range(1, 10):
    print(f"{user_number} X {i} = {user_number * i}")
# 수를 입력하세요. :12
# 12 X 1 = 12
# 12 X 2 = 24
# 12 X 3 = 36
# 12 X 4 = 48
# 12 X 5 = 60
# 12 X 6 = 72
# 12 X 7 = 84
# 12 X 8 = 96
# 12 X 9 = 108

# # 해설
dan = int(input("생성할 단을 입력해주세요"))

for i in range(1,10):
    print(f"{dan}x{i}={dan * i}")

# 문제 3. 3의 배수 합 구하기
x = 0
for i in range(3, 101, 3):
    x += i
print(x) # 1683

# #해설
result = 0
for i in range(3,101,3):
    result += i # 해당 값을 계속 더하는 복합 대입 연산자
for i in range(1, 101):
    if % == 0: # 나누기 활용 두가지 방법 다 가능
        result += i
    print("3의 배수의 합 : ", result) 

# 문제 4. 짝수이면서 5의 배수인 수 출력하기
n = int(input("수를 입력하세요. "))
for i in range(1, n+1):
    if i % 2 == 0 and i % 5 == 0:
        print(i) # 10 20 30 40 50

# # 해설
n = int(input("수를 입력하세요. : "))

for i in range(1, n+1):
    if i % 2 == 0 and i % 5 == 0
        print(i)
'''

'''
print("============================")
# 루프 제어문
# 특정 조건 하에서만 작동하도록 구현
# break : 반복을 즉시 중단한다.
for i in range(10):
    if i == 5:
        break
    print(i) # 5에서 중단 print()함수 위치에 따라 다름
print("반복 종료") 
# 0
# 1
# 2
# 3
# 4
# 반복 종료

# continue : 현재 반복을 넘어감
for i in range(5):
    if i ==2:
        print("continue = 건너뜀")
        continue
    print(i)
print("반복 종료")

# 0
# 1
# continue = 건너뜀
# 3
# 4
# 반복 종료

# pass : 아무 동작도 하지 않고 자리만 차지(추후 구현 예정인 자리)
# 프로그램에 영향 없음.

for i in range(10):
    pass

# for -else 구문
for i in range(5):
    if i == 2:
        break
    print(i)
else:
    print("반복 종료") # break로 종료 시 else 구문 실행 x

'''

'''
# 중첩 for 문
# - 하나의 for 문 안에 다른 for문이 들어있는 구조


# 이중 for 문
for i in range(5):
    for j in range(5):
        print("i, j", i, j)
    print()

# i, j 0 0
# i, j 0 1
# i, j 0 2
# i, j 0 3
# i, j 0 4


# 실습 중첩 for문 연습 문제
# 문제 1. 구구단 만들기

for i in range(2, 10):
    print(f'[{i} 단]') # 위치 잘 기억하기!
    for j in range(1, 10):
        print(f"{i} X {j} = {i * j}")

# [2 단]
# 2 X 1 = 2
# 2 X 2 = 4
# 2 X 3 = 6
# 2 X 4 = 8
# 2 X 5 = 10
# 2 X 6 = 12
# 2 X 7 = 14
# 2 X 8 = 16
# 2 X 9 = 18
# [3 단]
# 3 X 1 = 3
# 3 X 2 = 6
# 3 X 3 = 9
# 3 X 4 = 12
# 3 X 5 = 15
# 3 X 6 = 18
# 3 X 7 = 21
# 3 X 8 = 24
# 3 X 9 = 27
# [4 단]
# 4 X 1 = 4
# 4 X 2 = 8
# 4 X 3 = 12
# 4 X 4 = 16
# 4 X 5 = 20
# 4 X 6 = 24
# 4 X 7 = 28
# 4 X 8 = 32
# 4 X 9 = 36
# [5 단]
# 5 X 1 = 5
# 5 X 2 = 10
# 5 X 3 = 15
# 5 X 4 = 20
# 5 X 5 = 25
# 5 X 6 = 30
# 5 X 7 = 35
# 5 X 8 = 40
# 5 X 9 = 45
# [6 단]
# 6 X 1 = 6
# 6 X 2 = 12
# 6 X 3 = 18
# 6 X 4 = 24
# 6 X 5 = 30
# 6 X 6 = 36
# 6 X 7 = 42
# 6 X 8 = 48
# 6 X 9 = 54
# [7 단]
# 7 X 1 = 7
# 7 X 2 = 14
# 7 X 3 = 21
# 7 X 4 = 28
# 7 X 5 = 35
# 7 X 6 = 42
# 7 X 7 = 49
# 7 X 8 = 56
# 7 X 9 = 63
# [8 단]
# 8 X 1 = 8
# 8 X 2 = 16
# 8 X 3 = 24
# 8 X 4 = 32
# 8 X 5 = 40
# 8 X 6 = 48
# 8 X 7 = 56
# 8 X 8 = 64
# 8 X 9 = 72
# [9 단]
# 9 X 1 = 9
# 9 X 2 = 18
# 9 X 3 = 27
# 9 X 4 = 36
# 9 X 5 = 45
# 9 X 6 = 54
# 9 X 7 = 63
# 9 X 8 = 72
# 9 X 9 = 81


# 구구단 만들기 해설
for i in range(2, 10):
    print(f"[ {i} 단 ]")
    for j in range(1,10):
        print(f"{i} X {j} = {i * j}")
    print() # 줄바꾸고 공백 두기

    
# 문제 2. 중첩 for 문 별찍기

n = int(input("몇 줄? :"))

print(f"왼쪽 정렬 > {n}")
for i in range(1, n+1):
    for j in range(i):
        print("*", end="")
    print()

# 왼쪽 정렬 > 10
# *
# **
# ***
# ****
# *****
# ******
# *******
# ********
# *********
# **********

print(f"오른쪽 정렬 > {n}")
for i in range(1, n+1):
    for j in range(n-i):
        print(" ", end="")
    for j in range(i):
        print("*", end="")
    print()

#     오른쪽 정렬 > 10
#          *
#         **
#        ***
#       ****
#      *****
#     ******
#    *******
#   ********
#  *********
# **********


print(f"가운데 정렬 > {n}")
for i in range(1, n+1):
    for j in range(n-i):
        print(" ", end="")
    for j in range(2 * i - 1):
        print("*", end="")
    print()

#     가운데 정렬 > 10
#          *
#         ***
#        *****
#       *******
#      *********
#     ***********
#    *************
#   ***************
#  *****************
# *******************
'''
'''
# 별찍기 해설
n = int(input("몇 줄 ? :"))

# 왼쪽 정렬
for i in range(1, n + 1):
    for j in range(i):
        print("*", end="")
    print()

n = int(input("몇 줄 ? :"))

# 오른쪽 정렬
for i in range(1, n + 1):
    # 공백 출력
    for j in range(n - i):
        print(" ", end="")
    for j in range(i):
        print("*", end="")
    print()

n = int(input("몇 줄 ? :"))

# 가운데 정렬
for i in range(1, n + 1):
    # 공백 출력
    for j in range(n - i):
        print(" ", end="")
    for j in range(2 * i - 1):
        print("*", end="")
    print()

'''
# 리스트 컴프리헨션(리스트 내포)
# - for문을 리스트에 한줄로 축약하여 새 리스트를 생성하는 문법
# [표현식(리스트의 원소) for 변수 in 반복대상 if 조건]
# - 표현식 : 값을 유도하는 식(표현)

# for문 이용
squares = []
for x in range(1,6):
    squares.append(x**2)
print(squares)          # [1, 4, 9, 16, 25]

# 리스트 컴프리헨션
squares2 = [x**2 for x in range(1,6)]
print(squares2)         # [1, 4, 9, 16, 25]

# 조건문 추가하기
squares3 = [x**2 for x in range(1,11) if x % 2==0]
print(squares3)         # [4, 16, 36, 64, 100]

# 딕셔너리, 집합 컴프리헨션
squares4 = {x: x**2 for x in range(1,6)}
print(squares4)         # {1: 1, 2: 4, 3: 9, 4: 16, 5: 25}

# 실습 1. 리스트 컴프리헨션 연습문제
# 문제 1. 제곱값 리스트 만들기
numbers = [n**2 for n in range(1,11)]
print(numbers)          # [1, 4, 9, 16, 25, 36, 49, 64, 81, 100]

# 문제 2. 3의 배수만 리스트로 만들기
numbers1 = [n for n in range(1,51) if n % 3==0]
print(numbers1)         # [3, 6, 9, 12, 15, 18, 21, 24, 27, 30, 33, 36, 39, 42, 45, 48]

# 문제 3. 문자열 리스트에서 길이가 5이상인 단어만 뽑기
fruits = ["apple", "fig", "banana", "plum", "cherry", "pear", "orange"]
fruits = [f for f in fruits if len(f)>=5]
print(fruits)           # ['apple', 'banana', 'cherry', 'orange']