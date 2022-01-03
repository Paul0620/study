# chapter02_02
# 객체 지향 프로그래밍(OOP) -> 코드의 재사용, 코드 중복 방지
# 규모가 큰 프로젝트(프로그램) -> 함수 중심 -> 데이터 방대 -> 복잡
# 클래스 중심 -> 데이터 중심 -> 객체로 관리


class Car:
    """
    Car class
    Author : Lee
    Date : 2022.01.03
    """

    # 클래스 변수 선언(모든 인스턴스가 공유)
    car_count = 0

    # __init__ 메소드 사용하여 입력값을 받을 수 있음
    def __init__(self, company, details):
        # 개발자 작성 약속 _변수명
        self._company = company
        self._details = details
        # self.car_count = 10
        Car.car_count += 1

    # str, repr메소드가 없다면 클래스명의 정보만 나옴
    # 간단하게 str - 사용자 레벨, repr - 개발자 레벨

    # __str__ 메소드를 활용하여 Car()클래스 내부에 담은 값을 출력할 수 있음
    def __str__(self):
        return "str : {} - {}".format(self._company, self._details)

    # 텍스트의 정보뿐만 아니라 본 목적인 객체를 사람이 이해할 수 있는 평문으로 표현할 수 있음
    def __repr__(self):
        return "repr : {} - {}".format(self._company, self._details)

    def __del__(self):
        Car.car_count -= 1

    def detail_info(self):
        print(f"Current ID : {id(self)}")
        print(f"Car Detail Info : {self._company} {self._details.get('price')}")


# self의 의미 - 인스턴스 메소드, self가 있어야 고유 id를 통해 정보를 확인할 수 있음
car1 = Car("Ferrari", {"color": "White", "horsepower": 400, "price": 8000})
car2 = Car("Bmw", {"color": "Black", "horsepower": 270, "price": 5000})
car3 = Car("Audi", {"color": "Silver", "horsepower": 300, "price": 6000})


# ID 확인 - 각자 고유의 값을 가지고 있음
print(id(car1))
print(id(car2))
print(id(car3))

print(car1._company == car2._company)
print(car1 is car2)
print()

# dir & __dict__ 확인
print(dir(car1))  # 해당 인스턴스가 가지고 있는 모든 인스턴스(매직)메소드와 인스턴스 변수 등을 리스트 형태로 출력
print(car1.__dict__)  # 해당되는 값이 있는 것들만 key와 value 형태로 정보를 보여줌

# Doctring - 클래스안에 달아놓은 코멘트를 작성해 놨다면 보는 방법
print(Car.__doc__)
print()

# detail_info 출력
car1.detail_info()
car2.detail_info()
Car.detail_info(car3)
# 에러
# Car.detail_info()
# 클래스 이름으로 접근시 전달할 인자가 없다면 에러가 발생함 왜냐면 값을 넘긴게 없기 때문에
print()

# 비교 - 왜 같은가? -> 클래스 자체는 하나이기 떄문에 같은 클래스를 찾는거라 같음, 부모가 같다
print(id(car1.__class__) == id(car2.__class__) == id(car3.__class__))
print()

# 공유확인
print(car1.car_count)
print(car1.__dict__)
print(dir(car1))
print()

# 접근
print(car1.car_count)
print(Car.car_count)  # 공유를 하는 것이다보니 클래스로 접근하는 것이 정석


# 삭제하고나서 공유되어있는 count 체크해보기
del car2
print(car1.car_count)
print(Car.car_count)


# 인스턴스 네임스페이스에 없으면 상위에서 검색
# 즉, 동일한 이름으로 변수 생성이 가능(인스턴스 검색 후 없으면 상위(클래스 변수, 부모클래스 변수))
