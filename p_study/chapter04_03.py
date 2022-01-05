# chapter04_03
# sequence란? - 데이터를 순서대로 하나씩 나열하여 나타낸 데이터 구조
# 시퀀스형
# 컨테이너(Container : 서로 다른 자료형[list, tuple, collections.deque])
# 플랫(Flat : 한개의 자료형[str, bytes, bytearray, array.array, memoryview])
# 가변형(list, bytearray, array.array, memoryview, deque)
# 불변형(tuple, str, bytes)
# 해시테이블
# key에 value를 저장하는 구조
# 기술면접 - 키값이 중복일 경우 처리방법 https://jinyes-tistory.tistory.com/12?category=841411
# 파이썬 dict이 해시테이블 예
# 해시테이블을 왜 사용하는가? 키 값의 연산 결과에 따라 직접 접근이 가능한 구조
# key 값을 해싱 함수 -> 해시주소 -> key에 대한 value 참조

# Dict 구조
# print(__builtins__.__dict__)

# Hash값 확인
t1 = (10, 20, (30, 40, 50))
t2 = (10, 20, [30, 40, 50])

print(hash(t1))  # 해시는 불변형만 사용가능
# print(hash(t2)) # 에러가 발생 리스트는 해시값으로 뽑아낼 수 없음 왜냐? 리스트는 값이 바뀔 수 있기 때문에
print()

# Dict Setdefault 예제
source = (
    ("k1", "val1"),
    ("k1", "val2"),
    ("k2", "val3"),
    ("k2", "val4"),
    ("k2", "val5"),
)

new_dict1 = {}
new_dict2 = {}

# No use Setdefault
for k, v in source:
    # k값이 딕셔너리에 있다면 기존 키값에 벨류값 추가
    if k in new_dict1:
        new_dict1[k].append(v)
    else:  # 없다면 새로 만들어서 추가
        new_dict1[k] = [v]

print(new_dict1)

# use Setdefault
for k, v in source:
    new_dict2.setdefault(k, []).append(v)

print(new_dict2)

# 주의사항
# 리스트 형식으로 데이터가 담기지 않음 가장 최근 값들만 담김
new_dict3 = {k: v for k, v in source}

print(new_dict3)
