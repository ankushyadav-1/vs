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