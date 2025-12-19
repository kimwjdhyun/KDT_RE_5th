# 연습(11.12)
# print("Hello World!")

# print("Mary's cosmetics")

# print('신씨가 소리질렀다 "도둑이야"')

# print("c:\windows")

# print("안녕하세요. \n만나서\t\t반갑습니다")
#'\t'는 탭을 의미, '\n'은 줄바꿈을 의미
# print("오늘은", "일요일")

# print('naver','kakao','sk','samsung' , sep=';')
# sep= 인자로 출력되는 값들 사이에 공백 대신 출력할 값
# print("naver", "kakao", "sk", "samsung", sep="/")

# print("first", end='');print("second")
# 세미콜론(;)은 한줄에 여러 개의 명령을 작성하기 위해 사용
# print(5/3)
'''
삼성전자 = 50000
총평가금액 = 삼성전자 * 10
print(총평가금액)

시가총액 = 298000000000000
현재가 = 50000
PER = 15.70
print(시가총액, type(시가총액))
print(현재가, type(현재가))
print(PER, type(PER))

'''
'''
s = "hello"
t = "python"

print(s+'!', t)
'''
'''
a = "132"
# print(type(a))
# typr() 함수는 테이터 타입을 판별
'''
'''
num_str = "720"
num_int=int(num_str)
print(num_int, type(num_int))
'''
# num = 100
# num_str = str(num)
# print(num_str, type(num_str))

# num_str = "15.79"
# num_float = float(num_str)
# print(num_float, type(num_float))

'''
year = "2020"
print(int(year)-3)
print(int(year)-2)
print(int(year)-1)
'''
# month = 48584
# 총금액 = month * 36
# print(총금액)
#=================================================================
# 연습(11.13)
'''
apple = ['pad', 'phone', 'pods', 'max', 'book', 'tag']
print(len(apple))
apple.append('keyboard')
print(apple)
print(len(apple))

apple.extend(['vision', 'mac'])
print(apple)

apple.insert(5, 'pro')
print(apple)

apple.remove('keyboard')
print(apple)
print(apple.pop())
print(apple.pop(3))
print(apple)

apple.sort()
print(apple)
apple.sort(reverse=True)
print(apple)

sorted_apple = sorted(apple)
sorted_apple_r = sorted(apple, reverse=True)
print(sorted_apple)
print(sorted_apple_r)
print(apple)
'''
'''
letters = "python"
print(letters[0], letters[2]) # p t

license_plate = "24가 2210"
print(license_plate[3:]) # 2210

string = "홀짝홀짝홀짝"
print(string[::2]) # 홀홀홀

string = "python"
print(string[::-1]) # nohtyp

phone_number = "010-1234-5678"
phone_number1 = phone_number.replace("-", "")
print(phone_number1) # 010 1234 5678

string = 'abcdfe2a354a32a'
string1 = string.replace("a", "A")
print(string1)

a = "3"
b = "4"
print(a + b) # 34

a = '-'
print(a*80)

t1 = "python"
t2 = "java"
t3 = t1 + ' ' + t2 + ' '
print(t3 * 4)

name1 = "김민수" 
age1 = 10
name2 = "이철희"
age2 = 13
print(이름: {name1} 나이: {age1}
 이름: {name2} 나이: {age2})

상장주식수 = "5,969,782,550"
컴마제거 = 상장주식수.replace(",","")
형변환 = int(컴마제거)
print(형변환, type(형변환))

분기 = "2020/03(E) (IFRS연결)"
print(분기[:7])

data = "   삼성전자    "
data1 = data.strip()
print(data1) # 문자열에서 strip() 사용시 좌우 공백 제거
'''

# price = ['20180728', 100, 130, 140, 150, 160, 170]
# print(price[1:]) # [100, 130, 140, 150, 160, 170]

# nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
# print(nums[::2]) # [1, 3, 5, 7, 9]
# print(nums[1::2]) # [2, 4, 6, 8, 10]
# print(nums[::-1]) # [10, 9, 8, 7, 6, 5, 4, 3, 2, 1]

# interest = ['삼성전자', 'LG전자', 'Naver']
# print(interest[0], interest[2]) # 삼성전자 Naver

# string = "삼성전자/LG전자/Naver"
# interest = string.split("/")
# print(interest) # ['삼성전자', 'LG전자', 'Naver']

# data = [2, 4, 3, 1, 5, 10, 9]
# data.sort()
# print(data) # [1, 2, 3, 4, 5, 9, 10]

# my_variable = ()
# print(type(my_variable)) # <class 'tuple'>

# tuple1 = (1,)
# print(tuple1) # (1,)

# interest = ('삼성전자', 'LG전자', 'SK Hynix')
# list1 = list(interest)
# print(type(list1)) # <class 'list'>

# interest = ['삼성전자', 'LG전자', 'SK Hynix']
# tuple1 = tuple(interest)
# print(type(tuple1)) # <class 'tuple'>

