import numpy as np
import matplotlib.pyplot as plt

FileName = 'signal01.dat'
Data = np.array(list(map(float, np.genfromtxt(FileName, delimiter='\t', dtype=str))))
DataNew = np.arange(Data.size)
p = 11
print(Data[(p - 10):p].sum())
for i in range(Data.size):
    if i > 11:

        DataNew[i] = (Data[i - 10:i].sum()) / Data[i - 10:i].size

    else:
        DataNew[i] = (Data[0:i].sum()) / (Data[0:i].size + 1)
print(DataNew)
plt.plot(DataNew)
plt.show()
