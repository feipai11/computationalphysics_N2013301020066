# _*_ coding: utf-8 _*_

# Use the class founction for the first time
# the adiabatic model is used in this progrem

import numpy as np
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

theta=np.linspace(15,75,12)
d_final=[]
for i in range(len(theta)):
    d=Drag_cannon(flight_state(0,0,100*2**0.5*math.cos(theta[i]/57.325),100*2**0.5*math.sin(theta[i]/57.325)))
    d.shot()
    d.show_trace()
    plt.plot(x,y,label=r'draged$\theta=%f^\circ$'%theta[i])
    plt.legend(loc='best',prop={'size':11},frameon=False)
    d_final.append(x[-1])
plt.show()

theta1=np.linspace(13.5,73.5,12)
width=3
plt.bar(theta1,d_final,width,color='b')
plt.xlabel(r'$\theta/^\circ$')
plt.ylabel('Relative Impact')
plt.title('the influence caused by the airdrag')
plt.show()
