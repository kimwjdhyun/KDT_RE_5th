'''
set(집합)
- 원소의 중복을 허용하지 않는 여러 데이터의 모음
- 순서가 없는 컬렉션 자료형
'''

# set 만들기
s1 = {1,2,3}
print(s1, type(s1)) # {1, 2, 3} <class 'set'>

s2 = {1,1,1,1,1,2,2,2,3,3,3,3,3,4,4,}
print(s2) # {1, 2, 3, 4}, 중복 허용 x(자동 제거)

# 빈 set 만들기
# - 중괄호에 원소를 넣지 않고 만들면 빈 dict(dictionary)로 인식됨
s3 = {}
print(type(s3)) # <class 'dict'>

# set 함수로 생성
s4 = set()
print(s4, type(s4)) # set() <class 'set'>

# set 함수의 활용 : 원소의 중복 제거
my_list = [1,1,1,1,2,2,2,3,3,3,3,4,4,4,4]
s5 = set(my_list)
print(s5, type(s5)) # {1, 2, 3, 4} <class 'set'>

# 인덱싱 x
# s1[1] # TypeError: 'set' object is not subscriptable

##**해시값에 대해 공부하기**

# 자료형 제한
# - 가변 자료형은 원소로 사용할 수 없다.
# s1 = {1,2,3,[1,2,3]} # TypeError: cannot use 'list' as a set element (unhashable type: 'list')
'''
# set 연산
# - 집합의 연산 : 합집하브 교집합, 차집합, 대칭차집합
a = {1,2,3}
b = {3,4,5}

# 합집합 (|, .union())
s_union1 = a | b
s_union2 = a.union(b)
print("합집합", s_union1) # 합집합 {1, 2, 3, 4, 5}
print("합집합", s_union2) # 합집합 {1, 2, 3, 4, 5}

# 교집합(&, .intersection())
s_inter1 = a & b
s_inter2 = a.intersection(b)
print("교집합", s_inter1) # 교집합 {3}
print("교집합", s_inter2) # 교집합 {3}

# 차집합 (-, difference())
s_diff1 = a - b
s_diff2 = a.difference(b)
print("차집합", s_diff1) # 차집합 {1, 2}
print("차집합", s_diff2) # 차집합 {1, 2}
print(b-a) # {4, 5}

# 대칭 차집합 (^, symmetric_difference)
s_symm1 = a ^ b
s_symm2 = a.symmetric_difference(b)
print("대칭 차집합", s_symm1) # 대칭 차집합 {1, 2, 4, 5}
print("대칭 차집합", s_symm2) # 대칭 차집합 {1, 2, 4, 5}
'''
'''
# 실습 1. set 종합 연습
# 문제1. 중복 제거 및 개수 세기

submissions = ['kim', 'lee', 'kim', 'park', 'choi', 'lee', 'lee']
submissions1 = set(submissions)
print(submissions1)                        # {'kim', 'park', 'choi', 'lee'}
print("제출한 학생 수:", len(submissions1)) # 제출한 학생 수: 4
print("제출자 명단:", submissions1)         # 제출자 명단: {'kim', 'park', 'choi', 'lee'}

# 문제2. 공통 관심사 찾기
user1 = {'SF', 'Action', 'Drama'}
user2 = {'Drama', 'Romance', 'Action'}
print("공통 관심 장르: ",user1&user2) # 공통 관심 장르:  {'Drama', 'Action'}
print("서로 다른 장르: ",user1^user2) # 서로 다른 장르:  {'SF', 'Romance'}
print("전체 장르: ",user1|user2)      # 전체 장르:  {'Romance', 'SF', 'Drama', 'Action'}


# set 메서드
s1 = {1,2,3}

# 원소 추가
s1.add(4)
print("원소 추가", s1) # 원소 추가 {1, 2, 3, 4}

s1.update((5,6,7))
print("여러 원소 추가", s1) # 여러 원소 추가 {1, 2, 3, 4, 5, 6, 7}

# 원소 제거
s1.remove(4)
print("원소 제거1", s1) # 원소 제거1 {1, 2, 3, 5, 6, 7}
# s1.remove(100) # KeyError: 100 - 존재하지 없는 원소 삭제 시도 시 에러

s1.discard(100) # 존재하지 않는 원소 무시
s1.discard(6)
print("원소 제거2", s1) # 원소 제거2 {1, 2, 3, 5, 7}

deleted = s1.pop() # 임의의 원소를 제거하고 반환하여 출력함
print("원소 제거3", s1, deleted) # 원소 제거3 {2, 3, 5, 7} 1



# 부분 집합 (subset) 관련 메서드
a = {10, 20, 30, 40, 50} # 상위 집합
b = {20, 30 ,40, 50} # 부분 집합
c = {10, 200, 300, 400, 500}

# 부분 집합 여부 판단
print(b.issubset(a)) # True
print(a.issubset(b)) # False

# 상위 집합 여부 판단
print(b.issuperset(a)) # False
print(a.issuperset(b)) # True

# 공통 원소가 없는지 여부 판단
print(a.isdisjoint(b)) # False
print(a.isdisjoint(c)) # False
print(b.isdisjoint(c)) # True
'''
# 실습 2 
'''
# 문제 1. 부분집합 관계 판단
my_certficates = {'SQL', 'Python', 'Linux'}
job_required = {'SQL', 'Python'}

print("지원 자격 충족 여부 : ", job_required.issubset(my_certficates)) # 지원 자격 충족 여부 :  True
a = job_required.issubset(my_certficates)

print("지원 자격 충족 여부 : ", a)

# 11. 16.

movie_rank = ["닥터스트레인지", "스플릿", "럭키"]
print(movie_rank) # ['닥터스트레인지', '스플릿', '럭키']
movie_rank.append("배트맨")
print(movie_rank) # ['닥터스트레인지', '스플릿', '럭키', '배트맨']
del movie_rank[2]
print(movie_rank) # ['닥터스트레인지', '스플릿', '배트맨']
del movie_rank[2]
del movie_rank[1]
print(movie_rank) # ['닥터스트레인지']

lang1 = ["C", "C++", "JAVA"]
lang2 = ["Python", "Go", "C#"]
langs = lang1 + lang2
print(langs) # ['C', 'C++', 'JAVA', 'Python', 'Go', 'C#']
nums = [1, 2, 3, 4, 5, 6, 7]
print("max :", max(nums), "min :", min(nums)) # max : 7 min : 1
print(sum(nums)) # 28

cook = ["피자", "김밥", "만두", "양념치킨", "족발", "피자", "김치만두", "쫄면", "소시지", "라면", "팥빙수", "김치전"]
print(len(cook)) # 12

average = sum(nums) / len(nums)
print(average) # 4.0
'''
