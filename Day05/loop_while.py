x = 10
while x > 0:
    print("불금인데 학원온거 ㅇㅈ")
    x -= 1
.


while True:
    x = int(input("숫자 0을 넣어야 멈춤: "))
    if x == 1:
        print(f"아이스 아메리카노")
    elif x == 2:
        print(f"아이스 라떼")
    elif x == 0:
        break


quiz1

while True:
    x = int(input("언어를 고르세요(1.python 2.java 3.c++): "))
    if x == 1:
        print(f"python")
    elif x == 2:
        print(f"java")
    elif x == 3:
        print(f"c++")
    elif x == 4:
        print(f"프로그램 종료")
        break
    else:
        print(f"숫자를 잘못 입력 하였습니다")



while True:
    print("계산기 프로그램!")
    num1 = int(input("정수1 입력: "))
    num2 = int(input("정수2 입력: "))
    codeNumber = int(input("0.프로그램 종료, 1.더하기, 2.빼기, 3.곱하기, 4.제곱, 5. 나누기(몫): "))

    if codeNumber == 0:
        print("프로그램 종료")
        break
    elif codeNumber == 1:
        print(num1 + num2)
    elif codeNumber == 2:
        print(num1 - num2)
    elif codeNumber == 3:
        print(num1 * num2)
    elif codeNumber == 4:
        print(num1 ** num2)
    elif codeNumber == 5:
        print(num1 // num2)
    else:
        print("다시 입력하여 주세요!")