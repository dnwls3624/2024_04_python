# #quiz1
# num = int(input("정수입력: "))
# if num % 2 == 1 and num > 0:
#     print("양의 홀수")
# if num % 2 == 0 and num > 0:
#     print("양의 짝수")
# if num % 2 == 1 and num < 0:
#     print("음의 홀수")
# if num % 2 == 0 and num < 0:
#     print("음의 짝수")
# if num == 0:
#     print("0")
# #or
# if num > 0:
#     if num % 2 == 1:
#         print("양의 홀수 입니다")
#     else:
#         print("양의 짝수 입니다")
# elif num == 0:
#     print("0")
# else:
#     if num % 2 == 1:
#         print("음의 홀수 입니다")
#     else:
#         print("음의 짝수 입니다.")
#
# #or
#
# if isPositive and isOdd:
#     print("양의 홀수 입니다")
# elif isPositive and isEven:
#     print("양의 짝수 입니다.")
# elif isNegative and isOdd:
#     print("음의 홀수 입니다")
# elif isNegative and isEven:
#     print("음의 짝수 입니다")
# else:
#     print("0입니다.")

#quiz2
#
# x = int(input("x축 좌표값 입력: "))
# y = int(input("y축 좌표값 입력: "))
#
#
# if isXZero and isYZero:
#     print("원점 입니다.")
# elif isYZero:
#     print("x축 위에 존재합니다")
# elif isXZero:
#     print("y축 위에 존재합니다")
# elif isXPositive and isYPositive:
#     print("1사분면 위에 존재합니다.")
# elif isXNegative and isYPositive:
#     print("2사분면 위에 존재합니다.")

#quiz4

# price = int(input("구매한 가격: "))
# if price >= 200000:
#     print(f"구매 금액은{price}원, 할인율은{20}%, 할인 금액은{price * 0.2}, 결제 금액은{price - price * 0.2}입니다. ")
# elif price >= 100000:
#     print(f"구매 금액은{price}원, 할인율은{10}%, 할인 금액은{price * 0.1}, 결제 금액은{price - price * 0.1}입니다.")
# elif price >= 50000:
#     print(f"구매 금액은{price}원, 할인율은{5}%, 할인 금액은{price * 0.05}, 결제 금액은{price - price * 0.05}입니다.")
# else:
#     print(f"구매 금액은{price}원, 할인율은{0}%, 할인 금액은{price * 0}, 결제 금액은{price - price * 0}입니다.")
