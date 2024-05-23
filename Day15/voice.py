from gtts import gTTS

text = "안녕 나영아 하하하"
a = gTTS(text, lang='ko')
a.save('result.mp3')

