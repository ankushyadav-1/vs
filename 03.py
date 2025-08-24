#Consider the data given below. Create a bar chart depicting the downloads of  the app.  
  
#App Name	App Price in Rs.	Total Downloads
#Angry Bird	75	197000
#Teen Titan	120	209000
#Marvel Comics	190	414000
#ColorMe	245	196000
#Fun Run	550	272000
#Crazy Taxi	55	311000
#Igram Pro	175	213000
#WApp Pro	75	455000
#Maths Formulas	140	278000


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
