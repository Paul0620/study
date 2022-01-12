"""
Chapter2 Advanced(2) - Property(1) - Underscore
Keyword - access modifier(접근지정자), Underscore
"""
"""
다양한 언더스코어 활용
파이썬 접근지정자 설명
"""

# Ex1
# Use Underscore
# 1. 인터프리터, 2. 값 무시, 3. 네이밍(구체화, 자릿수)

# Unpacking
x, _, y = (1, 2, 3)  # x = 1, y = 3
a, *_, b = (1, 2, 3, 4, 5)  # a = 1, b = 5

print("Ex1 > ", x, y, a, b)

for _ in range(10):
    pass

for _, val in enumerate(range(10)):
    pass

# '_'는 값을 무시할 때 사용

# Ex2
# 접근지정자
# name - public
# _name - protected
# __name - private
# 파이썬에서 위의 규칙을 따라 작성 -> Public은 강제가 아니다. 약속된 규약에 따라 코딩 장려(자유도, 책임감 장려)
# 타 클래스(클래스 변수, 인스턴스 변수 값 쓰기 장려 안함)
# -> Name Mangling - 파이썬이 변수/함수의 이름을 짓이겨서 다른 이름으로 바꿔버리는 것을 말함, 변수/함수명 앞에 __ 두개를 붙여서 표현
# 언제 사용하는가? - 1. 클래스의 속성값을 외부에서 접근하기 힘들게 할 때(private화), 2. 하위 클래스가 상위 클래스의 속성을 오버라이딩 하는 것을 막을 때
# 타 클래스 __ 가 변수/함수 앞에 붙어있다면 접근하지 않는 것이 원칙

# No use Property
class SampleA:
    def __init__(self):
        self.x = 0
        self.__y = 0
        self._z = 0


a = SampleA()

a.x = 1

print(f"Ex2 > x : {a.x}")
# print(f"Ex2 > y : {a.__y}") # attribute가 없다고 나옴
print(f"Ex2 > z : {a._z}")
# print("Ex2 > ", dir(a))  # private 변수는 임의의 이름으로 변경하여 접근하지 못하게만 처리
# 굳이 바꾸고 싶다면??
a._SampleA__y = 2  # 임의의 변경된 이름으로 접근하면 수정 가능 하지만 규약을 지키기 위해 안건드리는 것을 권장
print(f"Ex2 > __y : {a._SampleA__y}")


# Ex3
# 메소드 활용하여 private 수정 Getter, Setter
class SampleB:
    def __init__(self):
        self.x = 0
        self.__y = 0  # _SampleB__y

    def get_y(self):
        return self.__y

    def set_y(self, value):
        self.__y = value


b = SampleB()

b.x = 1
b.set_y(2)

print(f"Ex3 > x : {b.x}")
print(f"Ex3 > y : {b.get_y()}")


# private을 억지로 변수 접근 후 수정 부분에서 일관성 및 가독성이 하락한다
# b._SampleB__y = 343

print("Ex3 > ", dir(b))
