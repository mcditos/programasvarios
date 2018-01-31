import os
import matplotlib.pyplot as plt
import numpy as np
path="/run/media/cbarrios/NuevoVol/.dat"
A=np.array([])
for file in os.listdir(path):
  if file.startswith("Ariel"):
    A=np.append(A,file)
fig=plt.figure(1)
for k in range (0,len(A)):
	Data=np.loadtxt("/run/media/cbarrios/NuevoVol/.dat/"+A[k])     
	Data=Data.transpose()
	fig
	plt.plot(Data[2,:],Data[3,:])
	

fig.savefig("maria.png")
print(Data[:,0])
print(Data.shape)
