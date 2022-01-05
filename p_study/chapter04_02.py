# chapter04_02
# sequence란? - 데이터를 순서대로 하나씩 나열하여 나타낸 데이터 구조
# 시퀀스형
# 컨테이너(Container : 서로 다른 자료형[list, tuple, collections.deque])
# 플랫(Flat : 한개의 자료형[str, bytes, bytearray, array.array, memoryview])
# 가변형(list, bytearray, array.array, memoryview, deque)
# 불변형(tuple, str, bytes)
# 리스트 및 튜플 고급

# Tuple Advanced
# Unpacking ex) b, a = a, b
print(divmod(100, 9))
print(divmod(*(100, 9)))  # tuple로 감싸져 있을때 *를 이용하여 Unpacking을 하여 진행해야 결과값이 나옴
print(*(divmod(100, 9)))  # *를 이용하여 튜플을 꺼내어 보여줌
print()

x, y, *rest = range(10)
print(x, y, rest)  # x = 0,  y = 1, rest = [2, 3, 4, 5, 6, 7, 8, 9, 10]

x, y, *rest = range(2)
print(x, y, rest)  # x = 0, y = 1, rest = [] 만약 rest 앞에 * 이 없다면 에러발생

x, y, *rest = 1, 2, 3, 4, 5
print(x, y, rest)
print()

# Mutable(가변) vs Immutable(불변)
l = (15, 20, 25)  # tuple 불변형
m = [15, 20, 25]  # list 가변형

print(l, id(l))
print(m, id(m))

l = l * 2
m = m * 2

# 이 두개의 경우는 변수를 재선언 한거기 때문에 위의 처음 변수선언과 id값이 둘다 다르다
print(l, id(l))
print(m, id(m))

l *= 2
m *= 2

print(l, id(l))  # id값이 재할당이 이루어짐
print(m, id(m))  # 가변형이라 id값이 그대로임
print()

# sort vs sorted
# 정렬방식 종류 reverse, key=len, key=str.lower, key=func...
# sorted : 정렬 후 새로운 객체 반환, 원본 수정 안됨
f_list = ["orange", "apple", "mango", "papaya", "lemon", "strawberry", "coconut"]
print("원본 ", f_list)
print("sorted ", sorted(f_list))  # 정렬
print("sorted reverse ", sorted(f_list, reverse=True))  # 역순
print("sorted len ", sorted(f_list, key=len))  # 길이순
print("sorted 함수사용 ", sorted(f_list, key=lambda x: x[-1]))  # 맨 마지막 글자를 기준으로 정렬
print(
    "sorted 함수사용 reverse ", sorted(f_list, key=lambda x: x[-1], reverse=True)
)  # 역순 정렬
print()

# sort : 정렬 후 객체 직접 변경, 원본 수정 됨
# 반환 값 확인(None)
# 원본이 수정된거라 원본을 입력하면 변환된 것이 출력됨
print("sort ", f_list.sort(), f_list)
print("sort reverse ", f_list.sort(reverse=True), f_list)
print("sort len ", f_list.sort(key=len), f_list)
print("sort 함수사용 ", f_list.sort(key=lambda x: x[-1]), f_list)
print("sort 함수사용 reverse ", f_list.sort(key=lambda x: x[-1], reverse=True), f_list)
print()

# list vs Array 적합한 사용법
# 리스트 기반 : 융통성, 다양한 자료형, 범용적 사용
# 숫자 기반 : 배열(리스트와 거의 화환가능)
