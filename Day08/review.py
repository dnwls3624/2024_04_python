#quiz1
# 양의 정수 n을 매개변수로 받아들여, n의 홀짝성에 따라 다른 계산을 수행하는 프로그램을 작성
# 만약 n이 홀수면, n이하의 모든 홀수의 합을 반환
# 만약 n이 짝수면, n이하의 모든 짝수의 합을 반환

# num = int(input("정수 입력: "))

# result = 0

# if num % 2 == 1:
#     for x in range(num+1):
#         if x % 2 == 1:
#             result += x
# else:
#     for x in range(num + 1):
#         if x % 2 == 0:
#             result +=  x ** 2
# print(result)

#quiz2
# 정수 배열 arr 와 자연수 k가 주어집니다. 이때 k의 홀짝성에 따라 배열에
# 다른 연산을 적용합니다. 만약 k가 홀수라면 배열 arr의 모든 원소에 k를 곱하고
# k가 짝수면 모든 원소에 k를 더합니다.
#

k = int(input("정수 입력: "))
arr = [1,2,3]

newList = []

if k % 2 == 1:
    for x in arr:
        newList.append(x * k)
else:
    for x in arr:
        newList.append(x + k)
print(newList)



        
        


