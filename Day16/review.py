# 1. 조건에 맞게 수열 변환하기
# 정수 배열 arr와 자연수 k가 주어진다
# 만약 k가 홀수라면 arr의 모든 원소에 k를 곱하고, 짝수면 k를 더한다
# 이러한 변환을 마친후 arr를 return하는 solution함수를 완성하세요

#내답
def solution(arr, k):
    if k % 2 == 1:
        return [x * k for x in arr]
    else:
        return [x + k for x in arr]
print(solution([1, 2, 3, 100, 99], 3))


#정답
def solution(arr, k):
    return [x * k if k % 2 == 1 else x + k for x in arr]

print(solution([1, 2, 3, 100, 99], 3))


# 2.A강조하기
# 문자열 myString이 주어진다 myString 에서 알파벳 a가 등장하면 전부A로 변환하고
# A가 아닌 모든 대문자 알파벳은 소문자 알파벳으로 변환하여 return하는 solution1함수를 완성하세요

#내답
def solution1(myString):
    result = ""
    for alphabet in myString:
        if alphabet == 'a':
            result = 'A'
        elif alphabet.isupper():
            result = alphabet.lower()
        else:
            result = alphabet
    return result

print(solution1("aasdjmas;dkljA"))



#정답
def solution1(myString):
    return "".join(['A' if x == 'a' else x.lower() for x in "aasdjmas;dkljA"])


# 3.오늘 날짜 [05-24,05-25,...06-24] 출력하기

import datetime


def solution3(x):
    today = datetime.date.today()
    future_time = today + datetime.timedelta(days=x)
    return future_time.strftime("%m-%d")

a = [solution3(x) for x in range(31)]

print(a)
