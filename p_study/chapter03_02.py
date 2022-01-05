# chapter03_02
# Special(Magic) Method
# 파이썬의 핵심 -> 시퀀스(Sequence), 반복(Iterator), 함수(Functions), Class(클래스)
# 매직 메소드란? - 클래스안에 정의할 수 있는 특별한(Built in  = 이미 만들어져 있는) 메소드
# 작성 형식은 더블언더 스코어 이루어져 있음

# 클래스 예제2
# (5, 2) + (4, 3) = (9, 5)
# (10, 3) * 5 = (50, 15)
# max((5, 10)) = 10


class Vector(object):  # object의 경우는 생략이 가능
    # *args -> arguments(인자들), **kwargs -> keyword arguments(키워드 된 인자들)
    # *args로 받게되면 튜플형태로 모든 인자들을 받게된다
    # **kwargs는 dictionary의 형태만 받는다.
    # 순서를 지켜서 args, kwargs 순으로 데이터를 넣어줘야함 타입이 다르기 때문에
    def __init__(self, *args):
        """Create a vector, example : v = Vector(5, 10)"""
        if len(args) == 0:
            # 언팩킹 처리
            self._x, self._y = 0, 0
        else:
            self._x, self._y = args

    def __repr__(self):
        """Return the vector informations."""
        # %r은 repr에서 사용하는 문자열 %s라면 str에서 사용
        return "Vector(%r, %r)" % (self._x, self._y)

    def __add__(self, other):
        """Return ther vector addition of self and other"""
        return Vector(self._x + other._x, self._y + other._y)

    def __mul__(self, y):
        return Vector(self._x * y, self._y * y)

    def __bool__(self):
        # x, y중 큰 값이 0보다 크다면 True
        return bool(max(self._x, self._y))


# Vector 인스턴스생성
v1 = Vector(5, 7)
v2 = Vector(23, 35)
v3 = Vector()

# 매직메소드 출력
# 클래스가 아닌 메소드에 doc 설정하기
print(Vector.__init__.__doc__)
print(Vector.__repr__.__doc__)
print(Vector.__add__.__doc__)
print()
print(v1, v2, v3)
print(v1 + v2)
print(v1 * 3)
print(v2 * 10)
print(bool(v1), bool(v2), bool(v3))
