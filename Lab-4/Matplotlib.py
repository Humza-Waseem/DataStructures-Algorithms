import matplotlib.pyplot as plt
import pandas as pd
import numpy as np


x = [1,2,3,4,5]
y = [2,4,6,7,8]

# to plot the graph 
plt.plot(x,y,label='redLine',color="red")

plt.title("Its my graph"  , fontdict = {'fontname': 'Times New Roman', 'fontsize':20})
plt.xlabel('x axis')
plt.ylabel('y axis')

plt.xticks([1,2,3,4,5])
plt.yticks([2,4,6,7,8])

plt.legend()
plt.show()
