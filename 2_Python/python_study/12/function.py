print('Type1.입력값 o(매개변수 1개), 결과값 x')
def say_hello(n):
    for i in range(n):
        print('hello')

say_hello(3)

print('Type2. 입력값 o(매개변수 2개), 결과값x')
def what_is_bigger(x, y):
    if x > y:
        print(x, '가 더 크다')
    elif y > x:
        print(y, '가 더 크다')
    else:
        print(x, '=', y, '서로 같다')

what_is_bigger(2, 4)
what_is_bigger(3, 1)
what_is_bigger(7, 7)

print('Type2. 입력값 o (매개변수 2개), 결과값 x')
def what_is_bigger(x, y): # 정의
    if x > y:
        print(x, '가 더 크다')
    elif y > x:
        print(y, '가 더 크다')
    else:
        print(x, '=', y, '서로 같다')

what_is_bigger(2, 4) # 호출 
what_is_bigger(3, 1)
what_is_bigger(7, 7)
