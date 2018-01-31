
import pickle as pl
import matplotlib.pyplot as plt 
print("intoduzca el nombre del archivo a graficar")
nombre=raw_input()
# Load figure from disk and display
fig_handle = pl.load(open(nombre,'rb'))
plt.show()
