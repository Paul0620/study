# chapter05_02
# https://docs.python.org/ko/3/howto/functional.html
# 함수형 프로그래밍 - 순수함수만을 이용해서 프로그래밍
# 일급함수(First-Class)(일급객체)
# 클로저 기초

# 파이썬 변수 범위(scope)

# 예제 1
def func_v1(a):
    print(a)
    print(b)


# func_v1(10)

# 에제 2
# 전역변수(global)
b = 20


def func_v2(a):
    # 지역변수(local)
    print(a)
    print(b)


func_v2(10)
print()


# 예제 3
c = 30


def func_v3(a):
    global c  # c = 30을 선언
    print(a)
    print(c)
    c = 40


print("함수 실행 전 >>", c)
func_v3(10)
print("함수 실행 후 >>", c)
print()


# Closure(클로저) 사용 이유
# 서버 프로그래밍 -> 동시성(Concurrency)제어 -> 메모리 공간에 여러 자원이 접근 -> 교착상태(Dead Lock)
# 메모리를 공유하지 않고 메시지 전달로 처리하기 위한 -> Erlong
# 클로저는 공유하되 변경되지 않는(Immutable, Read Only) 적극적으로 사용 -> 함수형 프로그래밍하고도 연결이 된다.
# 클로저는 불변자료구조 및 atom, STM -> 멀티스레드(Coroutine) 프로그래밍에 강점을 제공

a = 100

print(a + 100)
print(a + 1000)

# 결과 누적(함수 사용)
print(sum(range(1, 51)))
print(sum(range(51, 101)))
print()

# 클래스 이용
class Averager:
    def __init__(self):
        self._series = []

    # 클래스를 함수처럼 호출할 수 있다.
    def __call__(self, v):
        self._series.append(v)
        print(f"inner >> {sum(self._series)} / {len(self._series)}")
        print(f"inner_list >> {self._series}")
        return sum(self._series) / len(self._series)


# 인스턴스 생성
averager_cls = Averager()

print(averager_cls(10))
print(averager_cls(30))
print(averager_cls(50))
print(averager_cls(193))
