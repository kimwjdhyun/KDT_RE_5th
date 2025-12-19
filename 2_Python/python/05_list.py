'''
리스트(list)
- 여러 값들을 순서대로 저장할 수 있는 자료형
- 인덱스(index) : 각 값에 부여된 순서(0부터 시작)
- 가변 자료형(mutable) : 원소의 추가/수정/삭제 가능
'''

# 리스트 만들기
# list1 = [] # 빈 리스트
# list2 = ["안녕하세요", "반갑습니다"]
# list3 = [10, "좋아요.", 3.14, [1,2,3,4,]]

# print(list1, list2, list3)

# list4 = list()
# list5 = list("코딩온")
# print(list4, list5)


# # ===============
# # 인덱싱과 슬라이싱
# my_list = [1,2,3,4,5]
# print(my_list[0]) # 1
# print(my_list[-1]) # 5
# my_list[3] = -1
# print(my_list) # 리스트는 수정이 가능하다.

# # number = input("네 자릿수 정수를 입력하세요 :")
# number = [0, 1, 2, 3]
# 천 = number[0]
# 백 = number[1]
# 십 = number[2]
# 일 = number[3]
# print(천, 백, 십, 일)

# # -----------
# # 슬라이싱
# my_numbers = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100]
# print(my_numbers[1:4]) # [20, 30, 40]
# print(my_numbers[3:]) # [40, 50, 60, 70, 80, 90, 100]
# print(my_numbers[:4]) # [10, 20, 30, 40]
# my_numbers[2:4] = [300, 400]
# print(my_numbers)

#  실습 1.
# 문제1. 첫 번째 요소와 마지막 요소 출력하기
# nums = [10, 20, 30, 40, 50]
# print(nums[0], nums[-1])

# 문제 2. 가운데 세 개의 요소 추출하기
# nums = [100, 200, 300, 400, 500, 600, 700]
# print(nums[2:5])

# 문제 3. 리스트의 원소 두배 하기
# nums = [1, 2, 3, 4, 5]
# nums[:] = [2, 4, 6, 8, 10] 
# print(nums[:])

#  문제 4. 리스트 뒤집어서 출력하기
# items = ["a", "b", "c", "d", "e"]
# print(items[::-1])

#  문제 5. 짝수 인덱스 요소만 출력하기
# data = ["zero", "one", "two", "three", "four", "five"]
# print(data[0],data[2],data[4])
# print(data[::2]) #<- 두칸 간격으로 슬라이싱

#  문제 6. 슬라이싱으로 리스트 수정하기
# movies = ["인셉션", "인터스텔라", "어벤져스", "라라랜드", "기생충"]
# movies[2:4] = ["매트릭스", "타이타닉"]
# print(movies)

# 문제 7. 특정 규칙에 따라 요소 추출
# subjects = ["국어", "수학", "영어", "물리", "화학", "생물", "역사", "지구과학", "윤리"]
# print(subjects[3::2])
# print(subjects[3:8:2]) # <- 3번 인덱스부터 2칸씩 추출

# 문제 8. 리스트를 3개 구간으로 나누어 역순 병합
# data = ["A", "B", "C", "D", "E", "F", "G", "H", "I"]
# x = data[:3]
# y = data[4:7]
# z = data[6:]
# print(x[::-1], y[::-1], z[::-1])
# print(data[0:3][::-1], end=" ")
# print(data[3:6][::-1], end=" ")
# print(data[6:][::-1]) # <- 줄바꿈 없애기 활용!

# 인덱싱, 슬라이싱 주의 사항
# my_list = [1, 2, 3, 4]
# my_list[5]
# my_list[5] # IndexError: list index out of range

# my_list = [1, 2, 3, 4, 5]
# print(my_list[4:1:2]) # []
# print(my_list[1:3:-1]) # []

#================
# 리스트 연산 - del
'''
my_list = [10, 20, 30, 40, 50]
del my_list[2] # 특정 요소 삭제
print(my_list) # [10, 20, 40, 50]
del my_list[1:3] # 슬라이스 범위 삭제
print(my_list) # [10, 50]
del my_list # 리스트 삭제
print(my_list) # NameError: name 'my_list' is not defined
'''

# 리스트 연산 - +
'''
list1 = ["가", "나", "다"]
list2 = ["라", "마", "바"]
new_list = list1 + list2
print(list1, list2, new_list, sep="/") # ['가', '나', '다']/['라', '마', '바']/['가', '나', '다', '라', '마', '바']
'''

