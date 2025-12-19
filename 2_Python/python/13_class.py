# 클래스(class)
# - 데이터와 기능을 하나로 묶는 구조
# - 개념적(기능적)으로 유사한 관계에 있는것들을 묶어줌

# 클래스 기본 문법
# 클래스의 정의
class ClassName : 
    # 생성자(constructor) : 인스턴스(객체)가 생성될 때 호출
    # 인스턴스 변수를 초기화, 기본 상태 설정
    # 하나의 클래스에서 하나만 정의가 가능
    def __init__(self, name):
        # 인스턴스 변수
        # self : 인스턴스 자기 자신을 가리킴
        self.name = name # 입력받은 값
        self.age = 0 # 선언도 가능
    
    #  (인스턴스)메서드
    def method_name(self) :
        print(f"이 인스턴스의 이름은 {self.name}입니다.")

# 인스턴스 생성
my_instance = ClassName("kimwjdhyun")
print(my_instance.name)             # 이 인스턴스의 이름은 kimwjdhyun입니다.
my_instance.method_name()

another_instance = ClassName("wjdhyun") # 이 인스턴스의 이름은 wjdhyun입니다.
another_instance.method_name()

# 실습 1. class 만들기
# 문제 1. 책 클래스 만들기

class Book:
    def __init__(self, title, author, total_pages, my_page):
        self.title = title
        self.author = author
        self.total_pages = int(total_pages)
        self.my_page = int(my_page)
        self.current_page = float((my_page * 100) / total_pages)

    def method_title(self):
        print(f"이 책의 제목은 {self.title}입니다.")

    def method_author(self):
        print(f"이 책의 저자는 {self.author}입니다.")

    def read_page(self):
        print(f"이 책은 총 {self.total_pages}페이지이며, 현재 {self.my_page}페이지 까지 읽었습니다.")

    def progress(self):
        print(f"현재 {self.current_page}% 읽었습니다.")

my_instance = Book("Harry Potter and the Sorcerer's Stone", "J. K. Rowling", 472, 256)
my_instance.method_title()
my_instance.method_author()
my_instance.read_page()
my_instance.progress()

# 해설 


# 문제 2. Rectangle 클래스 구현
'''
class Rectangle:
    def __init__(self, width, height):
        self.width = width
        self.height = height

    def area(self):
        return self.width * self.height
    
wid = int(input("가로 : ")) # 12
hei = int(input("세로 : ")) # 12
Rectangle = Rectangle(wid, hei)
print("넓이는", Rectangle.area()) # 넓이는 144

'''

'''
# 클래스 변수
# - 클래스가 가지고 있는 변수
# 모든 인스스턴스가 공유할 수 있음
class Dog:
    # 클래스 변수
    kind = "강아지"

    def __init__(self, species, name, age):
        self.species = species
        self.name = name
        self.age = age

dog1 = Dog("포메라니안", "리치", 12)
dog2 = Dog("비숑", "구름", 10)

print("인스턴스1", dog1.kind) # 인스턴스1 강아지
print("인스턴스2", dog2.kind) # 인스턴스2 강아지
print("클래스", Dog.kind)     # 클래스 강아지

# 클래스 메서드
# 클래스 자체를 대상으로 동작하는 메서드
# 클래스 데이터를 조작하는데 사용

class Book2:
    book_count = 0

    def __init__(self, title, author):
        Book2.book_count += 1
        self.title = title
        self.author = author

    # 클래스 메서드
    @classmethod # 데코레이터
    def get_count(cls):
        print(f"현재 {cls.book_count}권의 책을 가지고 있다.")

book1 = Book2("B1", "author1")
book2 = Book2("B2", "authot2")

print(Book2.book_count) # 현재 2권의 책을 가지고 있다.
Book2.get_count()

# 정적 메서드
# - 클래스나 인스턴스의 데이터를 조작하지 않는 클래스 함수
# - 클래스나 인스턴스의 상태에 의존하지 않는 일반 함수
# - 개념적으로는 클래스와 연관이 있으나, 클래스나 인스턴스의 데이터를 조작하지 않음


class OperationTool:

    @staticmethod # 데코레이터
    def add(a, b):
        return a +b
    
print(OperationTool.add(10, 20)) # 30

# 실습 2. 클래스 변수, 메서드 연습
# 문제 1. User 클래스 구현

class User:
    total_users = 0
    
    def __init__(self, username, points):
        self.username = username
        self.points = points
        User.total_users += 1
    
    def add_points(self, amount):
        self.points += amount
    
    def get_rank(self):
        if 0 <= self.points < 100:
            return "Bronze"
        elif 100 <= self.points < 500:
            return "Silver"
        elif 500 <= self.points:
            return "Gold"
        else:
            return "등급이 존재하지 않습니다."
    
    @classmethod
    def get_total_users(cls):  
        print(f"총 {cls.total_users}명의 유저가 있습니다.") # 총 4명의 유저가 있습니다

user1 = User("wjdhyun", 300)
user2 = User("kimjeonghyun", 40)
user3 = User("kimwjdhyun", 500)
user4 = User("unrank", -45)

User.get_total_users()
print(f"{user1.username}님의 등급: {user1.get_rank()}") # wjdhyun님의 등급: Silver
print(f"{user2.username}님의 등급: {user2.get_rank()}") # kimjeonghyun님의 등급: Bronze
print(f"{user3.username}님의 등급: {user3.get_rank()}") # kimwjdhyun님의 등급: Gold
print(f"{user4.username}님의 등급: {user4.get_rank()}") # unrank님의 등급: 등급이 존재하지 않습니다.

# 접근 제어와 정보 은닉
# 데이터 무결성을 보호하기 위함
# 코드 안정성을 향상시키기 위함

class person2:
    def __init__(self, name, age):
        # public
        self.name = name
        # private : 언더바(__) 두개를 변수 앞에 붙여서 정의
        self.__age = age
    
    # getter
    def get_age(self):
        return self.__age
    
    # setter
    def set_age(self, value):
        if value > 120 or value < 0:
            print("유효하지 않은 나이입니다.")
        else:
            self.__age = value

p1 = person2("kimwjdgyun", 28)
print(p1.name)
# print(p1.__age) # AttributeError
print(p1.get_age()) # 28
p1.set_age(-10) # 유효하지 않은 나이입니다.

# @property 데코레이터
# - 메서드를 속성처럼 보이게 만들어주는 데코레이터

class EX:
    def __init__(self):
        self.__value = 0

    # getter
    @property # ()생략 속성으로 사용하기 때문
    def value(self):
        return self.__value
    
    # setter
    @value.setter
    def value(self, val):
        if val < 0:
            print("유효하지 않은 값입니다.")
        else:
            self.__value = val
        
ex1 = EX()
print(ex1.value) # 0
ex1.value = 100
print(ex1.value) # 100 : @property로 속성 처럼 사용
ex1.value = -100
print(ex1.value) # 유효하지 않은 값입니다., 100

'''

