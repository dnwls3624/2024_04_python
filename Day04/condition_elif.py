# num = int(input('점수 입력: '))
# if num >= 90:
#     print("A등급")
# elif num >= 80:
#     print("B등급")
# elif num >= 70:
#     print("C등급")
# else:
#     print("과락입니다.")


# 국,영,수 점수를 3개 입력받고,
# 평균이 90점 이상 'A', 80이상 'B' 70이상 'C', 60이상 'D'
# 나머지는 F로 나타내는 프로그램 작성하기

# kor = int(input('국어 점수 입력: '))
# eng = int(input('영어 점수 입력: '))
# math = int(input('수학 점수 입력: '))
# avg = (kor + eng + math) / 3
# if avg >= 90:
#     print("A등급 입니다.")
# elif avg >= 80:
#     print("B등급입니다.")
# elif avg >= 70:
#     print("C등급 입니다.")
# elif avg >= 60:
#     print("D등급 입니다.")
# else:
#     print("F등급 입니다.")

# nested condition
score = int(input("점수 입력: "))
if score > 60:
    if score == 100:
        print("만점 입니다.")
    else:
        print("합격 입니다.")
else:
    if score == 0:
        print("이건 좀...")
    else:
        print("불합격 입니다.")


