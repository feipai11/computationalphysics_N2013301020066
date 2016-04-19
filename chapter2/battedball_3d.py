# _*_ coding: utf-8 _*_

# Use the class founction for the first time
# the adiabatic model is used in this progrem

import numpy as np
import matplotlib.pyplot as plt
import math
from mpl_toolkits.mplot3d import Axes3D

g=9.8
b2m=4e-4
s2m=4.1e-4
class flight_state:
    def __init__(self, _x=0,_y=0,_z=0,_vx=0,_vy=0,_vz=0,_t=0):
        self.x=_x
        self.y=_y
        self.z=_z
        self.vx=_vx
        self.vy=_vy
        self.vz=_vz
        self.t=_t
class Ball:
    def __init__(self,_fs=flight_state(0,0,0,0,0,0,0),_dt=0.1):
        self.ball_flight_state=[]
        self.ball_flight_state.append(_fs)
        self.dt=_dt
        #self.w=[]
        #self.w.append[w1]
        #self.w.append[w2]
        #self.w.append[w3]
        #print self.w
        #print self.cannon_flight_state[-1].x,self.cannon_flight_state[-1].y
    def next_state(self,current_state):
        global g
        next_x=current_state.x+current_state.vx*self.dt        
        next_vx=current_state.vx
        next_y=current_state.y+current_state.vy*self.dt
        next_vy=current_state.vy
        next_z=current_state.y+current_state.vz*self.dt
        next_vz=current_state.vz-g*self.dt
        next_t=current_state.t+self.dt
        #print next_x,next_y,next_z
        return flight_state(next_x,next_y,next_z,next_vx,next_vy,next_vz,next_t)
    def shot(self):
        while not(self.ball_flight_state[-1].z<0):
            self.ball_flight_state.append(self.next_state(self.ball_flight_state[-1]))
        r = - self.ball_flight_state[-2].z / self.ball_flight_state[-1].z
        self.ball_flight_state[-1].x = (self.ball_flight_state[-2].x + r * self.ball_flight_state[-1].x) / (r + 1)
        self.ball_flight_state[-1].y = (self.ball_flight_state[-2].y + r * self.ball_flight_state[-1].y) / (r + 1)
        self.ball_flight_state[-1].z= 0
        #print self.cannon_flight_state[-1].x,self.cannon_flight_state[-1].y
    def show_trace(self):
        global x,y,z
        x=[]
        y=[]
        z=[]
        for fs in self.ball_flight_state:
            x.append(fs.x)
            y.append(fs.y)
            z.append(fs.z)
class Spin_ball(Ball):
    def next_state(self,current_state):
        global g,b2m,s2m
        #w=2000
        v=math.sqrt(current_state.vx**2+current_state.vy**2)
        next_x=current_state.x+current_state.vx*self.dt
        next_vx=current_state.vx+(-b2m*v*current_state.vx+s2m*(-self.w[2]*current_state.vy+self.w[1]*current_state.vz))*self.dt
        next_y=current_state.y+current_state.vy*self.dt
        next_vy=current_state.vy-g*self.dt+(s2m*(self.w[2]*current_state.vx-self.w[0]*current_state.vz)-b2m*v*current_state.vy)*self.dt
        next_z=current_state.z+current_state.vz*self.dt
        next_vz=current_state.z+(-b2m*v*current_state.vz+s2m*(self.w[0]*current_state.vy-self.w[1]*current.state.vx))*self.dt
        next_t=current_state.t+self.dt
        return flight_state(next_x,next_y,next_vx,next_vy,next_z,next_vz,next_t)
#class Kunckleball(Ball):
fig = plt.figure()
ax = fig.add_subplot(111,projection='3d')
c1=Ball(flight_state(0,0,50,5,0,0,0),_dt=0.1)
c1.shot()
c1.show_trace()
ax.plot(x,y,z,label=r'free ball')
ax.set_xlabel('x/m', fontsize = 12)
ax.set_ylabel('y/m', fontsize=12)
ax.set_zlabel('z/m',fontsize=12)
#plt.legend(loc='best',prop={'size':8},frameon=False)
#c1_final=x[-1]
#w=np,linspace()
#w_space=np.linspace(-200,1600,9)
#for i in range(len(w_space)):
#    w=w_space[i]
#    d1=Spin_ball(flight_state(0,0,50,50*math.tan(30/57.3),0,0,0),_dt=0.1,_w=[0,0,w])
#    d1.shot()
#    d1.show_trace()

#    ax.plot(x,y,z,':',label=r'actual $\omega=%d$'%w,lw=1)
#    plt.legend(loc='best',prop={'size':8},frameon=False)
#d1_final=x[-1]

#plt.text(190,145,r'Initial $\theta=30^\circ$',fontsize=18)
#plt.xlabel('horizontal')
#plt.ylabel('vertical')
#plt.title('the trajectory of the baseball',fontsize=16)
plt.show()

