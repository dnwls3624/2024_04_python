#length
len: 문자열 또는 리스트의 길이를 알려주는 기능
print(len("hello")) # 5
print(len([2, 4, 6, 8, 10])) #5

# max, min
print(max([2, 12, 3, 51, 23, 312, 3312, 11])) # 3312
print(min([2, 12, 3, 51, 23, 312, 3312, 11])) # 2

#sum
print(sum([1,2,3,4,5])) #15







#quiz1
# 영어 기사 스크랩 해오고,
# 단어길이가 6글자 이상
# 단어들만 출력하기

# news = """President Joe Biden is casting the 2024 election partly as a referendum on Donald Trump, but it’s a harder card to play now that he’s in office and some voters have warming memories of the former president’s chaotic term."""
#
# words = news.split()
# for x in words:
#     if len(x) >= 6:
#         print(x)






# quiz2
# 문자 길이가 5글자 이하이고 알파벳 a,e 포함되면 대문자로 출력
# 그게 아니면 그 과일의 문자 길이를 출력하는 프로그램

fruits = ["apple","banana","kiwi","mango","strawberry","pineapple","melon"]


for x in fruits:
    if len(x) <= 5 and ("a" in x or "e" in x):
        print(x.upper())
    else:
        print(len(x))




