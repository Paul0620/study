# chapter04_01
# sequence란? - 데이터를 순서대로 하나씩 나열하여 나타낸 데이터 구조
# 시퀀스형
# 컨테이너(Container : 서로 다른 자료형[list, tuple, collections.deque])
# 플랫(Flat : 한개의 자료형[str, bytes, bytearray, array.array, memoryview])
# 가변형(list, bytearray, array.array, memoryview, deque)
# 불변형(tuple, str, bytes)
# 리스트 및 튜플 고급

# 지능형 리스트(Comprehending lists)
chars = "+_)(*&^%$#@!~"
code_list1 = []

for s in chars:
    # 유니코드 리스트 - ord()로 각 문자를 유니코드로 변환
    code_list1.append(ord(s))
print(code_list1)

# 한줄 코딩
code_list2 = [ord(s) for s in chars]
print(code_list2)

# Comprehending list + Map, Filter
code_list3 = [ord(s) for s in chars if ord(s) > 40]
print(code_list3)

# 람다 표현 - lambda 매개변수 : 표현식
# map 표현 - map(함수, 리스트)
code_list4 = list(filter(lambda x: x > 40, map(ord, chars)))
print(code_list4)

# 문자형으로 다시 변환
print([chr(s) for s in code_list1])
print([chr(s) for s in code_list2])
print([chr(s) for s in code_list3])
print([chr(s) for s in code_list4])
print()

# Generator 생성
# gnerator란? - iterator(반복자)를 생성해주는 함수
import array

# Generator : 한 번에 한 개의 항목을 생성(메모리 유지를 하지 않음)
tuple_g = (ord(s) for s in chars)
array_g = array.array("I", (ord(s) for s in chars))

print(type(tuple_g), tuple_g)  # 리스트처럼 바로 보여주는 것이 아니라 준비만 된 상태
print(next(tuple_g))  # 값을 하나하나 보여줌

print(type(array_g), array_g)
print(array_g.tolist())  # array를 tolist()를 통해 리스트를 반환함
print()

# 제너레이터 예제
print(("%s" % c + str(n) for c in ["A", "B", "C", "D"] for n in range(1, 21)))

for s in ("%s" % c + str(n) for c in ["A", "B", "C", "D"] for n in range(1, 21)):
    print(s)
print()

# 리스트 주의
# 깊은 복사(deep copy), 얕은 복사(shallow copy)
marks1 = [["~"] * 3 for _ in range(4)]
marks2 = [["~"] * 3] * 4

print(marks1)
print(marks2)
print()

# 수정
marks1[0][1] = "X"  # [0][1]의 값만 바뀜
marks2[0][1] = "X"  # 모든 배열의 [1]값이 다 바뀜 왜? -> 배열 하나의 주소값이 4개가 같은 것으로 복사된거라

print(marks1)
print(marks2)

print([id(i) for i in marks1])  # 주소값이 다르다
print([id(i) for i in marks2])  # 주소값이 똑같다
