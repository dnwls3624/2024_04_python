# 콘솔창에 내용 출력 기능
print("파이썬 공부 복습")

#변수
# 1.숫자 시작 안됨
# 2.특수문자_ 빼고 가능
# 3.예약어 안됨[추후 배울 것]
# 4. 두 단어 이상 합쳐지면 snake,camel 이름으로 짓기
language = "한국어"
print(f"지금 설정한 언어는 {language}")

# 콘솔창에 유저에게 글을 입력 받는 기능 input
number = input("좋아하는 번호는?")
print(f"좋아하시는 번호는 {number}")

# # 어제의 일기 프로그램
# date = input("어제 날짜는?")
# event = input("어제 있었던 주요 사건은?")
# print(f"어제는 {date}, 주요 사건은{event} 였습니다.")

#아침,점심,저녁 먹은 메뉴 보여주기 프로그램

date = input("오늘의 날짜")
breakfast = input("오늘 아침메뉴는?")
lunch = input("오늘 점심메뉴는?")
diner = input("오늘 저녁메뉴는?")
print(f"오늘은 {date},아침에는 {breakfast}, 점심에는 {lunch}, 저녁에는 {diner}를 먹었습니다")
