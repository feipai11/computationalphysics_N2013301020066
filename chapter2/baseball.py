#
#It's a better practice to separate algorithm with the problem so that if
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

from math import *
from pylab import plot, show, legend, xlabel, ylabel, cla, clf
import numpy as np

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
    def __init__(self, init_state, start_time, dt=0.1, iterator
                 = Euler_algorithm):
        self.state = list(init_state)
        self.time = start_time
        self.dt = dt
        self.iterator = iterator
        self.state_container = [[start_time] + init_state]  # element format [time, x0,x1,...]

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
            self.state = [ i[0]+i[1]
                           for i in zip(self.state,
                                        self.iterator(self.state, self.dt,
                                                      self.system_ODE))]
            self.state_container.append([self.time] + self.state)

class baseball(simulator):
    '''
    normal cannon
    '''
    def __init__(self, init_state = (0.,0.,0.,0.), start_time=0, dt=0.1, iterator
                 = Euler_algorithm):
        simulator.__init__(self, init_state, start_time, dt, iterator)
        self.gravity = 9.8

    def stop_condition(self):
        '''
        Stop simulation when y<0
        '''
        if self.state[1]>1000:
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
            input_state[2],
            input_state[3],
            0.,
            -self.gravity
            ]

    def show_trajectory(self):
        '''
        Plot trajectory
        '''
        container = np.array(self.state_container).transpose()
        global x,y
        x=container[1]
        y=container[2]
        #plot(container[1], container[2],label =
         #       str(container[4][0]/container[3][0]))  # plot x,y, label vy/vx of init
        #legend(loc='upper right')
        #xlabel('x/m')
        #ylabel('y/m')
#        show()

class spin_ball(baseball):
    '''
    cannon trajectory with constant drag coefficient
    '''
    def __init__(self, init_state = (0.,0.,0.,0.), start_time=0, dt=0.1, iterator
                 = Euler_algorithm):
        baseball.__init__(self, init_state, start_time, dt, iterator)
        self.drag_coef = 4.e-5
        self.spin_coef = 4.e-5

    def system_ODE(self, input_state):
        '''
        return [dx/dt, dy/dt, dvx/dt, dvy/dt]
        Note that:
            dx/dt = vx
            dy/dt = vy
            dvx/dt = -F_drag_x
            dvy/dt = -F_drag_y - g
        '''
        global wz
        speed = (input_state[2]**2+input_state[3]**2)**0.5
        return [
            input_state[2],
            input_state[3],
            -self.drag_coef*speed*input_state[2]-self.spin_coef*wz*input_state[3],
            -self.drag_coef*speed*input_state[3]-self.gravity+self.spin_coef*wz*input_state[2]
            ]
a1 = baseball([0.,0.,400., 0.])
a1.integrate()
a1.show_trajectory()
plot(x,y)
#wz=2000
#a2 = spin_ball([0.,0.,400., 0.])
#a2.integrate()
#a2.show_trajectory()
plot(x,y)
#a3 = iso_drag_cannon([0.,0.,400., 400.])
#a3.integrate()
#a3.show_trajectory()
show()
