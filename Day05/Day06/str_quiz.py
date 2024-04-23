#1. 뉴스 기사를 스크랩
# 유저가 입력한 단어를 모두 대문자화
# 다시 보여주기

#2. 영어기사 스크랩
# 단어 사이에 🍅 넣고 출력하기

news = "Prosecutors and Trump’s attorneys delivered opening statements and the first witness – a former National Enquirer publisher – was called Monday in the historic and unprecedented criminal trial of a former president."

word = input("단어 입력: ")
newNews = news.replace(word,word.upper())
print(newNews)

newNews = news.replace(" ", "🍅")
print(newNews)

#or

words = news.split(" ")
news1 = "🍅".join(words)
print(news1)