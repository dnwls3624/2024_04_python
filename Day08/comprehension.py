# comprehension
#[0~100]리스트 출력

# numList = []
# for x in range(101):
#     numList.append(x)
# print(numList)

#or

# a = [x for x in range(101)]
# print(a)

# "apple" =>

# b = [x for x in "apple"]
# print(a)

# 0~10 짝수만 리스트
# c = [x for x in range(11) if x % 2 == 0]
# print(c)
#
# 0~100 홀수만 리스트
# d = [x for x in range(101) if x % 2 == 1]
# print(d)





# 0~100 짝수를 제곱인 형태인 리스트

# e = [x**2 for x in range(101) if x % 2 == 0]
# print(e)

# f = [x+10 for x in range(11) if x % 2 == 1]
# print(f)

# fruits = ["apple", "banana", "kiwi","grape","orange"]

#
# # => [5,6,4,5,6]
#
# g = [len(x) for x in fruits if 'i' in x]
# print(g)



# 매핑 컴프리헨션
# 홀수는 10 짝수는 20 더하기
# h = [x + 10 if x % 2 == 1 else x + 20 for x in range(101)]
# print(h)

fruits = ["apple", "banana", "kiwi","grape","orange"]
#5글자 미만이면 글자의 길이로 나타내고, 아니면 대문자화 하기

i = [len(x) if len(x) <= 5 else x.upper()  for x in fruits]
print(i)


