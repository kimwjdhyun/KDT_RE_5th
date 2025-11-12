#  정수형 (interger, int)
#  크기 제한이 없다
my_int1 = 100
my_int2 = 10999999999999999999999999999999999999999999999999
print(type(my_int1)) # <class 'int'>

# 실수형 (float)
# 부동 소수점 방식
my_float = 100.0
print(type(my_float)) # <class 'float'>

# 문자열(string, str)
my_str1 = ' ' # 빈 문자열
my_str2 = " " # 공백 문자열
my_str3 = "안녕하세요"

# 문자열 여러줄로 만들기
multi_str = """코딩을하는
처음 배우는
파이썬 언어
"""
print(multi_str)
print(type(my_str1)) #<class 'str'>

# 따옴표 속에 따옴표 쓰기
print("'python'코딩언어")
# print(""에러"")

#불리언형 = 논리형 (boolean, bool)
# 참과 거짓을 표현하는 자료형
print(True)
print(False)
print(type(True)) # <class 'bool'>

# 형 변환(Type casting)
# 명시적 형변환 vs 암시적 형변한

# 1. 정수로 변환 : int()
# 1) 실수 -> 정수
# 2) 문자열로 표현된 정수 -> 정수
# 3) 논리형 -> 정수
# 가능한 경우
print(int(3.14)) # 3
print(int("100")) # 100
print(int(True)) # 1
print(int(False)) # 0
# 불가능한 경우
# print(int("3.14")) 실수의 문자열 x
# print(int("abc")) 숫자가 아닌 문자열 x

# 실수로 변환 : float()
'''
1) 정수 -> 실수
2) 문자열로 표현된 실수 -> 실수
3) 문자열로 표현된 정수 -> 실수
4) 논리형 -> 실수
'''

# 가능한 경우
print(float(7)) # 7.0
print(float('3.14')) # 3.14
print(float('100')) # 100.0
print(float(True), float(False)) # 1.0 0.0
# 불가능한 경우
# print(float("abc")) 숫자가 아닌 문자형은 x

# 암시적 형변환
# 정수와 실수의 연산에서 자동으로 실행되는 연산
print(10 + 5.0) # 15.0

# 문자열로 변환 : str()
# 논리형으로 변환 : bool()
print (bool(1)) # True

