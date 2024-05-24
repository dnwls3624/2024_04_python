# 메가커피 당일 매출 기록표

# 이름 메뉴 몇시 결제수단 매장/포장

import pandas
from faker import Faker
import random
import datetime


# def time(x):
#     s = detetime.datetime.strftime("07:00", "%H:%M")
#     e = detetime.datetime.strftime("22:00", "%H:%M")
#     total = int((e-s).total_seconds() / 60) #전체 몇분
#     random_minutes = random.randint(0, total)
#     return s + datetime.timedelta(minutes=random_minutes)
#
# print(get_random_time().strftime("%H:%M"))



f = Faker('ko_KR')
menuList = ["아이스 아메리카노","바닐라 라떼","자몽에이드","레몬에이드","딸기라뗴","카페모카","수박주스"]
payList = ["cash","card","kakao pay", "samsung pay"]




data = {
    'name': [f.name() for x in range(1000)],
    'menu': [random.choice(menuList) for x in range(1000)],
    # 'time': [time for x in range(1000)],
    'pay': [random.choice(payList) for x in range(1000)],
    'togo':[random.choice(["포장","매장"]) for x in range(1000)],

}

df = pandas.DataFrame(data)
df.to_csv('mega.csv',index=False,encoding='cp949')