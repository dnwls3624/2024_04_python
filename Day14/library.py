# import math
# import random
#
# 랜덤으로 여섯개의 숫자를 뽑아주는 프로그램[1~45] 중복 x
#
import random

lotto = []

while True:
    num = random.randint(1, 46)
    if lotto.count(num) == 0:
        lotto.append(num)
        if len(lotto) == 6:


            break

lotto.sort()
print(lotto)


# print(random.choice(["사과","바나나"."집가고싶다"]))



# 유저에게 6개번호 받고 몇등인지 알려주는프로그램

import random

lotto = []

while True:
    num = random.randint(1, 46)
    if lotto.count(num) == 0:
        lotto.append(num)
        if len(lotto) == 6:

            break

yourNumber = [int(input(f"{x}. 번호입력:")) for x in range(6)]
rank = 6
for x in lotto:
    if yourNumber.count(x) > 0:
        rank -= 1
print(f"로또: {lotto}")
print(f"당신: {yourNumber}")
print(f"{rank}등 축하합니다!")
