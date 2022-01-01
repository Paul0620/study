# chapter02_01
# 객체 지향 프로그래밍(OOP) -> 코드의 재사용, 코드 중복 방지
# 규모가 큰 프로젝트(프로그램) -> 함수 중심 -> 데이터 방대 -> 복잡
# 클래스 중심 -> 데이터 중심 -> 객체로 관리

# 일반적인 코딩
# 차량_01
car_company_01 = "Ferrari"
car_detail_01 = [{"color": "White"}, {"horsepower": 400}, {"price": 8000}]

# 차량_02
car_company_02 = "Bmw"
car_detail_02 = [{"color": "Black"}, {"horsepower": 270}, {"price": 5000}]

# 차량_03
car_company_03 = "Audi"
car_detail_03 = [{"color": "Silver"}, {"horsepower": 300}, {"price": 6000}]


# 위 방식은 개수가 늘수록 불편함
# 리스트 구조로 작성
# 관리하기가 불편
# 왜? 인덱스 접근 시 실수 가능성과 삭제 불편
car_company_list = ["Ferrari", "Bmw", "Audi"]
car_detail_list = [
    {"color": "White", "horsepower": 400, "price": 8000},
    {"color": "Black", "horsepower": 270, "price": 5000},
    {"color": "Silver", "horsepower": 300, "price": 6000},
]

del car_company_list[1]
del car_detail_list[1]

print(car_company_list)
print(car_detail_list)
print()


# 딕셔너리 구조
# 코드 반복 지속, 중첩 문제(key)가 있다, 키 조회 예외 처리 등
car_dicts = [
    {
        "car_company": "Ferrari",
        "car_detail": {"color": "White", "horsepower": 400, "price": 8000},
    },
    {
        "car_company": "Bmw",
        "car_detail": {"color": "Black", "horsepower": 270, "price": 5000},
    },
    {
        "car_company": "Audi",
        "car_detail": {"color": "Silver", "horsepower": 300, "price": 6000},
    },
]

# pop(key)나 del을 이용해 제거
del car_dicts[1]
print(car_dicts)
print()


# 클래스 구조
# 구조 설께 후 재사용성 증가, 코드 반복 최소화, 메소드를 활용


class Car:
    # __init__ 메소드 사용하여 입력값을 받을 수 있음
    def __init__(self, company, details):
        self._company = company
        self._details = details

    # str, repr메소드가 없다면 클래스명의 정보만 나옴
    # 간단하게 str - 사용자 레벨, repr - 개발자 레벨

    # __str__ 메소드를 활용하여 Car()클래스 내부에 담은 값을 출력할 수 있음
    def __str__(self):
        return "str : {} - {}".format(self._company, self._details)

    # 텍스트의 정보뿐만 아니라 본 목적인 객체를 사람이 이해할 수 있는 평문으로 표현할 수 있음
    def __repr__(self):
        return "repr : {} - {}".format(self._company, self._details)


car1 = Car("Ferrari", {"color": "White", "horsepower": 400, "price": 8000})
car2 = Car("Bmw", {"color": "Black", "horsepower": 270, "price": 5000})
car3 = Car("Audi", {"color": "Silver", "horsepower": 300, "price": 6000})

print(car1)
print(car2)
print(car3)

# 딕셔너리 형태로 확인할 때 사용
print(car1.__dict__)
print(car2.__dict__)
print(car3.__dict__)

# 사용가능한 메소드, 변수 목록 출력ㄴ
# print(dir(car1))

print()

# 리스트 선언하여 출력
car_list = []
car_list.append(car1)
car_list.append(car2)
car_list.append(car3)

print(car_list)

print()

for i in car_list:
    # 명시적으로 사용하여 출력할 수도 있다.
    print(repr(i))
