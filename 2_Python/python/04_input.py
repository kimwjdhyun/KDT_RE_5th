# 사용자 입력 (input)
# - input 함수 : 콘솔을 통해 사용자로부터 문자열 형태로 입력 받음

# input 함수 사용법
# my_input = input("콘솔에 띄울 설명")
# name = input("이름을 입력하세요:")
# print (name) # 터미널창에서 입력 가능

# 숫자로 활용 시 '형 변환'필요
# a = int(input())
# b = int(input()) # 정수형
# print(a + b)

# c = float(input())
# d = float(input()) # 실수형
# print(c+d)

# 여러 자료 입력하기
# 문자열을 쪼개주는 함수 : split()
# 기본 구분자 : 공백

# 다른 구분자 사용
# apple, banana, grape = input().split('-')
# print(apple, banana, grape)

# 실습 1.
# name = input()
# age = input()
# my_input = input(f"안녕하세요. 저는 {name}이고, {age}살입니다.")

# 실습 2.
# 가로 = int(input())
# 세로 = int(input())
# 넓이 = 가로 * 세로
# 둘레 = 2*(가로 + 세로)

# print(f"넓이 :{넓이}")
# print(f"둘레: {둘레}")

# number = int(input())
# number1 = input('천의 자리: ')
# number2 = input('백의 자리: ')
# number3 = input('십의 자리: ')
# number4 = input('일의 자리: ')
# print(number, number1,number2,number3,number4)



# n1, n2, n3 = input("발표자 이름 3명을 입력하세요").split()
# t1, t2, t3 = input("발표 주제 3개를 입력하세요").split()

# print(f'''발표 순서 안내입니다.
# 1조 발표자:{n1}-주제:{t1}
# 2조 발표자:{n2}-주제:{t2}
# 3조 발표자:{n3}-주제:{t3}''')

# year, month, day = input("년, 월, 일을 입력해주세요").split()
# day, min, sec = input("시, 분, 초를 입력해주세요").split()

# print(f'''
# RE3의개강일은 {year}년 {month}월 {day}일
# 시작 시간은 {day}시 {min}분 {sec}초 입니다.''')

