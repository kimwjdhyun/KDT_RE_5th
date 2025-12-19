'''
딕셔너리(dictionary)
- 키 -값 쌍으로 묶어서 데이터를 저장하는 자료형
- 키는 유일해야함. 값은 중복이 가능
- 변경가능한 자료형
- 순서가 보장되지 않았다가, 파이썬 3.7 이후 순서가 보장됨.
'''

# dict 만들기
d1 = {} # 빈 dict 만들기
print(type(d1)) # <class 'dict'>

person = {"name" : "홍길동", "age" : 25}
print(person) # {'name': '홍길동', 'age': 25}

d2 = dict()
print(d2, type(d2)) # {} <class 'dict'>

# 키가 문자열일 때 가능한 방법
movie = dict(title="inter", director="nolan")
print(movie, movie["director"]) # {'title': 'inter', 'director': 'nolan'} nolan
# 대괄호 사용으로 해당 부분만 출력 가능

# 리스트나 튜플로 만들기
pairs = [("name", "wjdhyun"), ("age", 28), ("job", "none")]
person2 = dict(pairs)
print(person2) # {'name': 'wjdhyun', 'age': 28, 'job': 'none'}

# zip() 함수 활용
keys = ["title", "director", "year"]
value = ["기생충", "봉준호", "2019"]
movie2 = dict(zip(keys, value))

print(movie2) # {'title': '기생충', 'director': '봉준호', 'year': '2019'}

# 키로 사용할 수 없는 자료형
# 키 - 불변 자료형만 사용해야 한다.
d1 = {(1, 2, 3) : (1, 2, 3)} # 튜플은 불변자료형 => 사용 가능
d2 = {1 : 10} # 숫자 사용 가능
# d3 = {[1, 2, 3] : "리스트 값을 키로?"} # TypeError: cannot use 'list' as a dict key (unhashable type: 'list')
# print(d3) # 리스트는 사용 불가 !



# dict 데이터 조회
print(person2["name"]) # wjdhyun
print(person2["age"]) # 28
# print(person2["city"]) # KeyError: 'city' 존재하지 않는 키는 에러 발생!
print(person2.get("city")) # None # get() 함수는 키가 없을 경우 None을 반환함.(default값이 None)

print(person2.get("email", "이메일이 존재하지 않습니다.")) # 이메일이 존재하지 않습니다.

# get() 사용 예제
user_data = {
    "username" : "wjdhyun",
    "email" : "wjdhyun@naver.com",
    "password" : "123456789"
}

key = input("조회할 정보를 입력하세요(username, email, password):")
result = user_data.get(key, "존재하지 않는 데이터 입니다.") # 조회할 정보를 입력하세요(username, email, password):name
print(result) # 존재하지 않는 데이터 입니다.

# 데이터 추가 및 수정
# 1) 기본적인 추가, 수정 방법
user_data["phone"] = "010-1234-5678" 
user_data["username"] = "kimwjdhyun"
print(user_data) # {'username': 'kimwjdhyun', 'email': 'wjdhyun@naver.com', 'password': '123456789', 'phone': '010-1234-5678'}

# 2) update() 메서드 활용
user_data.update({"nickname" : "kim"})

# 키가 문자열인 경우
user_data.update(phone="010-9876-5432")

# 다른 딕셔너리 추가
extra_data = {"city" : "jeju"}
user_data.update(extra_data)

print(user_data) # {'username': 'kimwjdhyun', 'email': 'wjdhyun@naver.com', 'password': '123456789', 'phone': '010-9876-5432', 'nickname': 'kim', 'city': 'jeju'}

# 딕셔너리 데이터 삭제
del user_data["city"]
print(user_data) # city 항목 삭제

# 키로 제거(pop()메서드)
nickname = user_data.pop("nickname")
print("pop>> ",user_data, nickname, sep=" /// ") # pop>>  /// {'username': 'kimwjdhyun', 'email': 'wjdhyun@naver.com', 'password': '123456789', 'phone': '010-9876-5432'} /// kim

# 가장 마지막 요소를 제거(popitem())
phone = user_data.popitem()
print("popitem>> ", user_data, phone, sep = " /// ") # popitem>>  /// {'username': 'kimwjdhyun', 'email': 'wjdhyun@naver.com', 'password': '123456789'} /// ('phone', '010-9876-5432')

# dict 비우기(clear())
user_data.clear()
print("clear>> ", user_data) # clear>>  {} 빈 딕셔너리

# dict 삭제하기
del user_data
print(user_data) # NameError: name 'user_data' is not defined 삭제되서 에러 발생

# dict 주요 메서드
user_data = {
    "username" : "wjdhyun",
    "email" : "wjdhyun@naver.com",
    "password" : "123456789"
}

# keys() : 모든 키를 반환(리스트처럼 보이지만 실제 리스트는 x)
print("키", user_data.keys()) # 키 dict_keys(['username', 'email', 'password'])
print("키", list(user_data.keys())) # 키 ['username', 'email', 'password']

# values : 모든 값을 반환
print("값", list(user_data.values())) # 값 ['wjdhyun', 'wjdhyun@naver.com', '123456789']

# items : 모든 (키, 값)쌍을 반환
print("쌍", list(user_data.items())) # 쌍 [('username', 'wjdhyun'), ('email', 'wjdhyun@naver.com'), ('password', '123456789')]




# 실습 1. 딕셔너리 종합 문제(1)
user = {}
print(type(user)) # <class 'dict'>
user.update({"username" : "skywalker", "email" : "sky@example.com", "level" : "5"})
print(user) # {'username': 'skywalker', 'email': 'sky@example.com', 'level': '5'}
email_value = user["email"]
print(email_value) # sky@example.com
user["level"] = "6"
print(user) # {'username': 'skywalker', 'email': 'sky@example.com', 'level': '6'}
print(user.get("phone", "미입력")) # 미입력
user.update({"nickname" : "sky"})
user.pop("email")
print(user) # {'username': 'skywalker', 'level': '6', 'nickname': 'sky'}
user.update({"signup_date" : "2025-11-17"})
print(user.setdefault("signup_date", "2025-11-17")) # {'username': 'skywalker', 'level': '6', 'nickname': 'sky'}, 2025-11-17

# 실습2. 딕셔너리 종합 연습 문제(2)
students = {}
students.update({"Alice" : 85, "Bob" : 90, "Charlie" : 95})
print(students, type(students)) # {'Alice': 85, 'Bob': 90, 'Charlie': 95} <class 'dict'>
students.update({"David" : 80})
students["Alice"] = 88
students.pop("Bob")
print(students) # {'Alice': 88, 'Charlie': 95, 'David': 80}