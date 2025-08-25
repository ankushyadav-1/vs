
#: Write a python program to generate line graph with suitable title and labels. Where x is the year of performance with values 2014,2015,2016,2017,2018 and 2019. And y axis shows  the profit of a particular company in Rs.(Millions).

import matplotlib.pyplot as plt

x = [2014,2015,2016,2017,2018,2019]
y = [10.5,19,31,45,52,69]

plt.plot(x,y)
plt.xlabel('Year')
plt.ylabel('Profit in Rs.(Millions)')
plt.title('Profit of a company')
plt.legend(['Profit'])
plt.show()
#: Write a python program to generate line graph with suitable title and labels. Where x is the year of performance with values 2014,2015,2016,2017,2018 and 2019. And y axis shows  the profit of a particular company in Rs.(Millions).

import matplotlib.pyplot as plt
import numpy as np

x = np.array([2014,2015,2016,2017,2018,2019])
y = np.array([1.5,1.69,1.71,1.82,1.99,2.10])

plt.plot(x,y)
plt.xlabel('Year')
plt.ylabel('Profit')
plt.title('Line Graph')
plt.legend(['Profit'])
plt.show()


