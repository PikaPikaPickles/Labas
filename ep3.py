import numpy as np
import matplotlib.pyplot as plt

FileName = 'Daar.dat'
Data = np.array(list(map(float, np.genfromtxt(FileName, delimiter='\t', dtype=str))))
DataOfData = np.array([[50]])
A = np.eye(Data.size)
# print(A)
for k in range(50):
    for l in range(50):
        if k == l + 1:
            A[k][l] = -1

DataOfData = np.zeros((15, 50))
for i in range(15):
    Data = Data - 0.5 * np.dot(Data, A)
    DataOfData[i] = Data
plt.plot(DataOfData)
plt.show()
