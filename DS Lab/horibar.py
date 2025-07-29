import numpy as np
import matplotlib.pyplot as plt
x=np.array(['Java','Python','PHP','Javascript','C#','C++'])
y=np.array([22.2,17.6,8.8,8,7.7,6.7])
colors=['red','yellow','green','blue','pink','grey']
plt.barh(x,y,color=colors)
plt.title('Bar Chart')
plt.ylabel('Programming Language')
plt.xlabel('Popularity')
plt.show()
