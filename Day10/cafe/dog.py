# 변수들[명사] + 함수들[동사] = 클래스
class Dog:
    def __init__(self, a,b,c):
        self.name = a
        self.breed = b
        self.happiness = 0

        def intro(self):
            print(f"{self.name},{self.breed}, {self.happiness}")

        def eating(self):


a = Dog("제니", "푸들")
a.intro()
b = Dog("맥스", "달마시안")
b.intro()
c = Dog("보리", "비숑")
c.intro()


