# 커피 판매 프로그램 ver.1
# from coffee

coffeList = [{'name': '아메리카노', 'price': 2000}, {'name': '라떼', 'price': 2500}, {'name': '바닐라라떼', 'price': 3000}]

while True:
    codeNumber = int(input("1.커피 판매 2.커피 메뉴 추가 3. 프로그램 종료: "))
    if codeNumber == 1: # 커피 판매 알고리즘 만들기
        for index, item in enumerate(coffeList):
            print(f"{index}. {item['name']} {item['price']}원")
        coffeNumber = int(input("번호 입력: "))
    elif codeNumber == 2: # 커피 추가 알고리즘 만들기
        newCoffeName = input("커피 이름:")
        newCoffePrice = int(input("커피 가격:"))
        newCoffeMenu = {'name':newCoffeName, 'price':newCoffePrice}
        coffeList.append(newCoffeMenu)
        print(f"{newCoffeName}이 추가되었습니다.")
    elif codeNumber == 3:
        print("프로그램 종료!")
        break



# 커피 판매 프로그램 ver.1

