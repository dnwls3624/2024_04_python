import matplotlib.pyplot as plt
import pandas

# x : age
# y : salaly

x = [1,2,3,4,5]
y = [10,20,25,30,35]
#
plt.plot(x,y)
# plt.show()

df = pandas.read_csv('company.csv',encoding='cp949')
# job_satisfaction = df['job_satisfaction'].value_counts()

# job_satisfaction.plot.pie()
# plt.show()

x = df['age']
y = df['salary']

plt.hist2d(x,y)
plt.show()

