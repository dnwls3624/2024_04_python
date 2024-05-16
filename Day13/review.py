# quiz1
# 1.문자열 뒤집기
# 문자열 my_string이 매개변수로 주어진다 my_string을 거꾸로 뒤집은 문자열을 return하도록 함수를 완성해주세요

#
# def reversedWord(my_string):
#     wordList = list(my_string)
#     wordList.reverse()
#     reversedWord ="".join(wordList)
#     return reversedWord
#
# print(reversedWord("korea"))
#
# #quiz2
# a = ["problemsolving", "practiceguitar","swim","studygraph"]
# b = [True,False,True,False]
#
# num = 0
# doneList = []
# for x in a:
#     if b[num] == True:
#         doneList.append(x)
#     num += 1
#
# todolist = ["problemsolving", "practiceguitar", "swim", "studygraph"]
# doneList = [True, False, True, False]
#
# def filterDoneList(todolist,doneList):
#     return [item for index, item in enumerate(todolist) if doneList[index] == True]




class Animal:
    def __init__(self, name, bread):
        self.name = name
        self.bread = bread

        def eat(self):
            print("냠냠냠")

        def sound(self):
            pass

        def intro(self):
            print(f"이름:{self.name},종:{self.breed}, 소리:{self.sound()}")


class Dog(Animal):

    def sound(self):
        print("멍멍")

class Cat(Animal):

    def sound(self):
        print("야옹")






#퀴즈
관리자, 편집자, 뷰어 라는 각각 사용자가 존재
모두 접근하기라는 함수를 가지고 있다
모두 userName이라는 속성도 가지고 있다

manager,editor,viewer

관리자- 유저만들기
편집자- 편집하기
뷰어- 조회하기

class user:

    def __init__(self, userName):
        self.userName = userName

    def access(self):
        pass

class Admin(user):
    def access(self):
        print("관리자가 접근합니다.")

    def createUser(self):
        print("유저를 만
    def edit(self):
        print("편집을 합니다.")

class Viewer(user):
    def access(self):
        print("뷰어가 접근합니다.")

    def view(self):
        print("조회를 합니다.")

class Editor(user):
    def access(self):
        print("편집자가 접근합니다.")



