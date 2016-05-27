# It's a better practice to separate algorithm with the problem so that if
# Euler algorithm doesn't satisfy your requirement for accuracy, you can always
# switch to some more powerful algorithms
# For convenience sake, let's use the convension that system state be described
# by:
#
#   state = [x, y, vx, vy]
#
# And generally, the ODE defined on system state takes the form:
#
#       def Your_ODE(system_state = [x0, x1, x2, x3, ...]):
#           return time_differential_of_state = [dx0/dt, dx1/dt, dx2/dt,...]
#
# Now I shall write the program with these convensions.

from math import exp
from pylab import *
import numpy as np
#from vpython import *

def Euler_algorithm(input_state, dt, ODE_set):
    ''' return [dx0, dx1, dx2, ...]
    Euler algorithm for single time step iteration:
    '''
    derivative = ODE_set(input_state)
    return [i*dt for i in derivative]

class simulator:
    '''
    basic simulator class, all concrete model should be derived from this one
    '''
    def __init__(self, init_state, start_time, dt, iterator = Euler_algorithm):
        self.state = list(init_state)
        self.time = start_time
        self.dt = dt
        self.iterator = iterator
        self.state_container = [[start_time] + self.state]  # element format [time, x0,x1,...]

    def stop_condition(self):
        ''' return boolean
        Placeholder function: override it in concrete model
        indicate the condition to stop:
            True: iteration of self.integrate() will be stoped
            False: iteration of self.integrate() will continue
        '''
        return True

    def system_ODE(self, input_state):
        ''' return [dx0/dt, dx1/dt, ...]
        Placeholder ODE
        '''
        return input_state

    def integrate(self):
        '''
        Intergrate the system until stop_condition is met. All iteration
        results are stored in state_container
        '''
        while not self.stop_condition():
            self.time += self.dt
            self.state = [ i[0]+i[1] for i in zip(self.state,self.iterator(self.state, self.dt,self.system_ODE))]
            self.state_container.append([self.time] + self.state)

class whether(simulator):
    '''
    normal cannon
    '''
    def __init__(self, init_state = (0.,0.,0.), start_time=0, dt=0.0001, iterator = Euler_algorithm,tfinal=50,r=5):
        simulator.__init__(self, init_state, start_time, dt, iterator)
        self.tfinal=tfinal
        #print self.time
        self.r=r

    def stop_condition(self):
        '''
        Stop simulation when y<0
        '''
        if self.time > self.tfinal:
            return True
        return False

    def system_ODE(self, input_state):
        '''
        return [dx/dt, dy/dt, dvx/dt, dvy/dt]
        Note that:
            dx/dt = vx
            dy/dt = vy
            dvx/dt = 0
            dvy/dt = -g
        '''
        return [
            10*(input_state[1]-input_state[0]),
            -input_state[0]*input_state[2]+self.r*input_state[0]-input_state[1],
            input_state[0]*input_state[1]-8.0/3.0*input_state[2],
            ]

    def show_trajectory(self):
        '''
        Plot trajectory
        '''
        global container
        container = np.array(self.state_container).transpose()
        #np.savetxt('position.dat',container,fmt='%12.6',delimiter='')
        plot(container[1], container[3],label = 'r=%d'%self.r)  # plot x,y, label vy/vx of init
        legend(loc='upper right',prop = {'size':11},frameon = False)
        xlabel('x')
        ylabel('z')
    def show_amp(self):
        global container
        container = np.array(self.state_container).transpose()
        #np.savetxt('position.dat',container,fmt='%12.6',delimiter='')
        plot(container[0],container[3],label = 'r=%d'%self.r)
        legend(loc='best',prop = {'size':11},frameon = False)
        xlabel('t/s')
        ylabel('z')

'''
fig=figure()
rd=[5,10,25]
for i in range(3):
    #ri=rd[i]
    a=whether((1.,0.,0.),r=rd[i])
    a.integrate()
    a.show_amp()
'''

    

a = whether((1.,0.,0.),tfinal=2000,dt=0.001,r=25)
a.integrate()
a.show_trajectory()
show()
#data=np.loadtxt('position.dat')
x=[]
y=[]
for i in range(len(container[0,:])):
    if abs(container[2][i])<0.001:
        x.append(container[1,i])
        y.append(container[3,i])
plt.scatter(x,y,s=2,alpha=0.8)
show()
#show()
