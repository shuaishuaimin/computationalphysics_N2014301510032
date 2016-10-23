#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import pylab as pl
import math
class cannon_shell:
    def __init__(self,time_step=0.01,):
        self.dt = time_step
        self.l_x=[0]
        self.l_y=[0]
    def run(self):
        print('distanceX->')
        distance_x=float(input())
        print('distanceY(Y<0)->')
        distance_y=float(input())

        x=0
        y=0
        angle=9
        vmin = []
        Angle=[]
        while(angle<=50):                 #扫描角度，求各角度下，发射距离一定，炮弹的发射速度，求出速度最小值
            angle=angle+1
            x0=0
            v0=150
            while(x0<=distance_x):         #扫描速度，求角度一定，发射距离一定时的炮弹发射速度

                cos1 = math.cos(angle*math.pi/180)
                sin1 = math.sin(angle*math.pi/180)
                vx = v0*cos1
                vy = v0*sin1
                while(y>=distance_y):  #仅支持distance_y<0
                    g = 9.8             #求角度一定，速度一定时，发射距离
                    a = (1 - 6.5e-3 * y / 288) ** 2.5
                    x = x + vx * self.dt
                    y = y + vy * self.dt
                    v = math.sqrt(vx ** 2 + vy ** 2)
                    vx = vx - 4e-5 * v * vx * self.dt * a
                    vy = vy - (4e-5 * v * vy * self.dt * a + g) * self.dt

                x0=x
                v0=v0+10
            vmin.append(v0)
            Angle.append(angle)
        vm=min(vmin)
        print(vm-10)
a=cannon_shell()
a.run()
