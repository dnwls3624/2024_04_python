#quiz1
# 사용자로부터 전체 이메일 주소를 입력받는다
# 예를들어 dnwls3624@naver.com 같은 형식
# 프로그램은 입력받은 이메일 주소에서 사용자 이름 부분과 도메인 부분을 분리하여 출력
# 사용자 이름과 도메인이 어떻게 구분되는지 확인


# def splitEmail(email):
#     arr = email.split("@")
#     return {"user": arr[0], "domain": arr[1]}
#
# # quiz2
# 문자열을 입력받는다
# 입력된 문자열은 두 가지 마법적 변환을 거치게된다
# 하나는 문자열을 뒤집어 순서를 바꾼다
# 다른 하나는 문자열의 문자들을 알파벳 순서로 정렬한다
# 예를들어'mega'를 뒤집힌 'agem'과 알파벳 순으로 정렬된 'aemg'가 결과로 나온다

# def spellingMagic(word):
#     spellingList = list(word) # [m,e,g,a]
#     spellingList.sort() #정렬화 [a,e,g,m]
#     result = "".join(spellingList) # list -> str
#
#     spellingList1 = list(word)
#     spellingList1.reverse()
#     result1 = "".join(spellingList1)
#     return {"sorted":result, "reversed":result1}
#
# print(spellingMagic("koreait"))

#quiz3
# 정수 n이 주어졌을 때, 홀수면 "odd" Wkrtnaus "even"을 돌려주는 함수만들기

def oddEven(n):
    if n % 2 == 1:
        return "odd"
    else:
        return "even"

