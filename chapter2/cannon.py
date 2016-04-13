# _*_ coding: utf-8 _*_

# Use the class founction for the first time
# the adiabatic model is used in this progrem

import numpy
import matplotlib.pyplot as plt
import math

g=9.8
b2m=5e-5
class flight_state:
    def __init__(self, _x=0,_y=0,_vx=0,_vy=0,_t=0):
        self.x=_x
        self.y=_y
        self.vx=_vx
        self.vy=_vy
        self.t=_t
class Cannon:
    def __init__(self,_fs=flight_state(0,0,0,0,0),_dt=0.1):
        self.cannon_flight_state=[]
        self.cannon_flight_state.append(_fs)
        self.dt=_dt
        #print self.cannon_flight_state[-1].x,self.cannon_flight_state[-1].y
    def next_state(self,current_state):
        global g
        next_x=current_state.x+current_state.vx*self.dt        
        next_vx=current_state.vx
        next_y=current_state.y+current_state.vy*self.dt
        next_vy=current_state.vy-g*self.dt
        next_t=current_state.t+self.dt
        return flight_state(next_x,next_y,next_vx,next_vy,next_t)
    def shot(self):
        while not(self.cannon_flight_state[-1].y<0):
            self.cannon_flight_state.append(self.next_state(self.cannon_flight_state[-1]))
        r = - self.cannon_flight_state[-2].y / self.cannon_flight_state[-1].y
        self.cannon_flight_state[-1].x = (self.cannon_flight_state[-2].x + r * self.cannon_flight_state[-1].x) / (r + 1)
        self.cannon_flight_state[-1].y = 0
        #print self.cannon_flight_state[-1].x,self.cannon_flight_state[-1].y
    def show_trace(self):
        global x,y
        x=[]
        y=[]
        for fs in self.cannon_flight_state:
            x.append(fs.x)
            y.append(fs.y)
class Drag_cannon(Cannon):
    def next_state(self,current_state):
        global g,b2m
        v=math.sqrt(current_state.vx**2+current_state.vy**2)
        next_x=current_state.x+current_state.vx*self.dt
        next_vx=current_state.vx-b2m*v*current_state.vx*self.dt
        next_y=current_state.y+current_state.vy*self.dt
        next_vy=current_state.vy-g*self.dt-b2m*v*current_state.vy*self.dt
        next_t=current_state.t+self.dt
        return flight_state(next_x,next_y,next_vx,next_vy,next_t)

c1=Cannon(flight_state(0,0,100,100,0),_dt=0.1)
c1.shot()
c1.show_trace()
plt.plot(x,y,'g',label=r'free$\theta=45^\circ$')
plt.legend(loc='best',prop={'size':11},frameon=False)
c1_final=x[-1]
d1=Drag_cannon(flight_state(0,0,100,100,0),_dt=0.1)
d1.shot()
d1.show_trace()
plt.plot(x,y,'g-.',label=r'draged$\theta=45^\circ$')
plt.legend(loc='best',prop={'size':11},frameon=False)
d1_final=x[-1]

c2=Cannon(flight_state(0,0,100*2**0.5*math.cos(60/57.325),100*2**0.5*math.sin(60/57.325)))
c2.shot()
c2.show_trace()
plt.plot(x,y,'r',label=r'free$\theta=60^\circ$')
plt.legend(loc='best',prop={'size':11},frameon=False)
c2_final=x[-1]
d2=Drag_cannon(flight_state(0,0,100*2**0.5*math.cos(60/57.325),100*2**0.5*math.sin(60/57.325)))
d2.shot()
d2.show_trace()
plt.plot(x,y,'r-.',label=r'draged$\theta=60^\circ$')
plt.legend(loc='best',prop={'size':11},frameon=False)
d2_final=x[-1]

c3=Cannon(flight_state(0,0,100*2**0.5*math.cos(30/57.325),100*2**0.5*math.sin(30/57.325)))
c3.shot()
c3.show_trace()
plt.plot(x,y,'b',label=r'free$\theta=30^\circ$')
legend3=plt.legend(loc='best',prop={'size':11},frameon=False)
c3_final=x[-1]
d3=Drag_cannon(flight_state(0,0,100*2**0.5*math.cos(30/57.325),100*2**0.5*math.sin(30/57.325)))
d3.shot()
d3.show_trace()
plt.plot(x,y,'b-.',label=r'draged$\theta=30^\circ$')
plt.legend(loc='best',prop={'size':11},frameon=False)
d3_final=x[-1]

c4=Cannon(flight_state(0,0,100*2**0.5*math.cos(37.5/57.325),100*2**0.5*math.sin(37.5/57.325)))
c4.shot()
c4.show_trace()
plt.plot(x,y,'y',label=r'free$\theta=37.5^\circ$')
plt.legend(loc='best',prop={'size':11},frameon=False)
c4_final=x[-1]
d4=Drag_cannon(flight_state(0,0,100*2**0.5*math.cos(37.5/57.325),100*2**0.5*math.sin(37.5/57.325)))
d4.shot()
d4.show_trace()
plt.plot(x,y,'y-.',label=r'draged$\theta=37.5^\circ$')
plt.legend(loc='best',prop={'size':11},frameon=False)
d4_final=x[-1]

c5=Cannon(flight_state(0,0,100*2**0.5*math.cos(52.5/57.325),100*2**0.5*math.sin(52.5/57.325)))
c5.shot()
c5.show_trace()
plt.plot(x,y,'c',label=r'free$\theta=52.5^\circ$')
plt.legend(loc='best',prop={'size':11},frameon=False)
c5_final=x[-1]
d5=Drag_cannon(flight_state(0,0,100*2**0.5*math.cos(52.5/57.325),100*2**0.5*math.sin(52.5/57.325)))
d5.shot()
d5.show_trace()
plt.plot(x,y,'c-.',label=r'draged$\theta=52.5^\circ$')
plt.legend(loc='best',prop={'size':11},frameon=False)
d5_final=x[-1]

plt.xlabel('x')
plt.ylabel('y')
plt.title('the trajectory of the cannon shell',fontsize=16)
plt.show()

theta=[45,60,30,37.5,52.5]
theta1=[42.5,57.5,27.5,35,50]
effect=[(c1_final-d1_final)/c1_final,(c2_final-d2_final)/c2_final,(c3_final-d3_final)/c3_final,(c4_final-d4_final)/c4_final,(c5_final-d5_final)/c5_final]

width=5
plt.bar(theta1,effect,width,color='coral')
plt.xlabel(r'$\theta/^\circ$')
plt.ylabel('Relative Impact')
plt.title('the influence caused by the airdrag')
plt.show()