# temp = ('apple', 'banana', 'cake')
# a, b, c = temp
# print(a, b, c) # apple banana cake

# data = tuple(range(2, 100, 2))
# print( data ) # (2, 4, 6, 8, 10, 12, 14, 16, 18, 20, 22, 24, 26, 28, 30, 32, 34, 36, 38, 40, 42, 44, 46, 48, 50, 52, 54, 56, 58, 60, 62, 64, 66, 68, 70, 72, 74, 76, 78, 80, 82, 84, 86, 88, 90, 92, 94, 96, 98)

# a = 10
# b = 20
# print("a의 값은 ", a)
# print("b의 값은 ", b)
# print("a와 b의 합은", a + b)

# # 파이썬 분기문
# print(3 == 5) # False
# x = 4
# print(1 < x < 5) # True
# print ((3 == 3) and (4 != 3)) # True


# 11월 17일 복습
#구분자
# year, month, day, hour, minute, second = input().split()

# print(year, month, day, sep='-', end='T')
# print(hour, minute, second, sep=':')2025, 11, 17, 21, 26, 37
# #논리 연산자
# korean = 92
# english = 47
# mathematics = 86
# science = 81
 
# print(korean >= 50 and english >= 50 and mathematics >= 50 and science >= 50)

# kor = int(90)
# eng = int(81)
# mat = int(86)
# sci = int(80)

# print(kor >= 90 and eng > 80 and mat > 85 and sci >=80)

# kor1 = int(90)
# eng1 = int(80)
# mat = int(85)
# sci1 = int(80)

# print(kor1 >= 90 and eng1 > 80 and mat1 > 85 and sci1 >=80)


#  문자열 여러줄

# s = ("""
# 'Python' is a 'programming language'
# that lets you work quickly
# and
# integrate systems more effectively.
# """)
# print(s)

# 튜플 리스트, rangeI()

# a = tuple(range(-10, 10, 2))
# b = tuple(range(-10, 10, 3))
# print(a, b, sep = '\n')

# 11 18 슬라이스부터 할것

# 11, 19 추가 문제

'''
문제 : 로그인 시스템 구현

임의의 id와 비밀번호 세팅
중첩 while문 사용
breat, continue 사용할 것
실행 화면과 같은 모습으로 만들어주세요
'''


# my_id = "kimwjdhyun"
# my_pw = "123321"

# while True :
    # print('''
    #       "=== 로그인 화면 ===
    #       1. 로그인
    #       2. 종료"
    #       ''')
    # check = int(input("선택 : "))

    # if check == 1 :
    #     user_id = input(" ID : ")
    #     user_pw = input(" PW : ")
    #     if user_id == my_id and user_pw == my_pw :
    #         print(" 로그인 성공 ! ")

    #         while True :
    #             print('''
    #                       "===== 메 뉴 =====
    #                       1. 정보 보기
    #                       2. 설 정
    #                       3. 로그아웃
    #                       ================"
    #                       ''')
                    
    #             menu_check = int(input(" 메뉴 선택 : "))

    #             if menu_check == 1 :
    #                     print("회원 정보입니다.")
    #             elif menu_check == 2 :
    #                     print("설정 메뉴입니다.")
    #             elif menu_check == 3 :
    #                  print("로그아웃합니다.")
    #                  break
    #             else :
    #                  print("잘못된 선택입니다.")
    #                  continue
                
    #         if check == 2 :
    #             print("종료합니다.")
    #             break
        
    #     else :
    #          print("로그인 실패!")
    # elif check == 2:
    #      print("종료합니다.")
    #      break
    # else : 
    #      print("잘못된 선택입니다.")


# 11-19 코딩도장 복습
# x = 0
 
# if x == 4:
#     print('A')
# elif x == 3:
#     print('B')
# elif x == 2:
#     print('C')
# elif x == 1:
#     print('D')
# else:
#     print('E')


# 표준 입력으로 나이(만 나이)가 입력됩니다(입력 값은 7 이상 입력됨).
#  교통카드 시스템에서 시내버스 요금은 다음과 같으며 각 나이에 맞게 요금을 차감한 뒤 
# 잔액이 출력되게 만드세요(if, elif 사용). 현재 교통카드에는 9,000원이 들어있습니다.

# 어린이(초등학생, 만 7세 이상 12세 이하): 650원
# 청소년(중∙고등학생, 만 13세 이상 18세 이하): 1,050원
# 어른(일반, 만 19세 이상): 1,250원

# age = int(input())
# balance = 9000

# if age >= 19 :
#     balance -= 1250
# elif age >= 13 :
#     balance -= 1050
# elif age >= 7 :
#     balance -= 650

# print(balance)


# for i in range(1, 10):
#     for j in range(1, 10):
#         print(f"{i} x {j} = {i * j}")

