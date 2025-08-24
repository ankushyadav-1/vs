<<<<<<< HEAD
#: Write a python program to generate line graph with suitable title and labels. Where x is the year of performance with values 2014,2015,2016,2017,2018 and 2019. And y axis shows  the profit of a particular company in Rs.(Millions).

import matplotlib.pyplot as plt

x = [2014,2015,2016,2017,2018,2019]
y = [10,20,30,40,50,60]

plt.plot(x,y)
plt.xlabel('Year')
plt.ylabel('Profit in Rs.(Millions)')
plt.title('Profit of a company')
plt.legend()
plt.show()
=======
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

>>>>>>> 3c9c742133ba84fee9a4b2bed9f365c392f7b214
