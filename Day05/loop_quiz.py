#1. 1~100까지의 총합을 나타내는 프로그램
total = 0
for x in range(1,101):
    total += x
print(total)

#2. 유저에게 과일을 입력 받고 모음을 제거한 단어로 나타내기!


# fruit = input("과일 이름: ")
# for x in fruit:
#     if x != 'a' and x != 'e' and x != 'i' and x != 'o' and x != 'u':
#         print(x)

#or
# fruit = input("과일 이름: ")
# word = ""
# for x in fruit:
#     if not x in 'aeiou':
#         word += x
#     print(word)