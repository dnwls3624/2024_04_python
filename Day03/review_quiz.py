  Quiz1
"현재 원화를 입력 하면 달러로 바뀌는 프로그램을 작성하세요!"
-예시:1410 -> 1$

won = int(input("원화 입력 하세요:"))
rate = 1400
print(f"달러: {won/rate}$ 입니다.")


  Quiz2
("사용자로부터 두 개의 숫자를 입력받아, 이 두 숫자에 합,차,곱,몫,나머지,제곱을 계산하는 프로그램을 만들어보세요."
 " 입력받은 두숫자에 대해 다음과 같은 연산 결과를 출ㄹ력해주는 프로그램을 작성해보세요")

num1 = int(input("첫 번째 정수:"))
num2 = int(input("두 번째 정수:"))
result = int(num1) + int(num2)
print(f"합:{result}")
result = int(num1) - int(num2)
print(f"차:{result}")
result = int(num1) * int(num2)
print(f"곱:{result}")
result = int(num1) // int(num2)
print(f"몫:{result}")
result = int(num1) % int(num2)
print(f"나머지:{result}")
result = int(num1) ** int(num2)
print(f"제곱:{result}")

  Quiz3
radius = int(input("원의 반지를:"))
pi = 3.14
print(f"원의 넓이:{radius**2*pi},원의 둘레:{radius*2pi}")
