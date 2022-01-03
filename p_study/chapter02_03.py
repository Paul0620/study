# chapter02_03
# 객체 지향 프로그래밍(OOP) -> 코드의 재사용, 코드 중복 방지
# 규모가 큰 프로젝트(프로그램) -> 함수 중심 -> 데이터 방대 -> 복잡
# 클래스 중심 -> 데이터 중심 -> 객체로 관리

# Instance Method
# - 클래스 안에서 instance를 만들고, instance를 통해서만 호출이 되는 메소드를 부른다. 첫번째 인자로 self가 있어야함.
# Class Method
# - 클래스를 통해서 호출되는 함수 클래스명.함수명 식으로 호출해서 사용. 클래스안에서 일어나느 변화(설정 값 등)을 주고 싶을 때 사용한다. 첫번째 인자로 cls가 있어야함.
# Static Method
# - 클래스 밖에 있는 함수와 큰 차이가 없지만 클래스의 특성을 갖는 메소드이다. 함수 정의시 함수내에서 인자를 따로 받지 않는다. 클래스와 연관성이 있는 함수를 클래스 안에 정의하여 클래스나 인스턴스를 통해 호출하여 편하게 사용하기 위함.


class Car:
    """
    Car class
    Author : Lee
    Date : 2022.01.03
    Description : Class, Static, Instance Method
    """

    # argument = 전달인자 = 값
    # 함수 호출 시 값을 전달한다고 해서 전달인자라고도 함, 수시로 변하는 값

    # parameter = 매개변수 = 변수
    # 함수 내부에 있는 인자, 특정한 값으로 정해져 있는 것이 아니라, 함수가 호출하며 건네준 argument값이 담기게 됨
    # 매게체 역할을 하기 때문에 매개변수라고도 한다.

    # 클래스 변수 선언(모든 인스턴스가 공유)
    price_per_raise = 1.0

    # __init__ 메소드 사용하여 입력값을 받을 수 있음
    def __init__(self, company, details):
        # 개발자 작성 약속 _변수명
        self._company = company
        self._details = details
        # self.car_count = 10

    def __str__(self):
        return "str : {} - {}".format(self._company, self._details)

    def __repr__(self):
        return "repr : {} - {}".format(self._company, self._details)

    # Instance Method
    # 인스턴스 변수에 엑세스 할 수 있도록 첫 번째 인자에 항상 객체 자신을 의미하는 self 파라미터를 갖는 것들 말함
    # self : 객체의 고유한 속성 값을 사용
    def detail_info(self):
        print(f"Current ID : {id(self)}")
        print(f"Car Detail Info : {self._company} {self._details.get('price')}")

    # Instance Method
    def get_price(self):
        return f'Before Car Price -> company : {self._company}, price : {self._details.get("price")}'

    # Instance Method
    def get_price_culc(self):
        return f'Before Car Price -> company : {self._company}, price : {self._details.get("price") * Car.price_per_raise}'

    # Class Method
    # 모든 인자가 공유하는 클래스를 넘겨준다.
    # 처음 받는 인자가 약속되어있음 cls
    @classmethod
    def raise_price(cls, per):
        if per <= 1:
            print("Please Enter 1 Or More")
            return
        else:
            cls.price_per_raise = per
            print("Succeed price increased.")

    # Staic Method
    # 아무것도 받는 파라미터가 없다
    @staticmethod
    def is_bmw(inst):
        if inst._company == "Bmw":
            return f"OK! This car is {inst._company}"
        else:
            return "Sorry. This is not Bmw."


# self의 의미 - 인스턴스 메소드, self가 있어야 고유 id를 통해 정보를 확인할 수 있음
car1 = Car("Ferrari", {"color": "White", "horsepower": 400, "price": 8000})
car2 = Car("Bmw", {"color": "Black", "horsepower": 270, "price": 5000})

# 전체정보
car1.detail_info()
car2.detail_info()
print()

# 가격정보
# print(car1._details.get("price")) 직접 접근하는 것은 보안상 좋지 않음
print(car1.get_price())
print(car2.get_price())

# 가격 인상(클래스 메소드 미사용) 권장하는 방식은 아님
Car.price_per_raise = 1.4

# 가격정보(인상 후)
print(car1.get_price_culc())
print(car2.get_price_culc())
print()

# 가격 인상(클래스 메소드 활용)
Car.raise_price(1.6)

# 가격정보(인상 후)
print(car1.get_price_culc())
print(car2.get_price_culc())
print()

# Bmw확인
# 클래스나 인스턴스 둘다 호출 가능, 유연한 성격을 가지고 있음
# 인스턴스 호출(Static)
print(car1.is_bmw(car1))
print(car2.is_bmw(car2))
# 클래스 호출(Static)
print(Car.is_bmw(car1))
print(Car.is_bmw(car2))
