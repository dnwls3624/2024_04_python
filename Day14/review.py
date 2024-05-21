# 1. 제일 작은 수 제거하기
# 정수를 저장한 배열, arr 에서 가장 작은 수를 제거한 배열을 리턴하는 함수, solution을 완성하세요
# 단, 리턴하려는 배열이 빈 배열인 경우엔 배열에 -1을 채워 리턴하세요
# 예를들어 arr이 [4,3,2,1]인 경우는 [4,3,2]를 리턴 하고,[10]면 [-1]을 리턴 합니다.


a = [1,3,2,5,10]
a. remove((min(a)))
# del a[0]
print(a)

List = [4,3,2,1]
def solution(arr):
    if len(arr) == 1:
        return [-1]
    else:
        arr.remove(min(a))
        return arr


# 2.문자열 섞기
# 두 문자열의 각 문자가 앞에서부터 서로 번갈아가면서 한 번씩 등장하는 문자열을 만들어 return 하는
# solution 함수를 완성해 주세요

def solution1(str1,str2):
    text = ""
    for x in range(len(str1)):
        text += str1[x]
        text += str2[x]
    return text

print(solution1("aaaa","cccc"))

# 3. x 사이의 개수
# 문자열 mysiring이 주어집니다. mysiring을 문자"x"를 기준으로 나눴을 때 나눠진 문자열 각각의 길이를
# 순서대로 저장한 배열을 return하는 solution함수를 완성해 주세요


def solution(str):
    return list(map(lambda x: len(x), filter(lambda x: len(x) > 0, str.split("x"))))

# 4. 5명씩
def solution4(arr):
    return [item for index,item in enumerate(arr) if index % 5 == 0]




class Animal:
    def __init__(self, name):
        self.name = name

    def speak(self):
        return "소리 내는중"

class Dog(Animal):
    def __init__(self, name, bread):
        super().__init__(name)
        self.bread = bread

    def speak(self):
        return f"{super().speak()}...멍멍"

    a = Dog("흰둥이", "하얀개")
    print(a.speak())

