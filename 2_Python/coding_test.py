def solution(a, b):
    ab = int(str(a) + str(b))
    ab2 = 2 * int(a) * int(b)

    if ab > ab2 :
        return ab
    elif ab < ab2 :
        return ab2
    
print(solution(2, 91)) # 364
print(solution(91, 2)) # 912


common = (1, 2, 3, 4)

# def solution(common):
#     length = len(common)
#     first = common[1] - common[0]
#     second = common[2] - common[1]
#     third = common[1] // common[0]
#     if first != second or first == 0:
#         answer = common[length-1] * third
#     else:
#         answer = common[length-1] + first
#     return answer

# 모범답안

# def solution(common):
#     answer = 0
#     a,b,c = common[:3]
#     if (b-a) == (c-b):
#         return common[-1]+(b-a)
#     else:
#         return common[-1] * (b//a)
#     return answer

def solution(num1, num2):
    -50000<=num1<=50000
    -50000<=num2<=50000
    return num1 + num2
    
def solution(num1, num2):
    answer = num1 / num2
    return answer*1000

def solution(num1, num2):
    if num1 == num2:
        return 1
    elif num1!=num2:
        return -1

def solution(numer1, denom1, numer2, denom2):
    numer=numer1 * denom2 + numer2*denom1
    denom=denom1* denom2


    i=[]
    for num in range(1, min(numer,denom)+1):
        if numer%num==0 and denom%num==0:
            i.append(num)
            print(i)
    gn=max(i)
    print ("최대공약수:", gn)

    answer=[numer/gn,denom/gn]
    return answer

def solution(numbers):
    answer = [i*2 for i in numbers]
    return answer

def solution(n):
    return list(range(1, n+1, 2))
n = 100
print(solution(n))  

def solution(n):
    answer = 0
    
    if n % 7 == 0:
        answer = n / 7
    else:
        answer = n // 7 + 1
    return answer
print(solution(15))  # 3
print(solution(28))  # 4


def solution(n):
    return (n - 1) // 7 + 1
print(solution(15))  # 3
print(solution(28))  # 4

def solution(n):
    answer = 1
    
    while (6 * answer) % n != 0:
         answer += 1
         return answer
    
def solution(slice, n):
    slice = n / slice
    if n % slice == 0:
        return n // slice
    else:
        return n // slice + 1
    
print(solution(7, 10))  # 2
print(solution(4, 12))  # 3

# def solution(numbers):
#     return sum(numbers) / len(numbers)



# def func1(num):
#     if 0 > num:
#         return 0
#     else:
#         return num

# def func2(num):
#     if num > 0:
#         return 0
#     else:
#         return num

# def func3(station):
#     num = 0
#     for people in station:
#         if people == "Off":
#             num += 1
#     return num

# def func4(station):
#     num = 0
#     for people in station:
#         if people == "On":
#             num += 1
#     return num


# def solution(seat, passengers):
#     num_passenger = 0
#     for station in passengers:
#         num_passenger += func4(station)

#         num_passenger -= func3(station)

#     answer = func1(seat - num_passenger) + func2(num_passenger - seat)

#     return answer
'''
def solution(nickname):
    answer = ""
    for letter in nickname:
        if letter == "l":
            answer += "I"
        elif letter == "w":
            answer += "vv"
        elif letter == "W":
            answer += "VV"
        elif letter == "O":
            answer += "0"
        else:
            answer += letter
    if len(answer) < 3:
        answer += "o"
    if len(answer) > 8:
        answer = answer[:8]
    return answer

def solution(numbers, our_score, score_list):
    answer = []
    for i in range(len(numbers)):
        if numbers[our_score[i]] == score_list[i]:
            answer.append("Same")
        else:
            answer.append("Different")
    
    return answer
'''
'''
def solution(storage, num):
    clean_storage = []
    clean_num = []
    for i in range(len(storage)):
        if storage[i] in clean_storage:
            pos = clean_storage.index(storage[i])
            clean_num[pos] += num[i]
        else:
            clean_storage.append(storage[i])
            clean_num.append(num[i])
            
    # 아래 코드에는 틀린 부분이 없습니다.
            
    max_num = max(clean_num)
    answer = clean_storage[clean_num.index(max_num)]
    return answer
'''
'''
a = int(input())
b = int(input())
def solution(a, b):
    q = str(a)
    w = str(b)
    e = int(a)
    r = int(b)
    
    if int(q+w) > 2*e*r:
        return q + w
    elif int(q+w) == 2*e*w:
        return q + w
    elif int(q+w) < 2*e*r:
        return 2*e*r
    
'''

# def solution(a, b, included):
#     answer = 0
#     for i in range(len(included)):
#         if included[i] == True:
#             answer += a + i * b
#     return answer
    
def solution(num_list):
    s = sum(num_list)
    m = 1
    for num in num_list:
        m*=num
        if s**2 < m
            return 1
        else:
            return 0
        
def solution(numlog):
    sol = {"w": 1, "s": -1, "d": 10, "a": -10}
    answer = ""
    for i in range(1, len(numlog)):
        a = numlog[i] - numlog[i-1]
        
        for k, v in sol.items():
            if v == a:
                answer += k
                break
    
    return answer       


# 정수 배열 arr와 2차원 정수 배열 queries이 주어집니다. queries의 원소는 각각 하나의 query를 나타내며, [i, j] 꼴입니다.

# 각 query마다 순서대로 arr[i]의 값과 arr[j]의 값을 서로 바꿉니다.

# 위 규칙에 따라 queries를 처리한 이후의 arr를 return 하는 solution 함수를 완성해 주세요.

def solution(arr, queries):
    answer = []
    return answer