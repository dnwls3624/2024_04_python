# 1.핸드폰 번호 가리기
# 프로그래머스 모바일은 개인정보 보호를 위해 고지서를 보낼 때 고객들의 전화번호의 일부를 가립니다.
# 전화번호가 문자열 phone_number로 주어졌을 때, 전화번호의 뒷 4자리를 제외한 나머지 숫자를 전부 *으로 가린
# 문자열을 리턴하는 함수,solution을 완성해주세요



def solution(target):
    answer = ""
    for index, item in enumerate(list(target)):
        if len(target) - index <= 4:
            answer += item
        else:
            answer += "*"
    return answer

target = "01033334444"
print(solution(target))





# 2. 영어가 싫어요
# 영어가 싫은 강사님은 영어로 표기되어있는 숫자를 바꾸려 합니다.
# 문자열 numbers가 매개변수로 주어질때, numbers를 정수로 바꿔 return 하도록 solution 함수를 완성해주세요

numberStr = "onetwothreefour"
def solution1(numberStr):
    number_dict = {
        "zero": "0",
        "one": "1",
        "two": "2",
        "three": "3",
        "four": "4",
        "five": "5",
        "six": "6",
        "seven": "7",
        "eight": "8",
        "nine": "9",
    }
    for x in list(number_dict.keys()):
        if x in numberStr:
            numberStr = numberStr.replace(x, str(number_dict[x]))
    return numberStr
print(solution1(numberStr))