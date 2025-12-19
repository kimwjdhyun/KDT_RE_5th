'''
튜블(tuple)
- 순서가 존재하는 여러 데이터의 모음
- 불변(immutable) 자료형(list와 다르게 수정 불가)
'''


# ---- 튜플 생성
'''
my_tuple = (1, 2, 3, 4)
print(my_tuple) # (1, 2, 3, 4)
print(type(my_tuple)) # <class 'tuple'>

my_tuple2 = 5, 6, 7, 8 # 괄호 생략 가능, but 명확성을 위해 사용 권장
print(type(my_tuple2)) # (1, 2, 3, 4)

# 원소가 하나인 튜플 생성
single_el_tuple = (100,)

# 튜플 생성 함수로 생성

# 튜플 생성 함수로 생성 
my_tuple2 = tuple()
print(my_tuple2) # ()

my_tuple3 = tuple("codingon")
print(my_tuple3) # ('c', 'o', 'd', 'i', 'n', 'g', 'o', 'n')


# ---- 언패킹 ----
# 시퀀스에 저장된 여러 값을 여러 변수에 나눠 저장하는 것
# 튜플, 리스트, 문자열 등 시퀀스에 해당하는 것은 모두 가능
apple, banana, kiwi = ("apple", "banana", "kiwi")
print(apple, banana, kiwi) # apple banana kiwi

'''
# ----------
'''
# 불변성(immutable)
# - 객체가 생성된 이후 내부 데이터를 변경할 수 없는 것
my_tuple[0] = 100 # TypeError: 'tuple' object does not support item assignment
# 삭제
del my_tuple[1] # TypeError: 'tuple' object doesn't support item deletion
# * 튜플은 변경 불가능
# >튜플 자체는 삭제가 가능, but 원소 삭제는 불가능
del my_tuple
print(my_tuple) # NameError: name 'my_tuple' is not defined. Did you mean: 'my_tuple2'?
#  NameError : 삭제
'''
#-------튜플 수정----------
'''
my_tuple4 = (10, 20, 30)
new_tuple = (100,) + my_tuple4[1:]
print("원본 튜플", my_tuple4)     # 원본 튜플 (10, 20, 30)
print("새로운 튜플", new_tuple)   # 새로운 튜플 (100, 20, 30)
#  수정을 하게 되면 새로운 튜플 생성(원본은 변하지 않음)
'''

# 실습1. 튜플 종합 연습

#step1. 손상되 고객 정보 복원
# 고객 이름을  'eunji'로 변경
# 수정한 결과를 restored_user에 저장하고 출력
user = ("minji", "25", "seoul")
restored_user = ("eunji",) + user[1:]
print(restored_user) # ('eunji', 25, 'seoul')

#step2. 언패킹
# 튜플 restored_user 언패킹 하여 name, age, city에 저장
name, age, city = restored_user
print(restored_user) # ('eunji', '25', 'seoul')

# step3. 통계 분석
# minji 등장 횟수 출력
# soojin 등장 위치(인덱스)
users =  ("minji", "eunji", "soojin", "minji", "minji")
print(users.count("minji")) # 3
print(users.index("soojin")) # 2

# step4. 정렬

users2 = list(users)
print(users2) # ['minji', 'eunji', 'soojin', 'minji', 'minji']
users2[:] = ["민지", "은지", "수진", "민지", "민지"]
users2.sort()
print(users2) # ['민지', '민지', '민지', '수진', '은지']
users2_t = tuple(users2)
print(users2_t) # ('민지', '민지', '민지', '수진', '은지')