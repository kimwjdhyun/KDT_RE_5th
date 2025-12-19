# 주석 : # 한줄 주석
"""
-여러줄 주석(''' '''')
"""

# 출력 : print 함수
print("Hello World!")

# print 구분자 옵션
# sep : 기본값 = 공백
print("가", "나", "다", sep= "-")

# print 줄바꿈
# end 
print("안녕하세요.", end=" ")
print("반갑습니다.")

# 변수
'''
- 변수 : 자료를 저장하는 공간
- 선언 : 변수를 만드는 것
- 할당 : 변수에 값을 저장하는 것
- 초기화 : 처음으로 변수에 값을 할당하는 것
- = : 대입 연산자, 같다 라는 의미 x, 값을 할당하다의 의미
'''

# 변수의 선언과 할당
변수이름 = "저장할 자료값"
print(변수이름)

# 변수 이름 규칙
# 1st_place = 'Gold' -> error
first_place = "Gold"

# user name = "정현"
user_name = "정현"

# 예약어 사용 x

# 변수의 특징
# 저장한 값을 바꿀 수 있다
# 단, 한번에 하나씩만 저장
hello = "안녕하세요"
hello = "반갑습니다"
hello = "좋은 하루 되세요"
print(hello)

# 한 줄에 여러 변수
a = 1
b = 2
c = 3
a, b, c = 4, 5, 6

print(a, b, c)

x = 10
y = 20

x, y = y, x
print (x, y)