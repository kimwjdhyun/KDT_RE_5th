print('Type3. 입력값 x, 결과값 o')
def say_yes():
    return 'Yes!'

print(say_yes())

print('결과값을 반환하지 않으면?')
def func_return():
    return

print(func_return())

print('Type4. 입력값o, 결과값o')
def square_area(width, height):
    return width * height

square_width = 3
square_height = 4

print(square_area(square_width, square_height))

print('추가. 함수 내부에서 함수 호출하기')
def first(n):
    return n * 2
def second():
    x= first(3) + 5
    return x

print(second())

def func1(): 
    print('hihi') 
def func2(say): 
    print(say * 2) 
def func3(say): 
    return say 
def func4(): 
    return 'hihi'

func1()
func2('hi')
print(func3('hihi'))
print(func4() * 2)

def what_to_say(param1):
    print(param1)
what_to_say("Hello", "World")
