# -*- coding: utf-8 -*-
"""
Created on Thu Mar 19 16:59:27 2016
@author: AF
"""

import matplotlib.pyplot as plt


def read_initial(initial_file):
    itxt= open(initial_file)
    initial_data=[]
    data =[]  
    for lines in itxt.readlines():
        lines=lines.replace("\n","").split(",")
        initial_data.append(lines)
    print len(initial_data[0][0].split(' '))
    for i in range(len(initial_data[0][0].split(' '))):
        data.append([])
        for j in range(len(initial_data)):
            data[i].append(initial_data[j][0].split(' ')[i])
    itxt.close()
    return data     ### data[0] = x, data[1] = y1, data[2] = y2,...
    
#def draw_figure(data):
 #   for i in range(1,len(data)):
  #      plt.plot(data[0],data[i])
   # plt.xlabel('time(s)')
   # plt.ylabel('velocity(m/s)')
#    plt.text(3,0.8*y[0],'Time Constant ='+str(tc)+'s'+'\n'+'Time Step ='+str(dt)+'s')
   # plt.show()

# a=raw_input('please input your file name:')
def main():
    # a=raw_input('please input your file name:')
    data = read_initial('parachute_data2.0.txt')
    print data
    plt.plot(data[0],data[1],label='a=10,b=2')
    legend1=plt.legend(loc='upright')
    data = read_initial('parachute_data5.0.txt')
    print data 
    plt.plot(data[0],data[1],label='a=5,b=5')
    legend2=plt.legend(loc='upright')
    plt.xlabel(r'$t/s$')
    plt.ylabel(r'$v/m*s^{-1}$')
    plt.title('the relation between the velocity and time')
   # draw_figure(data1)
   # draw_figure(data2)
   #plt.plot(data1[0],data1[1])
   #plt.plot(data2[0],data2[1])
   
   
    plt.show()

main()      


