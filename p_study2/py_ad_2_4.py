"""
Chapter2 Advanced(2) - Method Overriding
Keyword - Overriding, OOP, 다형성
"""
"""
메소드 오버라이딩의 효과
1. 서브클래스(자식)에서 슈퍼(부모)클래스를 호출 후 사용
2. 메소드 재정의 후 사용가능
3. 부모클래스의 메소드를 추상화 후 사용가능(구조적 접근)
4. 확장이 가능, 다형성(다양한 방식으로 동작)
5. 가독성 증가, 오류가능성 감소, 메소드 이름 절약, 유지보수성 증가 등
"""

# Ex1
# 기본 Overriging 예제

# 부모 클래스
class ParentEx1:
    def __init__(self):
        self.value = 5

    def get_value(self):
        return self.value


# 자식 클래스
class ChildEx1(ParentEx1):
    pass


c1 = ChildEx1()
p1 = ParentEx1()

# 부모클래스 메소드 호출
print("Ex1 > ", c1.get_value())

# c1의 모든 속성 출력
print("Ex1 > ", dir(ChildEx1))

# 부모 & 자식 모든 속성 출력
print("Ex1 > ", dir(ParentEx1))
print("Ex1 > ", dir(ChildEx1))
print()

print("Ex1 > ", ParentEx1.__dict__)
print("Ex1 > ", ChildEx1.__dict__)
# 인스턴스화 되는 시점에 부모클래스의 속성이 담기는거라 __dict__로 자식클래스를 보면 부모클래스에게 상속받은 것들이 없음
print()


# Ex2
# 기본 Overriding 메소드 재정의


class ParentEx2:
    def __init__(self):
        self.value = 5

    def get_value(self):
        return self.value


class ChildEx2(ParentEx2):
    def get_value(self):
        return self.value * 10


c2 = ChildEx2()

# 자식 메소드 재정의 후 호출
print("Ex2 > ", c2.get_value())
print()


# Ex3
# Overriding 다형성 예제

import datetime


class Logger(object):
    def log(self, msg):
        print(msg)


class TimestampLogger(Logger):
    def log(self, msg):
        ts = datetime.datetime.now()
        msg = msg
        message = f"{ts} {msg}"
        # super().log(message)
        # 정확하게 입력하고 싶다면
        super(TimestampLogger, self).log(message)


class DateLogger(Logger):
    def log(self, msg):
        ts = datetime.datetime.now().strftime("%Y-%m-%d")
        msg = msg
        message = f"{ts} {msg}"
        super(DateLogger, self).log(message)


l = Logger()
t = TimestampLogger()
d = DateLogger()


# 메소드 재정의 실습
# print("Ex3 > ", l.log("Called logger."))
# print("Ex3 > ", t.log("Called timestamp logger."))
# print("Ex3 > ", d.log("Called date logger."))

l.log("Called logger.")
t.log("Called timestamp logger.")
d.log("Called date logger.")
