import numpy as np
B=np.loadtxt("/run/media/cbarrios/NuevoVol/Gerardo/Gerardo/astgmtdem/Pente-topografia-tuy-NR22.z")
for i in range (0,len(B)):
	if B[i]==0:
		B[i]=0
	elif B[i]>0 :
		B[i]=1
	elif B[i]<0 :
		print(B[i])
np.savetxt("/run/media/cbarrios/NuevoVol/Gerardo/Gerardo/astgmtdem/Pente_discreto_radio22.z",B,fmt="%i")
