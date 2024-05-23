# # 1. 태어난 년도로 띠 알아보기
# # 사용자에게 태어난 년도를 입력받아 그해에 해당하는 띠를 알려주는 기능을 구현하려한다
# # 12간지를 활용하여 태어난 년도를 입력하면 그 해의 띠를 반환하는 함수 작성
# #
# # birthYear = int(input("태어난 년도를 입력하세요 : "))
# #
def yearToZodiac(year):
        zodiac = {
            0: "원숭이",
            1: "닭",
            2: "개",
            3: "돼지",
            4: "쥐",
            5: "소",
            6: "호랑이",
            7: "토끼",
            8: "용",
            9: "뱀",
            10: "말",
            11: "양"
        }
        return zodiac[year % 12]

#
# # 2. 숫자 뒤집기
# # 자연수 n을 뒤집어 각 자리 숫자를 원소로 가지는 배열 형태를 돌려주는 solution 함수를 만들어 주세요
# # 예를들어 n이 12345면 [5,4,3,2,1]을 리턴합니다
#
#

def makeReverseList(x):
    return list(map(lambda x: int(x),reversed(list(str(12345)))))

# 3. 짝수는 싫어요
# 자연수가 주어질때 내림차순 리스트로 반환하는 솔루션
def solution(num):
    return [x for x in range(10) if x % 2 ==1]
print(makeReverseList(12345))


# 랜덤을 사용해서 띠함수를 사용하여
# 100개 띠들이 있는 리스트 만들기

import random
0
for x in range(10):
a = [yearToZodiac(random.randint(1930,2025) for x in range(100))]
print(a)


random.randint(0,100)
random.randint(["콜라","사이다","환타","스프라이트"])
random.shuffle(b)
b = ["콜라","사이다","환타","스프라이트"]
c = [6, 2, 1, 1]
d = random.choices(b, weights=c, k=10)
print(d)


