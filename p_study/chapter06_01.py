# chapter06_01
# 병행성(Concurrency)
# 이터레이터(Iterator), 제너레이터(Generator)
# 이터레이터 - next 함수 호출 시 계속 그 다음 값을 리턴해주는 객체
# - iter 특징 - 예로 for문으로 출력 후 또 한번 for문을 돌리면 읽어들이는 값이 없다 이미 앞선 for문에서 다 값을 읽었기 때문에
# 제너레이터 - next 호출시 그 값을 순차적으로 얻어낼 수 있음, 그 결과값을 얻어내기 위헤 return이 아닌 yield를 사용

# 파이썬 반복 가능한 타입
# collections, text, list, dict, set, tuple, unpacking, *args... : iterable

# 반복 가능한 이유? -> iter(x) 함수 호출
t = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"

# for c in t:
#     print(c)

# while
w = iter(t)

while True:
    try:
        print(next(w))  # 끝이 나올때까지 한글자씩 출력
    except StopIteration:  # 끝까지 왔다면 탈출
        break
print()

# 반복형 확인방법
from collections import abc

print(dir(t))  # 전체 확인
print(hasattr(t, "__iter__"))  # 반복형 말고도 다른 것들도 확인 가능
print(isinstance(t, abc.Iterable))  # 반복형인지 확인
print()


# next
class WordSplitter:
    def __init__(self, text):
        self._idx = 0
        self._text = text.split(" ")

    def __next__(self):
        print("Called __next__")
        try:
            word = self._text[self._idx]
        except IndexError:  # 인덱스 에러가 날때까지
            raise StopIteration("Stopped Iteration. ^^")
        self._idx += 1
        return word

    def __repr__(self):
        return "WordSplit(%s)" % (self._text)


wi = WordSplitter("Do today what you could do tomorrow")

print(wi)
print(next(wi))
print(next(wi))
print(next(wi))
print(next(wi))
print(next(wi))
print(next(wi))
print(next(wi))
# print(next(wi))
print()

# Generator 패턴
# 1. 지능형 리스트, 딕셔너리, 집합 -> 데이터 양 증가, 증가 후 메모리 사용량 증가 -> 제너레이터 사용 권장
# 2. 단위 실행 가능한 코루틴 작성 가능
# 3. 작은 메모리 조각 사용


class WordSplitGenerator:
    def __init__(self, text):
        self._text = text.split(" ")

    def __iter__(self):
        for word in self._text:
            # yield가 return 역할도 대신 해줌
            yield word  # 제너레이터

    def __repr__(self):
        return "WordSplitGenerator(%s)" % (self._text)


wg = WordSplitGenerator("Do today what you could do tomorrow")

wt = iter(wg)

print(wt, wg)
print()

print(next(wt))
print(next(wt))
print(next(wt))
print(next(wt))
print(next(wt))
print(next(wt))
print(next(wt))
# print(next(wt))
