import matplotlib.pyplot as plt
import pandas

df = pandas.read_csv('japan.csv')

# print(df['Country/Area'].value_counts())
# 2023에 각 나라별로 방문자수를 알고 싶음


year_2023 = df[(df['Year'] == 2023) & (df['Purpose_of_visit_to_Japan'] == 'Tourism')]
data = year_2023.groupby('Country/Area')['Visitor Arrivals'].sum()
print(data)


