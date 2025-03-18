'''
pip install numpy pandas matplotlib PyQt5
'''
   
import numpy as np
import matplotlib.pyplot as plt
import extractData

logSolver = 'log.simpleFoam'
outputData = 'output'

try:
    print(f"Buscando dados no arquivo {outputData}...")
    data = np.loadtxt(outputData,dtype=float,delimiter=',',skiprows=1)
    print("Dados encontrados e carregados com sucesso!")
except FileNotFoundError:
    print(f"Dados não encontrados. Criando arquivo {outputData}...")
    extractData.processLog(logSolver,outputData)
    print("Dados criados e carregados com sucesso!")

#---------------------Plots--------------------#


plt.figure(figsize=(9,7), dpi=100)
plt.yscale('log')
plt.xlabel('Time')
plt.ylabel('Residuals')

plt.plot(data[:,0],data[:,1],color='purple',label=r"$U_x$")
plt.plot(data[:,0],data[:,2],color='black',label=r"$U_y$")
plt.plot(data[:,0],data[:,3],color='blue',label=r"$\epsilon$")
plt.plot(data[:,0],data[:,4],color='red',label=r"$\kappa$")
plt.plot(data[:,0],data[:,5],color='green',label=r"$p$")

plt.legend()
plt.grid()

plt.show()
