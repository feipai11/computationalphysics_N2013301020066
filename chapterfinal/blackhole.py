from matplotlib.pyplot import *
import numpy as np
from visual import *
from matplotlib import animation



class Planet:
    def __init__(self,m1=1,x1=0,y1=0,vx1=0,vy1=0,m2=1,x2=0,y2=0,vx2=0,vy2=0,t=0,dt=0.001,tfinal=40):
        self.m1=m1
        self.x1=[]
        self.x1.append(x1)
        self.vx1=[]
        self.vx1.append(vx1)
        self.y1=[]
        self.y1.append(y1)
        self.vy1=[]
        self.vy1.append(vy1)
        self.m2=m2
        self.x2=[]
        self.x2.append(x2)
        self.vx2=[]
        self.vx2.append(vx2)
        self.y2=[]
        self.y2.append(y2)
        self.vy2=[]
        self.vy2.append(vy2)
        self.t=[]
        self.t.append(t)
        self.r=[]
        self.r.append(x2-x1)
        self.dt=dt
        self.tfinal=tfinal
        #print self.theta[-1],self.t[-1],self.w[-1]
        return
    def calculate(self):
        while self.t[-1] < self.tfinal:
            #r_next=((self.x1[-1]-self.x2[-1])**2+(self.y1[-1]-self.y2[-1])**2)**0.5
            self.vx1.append(self.vx1[-1]-4*np.pi**2*(self.x1[-1]-self.x2[-1])/self.r[-1]**3*self.dt)
            self.x1.append(self.x1[-1]+self.vx1[-1]*self.dt)
            self.vy1.append(self.vy1[-1]-4*np.pi**2*(self.y1[-1]-self.y2[-1])/self.r[-1]**3*self.dt)
            self.y1.append(self.y1[-1]+self.vy1[-1]*self.dt)
            self.vx2.append(self.vx2[-1]+4*np.pi**2*(self.x1[-2]-self.x2[-1])/self.r[-1]**3*self.dt)
            self.x2.append(self.x2[-1]+self.vx2[-1]*self.dt)
            self.vy2.append(self.vy2[-1]+4*np.pi**2*(self.y1[-2]-self.y2[-1])/self.r[-1]**3*self.dt)
            self.y2.append(self.y2[-1]+self.vy2[-1]*self.dt)
            self.r.append(self.r[-1]-1e-1*self.r[-1]**(-3)*self.dt)
            self.t.append(self.t[-1]+self.dt)
        return
    def plot_2d(self):
        #global x,y
        #x=self.x
        #y=self.y
        #fig=figure()
        #ax=axes(xlim=(-1.1,1.1),ylim=(-1.5,1.5))
        plot(self.x1,self.y1)
        plot(self.x2,self.y2)
        xlim(-1.1,1.1)
        ylim(-1.5,1.5)
        xlabel('x/AU')
        ylabel('y/AU')
        grid(True)
        axis('equal')
        #scatter([0],[0],s=500,color='red')
        #legend(loc='upper right',frameon=False)
        #title("the orbit of the planet")
        #show()
        return
a=Planet(x1=-1.,y1=0.,vx1=0.,vy1=np.pi,x2=1.,y2=0.,vx2=0.,vy2=-np.pi)
a.calculate()
a.plot_2d()
show()
