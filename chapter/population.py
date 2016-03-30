import numpy as np
import matplotlib.pyplot as plt
import math as ma
y=[]
t=[]
def ini():
    global tspan,a,b,etotal,h,y0
    tspan=raw_input('input yout final time:')
    tspan=float(tspan)
    y0=raw_input('input the initial population:')
    y0=float(y0)
    a=raw_input('input the constant a:')
    a=float(a)
    b=raw_input('input the constant b:')
    b=float(b)
    #h=raw_input('input the time step h:')
    #h=float(h)
    #t.append(0)
    #y.append(y0)
    return 

def calculate(tspan,y,h,t):
    for i in range(int(tspan/h)):
        t.append(t[-1]+h)
        y.append(y[i]+h*(a*y[i]-b*y[i]**2))
    return   

def store(tspan,y,h,t):
    name='population_data%s-%s-%s.txt'%(a,b,h)
    mydata=open(name,"w")
    for i in range(len(t)):
        print >> mydata,t[i],y[i]
    mydata.close
    return

def main():
    ini()
    #calculate(tspan,y,h,t)
    #store(tspan,y,h,t)
    if b==0:
        t=[0]
        y=[y0]
        h=0.01

        calculate(tspan,y,h,t)
        store(tspan,y,h,t)
        
        y_ex=[]
        for i in range(len(t)):
            y_ex.append(y0*ma.e**(a*t[i]))
        plot2=plt.plot(t,y_ex,'g',label='exact solution')
        legend2=plt.legend(loc='upper left')
        plot=plt.plot(t,y,'ro',label='numerical h=0.01')
        legend1=plt.legend(loc='upper left')
        t1=[0]
        y1=[y0]
        h=h/5
        calculate(tspan,y1,h,t1)
        plot1=plt.plot(t1,y1,'b*',label='numberical h=0.002')
        legend2=plt.legend(loc='upper left')

        #y2=[0]
        #t2=[y0]
        #h=4*h
        #calculate(tspan,y2,h,t2)
        #plot1=plt.plot(t2,y2,'k^',label='numberical h=0.02')
        #legend2=plt.legend(loc='upper left')
        plt.xlim(0.0,1.1)
        plt.xlabel('t')
        plt.ylabel('number')
        plt.title('the relation between population and time')
    else:
        t=[0]
        y=[y0]
        h=0.001

        calculate(tspan,y,h,t)
        #store(tspan,y,h,t)
        plot=plt.plot(t,y,'ro',label='numericial h=0.001')
        legend=plt.legend(loc='best')

        t2=[0]
        y2=[y0]
        h=0.005
        calculate(tspan,y2,h,t2)
        plot1=plt.plot(t,y,'bs',label='numberical h=0.005')
        legend2=plt.legend(loc='best')
        #store(tspan,y,h,t)
        y1=[y0]
        t1=[0]
        h=0.002
        calculate(tspan,y1,h,t1)
        plot1=plt.plot(t1,y1,'gv',label='numberical h=0.002')
        legend2=plt.legend(loc='best')
        plt.xlabel('t')
        plt.ylabel('number')
        plt.title('the relation between population and time')
    plt.show()

main()
        
        
