"""
Chapter3 Advanced(3) - Meta Class(1)
Keyword - Class of Class, Type, Meta Class, Custom Meta Class
"""
"""
메타클래스
1. 클래스를 만드는 역할 -> 의도하는 방향으로 클래스를 커스텀한다.
2. 프레임워크 작성 시 필수
3. 동적 생성(type), 커스텀 생성(type) 함수
4. 커스텀 클래스 -> 검증클래스 등
5. 엄격한 클래스 사용 요구, 메소드 오버라이드 요구
"""

# Ex1
# type 예제


class SampleA(object):  # Class == Object, 파이썬에서 클래스는 객체라 생각해도된다.
    pass


# 인스턴스화
obj1 = SampleA()  # 변수에 할당, 복사 가능, 새로운 속성, 함수의 인자로 넘기기 가능

# obj1 -> SampleA instance
# SampleA -> type meta class
# type -> type meta class

print("Ex1 > ", obj1.__class__)  # <class '__main__.SampleA'>
print("Ex1 > ", type(obj1))  # <class '__main__.SampleA'>
print("Ex1 > ", obj1.__class__ is type(obj1))
print(
    "Ex1 > ", obj1.__class__.__class__ is type(obj1).__class__
)  # <class 'type'>, 'type' 클래스가 모든 클래스의 메타 클래스인 것을 알 수 있다.
print(type.__class__)
print()


# Ex2
# type meta(Ex1 증명)

# int, dict

n = 10
d = {"a": 10, "b": 20}


class SampleB:
    pass


obj2 = SampleB()

for o in (n, d, obj2):
    print(f"Ex2 >  {type(o)}, {type(o) is o.__class__}, {o.__class__.__class__}")
print()

for t in int, float, dict, list, tuple:
    print(f"Ex2 > {type(t)}")
print("Ex2 > ", type(type))
