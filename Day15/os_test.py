# import os

# print(os.getlogin())
# desktop_path = os.path.join(os.path.join(os.environ['USERPROFILE']), 'Desktop')
# forder_name = "오늘은 목요일"
# forder_path = os.path.join(desktop_path,forder_name)
# os.mkdir(forder_path)


import os
import datetime
from  review import yearToZodiac
# 바탕화면 경로 따기
desktop_path = os.path.join(os.path.join(os.environ['USERPROFILE']), 'Desktop')
# 바탕화면경로와 폴더이름 합치기
forder_path = os.path.join(desktop_path,'과장님부당업무지시폴더')
# 폴더 만들기
os.mkdir(forder_path)
# 오늘 날짜 가져오기
start_date = datetime.date.today()

#폴더:용띠의해_5월_23일_목요일



for x in range(365):
    date_folder = start_date + datetime.timedelta(days=x)
    year_zodiac = yearToZodiac(int(date_folder,strftime("%Y")))
    forder_name = f"{year_zodiac}띠의해_{date_folder.strftime({"%m_%d_%A"})}"
    path = os.path.join(forder_path, forder_name)
    os.mkdir(path)

