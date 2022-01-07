# chapter06_03
# 병행성(Concurrency) - 한 컴퓨터가 여러 일을 동시에 수행 -> 단일 프로그램안에서 여러일을 쉽게 해결
# 병렬성(Parallelism) - 여러 컴퓨터가 여러 일을 동시에 수행 -> 속도
# 코루틴(Coroutine) - 단일(싱글) 쓰레드, 스택을 기반으로 동작하는 비동기 작업
# https://docs.python.org/ko/3/library/asyncio-task.html

# 쓰레드 - os에서 관리, cpu 코어에서 실시간, 시분할 비동기 작업 -> 멀티쓰레드라고도 함
# yield, send - 메인과 서브가 상호작용
# 코루틴 제어, 상태, 양방향 전송

# 서브루틴 - 메인루틴을 호출 -> 서브루틴에서 수행(흐름제어)
# 코루틴 - 루틴 실행 중 중지를 함(중지 위치를 기억했다가 나중에 다시 실행) -> 동시성 프로그래밍
# 코루틴 장점 - 쓰레드에 비해 오버헤드 감소
# 쓰레드 - 싱글쓰레드 or 멀티쓰레드 -> 코딩이 복잡 -> 복잡한 이유는 공유되는 자원 -> 교착 상태 발생 가능성, 컨텍스트 스위칭 비용 발생이 큼, 자원 소비 가능성 증가
# def -> async, yield -> await 대체 사용가능


# 코루틴 예제1
# 서브루틴
def coroutine1():
    print(">>> coroutine stated.")
    i = yield
    print(f">>> coroutine received : {i}")


# 메인 루틴
# 제너레이터 선언
cr1 = coroutine1()
print(cr1, type(cr1))
# yield 지점까지 서브루틴 수행
# next(cr1)

# 기본 전달 값 None
# cr1.send(100)  # send의 기능은 값도 보내주면서 next의 기능도 포함하고 있음


# 잘못된 사용
cr2 = coroutine1()
# yield가 있는 지점에 도착해서 처리해야 send를 수행할 수 있음
# cr2.send(100)


# 코루틴 예제2
# GEN_CREATED - 처음 대기 상태
# GEN_RUNNING - 실행 상태
# GEN_SUSPENDED - Yield 대기 상태
# GEN_CLOSED - 실행 완료 상태


def coroutine2(x):
    print(f">>> croutine started x = {x}")
    y = yield x
    print(f">>> croutine received y = {y}")
    z = yield x + y
    print(f">>> croutine received z = {z}")


cr3 = coroutine2(10)

from inspect import getgeneratorstate  # 상태보기 GEN_상태명

print(getgeneratorstate(cr3))
print(next(cr3))
print(cr3.send(100))
print()


# 코루틴 예제3
# StopIteration 자동 처리(3.5버전 이후에서 await로 처리 가능)
# 중첩 코루틴 처리


def generator1():
    for x in "AB":
        yield x

    for y in range(1, 4):
        yield y


t1 = generator1()
# print(next(t1))
# print(next(t1))
# print(next(t1))
# print(next(t1))
# print(next(t1))

t2 = generator1()
print(list(t2))  # for이 따로따로 있어서 병합되어서 나옴
print()


def generator2():
    # iterable이 끝날떄까지 반환하는 작성 양식 for문 방식과 같음
    yield from "AB"
    yield from range(1, 4)


t3 = generator2()

# print(next(t3))
# print(next(t3))
# print(next(t3))
# print(next(t3))
# print(next(t3))

t4 = generator2()
print(list(t4))
