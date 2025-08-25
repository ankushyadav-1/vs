import matplotlib.pyplot as plt
import numpy as np  

x = np.array(['Angry Bird','Teen Titan','Marvel Comics','ColorMe','Fun Run','Crazy Taxi','Igram Pro','WApp Pro','Maths Formulas'])  
y = np.array([197000,209000,414000,196000,272000,311000,213000,455000,278000])

plt.bar(x,y)
plt.xlabel('App Name')
plt.ylabel('Total Downloads')
plt.title('App Downloads')
plt.legend()
plt.show()