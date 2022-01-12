"""
Chapter 1
Python Advanced(1) - Python Variable Scope
Keyword - scope, global, nonlocal, locals, globals
"""
"""
전역변수는 주로 변하지 않는 고정 값에 사용한다.
지역변수는 함수 내에 로직 해결에 국한, 소멸주기 - 함수 실행 해제 시 
전역변수를 지역내에서 수정되는 것은 권장하지 않는다.
"""

# 예제1
a = 10  # Global variable


def foo():
    # Read global variable
    print("Ex1 > ", a)


foo()

# Read global variable
print("Ex1 > ", a)

# Ex2
b = 20


def bar():
    b = 30  # Local variable
    print("Ex2 > ", b)  # Read local variable


bar()
print("Ex2 > ", b)


# Ex3
c = 40


def foobar():
    # c = c + 10 # UnboundLocalError
    # c = 10
    # c += 100
    print("Ex3 > ", c)


foobar()


# Ex4
d = 50


def barfoo():
    global d
    d = 60
    d += 100
    print("Ex4 > ", d)


barfoo()


print("Ex4 > ", d)


# Ex5(중요!!!!)
def outer():
    e = 70

    def inner():
        nonlocal e  # 지역변수가 아님을 선언, 한단계 바깥쪽에 위치한 변수를 사용할 수 있음
        e += 10  # e = e + 10
        print("Ex5 > ", e)

    return inner


in_test = outer()  # Closure

in_test()


# Ex6
def func(var):
    x = 10

    def printer():
        print("Ex6 > ", "Printer Func Inner")

    print("Func Inner", locals())  # 지역 전체 출력


func("HI")


# Ex7
print("Ex7 > ", globals())  # 선언했던 변수, 함수에 대한 모든 것이 나옴


# Ex8(지역 -> 전역 변수 생성)
for i in range(1, 10):
    for k in range(1, 10):
        globals()[f"plus_{i}_{k}"] = i + k

print("Ex8 > ", plus_5_5)
print("Ex8 > ", plus_9_9)
