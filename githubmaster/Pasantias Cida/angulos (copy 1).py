import numpy as np
A=np.loadtxt("/run/media/cbarrios/NuevoVol/Gerardo/Gerardo/astgmtdem/teta-topografia-tuy-NR12.z")
for i in range(0,len(A)):
	if 90 < A[i]<= 180 :
		A[i]=180-A[i]

	elif 180 <A[i]<= 270 :
		A[i]=A[i]-180

	elif 270 < A[i]<= 360 :
		A[i]=360-A[i]
np.savetxt("/run/media/cbarrios/NuevoVol/Gerardo/Gerardo/astgmtdem/angulos_radio_12.z",A,delimiter="	",fmt="%f")

