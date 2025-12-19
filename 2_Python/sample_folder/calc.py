#calc.py
def add(a, b):
    print(a + b)

def subtract(a, b):
    print(a - b)

def multiply(a, b):
    print(a * b)    

def divide(a, b):
    if b != 0:
        print(a / b)
    else:
        print("0으로 나눌 수 없습니다.")
        return None
    
