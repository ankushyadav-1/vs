<<<<<<< HEAD
#: Given the following data of rainfall in different zones of India in mm for 12 months, Create multiple lines chart in a Figure to observe any trends from Jan to Dec.
#Zones	Jan	Feb	Mar	Apr	May	Jun	Jul	Aug	Sep	Oct	Nov	Dec
#North	14	13	13	19	16	20	15	17	19	17	15	12
#South	16	20	13	20	20	17	11	16	13	14	17	20

import matplotlib.pyplot as plt
import numpy as np  

x = np.array(['Jan','Feb','Mar','Apr','May','Jun','Jul','Aug','Sep','Oct','Nov','Dec'])  
y1 = np.array([14,13,13,19,16,20,15,17,19,17,15,12])
y2 = np.array([16,20,13,20,20,17,11,16,13,14,17,20])

plt.plot(x,y1)
plt.plot(x,y2)
plt.xlabel('Months')
plt.ylabel('Rainfall in mm')
plt.title('Rainfall in different zones of India')
plt.legend(['North','South'])
plt.show()
=======
#: Given the following data of rainfall in different zones of India in mm for 12 months, Create multiple lines chart in a Figure to observe any trends from Jan to Dec.
#Zones	Jan	Feb	Mar	Apr	May	Jun	Jul	Aug	Sep	Oct	Nov	Dec
#North	14	13	13	19	16	20	15	17	19	17	15	12
#South	16	20	13	20	20	17	11	16	13	14	17	20

import matplotlib.pyplot as plt
import numpy as np  

x = np.array([1,2,3,4,5,6,7,8,9,10,11,12])
y1 = np.array([14,13,13,19,16,20,15,17,19,17,15,12])
y2 = np.array([16,20,13,20,20,17,11,16,13,14,17,20])

plt.plot(x,y1)
plt.plot(x,y2)
plt.xlabel('Months')
plt.ylabel('Rainfall')  
plt.title('Rainfall in different zones of India')
plt.legend(['North','South'])
plt.show()

>>>>>>> 3c9c742133ba84fee9a4b2bed9f365c392f7b214
