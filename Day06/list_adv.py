fruits = ["apple", "banana", "kiwi", "mango"]
numbers = [1, 2, 3, 4, 5]
mix = ["안녕", 1, "집에갈래", 2, True, []]
starbucks = [["아메리카노","라떼"],["쥬스", "에이드"],["빵", "케이크"]]
print(starbucks[0][1]) # 라뗴
print(starbucks[2][0]) # 빵

# #kiwi == fruit[2]
# # print(fruits[1].upper())


##append[추가하다]
fruits.append("grape")
print(fruits)
# extend[확장하다]
fruits.extend(["strawberry", "orange"])
print(fruits)

# sort[정렬하다]
fruits.sort()
print(fruits)

# reverse[반대로 하다]
fruits.reverse()
print(fruits)

# pop[맨뒤에 있는거 빼기]
fruits.pop()
print(fruits)

# remove[제거하다]
fruits.remove()
print(fruits)

#count
fruits.append("banana")
x = fruits.count("banana")
print(x)

# for 리스트는 요소를 하나씩 빼준다
for x in fruits:
    print(x)
