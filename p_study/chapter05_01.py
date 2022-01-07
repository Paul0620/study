# chapter05_01
# https://docs.python.org/ko/3/howto/functional.html
# 함수형 프로그래밍 - 순수함수만을 이용해서 프로그래밍
# 일급함수(First-Class)(일급객체)
# 파이썬 함수 특징
# 1. 런타임 초기화
# 2. 변수 할당 가능
# 3. 함수 인수 전달 가능
# 4. 함수 결과 반환 가능(return)

# 함수 객체
def factorial(n):
    """Factorial Function -> n : int"""
    if n == 1:
        return 1
    else:
        return n * factorial(n - 1)


class A:
    pass


print(factorial(5))
print(factorial.__doc__)
print(type(factorial), type(A))
print(set(sorted(dir(factorial))) - set(sorted(dir(A))))
print(factorial.__name__)
print(factorial.__code__)  # 파일 위치와 코드라인 세부정보
print()

# 변수 할당하여 실행
var_func = factorial
print(var_func)
print(var_func(10))
print(list(map(var_func, range(1, 10))))
print()


# 함수 인수 전달 및 함수로 결과 반환 -> 고위 함수(Higher-order function)
# map, filter, reduce
print(list(map(var_func, filter(lambda x: x % 2, range(1, 6)))))
print([var_func(i) for i in range(1, 6) if i % 2])
print()

# reduce - 감소시켜가면서 누적하는 함수
from functools import reduce
from operator import add

# reduce(함수, 리스트)
print(reduce(add, range(1, 11)))
print(sum(range(1, 11)))

# 익명함수(lambda)
# 가급적 주석 작성 - 복잡한 함수 작성시 이해하기가 어려울 수도있다.
# 가급적 함수 작성이 권장
# 일반 함수 형태로 리펙토링 권장(이름이 있는 함수)

print(reduce(lambda x, t: x + t, range(1, 11)))
print()

# Callable - 호출 연산자 -> 메소드 형태로 호출이 가능한지 확인
# 호출 가능 확인
print(
    callable(str), callable(A), callable(factorial), callable(var_func), callable(3.14)
)
# 3.14는 함수호출이 가능한 부분이 아니라 False
print()

# partial 사용법 - 인수를 고정 -> 주로 콜백 함수에 사용
from functools import partial
from operator import mul

print(mul(10, 10))

# 인수 고정
five = partial(mul, 5)  # partial(함수, 고정숫자)
# 고정 추가
six = partial(five, 6)

print(five(10))
print(six())
print([five(i) for i in range(1, 11)])
print(list(map(five, range(1, 11))))
