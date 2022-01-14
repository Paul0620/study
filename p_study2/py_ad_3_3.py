"""
Chapter3 Advanced(3) - Meta Class(3)
Keyword - Type inheritance(타입 상속), Custom metaclass
"""
"""
메타클래스 상속
1. type클래스 상속
2. metaclass 속성 사용
3. 커스텀 메타 클래스 생성
    - 클래스 생성 가로채기(intercept)
    - 클래스 수정하기(modify)
    - 클래스 개선(기능추가)
    - 수정된 클래스 반환
"""

# Ex1
# 커스텀 메타클래스 생성 예제(Type 상속x)
def cus_mul(self, d):
    for i in range(len(self)):
        self[i] = self[i] * d


def cus_replace(self, old, new):
    while old in self:
        self[self.index(old)] = new


# list를 상속받는 메소드 2개 추가
CustomList1 = type(
    "CustomList1",
    (list,),  # 리스트를 상속받았기 때문에 초기값에 리스트를 담을 수 있음
    {"desc": "커스텀 리스트1", "cus_mul": cus_mul, "cus_replace": cus_replace},
)

c1 = CustomList1([1, 2, 3, 4, 5, 6, 7, 8, 9, 10])  # self의 초기값이 리스트형태라 초기값을 미리 담아준다

c1.cus_mul(1000)

print("Ex1 > ", c1)

c1.cus_replace(1000, 7777)

print("Ex1 > ", c1)
print("Ex1 > ", c1.desc)
# print("Ex1 > ", dir(c1))
print()


# Ex2 - 이걸 이해하고 다룰 정도면 실력자!
# 커스텀 메타클래스 생성 예제(Type 상속o)

# class MetaClassName(type):
#     # type을 상속 받으면 사용할 수 있는 메소드들이 있다.
#     def __new__(metacls, name, bases, namespace):
#         코드 작성

# 실행 순서 new -> init -> call
class CustomListMeta(type):
    # 생성된 인스턴스 초기화
    def __init__(self, object_or_name, bases, dict):
        print("2. __init__ >", self, object_or_name, bases, dict)
        super().__init__(object_or_name, bases, dict)

    # 인스턴스 실행
    def __call__(self, *args, **kwargs):
        print("3. __call__ >", self, *args, **kwargs)
        return super().__call__(*args, **kwargs)

    # 클래스 인스턴스 생성(메모리 초기화)
    def __new__(matacls, name, bases, namespace):
        print("1. __new__ >", matacls, name, bases, namespace)
        namespace["desc"] = "커스텀리스트2"
        namespace["cus_mul"] = cus_mul
        namespace["cus_replace"] = cus_replace

        return type.__new__(matacls, name, bases, namespace)


CustomList2 = CustomListMeta("CustomList2", (list,), {})

c2 = CustomList2([1, 2, 3, 4, 5, 6, 7, 8, 9, 10])
c2.cus_mul(1000)
c2.cus_replace(1000, 7777)

print("Ex2 > ", c2)
print("Ex2 > ", c2.desc)

# 상속 확인
print(CustomList2.__mro__)
