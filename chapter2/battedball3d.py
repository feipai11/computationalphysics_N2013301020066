import argparse
import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import axes3d

class baseball_normal:
    def __init__(self, v, theta, w, y0, z0, x1, y1, z1):
        ###------- position of the picher -----------
        self.y0 = y0  
        self.z0 = z0
        ###------- position of the home plate -------
        self.x1 = x1
        self.y1 = y1
        self.z1 = z1
        ###------------------------------------------
        self.dt = 0.01
        self.v = v*0.44704
        self.theta = theta
        self.w = w*2*np.pi

        
    def calculate(self):
        vx = []
        vy = []
        vz = []
        vx.append( self.v * np.cos(self.theta*np.pi/180))
        vy.append( self.v * np.sin(self.theta*np.pi/180))
        vz.append(0)
        t = []
        self.x = []       ### forward and backward
        self.y = []       ### up and down
        self.z = []       ### left and right
        t.append(0)
        self.x.append(0)
        self.y.append(self.y0)
        self.z.append(0)
        i = 1
        while ( self.y[-1] >= self.y1 ):
            v = np.sqrt(vx[i - 1]**2+vy[i - 1]**2+vz[i - 1]**2)
            B = 0.0039 + 0.0058/(1 + np.e**((v - 35)/5))
            vx.append(vx[i - 1] - B*self.dt*v*vx[i - 1] - 0.00041*vy[i - 1] * self.w*self.dt)
            vy.append(vy[i - 1] - 9.8*self.dt - B*self.dt*v*vy[i - 1] + 0.00041*vx[i - 1] * self.w*self.dt)
            vz.append(vz[i - 1])
            self.x.append(self.x[i - 1] + 0.5*(vx[i - 1] + vx[i])*self.dt)
            self.y.append(self.y[i - 1] + 0.5*(vy[i - 1] + vy[i])*self.dt)
            self.z.append(self.z[i - 1] + 0.5*(vz[i - 1] + vz[i])*self.dt)
            t.append(t[i - 1] + self.dt)
            i+= 1
        self.x[-1] = self.x[-2]+(self.y1 - self.y[-2])*(self.x[-2] - self.x[-1])/(self.y[-2] - self.y[-1])
        self.z[-1] = self.z[-2]+(self.y1 - self.y[-2])*(self.z[-2] - self.z[-1])/(self.y[-2] - self.y[-1])
        self.y[-1] = self.y1
        return self.x, self.y, self.z  
        
    def plot2D(self):
        data = (raw_input("please input the two variables you want to plot from (x,y,z):").split(' '))
        notation = {'x': self.x, 'y':self.y,'z':self.z}
        plt.figure()
        plt.xlabel(data[0]+' (m)')
        plt.ylabel(data[1]+' (m)')
        plt.plot(notation[data[0]],notation[data[1]])
        plt.show()
        return 0    
    
    def plot3D(self):
        fig = plt.figure
        ax = fig.gca(projection='3d')
        ax.set_xlabel('x (m)', fontsize = 12)
        ax.set_ylabel('z (m)', fontsize = 12)
        ax.set_zlabel('y (m)', fontsize = 12)
        ax.plot(self.x,self.z,self.y)
        plt.show()
        return 0
    
    def store(self):           #### save the calculculate datas            
        data_file = open('data_2_19.txt','w')
        for i in range(len(self.x)):
                data_file.write(str(self.x))
                data_file.write(' ')
                data_file.write(str(self.y))
                data_file.write(' ')
                data_file.write(str(self.z))
                data_file.write('\n')
        print "all the datum have been written in file: data_2_19.txt"
            
    
