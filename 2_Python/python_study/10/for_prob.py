"""
numbers = [1, 22, 333, 4444, 55555]

for n in range(len(numbers)): # len(numbers): 5
    print(n, numbers[n])

numbers = [1, 22, 333, 4444, 55555]

for n in range(len(numbers)): # len(numbers): 5
    print(str(n) + "번째 값:" + str(numbers[n]))
"""
"""
nums = [] # 빈 리스트 생성

for i in range(1, 11):
    nums.append(i)

print(nums)
"""

# 3번
# 조건1. 학생 5명의 점수를 저장하는 scroe 리스트를 생성
# 조건2-1. 점수가 80점 이상이면 "점수: 합격"을 출력
# 조건2-2. 점수가 80점 밈나이면 "점수: 불합격"을 출력

score = [54, 97, 99, 36, 82]

for x in score:
    if x>= 80:
        print(x, ":합격")
    else:
        print(x, ":불합격")
        
