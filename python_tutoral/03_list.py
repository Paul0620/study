# 리스트란 서로 연관되어있는 원소끼리 그룹화

s_list = ["anna", "bibi", "coro"]

n_list = [1, 2, 3]

# 리스트 안의 특정 값을 가져오는 법
print("특정 값", s_list[1])

# 리스트의 길이를 보는법
print("리스트 길이", len(s_list))

# 리스트에서 가장 작은 값을 알고싶을 때
print("가장 작은 값", min(n_list))

# 리스트에서 가장 큰 값을 알고싶을 때
print("가장 큰 값", max(n_list))

# 합계
print("합계", sum(n_list))


# 통계를 내고 싶을 때 모듈
import statistics

# 평균값
print("평균값", statistics.mean(n_list))


# 랜덤 모듈을 활용하여 리스트안의 값을 랜덤하게 가져오기
import random

print("랜덤으로 대상 리스트안의 값을 가져오기", random.choice(s_list))
