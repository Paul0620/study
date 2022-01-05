# chapter03_03
# Special(Magic) Method
# 파이썬의 핵심 -> 시퀀스(Sequence), 반복(Iterator), 함수(Functions), Class(클래스)
# 매직 메소드란? - 클래스안에 정의할 수 있는 특별한(Built in  = 이미 만들어져 있는) 메소드
# 작성 형식은 더블언더 스코어 이루어져 있음

# 객체 -> 파이썬의 데이터를 추상화
# 모든 객체 -> id, type -> value

# 일반적인 튜플
# 두점 사이의 거리 구하기
pt1 = (1.0, 5.0)
pt2 = (2.5, 1.5)

# 루트 함수 sqrt
from math import sqrt

l_leng1 = sqrt((pt1[0] - pt2[0]) ** 2 + (pt1[1] - pt2[1]) ** 2)
print(l_leng1)

# 네임드 튜플을 사용하여서 두점 사이 구하기
# namedtuple이란? - 클래스와는 다르고 콜렉션스 모델 하위에 있다.
# dictionary의 성질을 가지고 있다.
from collections import namedtuple

# 네임드튜플 선언
Point = namedtuple("Point", "x y")

pt3 = Point(1.0, 5.0)
pt4 = Point(2.5, 1.5)

# print(pt3, pt3[0], pt3.x)
# 키로 접근하여 계산
l_leng2 = sqrt((pt3.x - pt4.x) ** 2 + (pt3.y - pt4.y) ** 2)
print(l_leng2)


# 네임드튜플 선언 방법들
Point1 = namedtuple("Point", ["x", "y"])
Point2 = namedtuple("Point", "x, y")
Point3 = namedtuple("Point", "x y")
# reanem의 Default는 False인데 True를 선언하여 중복된 키값이나 예약어를 사용할 수 있다.
Point4 = namedtuple("Point", "x y x class", rename=True)

# 출력
print(Point1, Point2, Point3, Point4)
print()

# Dict to Unpacking
temp_dict = {"x": 75, "y": 55}

# 객체 생성
p1 = Point1(x=10, y=35)
p2 = Point2(20, 40)
p3 = Point3(45, y=20)
p4 = Point4(10, 20, 30, 40)
p5 = Point3(**temp_dict)  # dict도 알아서 매핑함, 튜플은 * 한개 딕셔너리는 ** 두개 사용

print(p1)
print(p2)
print(p3)
print(p4)  # rename 테스트, _난수를 통해 키값을 임의로 만들어서 생성함
print(p5)

# 사용
print(p1[0] + p2[1])
print(p1.x + p2.y)

# Unpacking
x, y = p3

print(x, y)
print()

# 네임드튜플 메소드
temp = [52, 38]
# 리스트를 _make()를 사용하여 새로운 객체 생성
p6 = Point1._make(temp)

# _fields : 필드 네임 확인
# 키값명이 뭐가 존재하는지 확인
print(p1._fields, p2._fields, p4._fields)


# _asdict() : OrderedDict 반환
# 딕셔너리 형태로 반환
print(p1._asdict())
print(p4._asdict())
print(p6._asdict())
print()

# 실 사용 실습
# 반 20명, 4개의 반(A, B, C, D)
Classses = namedtuple("Classes", ["rank", "number"])

# 그룹 리스트 선언
numbers = [str(n) for n in range(1, 21)]
ranks = "A B C D".split()  # 공백을 기준으로

print(numbers)
print(ranks)
print()

# list Comprehension
students = [Classses(rank, number) for rank in ranks for number in numbers]

print(len(students))
print(students)
print()

# 추천 작성 방식
students2 = [
    Classses(rank, number)
    for rank in "A B C D".split()
    for number in [str(n) for n in range(1, 21)]
]

print(len(students2))
print(students2)


# 출력
for s in students2:
    print(s)
