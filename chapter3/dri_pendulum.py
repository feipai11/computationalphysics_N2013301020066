import matplotlib.pyplot as plt
import numpy as np
import math

g=9.8
l=9.8
wd=0.5
q=0.5

class Simple_pendulum:
    def __init__(self,_theta0=0.2,_w=0,_t0=0,_dt=math.pi/1000,_tfinal=500):
        self.theta=[]
        self.theta.append(_theta0)
        self.t=[]
        self.t.append(_t0)
        self.w=[]
        self.w.append(_w)
        self.dt=_dt
        self.tfinal=_tfinal
        #print self.theta[-1],self.t[-1],self.w[-1]
        return
    def calculate(self):
        global g,l
        while (self.t[-1]<self.tfinal):
            self.w.append(self.w[-1]-g/l*self.theta[-1]*self.dt)
            self.theta.append(self.theta[-1]+self.w[-1]*self.dt)
            self.t.append(self.t[-1]+self.dt)
        return
    def plot_2d(self,fd):
        #plt.plot(self.t,self.theta,label=r'$F_D=%.1f$'%fd)
        
        global x,dri_t,dotx
        x=self.theta
        dri_t=self.t
        dotx=self.w
        return
class Dri_pendulum(Simple_pendulum):
    def calculate(self,fd):
        global g,l,wd,q
        while (self.t[-1]<self.tfinal):
            self.w.append(self.w[-1]-(g/l*math.sin(self.theta[-1])+q*self.w[-1]-fd*math.sin(wd*self.t[-1]))*self.dt)
            if self.theta[-1]+self.w[-1]*self.dt>math.pi:
                self.theta.append(self.theta[-1]+self.w[-1]*self.dt-2*math.pi)
            elif self.theta[-1]+self.w[-1]*self.dt<-math.pi:
                self.theta.append(self.theta[-1]+self.w[-1]*self.dt+2*math.pi)
            else: 
                self.theta.append(self.theta[-1]+self.w[-1]*self.dt)
            self.t.append(self.t[-1]+self.dt)
        return
class Dri_pendulum_add(Simple_pendulum):
    def calculate(self,fd):
        global g,l,wd,q
        while (self.t[-1]<self.tfinal):
            self.w.append(self.w[-1]-(g/l*math.sin(self.theta[-1])+q*self.w[-1]-fd*math.sin(wd*self.t[-1]))*self.dt)
            self.theta.append(self.theta[-1]+self.w[-1]*self.dt)
            self.t.append(self.t[-1]+self.dt)
'''
fig=plt.figure(figsize=(12,9))
a=Dri_pendulum()
a.calculate(0.5)
a.plot_2d(0.5)
theta1=np.array(x)
w1=np.array(dotx)
d_x=[]
d_dotx=[]
for i in range(12000,len(dri_t)):
    if i % 4000==0:
        d_x.append(theta1[i])
        d_dotx.append(w1[i])
        #print d_x[-1]
dtheta1=np.array(d_x)
dw1=np.array(d_dotx)
plt.subplot(2,2,1)
plt.plot(theta1,w1)
plt.text(-0.38,-0.03,r'phrase $F_D=0.5$',fontsize=10)
#plt.txt
plt.subplot(2,2,2)
plt.scatter(dtheta1,dw1,s=1.5,alpha=0.8)
plt.text(-0.233133,0.3305,r'Poincare $F_D=0.5$',fontsize=10)

#a=Dri_pendulum(0.201,_tfinal=50)
#a.calculate(0.5)
#a.plot_2d(0.5)
#theta2=np.array(x)
#delta_theta=abs(theta2-theta1)
#plt.semilogy(dri_t,delta_theta)
#plt.xlabel('time(s)')
#plt.ylabel(r'$\Delta \theta/rad$',fontsize=16)
#plt.text(38.5,0.0001,r'$F_D=0.5$',fontsize=14)
'''
a=Dri_pendulum(_tfinal=20000)
a.calculate(1.2)
a.plot_2d(1.2)
theta1=np.array(x)
w1=np.array(dotx)
d_x1=[]
d_dotx1=[]
d_x2=[]
d_dotx2=[]
d_x3=[]
d_dotx3=[]
d_x4=[]
d_dotx4=[]
for i in range(12000,len(dri_t)):
    if i % 4000==0:
        d_x1.append(theta1[i])
        d_dotx1.append(w1[i])
for i in range(12000,len(dri_t)):
    if i % 4000==1000:
        d_x2.append(theta1[i])
        d_dotx2.append(w1[i])
for i in range(12000,len(dri_t)):
    if i % 4000==2000:
        d_x3.append(theta1[i])
        d_dotx3.append(w1[i])
for i in range(12000,len(dri_t)):
    if i % 4000==3000:
        d_x4.append(theta1[i])
        d_dotx4.append(w1[i])
fig=plt.figure(figsize=(12,10))
ax1=fig.add_subplot(221)
ax1.set_xlabel(r'$\theta$(rad)')
ax1.set_ylabel(r'$\omega$(rad/s)')
plt.scatter(d_x1,d_dotx1,s=1.5,alpha=0.6)
plt.text(-0.236515,-0.0219136,r'Poincare section of $\Delta \theta=0$',fontsize=10)
ax2=fig.add_subplot(222)
ax2.set_xlabel(r'$\theta$(rad)')
ax2.set_ylabel(r'$\omega$(rad/s)')
plt.scatter(d_x2,d_dotx2,s=1.5,alpha=0.6)
plt.text(-3.28114,0.167593,r'Poincare section of $\Delta\theta=\frac{\pi}{4}$',fontsize=10)
ax1=fig.add_subplot(223)
ax1.set_xlabel(r'$\theta$(rad)')
ax1.set_ylabel(r'$\omega$(rad/s)')
plt.scatter(d_x3,d_dotx3,s=1.5,alpha=0.6)
plt.text(-2.3436,0.105093,r'Poincare section of $\Delta\theta=\frac{\pi}{2}$',fontsize=10)
ax1=fig.add_subplot(224)
ax1.set_xlabel(r'$\theta$(rad)')
ax1.set_ylabel(r'$\omega$(rad/s)')
plt.scatter(d_x4,d_dotx4,s=1.5,alpha=0.6)
plt.text(0.20725,-0.238889,r'Poincare section of $\Delta\theta=\frac{3\pi}{4}$',fontsize=10)

'''
a=Dri_pendulum(_tfinal=500)
a.calculate(1.2)
a.plot_2d(1.2)
theta1=np.array(x)
w1=np.array(dotx)
plt.subplot(2,2,3)
plt.plot(theta1,w1)
plt.text(1.85,2.28,r'phrase $F_D=1.2$',fontsize=10)
plt.subplot(2,2,4)
plt.scatter(dtheta1,dw1,s=1.5,alpha=0.8)
plt.text(1.4,0.37,r'Poincare $F_D=0.5$',fontsize=10)
'''

plt.show()