# i = 2
# j = 5

# while i <= 32 or j>= 1 :
#     print(i, j)
#     i *= 2
#     j -= 1

# amount = int(input())


# while amount>= 1350 :
#     amount -= 1350
#     print(amount)

'''
user_id = "codingon"
user_pw = "abc123"

while True:     # 전체 프로그램 반복
    print("=== 로그인 화면 ===")
    print("1. 로그인")
    print("2. 종료")
    main_sel = input("선택: ")
    
    if main_sel == "2":
        print("프로그램을 종료합니다.")
        break
    elif main_sel != "1":
        print("잘못 선택하셨습니다.\n")
        continue
    
    # 로그인
    id_input = input("ID : ")
    pw_input = input("PW : ")
    
    if id_input != user_id or pw_input != user_pw:
        print("로그인 실패! 다시 시도해주세요.\n")
        continue
    
    print("로그인 성공!\n")
    
    # 로그인 후 메뉴 화면
    while True:
        print("=== 메뉴 ===")
        print("1. 정보 보기")
        print("2. 설정")
        print("3. 로그아웃")
        print("============")
            
        sel = input("메뉴 선택: ")
        
        if sel == "1":
            print("회원 정보입니다.\n")
            continue
        elif sel == "2":
            print("설정 메뉴입니다.\n")
            continue
        elif sel == "3":
            print("로그아웃합니다.\n")
            break  # 안쪽 while만 끊고 로그인 화면으로
        else:
            print("잘못 입력하셨습니다.\n")
            continue
        '''
'''
start, stop = map(int, input().split())
 
i = start
 
while True:
    if i > stop:
        break
    if i % 10 == 3:
        i += 1
        continue
    print(i, end=' ')
    i += 1

# 21 33
# 21 22 24 25 26 27 28 29 30 31 32    
'''


# 함수

def print_coin() :
    print("비트코인")
print_coin()

for i in range(100) :
    print_coin()

def print_coin() :
    for i in range(100) :
        print("비트코인")
print_coin()

# hello()
# def hello():
#     print("Hi")
# 함수를 정의하기 전에 호출을 함

def message() :
    print("A")
    print("B")

message()
print("C")
message()

# A
# B
# C
# A
# B

def print_with_smile(string) :
    print(string, ":D")

print_with_smile("안녕하세요")

def print_uppwe_price(price) :
    print(price * 1.3)

def print_sum(a, b) :
    print( a + b )

def print_arithmetic_operation(a, b) :
    print(a, "+", b, "=", a + b)
    print(a, "-", b, "=", a - b)
    print(a, "*", b, "=", a * b)
    print(a, "/", b, "=", a / b)
print_arithmetic_operation(3, 4)
# 3 + 4 = 7
# 3 - 4 = -1
# 3 * 4 = 12
# 3 / 4 = 0.75

def print_max(x, y, z) :
    if x >= y and x >= z :
        print(x)
    elif y >= x and y >= z :
        print(y)
    elif z >= x and z >= y :
        print(z)

print_max(10, 5, 8)   # 10
print_max(3, 15, 7)   # 15
print_max(6, 2, 20)   # 20

def print_reverse(string) :
    print(string[::-1])
print_reverse("python") # nohtyp

def print_score(score) :
    print(sum(score) / len(score))
print_score([1, 2, 3]) # 2.0

def print_even(even_list) :
    for i in even_list :
        if i % 2 == 0:
            print(i)
print_even([1, 3, 2, 10, 12, 11, 15])
# 2
# 10
# 12

def print_key(dic) :
    for key in dic :
        print(key)
print_key ({"이름":"김말똥", "나이":30, "성별":0})

# 이름
# 나이
# 성별

My_dict = {"10/26" : [100, 130, 100, 100],
           "10/27" : [10, 12, 10, 11]}

def print_value_by_key (My_dict, key) :
    print(My_dict[key])

print_value_by_key(My_dict, "10/26") # [100, 130, 100, 100]

def print_5xn(string) :
    num = int(len(string) / 5)
    for i in range(num + 1) :
        print(string[i*5 : 5+5])

def solution(ineq, eq, n, m):
    answer = 0
    
    if n > m and ineq ==">":
        answer = 1
    elif n < m and ineq == "<":
        answer = 1
    elif n == m and eq == "=":
        answer = 1

    return answer

def solution(a, b, flag):
    answer = 0
    
    if flag == True:
        answer = int(a + b)
        return answer
    elif flag != True:
        answer = int(a - b)
        return answer
    
def solution(code):
    ret = ""
    mode = 0
    
    for i in range(len(code)):
        if code[i] == "1":
            mode = 1 - mode 
        else:
            if mode == 0:
                if i % 2 == 0:
                    ret += code[idx]
            else:
                
                if i % 2 == 1:
                    ret += code[i]
    
    return ret if ret else "EMPTY"