class baseball_fullspin(baseball_normal):
    def calculate(self, w_x, w_y, w_z):
        w_x = w_x * 2 * np.pi
        w_y = w_y * 2 * np.pi
        w_z = w_z * 2 * np.pi
        vx = []
        vy = []
        vz = []
        vx.append( self.v * np.cos(self.theta*np.pi/180))
        vy.append( self.v * np.sin(self.theta*np.pi/180))
        vz.append(0)
        t = []
        self.x = []       ### forward and backward
        self.y = []       ### up and down
        self.z = []       ### left and right
        t.append(0)
        self.x.append(0)
        self.y.append(self.y0)
        self.z.append(0)
        i = 1
        while ( self.y[-1] >= self.y1 ):
            v = np.sqrt(vx[i - 1]**2+vy[i - 1]**2+vz[i - 1]**2)
            B = 0.0039 + 0.0058/(1 + np.e**((v - 35)/5))
            vx.append(vx[i - 1] - B*self.dt*v*vx[i - 1] + 0.00041*(w_y*vz[i - 1] - w_z*vy[i - 1])*self.dt)
            vy.append(vy[i - 1] - 9.8*self.dt - B*self.dt*v*vy[i - 1] +0.00041*(w_z*vx[i - 1] - w_x*vz[i - 1])*self.dt)
            vz.append(vz[i - 1] - B*self.dt*v*vz[i - 1] + 0.00041*(w_x*vy[i - 1] - w_y*vx[i - 1])*self.dt)
            self.x.append(self.x[i - 1] + 0.5*(vx[i - 1] + vx[i])*self.dt)
            self.y.append(self.y[i - 1] + 0.5*(vy[i - 1] + vy[i])*self.dt)
            self.z.append(self.z[i - 1] + 0.5*(vz[i - 1] + vz[i])*self.dt)
            t.append(t[i - 1] + self.dt)
            i+= 1
        self.x[-1] = self.x[-2]+(self.y1 - self.y[-2])*(self.x[-2] - self.x[-1])/(self.y[-2] - self.y[-1])
        self.z[-1] = self.z[-2]+(self.y1 - self.y[-2])*(self.z[-2] - self.z[-1])/(self.y[-2] - self.y[-1])
        self.y[-1] = self.y1
        return self.x, self.y, self.z

class baseball_rough(baseball_normal):
    def calculate(self):
        vx = []
        vy = []
        vz = []
        vx.append( self.v * np.cos(self.theta*np.pi/180))
        vy.append( self.v * np.sin(self.theta*np.pi/180))
        vz.append(0)
        t = []
        self.x = []       ### forward and backward
        self.y = []       ### up and down
        self.z = []       ### left and right
        t.append(0)
        self.x.append(0)
        self.y.append(self.y0)
        self.z.append(0)
        i = 1
        while ( self.y[-1] >= self.y1 ):
            v = np.sqrt(vx[i - 1]**2+vy[i - 1]**2+vz[i - 1]**2)
            B = (0.0013 + 0.0084/(1 + np.e**((v - 21)/2.5)))*(-(3 - np.e**(0.5*(v - 39)))/(1 + np.e**(0.5*(v - 39))) + 4)
            vx.append(vx[i - 1] - B*self.dt*v*vx[i - 1] - 0.00041*vy[i - 1] * self.w*self.dt)
            vy.append(vy[i - 1] - 9.8*self.dt - B*self.dt*v*vy[i - 1] + 0.00041*vx[i - 1] * self.w*self.dt)
            vz.append(vz[i - 1])
            self.x.append(self.x[i - 1] + 0.5*(vx[i - 1] + vx[i])*self.dt)
            self.y.append(self.y[i - 1] + 0.5*(vy[i - 1] + vy[i])*self.dt)
            self.z.append(self.z[i - 1] + 0.5*(vz[i - 1] + vz[i])*self.dt)
            t.append(t[i - 1] + self.dt)
            i+= 1
        self.x[-1] = self.x[-2]+(self.y1 - self.y[-2])*(self.x[-2] - self.x[-1])/(self.y[-2] - self.y[-1])
        self.z[-1] = self.z[-2]+(self.y1 - self.y[-2])*(self.z[-2] - self.z[-1])/(self.y[-2] - self.y[-1])
        self.y[-1] = self.y1
        return self.x, self.y, self.z
        
