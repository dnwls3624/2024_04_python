#quiz1
# 주어진 문자열 word의 각 문자를 정수 n만큼 반복하여 새로운 문자열을 생성하는 프로그램 작성

# word = input("단어입력: ")
# count = int(input("반복 횟수: "))
#
# newWord = ""
# for x in word:
#     newWord += x * count
# print(newWord)

# quiz2
# 사용자로부터 문자열을 입력받아, 그 문자열 내의 모든 모음(a,e,i,o,u)만 대문자로 변환하는 프로그램을 작성하세요.
# 다른 문자드은 원래의 상태를 유지합니다.
# 이프로그램은 문자열을 처리하여 모음만을 강조하는 방법을 보여줍니다

# word = input("단어를 입력: ")
#
# newWord = ""
# for x in word:
#     if x in "aeiou":
#         newWord += x.upper()
#     else:
#         newWord += x
# print(newWord)


# quiz3
# 문자열 my_string 이 주어졌을 때, 대문자는 소문자로, 소문자는 대문자로 변환한 결과를 반환하는 solution함수 작성
# 문자열은 오직 영어 대문자와 소문자로만 구성되어 있음

# word = input("단어 입력: ")
# newWord = ""
# for x in word:
#     if x. isupper():
#         newWord += x.lower()
#     else:
#         newWord += x.upper()
# print(newWord)

# quiz3
# 단어입력 받고 자음은 대문자화로 출력하기

word = input("단어입력: ")

newWord = ""
for x in word:
    if x not in "aeiou":
        newWord += x.upper()
    else:
        newWord += x
print(newWord)
