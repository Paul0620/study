"""
Chapter1 Advanced(1) - Lambda, Reduce, Map, Filter Functions
Keyword - lambda, reduce, map, filter
"""
"""
lambda 장점 - 익명, 힙 영역 사용 즉시 소멸, pythonic, 파이썬 가비지 컬렉션(Count=0)
일반함수 - 재사용성을 위해 메모리에 저장
한 번만 쓰고 말 것이다 lambda, 또 사용할 것이다 일반함수
*시퀀스형 전처리에 Reduce, Map, Filter를 주로 사용
시퀀스 - 데이터를 순서대로 하나씩 나열하여 나타낸 데이터 구조
전처리(Preprocessibg) - 제거 또는 수정하여 최대한 소스 데이터의 정확성을 높히는 것
"""

# Ex1
cul = lambda a, b, c: a * b + c
print("Ex1 > ", cul(10, 15, 20))


# Ex2
digits1 = [x * 10 for x in range(1, 11)]
print("Ex2 > ", digits1)

# lambda를 사용 안한다면?
# def ex2_func(x):
#     return x ** 2

result = list(map(lambda i: i ** 2, digits1))
print("Ex2.lambda > ", result)

# 지역변수와 전역변수를 활용하여 만들어보기
def also_square(nums):
    def double(x):
        return x ** 2

    return map(double, nums)


print("Ex2 > ", list(also_square(digits1)))


# Ex3
digits2 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
result = list(filter(lambda x: x % 2 == 0, digits2))
print("Ex3 > ", result)


def also_evens(nums):
    def is_even(x):
        return x % 2 == 0

    return filter(is_even, nums)


print("Ex3 > ", list(also_evens(digits2)))


# Ex4
from functools import reduce  # reduce - 여러 개의 데이터를 대상으로 누적 집계를 낼때 사용

digits3 = [x for x in range(1, 101)]
# reduece(집계 함수, 순회 가능한 데이터)
result = reduce(lambda x, y: x + y, digits3)  # x에 y값을 누적

print("Ex4 > ", result)


def also_add(nums):
    def add_plus(x, y):
        return x + y

    return reduce(add_plus, nums)


print("Ex4 > ", also_add(digits3))
