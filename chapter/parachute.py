#!/usr/bin/env python
# -*- coding: utf-8 -*-

#import pylab as pl
import json
from matplotlib import *
import matplotlib.pyplot as plt

v_para = []
t = []
dt=0
n=0
a=0
b=0

def initialize(v_para,t,_dt,_n,_a,_b):
    global dt, n ,a ,b
    print "initial velocity :"
    v_para.append(float(raw_input()))
    print "time step :"
    dt=float(raw_input())
    print "total time :"
    time = float(raw_input())
    t.append(0)
    print "constant a :"
    a = float(raw_input())
    print "constant b :"
    b = float(raw_input())

    n = int(time / dt)
    return

def calculate(v_para,t,dt,n,a,b):
    for i in range(1,n):
        v_para.append(v_para[i-1]+(a-b*v_para[i-1])*dt)
        t.append(t[-1]+dt)
    return

def store(v_para,t):
    c='parachute_data%s.txt'%b
    mydata = open(c,"w")
    for i in range(1,n):
        print >> mydata,t[i],v_para[i]
    mydata.close()
    return

def main():
    initialize(v_para,t,dt,n,a,b)
    calculate(v_para,t,dt,n,a,b)
    store(v_para,t)
    plot = plt.plot(t,v_para,'g',linewidth=2)
    plt.title('the relation between v and t')
    plt.xlabel(r'$t/s$') 
    plt.ylabel(r'$v/ms^{-1}$')
    #v_para=[]
    #t=[]
    #initialize(v_para,t,dt,n,a,b)
    #calculate(v_para,t,dt,n,a,b)
    #store(v_para,t)
    #plot2 = plt.plot(t,v_para,'r',linewidth=2)
    #plt.legend(handles=[plot],loc=4)
    plt.show()
    plt.savefig('myplot.png')
    return 

main()


