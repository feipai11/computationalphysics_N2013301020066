from matplotlib.pyplot import *
import numpy as np
import math as ma

g=9.8
l=1

class Simple_pendulum:
    def __init__(self,_theta0=0,_w=0,_t0=0,_dt=0.01):
        self.theta=[]
        self.theta.append(_theta0)
        self.t=[]
        self.t.append(_t0)
        self.w=[]
        self.w.append(_w)
        self.dt=_dt
        #print self.theta[-1],self.t[-1],self.w[-1]
        return
    def calculate(self):
        global g,l
        while (self.t[-1]<20):
            self.w.append(self.w[-1]-g/l*self.theta[-1]*self.dt)
            self.theta.append(self.theta[-1]+self.w[-1]*self.dt)
            self.t.append(self.t[-1]+self.dt)
        return
    def plot_2d(self):
        plot(self.t,self.theta,'b',label=r'liner $\theta_0=%.2f$'%self.theta[0])
        global x,dotx
        x=self.theta
        dotx=self.w
        return
class Simple_pendulum_euler(Simple_pendulum):
    def calculate(self):
        global g,l
        while (self.t[-1]<20):
            self.w.append(self.w[-1]-g/l*self.theta[-1]*self.dt)
            self.theta.append(self.theta[-1]+self.w[-2]*self.dt)
            self.t.append(self.t[-1]+self.dt)
        return
    def plot_2d(self):
        plot(self.t,self.theta,'g:',label=r'Euler $\theta_0=%.2f$'%self.theta[0])
class Nonliner_pendulum(Simple_pendulum):
    def calculate(self):
        global g,l
        while (self.t[-1]<20):
            self.w.append(self.w[-1]-g/l*ma.sin(self.theta[-1])*self.dt)
            self.theta.append(self.theta[-1]+self.w[-1]*self.dt)
            self.t.append(self.t[-1]+self.dt)
        return
    def plot_2d(self):
        plot(self.t,self.theta,'r',label=r'nonliner $\theta_0=%.2f$'%self.theta[0])
        global y,doty
        y=self.theta
        doty=self.w
a=Simple_pendulum(1)
a.calculate()
a.plot_2d()
a=Nonliner_pendulum(1)
a.calculate()
a.plot_2d()
xlabel('t/s')
ylabel(r'$\theta/rad$')
xlim(0.0,28.0)
title('Numerical solution of liner and nonliner pendulun')
legend(loc='best',prop={'size':11},frameon=False)
show()

plot(x,dotx,'r',label='Phrase diagram of liner pendulum')
plot(y,doty,'b',label='Phrase diagram of nonliner pendulum')
xlabel(r'$\theta/rad$')
ylabel(r'$\omega/rads^-1$')
#xlim(0.0,28.0)
title('Numerical solution of liner and nonliner pendulun')
legend(loc='best',prop={'size':11},frameon=False)
show()

plot(x,y,'b')
xlabel(r'liner$\theta/rad$')
ylabel(r'nonliner$\theta/rad$')
title('the period of liner and nonliner pendulun')
#legend(loc='best',prop={'size':11},frameon=False)
show()

#show()
