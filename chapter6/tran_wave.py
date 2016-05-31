from matplotlib.pyplot import *
import numpy as np
from matplotlib import animation

c=300
class Wave:
    def __init__(self,_x=np.linspace(0,1,100),_t=0,_dx=0.01,_tfinal=0.5):
        self.x=_x
        self.y=[list(np.exp(-1000*(_x-0.3)**2))]
        self.y.append(list(np.exp(-1000*(_x-0.3)**2)))
        self.t=[]
        self.t.append(_t)
        self.dx=_dx
        self.dt=_dx/c
        self.tfinal=_tfinal
    def cal(self):
        while self.t[-1]<self.tfinal:
            y_next=np.zeros(100)
            y_next[0]=0
            y_next[99]=0
            for i in range(1,98):
                if self.x[i]<0.5:
                    y_next[i]=-self.y[-2][i]+self.y[-1][i+1]+self.y[-1][i-1]
                else:
                    y_next[i]=2*0.75*self.y[-1][i]-self.y[-2][i]+0.25*(self.y[-1][i+1]+self.y[-1][i-1])
            self.y.append(y_next)
            self.t.append(self.t[-1]+self.dt)
    def plot_2d(self):
        plot(self.x,self.y[-1])
        show()
a=Wave()
a.cal()
#a.plot_2d()
fig = figure()
ax=axes(xlim=(0,1), ylim=(-1.2, 1.2))
line, = ax.plot([], [], lw=2)
def animate(i):    
    line.set_data(a.x, a.y[i])    
    return line,
def init():    
    line.set_data([], [])    
    return line,
anim = animation.FuncAnimation(fig, animate,init_func=init,frames=200, interval=20, blit=True)
show()
