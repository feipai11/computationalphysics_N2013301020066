from matplotlib.pyplot import *
import numpy as np
from visual import *



class Planet:
    def __init__(self,_m1=2e30,_m2=6e24,_x2=0,_y2=0,_vx2=0,_vy2=0,_m3=1.9e27,_x3=0,_y3=0,_vx3=0,_vy3=0,_t=0,_dt=0.01,_beta=2):
        '''self.x1=[]
        self.x1.append(_x1)
        self.vx1=[]
        self.vx1.append(_vx1)
        self.y1=[]
        self.y1.append(_y1)
        self.vy1=[]
        self.vy1.append(_vy1)
        '''
        self.x2=[]
        self.x2.append(_x2)
        self.vx2=[]
        self.vx2.append(_vx2)
        self.y2=[]
        self.y2.append(_y2)
        self.vy2=[]
        self.vy2.append(_vy2)
        self.x3=[]
        self.x3.append(_x3)
        self.vx3=[]
        self.vx3.append(_vx3)
        self.y3=[]
        self.y3.append(_y3)
        self.vy3=[]
        self.vy3.append(_vy3)
        self.m1=_m1
        self.m2=_m2
        self.m3=_m3
        self.dt=_dt
        self.t=[]
        self.t.append(_t)
        self.beta=_beta
        #print self.theta[-1],self.t[-1],self.w[-1]
        return
    def calculate(self):
        while self.t[-1]<5:
            r12=(self.x2[-1]**2+self.y2[-1]**2)**0.5
            r13=(self.x3[-1]**2+self.y3[-1]**2)**0.5
            r32=((self.x3[-1]-self.x2[-1])**2+(self.y3[-1]-self.y2[-1])**2)**0.5
            #self.vx1.append(self.vx1[-1]-4*np.pi**2*(self.x1[-1]-self.x2[-1])/r12**3*self.dt-4*np.pi**2*(self.x1[-1]-self.x3[-1])/r13**3*self.dt)
            #self.vy1.append(self.vy1[-1]-4*np.pi**2*(self.y1[-1]-self.y2[-1])/r12**3*self.dt-4*np.pi**2*(self.y1[-1]-self.y3[-1])/r13**3*self.dt)
            #self.x1.append(self.x1[-1]+self.vx1[-1]*self.dt)
            #self.y1.append(self.y1[-1]+self.vy1[-1]*self.dt)
            self.vx2.append(self.vx2[-1]+4*np.pi**2*(-self.x2[-1])/r12**3*self.dt+4*np.pi**2*(self.m3/self.m1)*(self.x3[-1]-self.x2[-1])/r32**3*self.dt)
            self.vy2.append(self.vy2[-1]+4*np.pi**2*(-self.y2[-1])/r12**3*self.dt+4*np.pi**2*(self.m3/self.m1)*(self.y3[-1]-self.y2[-1])/r32**3*self.dt)
            self.x2.append(self.x2[-1]+self.vx2[-1]*self.dt)
            self.y2.append(self.y2[-1]+self.vy2[-1]*self.dt)
            self.vx3.append(self.vx3[-1]+4*np.pi**2*(-self.x3[-1])/r13**3*self.dt-4*np.pi**2*(self.m2/self.m1)*(self.x3[-1]-self.x2[-1])/r32**3*self.dt)
            self.vy3.append(self.vy3[-1]+4*np.pi**2*(-self.y3[-1])/r13**3*self.dt-4*np.pi**2*(self.m2/self.m1)*(self.y3[-1]-self.y2[-1])/r32**3*self.dt)
            self.x3.append(self.x3[-1]+self.vx3[-1]*self.dt)
            self.y3.append(self.y3[-1]+self.vy3[-1]*self.dt)
            self.t.append(self.t[-1]+self.dt)
        return
    def plot_2d(self):
        #global x,y
        #x=self.x
        #y=self.y
        #font = {'family': 'serif','color':  'darkred','weight': 'normal','size': 16,}
        #font1 = {'family': 'serif','color':  'darkred','weight': 'normal','size': 12,}
        scatter([0],[0],color='red',s=100)
        plot(self.x2,self.y2,'b',lw=1,label='Earth')
        plot(self.x3,self.y3,'g',lw=2,label='Jupiter')
        xlabel('x/AU')
        ylabel('y/AU')
        grid(True)
        axis('equal')
        #scatter([0],[0],s=500,color='red')
        legend(loc='upper right',frameon=False,prop={'size':14})
        title('the orbit of the planet')
        text(-5.34, 5.716, r'$M=1000M_J$', fontdict={'size':14})
        #show()
        return
a=Planet(_m3=1.9e30,_x2=1.0,_y2=0,_vx2=0,_vy2=2*np.pi,_x3=5.2,_y3=0,_vx3=0,_vy3=2*np.pi*(1/5.2)**0.5,_t=0)
a.calculate()
a.plot_2d()
show()