# 리스트 반복 - *
'''
medal = ["금", "은", "동"]
new_list = medal * 3
print(medal, new_list, sep=" / ") # ['금', '은', '동'] / ['금', '은', '동', '금', '은', '동', '금', '은', '동']

'''
# 포함 여부 (in, not in)
'''
fruits = ["토마토", "사과", "수박", "바나나", "포도"]
print("포도" in fruits) # True
print("참외" not in fruits) # True
'''


# 실습 2.
# 문제 1. 부분 삭제 후 연결
# fruits = ["apple", "banana", "cherry", "grape", "watermelon", "strawberry"]
# del fruits[1:4]
# print("result", fruits) # 해설 result = fruits[:1] + fruits[1:]


# 문제 2. 반복 리스트 내부 요소 삭제
# letters = ["A", "B"]
# new_letters = letters * 3
# del new_letters[2]
# print(new_letters)

#====================
# 리스트 주요 메서드
#====================
'''
# 길이
numbers = [1,2,3,4,5]
print("1.len()", len(numbers), len("codingon")) # 1. len() 5 8

# # 삽입
numbers.append(6)
numbers.append(7)
numbers.append(8)
print("2. append()", numbers) # 2. append() [1, 2, 3, 4, 5, 6, 7, 8]

numbers. insert(2, 2.5)
numbers. insert(4, 3.5)
print("3. insert()", numbers) # 3. insert() [1, 2, 2.5, 3, 3.5, 4, 5, 6, 7, 8]

numbers.extend([9, 10])
print("4. extend()", numbers) # 4. extend() [1, 2, 2.5, 3, 3.5, 4, 5, 6, 7, 8, 9, 10]

# # 삭제
numbers.append(2.5)
numbers.remove(2.5)
print("5. remove()", numbers) # 5. remove() [1, 2, 3, 3.5, 4, 5, 6, 7, 8, 9, 10, 2.5]

a = numbers.pop(1)
print("6. pop()삭제한 요소", a) # 6. pop()삭제한 요소 2
print(numbers) # [1, 3, 3.5, 4, 5, 6, 7, 8, 9, 10, 2.5]
b = numbers.pop()
print("6. pop()삭제한 요소", b) # 6. pop()삭제한 요소 2.5
print(numbers) # [1, 3, 3.5, 4, 5, 6, 7, 8, 9, 10]

# # 정렬
numbers1 = [3,2,1,4]
numbers1.sort()
print("7-1. sort()", numbers1) # 7-1. sort() [1, 2, 3, 4]
numbers1.sort(reverse=True)
print("7-1. sort(reverse=True)", numbers1) # 7-1. sort(reverse=True) [4, 3, 2, 1]

numbers2 = [50, 52, 53, 51]
new_numbers = sorted(numbers2)
new_numbers_desc = sorted(numbers2, reverse=True) # desc : 내림차순
print("7-2. sorted()", numbers2, new_numbers, new_numbers_desc) # 7-2. sorted() [50, 52, 53, 51] [50, 51, 52, 53] [53, 52, 51, 50]
'''

# reverse() : 리스트 요소 뒤집기
my_numbers = [100,101,104, 103, 102]
my_numbers.reverse() # 리스트 자체를 뒤집음(원본 변경)
print("8-1. reverse()", my_numbers) # sort(reverse=True)는 정렬, reverse()는 뒤집기만 함.
# 출력 : 8-1. reverse() [102, 103, 104, 101, 100]

my_numbers2 = list(reversed(my_numbers)) # reversed()는 원본 배열을 바꾸지않음
print("8-2. reversed()", my_numbers2, my_numbers)
# 출력 : 8-2. reversed() [100, 101, 104, 103, 102] [102, 103, 104, 101, 100]

# count, max, min, sum 
numbers = [1, 2, 2, 2, 2, 3, 4, 5, 6, 7]
print("9. count()", numbers.count(2)) # 9. count() 4
print("10. max/min", max(numbers), min(numbers)) # 10. max/min 7 1
print("11. sum", sum(numbers)) # 11. sum 34

# 실습 1. 리스트 주요 메서드 복습 문제
# 문제 1. 기차 탑승 시뮬레이션

a = ["철수", "영희"]
a.extend(["민수", "지훈"])
print(a) # ['철수', '영희', '민수', '지훈']
a.remove("영희")
print(a) # ['철수', '민수', '지훈']
a.insert(1, "수진")
print(a) # ['철수', '수진', '민수', '지훈']
a.remove("민수")
a.reverse()
print(a) # ['지훈', '수진', '철수']



# 문제 2. 숫자 처리 게임

card = [5, 3, 7]
card.extend([4, 9])
print(card) # [5, 3, 7, 4, 9]
print(max(card), min(card)) # 9 3
print(sum(card)) # 28
card.sort()
print(card) # [3, 4, 5, 7, 9]
card.pop()
print(card) # [3, 4, 5, 7]


