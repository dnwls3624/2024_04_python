import sqlite3

connection = sqlite3.connect('RentCar.db')
cursor = connection.cursor()

print("렌트카 프로그램")
while(True):
    codeNumber = input("1.자동차 등록 2.멤버 등록 3.예약 하기[업데이트중] 4.종료: ")
    if codeNumber == "1":
        carNum = input("차량 고유번호를 입력하세요: ")
        carName = input("차량 이름을 입력하세요: ")
        colar = input("차량 색상을 입력하세요: ")
        company = input("차량 제조사를 입력하세요:")
        sql = f"""
        INSERT INTO CARS (carNum,carName,colar,company)
        VALUES ('{carNum}','{carName}','{colar}','{company}');
        """
    elif codeNumber == "2":
        id = int(input("ID를 입력하세요: "))
        name = input("이름을 입력하세요: ")
        address = input("주소를 입력하세요: ")
        phone = input("전화번호를 입력하세요: ")
        sql = f"""
        INSERT INTO MEMBERS (id,name,address,phone)
        VALUES ('{id}','{name}','{address}','{phone}');
        """



        cursor.execute(sql)
        connection.commit()
        connection.close()
        print("데이터베이스 저장 완료")










