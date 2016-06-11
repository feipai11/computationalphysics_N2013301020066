import numpy as np
from pylab import *

data_x=np.zeros((500,100))
data_x2a=np.zeros((500,100))
rand=np.random.random((500,100))
for j in range(data_x.shape[0]):
    for i in range(1,data_x.shape[1]):
        if rand[j][i]<0.25:
            data_x[j][i]=data_x[j][i-1]-1
            data_x2a[j][i]=data_x[j][i]**2
        elif rand[j][i]>=0.25:
            data_x[j][i]=data_x[j][i-1]+1
            data_x2a[j][i]=data_x[j][i]**2
x=np.linspace(0,99,100)
fig=figure(figsize=[11,5])
ax=fig.add_subplot(1,2,1)
scatter(np.linspace(0,99,100),data_x[1,:],c='red', s=15, label='red',alpha=0.7, edgecolors='none')
scatter(np.linspace(0,99,100),data_x[35,:],c='green', s=15, label='green',alpha=0.8, edgecolors='none')
scatter(np.linspace(0,99,100),data_x[65,:],c='blue', s=15, label='blue',alpha=0.9, edgecolors='none')
plot(x,0.58*x,'k:')
#legend(loc='best',frameon=False)
xlabel('step number')
ylabel('x')
ylim([0,60])
xlim([0,100])
title('Random work in dimension')
ax=fig.add_subplot(1,2,2)
z=np.zeros(100)
for j in range(500):
    z=z+data_x2a[j,:]
y=z/500
scatter(np.linspace(0,99,100),y,c='green',s=3,alpha=0.8,label='exprimental')
plot(x,0.267*x**2,'k',label=r'$y=0.27x^2$')
xlim([0,100])
ylim([0,2800])
legend(loc='best',frameon=False)
xlabel('step number(time)')
ylabel(r'$<x>^2$')
title('Random work in dimension')
show()


