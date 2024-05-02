# map(how, target): target을 바꿔주기
#1
# numList = [i for i in range(101)]
# [100,101,102,103,...,200]
# result = list(map(lambda x:x+100,numList))
# print(result)
#2
# emailList = ["abc@naver.com","mega@naver.com","korea@naver.com"]
#
# result =list(map(lambda x: x.split("@")[0],emailList))
# print(result)

# filter: target을 필터링 해줌
# result1 = list(filter(lambda x:x % 2 == 0, numList))
# print(result1)
#
#
# fruits = ["apple", "banana", "cherry", "kiwi"]
# result3 = filter(lambda x:len(x) <= 5, fruits)
# print(result3)
#
# result4 = filter(lambda x:'a' in x <= 5, fruits)
# print(result4)