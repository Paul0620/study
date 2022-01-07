# chapter06_02
# 병행성(Concurrency) - 한 컴퓨터가 여러 일을 동시에 수행 -> 단일 프로그램안에서 여러일을 쉽게 해결
# 병렬성(Parallelism) - 여러 컴퓨터가 여러 일을 동시에 수행 -> 속도

# Generator 예제1
def generator_ex1():
    print("Start")
    yield "A Point"
    print("Continue")
    yield "B Point"
    print("End")


temp = iter(generator_ex1())

# print(next(temp)) # 'Start', 'A Point'
# print(next(temp)) # 'Continue', 'B Point'
# rint(next(temp)) # 'End'

# for v in generator_ex1():
#   pass
# print(v)

# Gnerator 예제2
temp2 = [x * 3 for x in generator_ex1()]
temp3 = (x * 3 for x in generator_ex1())

# print(temp2)
# print(temp3)

for i in temp2:
    print(i)
print()

for i in temp3:
    print(i)
print()


# Generator 예제3(중요 함수)
# filterfalse, count, takewhile, accumulate, chain, projuct, groupby ...
import itertools

gen1 = itertools.count(1, 2.5)  # 1부터 2.5씩 증가

# print(next(gen1))
# print(next(gen1))
# print(next(gen1))
# .... 무한

# 조건식을 통해 무한으로 안돌게 제어
gen2 = itertools.takewhile(lambda n: n < 1000, itertools.count(1, 2.5))

for v in gen2:
    pass
    # print(v)

# 필터의 반대대로 출력 - filterfalse
gen3 = itertools.filterfalse(lambda n: n < 3, [1, 2, 3, 4, 5])

for v in gen3:
    pass
    # print(v)


# 누적 합계 - accumulate
gen4 = itertools.accumulate([x for x in range(1, 101)])

for v in gen4:
    pass
    # print(v)


# 연결1 - chain - 두개의 iterable을 연결
gen5 = itertools.chain("ABCDE", range(1, 11, 2))
print(list(gen5))

# 연결2 - chain - 튜플형 리스트로 만들기
gen6 = itertools.chain(enumerate("ABCDE"))
print(list(gen6))

# 개별 - iterable형태의 값을 하나씩 나눔
gen7 = itertools.product("ABCDE")
print(list(gen7))

# 개별 - 연산(경우의 수) - repeat를 이용하여 리스트의 조합을 내보냄
gen8 = itertools.product("ABCDE", repeat=2)  # repeat=짝의 개수 ex) 3이면 3가지의 모든 조합방식을 다 보여줌
print(list(gen8))

# 그룹화 - 중복되는 것들을 분류해서 몇개씩 있는지 볼 수 있음
gen9 = itertools.groupby("AAAABBCCCCDDEEE")
# print(list(gen9))
for chr, group in gen9:
    print(chr, " : ", list(group))
