#Quiz
#사용자로부터 10,000부터 99,999 사이의 양의 정수 n을 입력받아,
#해당 정수의 100의 자리 값을 출력하는 프로그램을 작성하세요
#예를 들어, 입력값이 12345라면 3이 100의 자리 값으로 출력 되어야 합니다

num = input("10,000부터 99,999 사이의 정수 입력:")
intnum = int(num) #ex)47592
hundred = intNum // 100 #475
result = hundred % 10
print(result)
