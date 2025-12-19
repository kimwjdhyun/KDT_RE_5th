name = ['강', '정', '이', '박', '정', '최', '오', '윤']

# 리스트 삭제하기
#1. pop(인덱스)
print("pop - 리스트 요소 삭제")
print("전:", name)
name.pop(0)
print("후:", name)
print()

print("전:", name)
name.pop()
print("후:", name)
print()

print("전:", name)
del name[2]
print("후:", name)
print()

print("전:", name)
del name[3:]
print("후:", name)
print()

print("전:", name)
name.remove('정')
print("후:", name)
print()

print("전:", name)
name.clear()
print("후:", name)
