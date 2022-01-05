# chapter03_01
# Special(Magic) Method
# 파이썬의 핵심 -> 시퀀스(Sequence), 반복(Iterator), 함수(Functions), Class(클래스)
# 매직 메소드란? - 클래스안에 정의할 수 있는 특별한(Built in  = 이미 만들어져 있는) 메소드
# 작성 형식은 더블언더 스코어 이루어져 있음

# 기본형
print(int)
print(float)


# 모든 속성 및 메소드 출력
# built in 메소드 때문에 메소드명을 일일이 작성하지 않고 간단하고 쉽게 작성할 수 있음
print(dir(int))
print(dir(float))
print()

n = 10

print(n + 100)
print(n.__add__(100))
# print(n.__doc__)
print(n.__bool__(), bool(n))
print(n * 100, n.__mul__(100))
print()

# 클래스 예제1
class Fruit:
    def __init__(self, name, price):
        # 인스턴스 변수
        self._name = name
        self._price = price

    def __str__(self):
        return f"Fruit Class Info : {self._name}, {self._price}"

    def __add__(self, x):
        print("called >> __add__")
        return self._price + x._price

    def __sub__(self, x):
        print("called >> __sub__")
        return self._price - x._price

    def __le__(self, x):
        print("called >> __le__")
        if self._price <= x._price:
            return True
        else:
            return False

    def __ge__(self, x):
        print("called >> __ge__")
        if self._price >= x._price:
            return True
        else:
            return False


# 인스턴스 생성
s1 = Fruit("Orange", 7500)
s2 = Fruit("Banana", 3000)

# +를 사용할 때 Fruit 클래스 안에 만들어둔 __add__를 사용하여 값을 내보냄
print(s1 + s2)

# 일반적인 계산
# print(s1._price + s2._price)

# 순서에 따라 self, x값이 다름
print(s1 - s2)
print(s2 - s1)
print()

# 매직메소드
print(s1 >= s2)
print(s1 <= s2)
print(s1 - s2)
print(s2 - s1)
print(s1)
print(s2)
