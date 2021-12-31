# chapter02_01
# 객체 지향 프로그래밍(OOP) -> 코드의 재사용, 코드 중복 방지
# 규모가 큰 프로젝트(프로그램) -> 함수 중심 -> 데이터 방대 -> 복잡
# 클래스 중심 -> 데이터 중심 -> 객체로 관리

# 일반적인 코딩
# 차량_01
car_company_01 = "Ferrari"
car_detail_01 = [{"color": "White"}, {"horsepower": 400}, {"price": 8000}]

# 차량_02
car_company_02 = "BMW"
car_detail_02 = [{"color": "Black"}, {"horsepower": 270}, {"price": 5000}]

# 차량_03
car_company_03 = "Audi"
car_detail_03 = [{"color": "Silver"}, {"horsepower": 300}, {"price": 6000}]

# 위 방식은 개수가 늘수록 불편함

# 리스트 구조로 작성
# 관리하기가 불편
# 왜? 인덱스 접근 시 실수 가능성과 삭제 불편
car_company_list = ["Ferrari", "BMW", "Audi"]
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
