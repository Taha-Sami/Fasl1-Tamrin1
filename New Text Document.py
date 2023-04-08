import numpy as np
import matplotlib.pyplot as plt
from math import pi, exp
from openpyxl import Workbook
x=np.arange(-5,10,0.2)
y=np.exp(x)
dy=y[1:]-y[:-1]
dx=x[1:]-x[:-1]
ydot=dy/dx

ydot=y.copy()
ydot[1:]=dy/dx
ydot[0]=ydot[1]

ddy=dy[1:]-dy[:-1]
yddot=ddy/(dx[:-1])

plt.plot(x,y,label='orginal')
plt.plot(x,ydot, label='mosh 1')
plt.plot(x[:-2],yddot, label='mosh 2')
plt.xlabel("x")
plt.legend()
plt.show()

yddot=dy.copy()
yddot[1:]=ddy/dx
yddot[0]=yddot[1]

wb_save=Workbook()
ws_save=wb_save.active
i=0
for x_i in x:
	ws_save[f"A{i+1}"]=x_i
	ws_save[f"B{i+1}"]=ydot[i]
	ws_save[f"c{i+1}"]=yddot[i]
	i+=1
wb_save.save("Tamrin1.xlsx")