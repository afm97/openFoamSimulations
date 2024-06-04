import numpy as np
import matplotlib.pyplot as plt
import pandas as pd

data_y = np.loadtxt('data_y.csv', delimiter=',',
                    skiprows=1)  # X Y Z Vu Vv Vw k
data_x = np.loadtxt('data_x.csv', delimiter=',',
                    skiprows=1)  # X Y Z Vu Vv Vw k

vvx_artigo = pd.read_csv('vvX-artigo.csv', header=None, sep=';')
kx_artigo = pd.read_csv('kX-artigo.csv', header=None, sep=';')
vvx_artigo_real = pd.read_csv('vvX-artigo-real.csv', header=None, sep=';')
kx_artigo_real = pd.read_csv('kX-artigo-real.csv', header=None, sep=';')

vuy_artigo = pd.read_csv('vuY-artigo.csv', header=None, sep=';')
ky_artigo = pd.read_csv('kY-artigo.csv', header=None, sep=';')
vuy_artigo_real = pd.read_csv('vuY-artigo-real.csv', header=None, sep=';')
ky_artigo_real = pd.read_csv('kY-artigo-real.csv', header=None, sep=';')

'''
plt.figure(1)
plt.rcParams['xtick.labelsize'] = 16
plt.rcParams['ytick.labelsize'] = 16

plt.plot(data_y[:, 3]/1.45, data_y[:, 1]/0.2,
         color='black', linewidth=2, label='OpenFoam')

plt.plot(np.array(vuy_artigo[0]), np.array(vuy_artigo[1]),
         color='red', linewidth=2, label='Allegrini')

plt.plot(np.array(vuy_artigo_real[0]), np.array(vuy_artigo_real[1]),
         color='blue', linewidth=2, label='Allegrini')

plt.legend(fontsize=20)
plt.grid()
plt.xlabel("$u/U_{fs}$", fontsize=20)
plt.ylabel("$y/H$", fontsize=20)
plt.title('standard $k-e$')

####################################################

plt.figure(2)
plt.rcParams['xtick.labelsize'] = 16
plt.rcParams['ytick.labelsize'] = 16

plt.plot(data_y[:, 6]/(1.45**2), data_y[:, 1]/0.2,
         color='black', linewidth=2, label='OpenFoam')

plt.plot(np.array(ky_artigo[0]), np.array(ky_artigo[1]),
         color='red', linewidth=2, label='Allegrini')

plt.plot(np.array(ky_artigo_real[0]), np.array(ky_artigo_real[1]),
         color='blue', linewidth=2, label='Allegrini')

plt.legend(fontsize=20)
plt.grid()
plt.xlabel("$k/U^2_{fs}$", fontsize=20)
plt.ylabel("$y/H$", fontsize=20)
plt.title('standard $k-e$')

####################################################
'''
plt.figure(3)
plt.rcParams['xtick.labelsize'] = 16
plt.rcParams['ytick.labelsize'] = 16

plt.plot((data_x[:, 0]-7.4)/0.2, data_x[:, 4]/1.45,
         color='black', linewidth=2, label='OpenFoam')

plt.plot(np.array(vvx_artigo[0]), np.array(vvx_artigo[1]),
         color='red', linewidth=2, label='Allegrini: SWF')

plt.plot(np.array(vvx_artigo_real[0]), np.array(vvx_artigo_real[1]),
         color='blue', linewidth=2, label='Allegrini: Measurement')

plt.legend(fontsize=20)
plt.grid()
plt.xlabel("$x/H$", fontsize=20)
plt.ylabel("$v/U_{fs}$", fontsize=20)
plt.title('standard $k-e$')

####################################################

plt.figure(4)
plt.rcParams['xtick.labelsize'] = 16
plt.rcParams['ytick.labelsize'] = 16

plt.plot((data_x[:, 0]-7.4)/0.2, data_x[:, 6]/(1.45**2),
         color='black', linewidth=2, label='OpenFoam')

plt.plot(np.array(kx_artigo[0]), np.array(kx_artigo[1]),
         color='red', linewidth=2, label='Allegrini: SWF')

plt.plot(np.array(kx_artigo_real[0]), np.array(kx_artigo_real[1]),
         color='blue', linewidth=2, label='Allegrini: Measurement')

plt.legend(fontsize=20)
plt.grid()
plt.xlabel("$x/H$", fontsize=20)
plt.ylabel("$v/U^2_{fs}$", fontsize=20)
plt.title('standard $k-e$')

plt.show()