# 실습 3. 접근 제어와 정보은닉 연습
# 문제 1. UserAccount 클래스 : 비밀번호 보호
class UserAccount:
    def __init__(self, username, password):
        self.username = username
        self.__password = password   
    
    
    def changed_password(self, old_pw, new_pw):
        if self.__password != old_pw:
            return "비밀번호가 틀렸습니다."
        elif self.__password == old_pw:
            print("이전 비밀번호입니다. 변경하시겠습니까?")
            return new_pw


    
    def check_password(self, __password):
        if __password == 123321:
            print("로그인 성공!")
            return True
        else:
            print("비밀번호가 틀렸습니다.")
            return False

user = UserAccount("kimwjdhyun", 123321)

user.check_password(123321) # 로그인 성공!
user.check_password(12321) # 비밀번호가 틀렸습니다.
user.changed_password(123321, 0) # 이전 비밀번호입니다. 변경하시겠습니까?

# 해설
# 실습 3. 문제 1.

class UserAccount:
    def __init__(self, username, password):
        self.username = username
        self.__password = password
    
    def changed_password(self, old_pw, new_pw):
        if old_pw == self.__password:
            self.__password = new_pw
            print("비밀번호가 변경되었습니다.")
        else:
            print("비밀번호가 일치하지 않습니다.")
    def check_password(self, password):
        return self.__password == password

uesr = UserAccount("user1", "pass123")
print(user.username)
# print(user.__password) # AttributeError

user.check_password("pass123") # True
user.changed_password("wrongpass", "newpass")

# 문제 2. Student 클래스 : 성적 검증(@property 사용)
class Student:
    def __init__(self, name, score):
        self.name = name
        self.__score = score
    
    @property
    def score(self):
        if 0 <= self.__score <= 100:
            return self.__score
        else:
            return 0  
    
    @score.setter
    def score(self, sco):
        if sco < 0 or sco > 100:
            print("잘못 입력했습니다.")
        else:
            self.__score = sco

student1 = Student("kimwjdhyun", 80)
print(f"이름 : {student1.name}")        # 이름 : kimwjdhyun
print(f"점수 : {student1.score}")       # 점수 : 80
student1.score = 95
print(f"점수: {student1.score}")        # 점수 : 95
student1.score = -80                    # 잘못 입력했습니다.
student1.score = 122                    # 잘못 입력했습니다.

# 문제 2. 해설

class Student:
    def __init__(self, name, score):
        self.name = name
        self.__score = score
 
    @property # getter의 역할
    def score(self):
        return self.__score
    
    @score.setter
    def score(self, value):
        if 0 <= value <= 100:
            self.__score = value
        else:
            raise ValueError("성적은 0에서 100사이여야 합니다.")
        
s1 = Student("alice", "85")
print(s1.name)
print(s1.score) # 85
s1.score = 95
print(s1.score)


