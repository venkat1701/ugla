import numpy as np
linList = np.linspace(4, 100, 15)
newlist=[]
for x in linList:
    newlist.append(np.int64(np.round(x)))
print(newlist)