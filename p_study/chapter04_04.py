# chapter04_04
# sequence란? - 데이터를 순서대로 하나씩 나열하여 나타낸 데이터 구조
# 시퀀스형
# 해시테이블(hashtable) -> 적은 리소스로 많은 데이터를 효율적으로 관리
# Dict -> Key 중복 허용을 하지 않음, Set -> 중복을 허용하지 않음
# Dict 및 Set(집합) 심화
# set의 형식 순서가 없고 집합안에서는 unique한 값을 가짐, mutable 객체, dict와 비슷하지만 key가 없다. 값만 존재
# 해시테이블로 구현되어있는 set의 시간복잡도는 O(1)이다. 왜냐? 해당 값을 해시 함수에 넣어 인덱스에 바로 접근하여 값을 찾기 때문에

# immutable Dict 수정이 불가능한
from types import MappingProxyType  # 읽기 전용의 dict 만들기

d = {"key1": "value1"}

# Read Only
# frozen이란 용어를 사용하기도함 변경불가라는 의미로
d_frozen = MappingProxyType(d)

print(d, id(d))
print(d_frozen, id(d_frozen))

# 수정 가능
d["key2"] = "value2"
print(d)

# 수정 불가
# d_frozen["key2"] = "value2"
# print(d_frozen) # 에러 발생 - 수정 불가기 때문에
print()

s1 = {"Apple", "Orange", "Apple", "Orange", "Kiwi"}
s2 = set(["Apple", "Orange", "Apple", "Orange", "Kiwi"])
s3 = {3}
s4 = set()  # {}로 비어있는 값을 선언하면 딕셔너리로 타입이 정해져버려서 set으로 선언해야함
s5 = frozenset({"Apple", "Orange", "Apple", "Orange", "Kiwi"})

s1.add("Melon")

# 추가 불가
# s5.add("Melon")

print(s1, type(s1))
print(s2, type(s2))
print(s3, type(s3))
print(s4, type(s4))
print(s5, type(s5))

# 선언 최적화
# 파이썬은 실행시 바이트 코드를 실행 -> 파이썬 인터프리터 실행
from dis import dis

# set을 사용하는 것보다 바로 만드는게 과정이 덜걸림
print("--------")
print(dis("{10}"))
print("--------")
print(dis("set([10])"))
print()

# 지능형 집합(Comprehending set)
from unicodedata import name  # 문자열로 이름을 뽑아내기 위해 사용

print("---------")
print({name(chr(i), "") for i in range(0, 256)})
