# _*_ coding: utf-8 _*_

# Use the class founction for the first time
# the adiabatic model is used in this progrem

import numpy as np
import matplotlib.pyplot as plt
import math

g=9.8
b2m=4e-4
s2m=4.1e-4
class flight_state:
    def __init__(self, _x=0,_y=0,_vx=0,_vy=0,_t=0):
        self.x=_x
        self.y=_y
        self.vx=_vx
        self.vy=_vy
        self.t=_t
class Ball:
    def __init__(self,_fs=flight_state(0,0,0,0,0),_dt=0.1):
        self.ball_flight_state=[]
        self.ball_flight_state.append(_fs)
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
        while not(self.ball_flight_state[-1].y<0):
            self.ball_flight_state.append(self.next_state(self.ball_flight_state[-1]))
        r = - self.ball_flight_state[-2].y / self.ball_flight_state[-1].y
        self.ball_flight_state[-1].x = (self.ball_flight_state[-2].x + r * self.ball_flight_state[-1].x) / (r + 1)
        self.ball_flight_state[-1].y = 0
        #print self.cannon_flight_state[-1].x,self.cannon_flight_state[-1].y
    def show_trace(self):
        global x,y
        x=[]
        y=[]
        for fs in self.ball_flight_state:
            x.append(fs.x)
            y.append(fs.y)
class Spin_ball(Ball):
    def next_state(self,current_state):
        global g,b2m,s2m,w
        #w=2000
        v=math.sqrt(current_state.vx**2+current_state.vy**2)
        next_x=current_state.x+current_state.vx*self.dt
        next_vx=current_state.vx-(b2m*v*current_state.vx+s2m*w*current_state.vy)*self.dt
        next_y=current_state.y+current_state.vy*self.dt
        next_vy=current_state.vy-g*self.dt+(s2m*w*current_state.vx-b2m*v*current_state.vy)*self.dt
        next_t=current_state.t+self.dt
        return flight_state(next_x,next_y,next_vx,next_vy,next_t)
#class Kunckleball(Ball):

c1=Ball(flight_state(0,0,50,50*math.tan(30/57.3),0),_dt=0.1)
c1.shot()
c1.show_trace()
plt.plot(x,y,'',label=r'free ball')
plt.legend(loc='best',prop={'size':8},frameon=False)
#c1_final=x[-1]
#w=np,linspace()
w_space=np.linspace(-200,1600,9)
for i in range(len(w_space)):
    w=w_space[i]
    d1=Spin_ball(flight_state(0,0,50,50*math.tan(30/57.3),0),_dt=0.1)
    d1.shot()
    d1.show_trace()
    plt.plot(x,y,':',label=r'actual $\omega=%d$'%w,lw=1)
    plt.legend(loc='best',prop={'size':8},frameon=False)
#d1_final=x[-1]

plt.text(190,145,r'Initial $\theta=30^\circ$',fontsize=18)
plt.xlabel('horizontal')
plt.ylabel('vertical')
plt.title('the trajectory of the baseball',fontsize=16)
plt.show()

#theta=[45,60,30,37.5,52.5]
#theta1=[42.5,57.5,27.5,35,50]
#effect=[(c1_final-d1_final)/c1_final,(c2_final-d2_final)/c2_final,(c3_final-d3_final)/c3_final,(c4_final-d4_final)/c4_final,(c5_final-d5_final)/c5_final]

#width=5
#plt.bar(theta1,effect,width,color='coral')
#plt.xlabel(r'$\theta/^\circ$')
#plt.ylabel('Relative Impact')
#plt.title('the influence caused by the airdrag')
#plt.show()
