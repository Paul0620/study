"""
Chapter3 Advanced(3) - Descriptor(1)
Keyword - descriptor, set, get, del, property
"""
"""
디스크립터
1. 객체에서 서로다른 객체를 속성값으로 가지는 것.
2. Read, Write, Delete 등을 미리 정의 가능
3. data descriptor(set, del), non-data descriptor(get)
4. 읽기 전용 객체 생성 장점, 클래스를 의도하는 방향으로 생성 가능
# 헷갈릴 떄 읽어볼 것
https://m.blog.naver.com/codeitofficial/221706621090
"""

# Ex1
# 기본적인 Descriptor 예제


class DescriptorEx1(object):
    def __init__(self, name="Default"):
        self.name = name

    def __get__(self, obj, objtype):
        return f"Get method called. -> self : {self}, obj : {obj}, objtype : {objtype}, name : {self.name}"

    def __set__(self, obj, name):
        print("Set method called.")
        if isinstance(name, str):
            self.name = name
        else:
            raise TypeError("Name should be string.")

    def __delete__(self, obj):
        print("Delete method called")
        self.name = None


class Sample1(object):
    name = DescriptorEx1()


s1 = Sample1()

# __set__ 호출
s1.name = "Descriptor Test1"

# 예외 발생
# s1.name = 123

# attr 확인
# __get__ 호출
print("Ex1 > ", s1.name)


# __delete__ 호출
del s1.name


# 재확안
# __get__ 호출
print("Ex1 > ", s1.name)
print()


# Ex2
# Property 클래스 사용 Descriptor 직접 구현
# class property(fget = None, fset = None, fdel = None, doc = None)

# 클래스 + 프로퍼티 기능까지 다 사용하는 범용적인 클래스
class DescriptorEx2(object):
    def __init__(self, value):
        self._name = value

    # Ex1과 다르게 클래스 내에서 다 해결하기 때문에 self만 있어도 됨
    def getVal(self):
        return f"Get method called. -> self : {self}, name : {self._name}"

    def setVal(self, value):
        print("Set method called.")
        if isinstance(value, str):  # value가 문자형이 아니라면
            self._name = value
        else:
            raise TypeError("Name should be string.")

    def delVal(self):
        print("Delete method called.")
        self._name = None

    name = property(getVal, setVal, delVal, "Property 테스트를 하는 name 필드입니다. 의미는 없습니다.")


s2 = DescriptorEx2("Descriptor Test2")

# 최초 값 확인
print("Ex2 > ", s2.name)

# setVal 호출
s2.name = "Descript Test2 Method"

# 예외 발생
# s2.name = 10

# getVal 호출
print("Ex2 > ", s2.name)

# delVal 호출
del s2.name

# 재확인
print("Ex2 > ", s2.name)

# Doc 확인
print("Ex2 > ", DescriptorEx2.name.__doc__)
