import pandas

df = pandas.read_csv("company.csv", encoding='cp949')
# 기본 열 뽑기
# print(df['name']) # 하나 열
# print(df[['name','age','salary']]) # 다중 열

# 조건으로 열 뽑기
# a = df['years_at_company'] >= 10
# b = df['job_satisfaction'] >= 8
# c = df['performance_score'] >= 80
#
# print(df[a & b & c])

# 열 추가
# 5년이하-사원
# 10년이하-과장
# 15년이하-부장
# df['test'] = df['age'] * df['years_at_company']


# def makeRank(x):
#     if x <= 5:
#         return '사원'
#     elif x <= 10:
#         return '과장'
#     else:
#         return '부장'


# apply 함수
# df['rank'] = df['years_at_company'].apply(makeRank)
# 'performance_score'

# 20점 - 권고 사직
# 50점 - 직급 유지
# 80점 - 보너스
# 100점 - 승진

def makeRate(x):
    if x <= 20:
        return "권고 사직"
    elif x <= 50:
        return "직급 유지"
    elif x <= 80:
        return "보너스"
    else:
        return "승진"

df['rate'] = df['performance_score'].apply(makeRate)
# print(df.info)
# print(df.describe())

print(df.sort_values(by='age'))