class baseball_smooth(baseball_normal):
    def calculate(self):
        vx = []
        vy = []
        vz = []
        vx.append( self.v * np.cos(self.theta*np.pi/180))
        vy.append( self.v * np.sin(self.theta*np.pi/180))
        vz.append(0)
        t = []
        self.x = []       ### forward and backward
        self.y = []       ### up and down
        self.z = []       ### left and right
        t.append(0)
        self.x.append(0)
        self.y.append(self.y0)
        self.z.append(0)
        i = 1
        while ( self.y[-1] >= self.y1 ):
            v = np.sqrt(vx[i - 1]**2+vy[i - 1]**2+vz[i - 1]**2)
            B = 0.0013 + 0.0084/(1 + np.e**((v - 65)/4))
            vx.append(vx[i - 1] - B*self.dt*v*vx[i - 1] - 0.00041*vy[i - 1] * self.w*self.dt)
            vy.append(vy[i - 1] - 9.8*self.dt - B*self.dt*v*vy[i - 1] + 0.00041*vx[i - 1] * self.w*self.dt)
            vz.append(vz[i - 1])
            self.x.append(self.x[i - 1] + 0.5*(vx[i - 1] + vx[i])*self.dt)
            self.y.append(self.y[i - 1] + 0.5*(vy[i - 1] + vy[i])*self.dt)
            self.z.append(self.z[i - 1] + 0.5*(vz[i - 1] + vz[i])*self.dt)
            t.append(t[i - 1] + self.dt)
            i+= 1
        self.x[-1] = self.x[-2]+(self.y1 - self.y[-2])*(self.x[-2] - self.x[-1])/(self.y[-2] - self.y[-1])
        self.z[-1] = self.z[-2]+(self.y1 - self.y[-2])*(self.z[-2] - self.z[-1])/(self.y[-2] - self.y[-1])
        self.y[-1] = self.y1
        return self.x, self.y, self.z
        
class baseball_wind(baseball_normal):
    
    def module(self,vx,vy,vx_w,vy_w):
        delta_vx = vx - vx_w
        delta_vy = vy - vy_w
        return np.sqrt(delta_vx**2 + delta_vy**2)
    
    def calculate(self,vx_w, vy_w):
        vx = []
        vy = []
        vz = []
        vx.append( self.v * np.cos(self.theta*np.pi/180))
        vy.append( self.v * np.sin(self.theta*np.pi/180))
        vz.append(0)
        t = []
        self.x = []       ### forward and backward
        self.y = []       ### up and down
        self.z = []       ### left and right
        t.append(0)
        self.x.append(0)
        self.y.append(self.y0)
        self.z.append(0)
        i = 1
        while ( self.y[-1] >= self.y1 ):
            v = self.module(vx[i - 1], vy[i - 1], vx_w, vy_w)
            B = 0.0039 + 0.0058/(1 + np.e**((v - 35)/5))
            vx.append(vx[i - 1] - B*self.dt*v*(vx[i - 1] - vx_w) - 0.00041*vy[i - 1] * self.w*self.dt)
            vy.append(vy[i - 1] - 9.8*self.dt - B*self.dt*v*(vy[i - 1] - vy_w) + 0.00041*vx[i - 1] * self.w*self.dt)
            vz.append(vz[i - 1])
            self.x.append(self.x[i - 1] + 0.5*(vx[i - 1] + vx[i])*self.dt)
            self.y.append(self.y[i - 1] + 0.5*(vy[i - 1] + vy[i])*self.dt)
            self.z.append(self.z[i - 1] + 0.5*(vz[i - 1] + vz[i])*self.dt)
            t.append(t[i - 1] + self.dt)
            i+= 1
        self.x[-1] = self.x[-2]+(self.y1 - self.y[-2])*(self.x[-2] - self.x[-1])/(self.y[-2] - self.y[-1])
        self.z[-1] = self.z[-2]+(self.y1 - self.y[-2])*(self.z[-2] - self.z[-1])/(self.y[-2] - self.y[-1])
        self.y[-1] = self.y1
        return self.x, self.y, self.z
        

## ---------------- full spin ---------------------
fig=plt.figure()
A = baseball_fullspin(100,10,0,1,0,0,0,0)
record_fullspin = A.calculate(0,300,300)
ax = fig.gca(projection='3d')
ax.plot(record_fullspin[0],record_fullspin[2],record_fullspin[1], label = r'$\omega_y=200 \omega_z=300$')
ax.set_xlabel('Horizontal distance (m)', fontsize = 12)
ax.set_ylabel('z axis (m)', fontsize = 12)
ax.set_zlabel('Vertical height (m)', fontsize = 12)
#ax.set_zlim(0.0,20)
#ax.set_ylim(-10,10)
B = baseball_normal(100,10,0,1,0,0,0,0)
record_normal=B.calculate()
ax.plot(record_normal[0],record_normal[2],record_normal[1], label = 'without spin')


ax.legend(loc='best',prop={'size':11},frameon=False)
plt.show()
