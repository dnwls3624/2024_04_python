# 1. 문자열 섞기
# 문자열 my_str과 n이 매개변수로 주어질 때, my_str을 길이 n씩 잘라서 저장한 배열을
# return하도록 solution함수를 완성해 주세요

def solution(my_str, n):
    return [my_str[x:x+n] for x in range(0, len(my_str), n)]

my_str = 'aslkdkaswfwf'
n = 3

print(solution(my_str, n))

# def solution(my_str, n):
#     arr = []
#     word = ""
#     for index, item in enumerate(my_str, 1):
#         word += item
#         if index % n == 0:
#             arr.append(word)
#             word = ""
#          return arr
# arr.append(word)
# my_str = 'aslkdkaswfwf'
# n = 3
# print(solution(my_str, n))







# 2. jadenCase 문자열 만들기
# jadenCase란 모든 단어의 첫 문자가 대문자이고, 그 외의 알파벳은 소문자인 문자열입니다.
# 단, 첫 문자가 알파벳이 아닐때에는 이어지는 알파벳은 소문자로 쓰면 됩니다.
# 문자열 s가 주어졌을 때, s를 jadenCase로 바꾼 문자열을 리턴하는 함수,solution을 완성해주세요

def solution1(s):
    return " ".join(word[0].upper() + word[1:].lower() for word in s.split())

s = "3people unFollowed me"
print(solution1(s))

def solution1(s):
    return " ".join([x.capitalize() + " " for x in s.split(" ")])

s = "3people unFollowed me"
print(solution1(s))
