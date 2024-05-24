#pandas 라이브러리 설치
import pandas
from faker import Faker
import random






pandas.Series()

# arr = [1 for x in range(101)]
# series = pandas.Series(arr)
# print(series)



# data = {
#     'movies': ["혹성탈출","범죄도시4","설계자","퓨리오사"],
#     'popcorn': ["오리지널 팝콘", "어니언 팝콘", "캬라멜 팝콘", "소금 팝콘"],
#     'beverage': ["콜라", "제로콜라", "사이다", "제로사이다"]
# }
#
# df = pandas.DataFrame(data)
# print(df)


# 학생이름 학년 전공 평균학점

# data = {
#     'name': ["김우진", "전수효", "김나영", "홍길동", "유재석", "강호동", "신동엽", "박명수", "노홍철", "정준하"],
#     'grade': ["1학년", "2학년", "3학년", "1학년", "2학년", "3학년", "4학년", "1학년", "1학년", "2학년"],
#     'major': ["컴공", "미술", "체육", "실용음악", "바이오", "컴공", "미술", "체육", "실용음악", "바이오"],
#     'score': ["A", "B", "C", "A", "B", "C", "F", "B", "C", "D"]
# }
#
# df = pandas.DataFrame(data)
# print(df)



#


f = Faker('ko_KR')
grade = ["1학년", "2학년", "3학년", "1학년", "2학년", "3학년", "4학년", "1학년", "1학년", "2학년"]
major = ["컴공", "미술", "체육", "실용음악", "바이오", "컴공", "미술", "체육", "실용음악", "바이오"]
score = ["A", "B", "C", "A", "B", "C", "F", "B", "C", "D"]




data = {
    'name': [f.name() for x in range(1000)],
    'grade': [random.randint(1,5) for x in range(1000)],
    'major': [random.choice(major) for x in range(1000)],
    'score': [round(random.uniform(1, 4.5), 2) for x in range(1000)],
}
df = pandas.DataFrame(data)
df.to_csv('university.csv',index=False,encoding='cp949')

