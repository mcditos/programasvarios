import numpy as np
B=np.loadtxt("/run/media/cbarrios/NuevoVol/Gerardo/Gerardo/astgmtdem/angulos_radio_12.z")
for i in range (0,len(B)):
	if B[i]<=15 :
		B[i]=1
	elif B[i]<=30 :
		B[i]=2
	elif B[i]<=45 :
		B[i]=3
	elif B[i]<=60 :
		B[i]=4
	elif B[i]<=75 :
		B[i]=5
	else :
		B[i]=6
np.savetxt("/run/media/cbarrios/NuevoVol/Gerardo/Gerardo/astgmtdem/angulos_radio_12_discreto.z",B,fmt="%i")