# 상속
# 부모 클래스의 속성과 메서드를 물려받아 새로운 자녀 클래스를 만드는 것

# 상속 기본 문법
# 부모 클래스

# class Animal:
#     def __init__(self, name):
#         self.name = name

#     def bark(seflv):
#         print("동물이 울음소리를 냅니다.")

# # 자식 클래스

# class Dog(Animal):
#     pass

# dog = Dog("호굼이")
# dog.bark()
# print(dog.name)

# 동물이 울음소리를 냅니다.
# 호굼이


# super() 사용
class Animal:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def bark(seflv):
        print("동물이 울음소리를 냅니다.")

# 자식 클래스

class Dog(Animal):
    def __init__(self, name, age):
        # super는 부모 클래스를 가리킴
        super().__init__(name, age)

dog = Dog("호굼이", 8) # age 추가안하면 에러 발생!
dog.bark()
print(dog.name) # 호굼이
print(dog.age) # 8



# 오버라이딩 사용

class Animal:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def bark(seflv):
        print("동물이 울음소리를 냅니다.")



class Dog(Animal):
    def __init__(self, name, age, species): # 부모클래스에 없는 속성도 자식 클래스에서 추가 할수 있다
        super().__init__(name, age)
        self.species = species

    # 오버라이딩
    def bark(self):
        super().bark() # 부모클래스에서 가져옴 : 동물이 울음소리를 냅니다.
        print("왈왈")

dog = Dog("호굼이", 9, "샤페이") 
dog.bark()          # 왈왈
print(dog.name)     # 호굼이
print(dog.age)      # 9
print(dog.species)  # 샤페이

# 실습 1. 상속과 오버라이딩 연습
# 문제 1. shape 클래스 오버라이딩

class Shape:
    def __init__(self, sides, base):
        self.sides = sides
        self.base = base

    def printinfo(self):
        print(f"변의 개수 : {self.sides}, 밑변의 길이 : {self.base}")

    def area(self):
        print("넓이 계산이 정의되지 않았습니다.")

shape=Shape(4, 10)
shape.area()
shape.printinfo()           # 넓이 계산이 정의되지 않았습니다.


class Rectangle(Shape):
    def __init__(self, sides, base, height):
        super().__init__(sides, base)
        self.height = height
    
    def area(self):
        value = self.base * self.height
        print(f"사각형의 넓이 : {value}")

rectangle = Rectangle(4, 10, 6)
rectangle.printinfo()        # 변의 개수 : 4, 밑변의 길이 : 10
rectangle.area()             # 사각형의 넓이 : 60


class Triangle(Shape):
    def __init__(self, sides, base, height):
        super().__init__(sides, base)
        self.height = height
    
    def area(self):
        value = (self.base * self.height) / 2
        print(f"삼각형의 넓이 : {value}")

triangle = Triangle(3, 10, 6)
triangle.printinfo()        # 변의 개수 : 3, 밑변의 길이 : 10
triangle.area()             # 삼각형의 넓이 : 30.0


# 추상 클래스(Abstract Class)
# 클래스의 구조를 정의하는 클래스

from abc import ABC, abstractmethod\

class Animal(ABC):
    # 추상 메서드
    @abstractmethod
    def bark(self):
        pass

class Dog(Animal):
    def bark(self):
        print("왈왈")

# a = Animal() # TypeError: Can't instantiate abstract class Animal with abstract method bark
a = Dog()
a.bark()        # 왈왈

# 실습 2. 추상 클래스 연습
# 문제 1. 추상 클래스 Payment 구현

from abc import ABC, abstractmethod

class Payment(ABC):
    @abstractmethod
    def pay(self, amount):
        pass

class CardPayment(Payment):
    def pay(self, amount):
        self.amount = amount
        print(f"카드로 {amount}원을 결제합니다.")

class CashPayment(Payment):
    def pay(self, amount):
        self.amount = amount
        print(f"현금으로 {amount}원을 결제합니다.")

card_payment = CardPayment()
card_payment.pay(500000000000)              # 카드로 500000000000원을 결제합니다.

cash_payment = CashPayment()
cash_payment.pay(34564564)              # 현금으로 34564564원을 결제합니다.

# 해설
class Payment(ABC):
    @abstractmethod
    def pay(self, amount):
        pass

class CardPayment(Payment):
    def __init__(self):
        super().__init__() # 생략하고 pass 사용 가능
    def pay(self, amount):
        self.amount = amount
        print(f"카드로 {amount}원을 결제합니다.")

class CashPayment(Payment):
    def __init__(self):
        pass
    def pay(self, amount):
        self.amount = amount
        print(f"현금으로 {amount}원을 결제합니다.")

card_payment = CardPayment()
card_payment.pay(10000)              # 카드로 10000원을 결제합니다.

cash_payment = CashPayment()
cash_payment.pay(4000)              # 현금으로 4000원을 결제합니다