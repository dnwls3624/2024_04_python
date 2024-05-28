# 1.문자열 잘라서 정렬하기
# 문자열 myString이 주어집니다. "x"를 기준으로 해당 문자열을 잘라내 배열을 만든 후
# 사전순으로 배열을 return 하는 solution 함수를 완성해 주세요

def solution(myString):
    newMyString = myString.split("x")
    sortedNewMyString = sorted(newMyString)
    return sortedNewMyString

myString = "axbxcxxxdxexf"
print(solution(myString))



def solution(myString):
    filterdList = list(filter(lambda x: len(x) != "",myString.split("x")))
    filterdList.sort()
    return filterdList

print(solution(myString))


# 2. 배열 원소 삭제하기
# 정수 배열 arr과 delete_list가 있습니다. arr의 원소 중 delete_list의 원소를 모두 삭제하고
# 남은 원소들은 기존의 arr에 있던 순서를 유지한 배열을 return 하는 solution함수를 작성하세요

arr = [293,1000,395,678,94]
delete_list = [94,777,104,1000,1,12]

def solution(arr, delete_list):
    return [x for x in arr if x not in delete_list]
print(solution(arr, delete_list))


def solution(arr, delete_list):
    return list(filter(lambda x: x not in delete_list,arr))


# 3. 최댓값 만들기
# 정수 배열 numbers가 매개변수로 주어집니다. numbers의 원소 중 두개를 곱해 만들 수 있는
# 최댓값을 return하도록 solution함수를 완성해주세요.

numbers = [1,2,-3,4,-5]


def solution(numbers):
    numbers.sort()
    if numbers[0] * numbers[1] > numbers[-1] * numbers[-2]:
        return numbers[0] * numbers[1]
    else:numbers[-1] * numbers[-2]
print(solution(numbers))





