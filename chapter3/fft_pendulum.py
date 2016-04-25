import matplotlib.pyplot as plt
import numpy as np
import math

g=9.8
l=9.8
wd=2.0/3
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
        global dt
        dt=_dt
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
        plt.plot(self.t,self.theta,label=r'$F_D=%.3f$'%fd)
        return
    def fft_cal(self,_xmax,fd):
        x=np.array(self.theta)
        N=len(x)
        n=N/2.0-1
        f=1/(N*dt)*np.arange(n-1)
        y=np.fft.fft(x)
        y=y[0:n]
        y=np.array(abs(y))
        plt.plot(f,y,label='$F_D=%.3f$'%fd)
        plt.xlim(0.0,_xmax)

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

fig=plt.figure(figsize=(12,10)) 
ax1=fig.add_subplot(421)
ax1.set_ylabel(r'$\theta$(rad)')
a=Dri_pendulum(_dt=0.01,_tfinal=100)
a.calculate(1.35)
a.plot_2d(1.35)
plt.legend(loc='best',prop={'size':10},frameon=False)
ax2=fig.add_subplot(422)
ax2.set_ylabel('intensity')
a.fft_cal(3,1.35)
plt.legend(loc='best',prop={'size':10},frameon=False)

ax3=fig.add_subplot(423)
ax3.set_ylabel(r'$\theta$(rad)')
a=Dri_pendulum(_dt=0.01,_tfinal=100)
a.calculate(1.44)
a.plot_2d(1.44)
plt.legend(loc='best',prop={'size':10},frameon=False)
ax4=fig.add_subplot(424)
ax4.set_ylabel('intensity')
a.fft_cal(2,1.44)
plt.legend(loc='best',prop={'size':10},frameon=False)
plt.text(0.620,5000,r'The frequency $\frac{\Omega_D}{2}$ appears',fontsize=11)

ax5=fig.add_subplot(425)
ax5.set_ylabel(r'$\theta$(rad)')
a=Dri_pendulum(_dt=0.01,_tfinal=100)
a.calculate(1.465)
a.plot_2d(1.465)
plt.legend(loc='best',prop={'size':10},frameon=False)
ax6=fig.add_subplot(426)
ax6.set_ylabel('intensity')
a.fft_cal(1.5,1.465)
plt.legend(loc='best',prop={'size':10},frameon=False)

ax7=fig.add_subplot(427)
ax7.set_xlabel(r'$t(s)$')
ax7.set_ylabel(r'$\theta$(rad)')
a=Dri_pendulum(_dt=0.01,_tfinal=100)
a.calculate(1.501)
a.plot_2d(1.501)
plt.legend(loc='best',prop={'size':10},frameon=False)
ax8=fig.add_subplot(428)
ax8.set_xlabel(r'$frequency(Hz)$')
ax8.set_ylabel('intensity')
a.fft_cal(1.5,1.501)
plt.text(0.543,3200,r'The frequency $Chaos$ appears',fontsize=11)
plt.legend(loc='best',prop={'size':10},frameon=False)
plt.show()
