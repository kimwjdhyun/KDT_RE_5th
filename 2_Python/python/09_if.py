'''
조건문
- 조건에 따라 프로그램의 실행 흐름을 분기시키는 제어문
- 조건 : 참 / 거짓을 구분할 수 있는 문장
'''
'''
# 조건문의 기초 문법
# if + 조건 -> 조건이 참이면 실행
# 들여쓰기 중요!!
a = int(input())
if a > 10:
    print("a는 10보다 커요.")
print("조건문 종료")

# # 들여쓰기 에러 예시
if a>10:
  print("조건문 종료")

print("a는 10보다 커요.") # IndentationError : 들여쓰기 오류

# 조건문에 실행할 코드를 작성하지 않았을 때
# pass로 해당 조건문을 넘어갈 수 있음
if a > 100:
   pass # 비워둘 경우 pass를 써야함(안쓸경우 에러 발생)

# 실습 2. if 조건문 연습
# 문제1. 날씨에 따른 준비물 안내
weather = input("오늘 날씨는 어떤가요?(비 / 맑음) :")
weather1 = "비"
weather2 = "맑음"
if weather==weather1:
   print("우산을 챙기세요!") # 비 / 우산을 챙기세요!
if weather==weather2:
    print("선크림을 바르세요!") # 맑음 / 선크림을 바르세요!

# if -else 문
# 조건이 참일 때는 if문을, 조건이 거짓일 때는 else문 실행
# else -> ~이 아니라면의 의미 -> 조건이 필요 x, if문과 반드시 같이 나와야 함.
a = int(input())
if a> 10:
    print("a는 10보다 커요.") # 4 / a는 10보다 작아요.
else:
    print("a는 10보다 작아요.") # 16 / a는 10보다 커요.

# 실습 2. if -else 연습
# 문제 1. 짝수 홀수 판별하기
number = int(input("정수를 입력해 주세요. :"))
if number%2 == 1:
    print("홀수입니다.") # 36 / 짝수입니다.
else:
    print("짝수입니다.") # 9999 / 홀수입니다.


# if -elif -else 문
# elif : else if의 약자
# elif에서 조건을 반드시 기록
# if가 있어야만 사용 가능

score = int(input())
if score>=90: 
    print("A") # 99 / A
elif score >=80:
    print("B") # 85 / B
elif score >=70:
    print("C") # 73 / C
elif score>=60:
    print("D") # 61 / D
else:
    print("F") # 13 / F


# 실습 3. if -elif -else문 연습
# 문제1. 나이에 따른 영화 관람 가능 여부
age = int(input("관람 가능 등급 : "))
if age >= 19:
    print("청소년 관람불가 가능") # 28 / 청소년 관람불가 가능
elif age >= 16:
    print("15세 이상 관람가") # 17 / 15세 이상 관람가
elif age >= 13:
    print("12세 이상 관람가") # 14 / 12세 이상 관람가
else:
    print("전체 관람가") # 7 / 전체 관람가

'''
# 문제2. 시, 분, 초 구하기
# time = int(input("초를 입력해주세요. :"))
# minute = time // 60
# second = time % 60
# hour = minute // 60
# minute %= 60

# if hour > 0:
#     print(f"{hour}시간 {minute}분 {second}초") # 4321 / 1시간 12분 1초
# elif minute > 0:
#     print(f"{minute}분 {second}초") # 123 / 2분 3초
# else:
#     print(f"{second}초") # 37 / 37초


# 해설
#60s = 1m, 6-m = 1h
# time = int(input("초를 입력하세요. :"))
# minute = time // 60
# second = time % 60
# hour = minute // 60
# minute %= 60

# if hour>0:
#     print(f"{hour}시간 {minute}분 {second}초")
# elif minute > 0:
#     print(f"{minute}분 {second}초")
# else:
#     print(f"{second}초")

# 중첩 조건문
# 하나의 if 문 안에 또 다른 if 문을 사용하는 것

# user_name = input("관리자 아이디를 입력하세요. :")
# password = input("비밀번호를 입력하세요. :")

# if user_name == "admin":
#     if password == "abcd":
#         print("로그인 성공") # 관리자 아이디를 입력하세요. :admin 비밀번호를 입력하세요. :abcd 로그인 성공
#     else:
#         print("비밀번호가 잘못됐습니다.") # 관리자 아이디를 입력하세요. :admin 비밀번호를 입력하세요. :sdfa 비밀번호가 잘못됐습니다.
# else:
#     print("잘못된 사용자입니다.") # 관리자 아이디를 입력하세요. :ad 비밀번호를 입력하세요. :cdsd 잘못된 사용자입니다.



# # 실습3. 중첩 조건문 연습
# # 문제 1. 편의점 도시락 구매하기

# food = input("식품명을 입력하세요.")
# price = int(input("금액을 입력하세요."))

# if food == "김밥":
#     if price >= 2500:
#         print("구매가 완료되었습니다.")
#     else:
#         print("잔액이 부족합니다.")
# if food == "삼각김밥":
#     if price >= 1500:
#         print("구매가 완료되었습니다.")
#     else:
#         print("잔액이 부족합니다.")
# if food == "도시락":
#     if price >= 4000:
#         print("구매가 완료되었습니다.")
#     else:
#         print("잔액이 부족합니다.")

# 해설
# 실습 5. 편의점 도시락 구매하기
#1)
# money = int(input("금액을 넣어주세요. :"))
# item = input("김밥 / 삼각김밥 / 도시락 중 골라주세요!") # 보기를 제시하는게 좋음, 의도한대로 되지 않을 수 있기 때문에

# KIMBAB = "김밥" # 변수 = 변하는 값, 상수 = 변하지 않는 값(보통 모두 대문자로 작성해서 표기)
# SAMKIM = "삼각김밥"
# DOSIRAK = "도시락"
# k_price, s_price, d_price = 2500, 1500, 4000

# if item == KIMBAB:
#     if money >= k_price:
#         print(f"{KIMBAB}을 구매했습니다.")
#     else:
#         print("금액이 부족해요.")
# elif item == SAMKIM:
#     if money >= s_price:
#         print(f"{SAMKIM}을 구매했습니다.")
#     else:
#         print("금액이 부족해요. ")
# elif item >= DOSIRAK:
#     if money >= d_price:
#         print(f"{DOSIRAK}을 구매했습니다.")
#     else:
#         print("금액이 부족해요. ")
# else: 
#     print("입력이 잘못됐습니다. ")

# 2) 딕셔너리 사용(간소화)
# money = int(input("금액을 넣어주세요. :"))
# item = input("김밥 / 삼각김밥 / 도시락 중 골라주세요!")

# prices = {
#     "김밥" : 2500, 
#     "삼각김밥" : 1500, 
#     "도시락" : 4000
# }
# if item in prices:
#     if money >= prices[item]:
#         print(f"{item}을 구입했습니다.")
#     else:
#         print("금액이 부족해요.")
# else :
#     print("입력이 잘못됐습니다. ")