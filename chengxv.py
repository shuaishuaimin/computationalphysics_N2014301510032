#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import pylab as pl
import time, os, operator

class EX_1_5(object):
    def __init__(self, number_of_a = 100, number_of_b = 0, time_constant = 1, time_of_duration = 5, time_step = 0.05):# Unit of time is sec
        try:# receive initial data, if no input, use directly setup. 
            number_of_a = int(input("Type in number of A(0~100) ->" ))
        except ValueError:
            number_of_a = 100
            print('Initialed as 100')
        try:
            number_of_b = int(input("Type in number of B(0~100) ->",))
        except ValueError:
            number_of_b = 0
            print('Initialed as 0')
        try:
            time_constant = float(input("Type in time constant(sec) ->" ))
        except ValueError:
            time_constant = 1
            print('Initialed as 1(sec)')
        try:
            time_step = float(input("Type in time step(sec) -> ",))
        except ValueError:
            time_step = 0.05
            print('Initialed as 0.05(sec)')
        try:
            time_of_duration = float(input("Type in total time(sec) -> " ))
        except ValueError:
            time_of_duration = 5
            print('Initialed as 5(sec)')

        self.t = [0,]
        self.na = [number_of_a]
        self.nb = [number_of_b]
        self.tau = time_constant
        self.dt = time_step
        self.time = time_of_duration
        self.stp =  int(float(time_of_duration)// float(time_step) +1)
        self.calc()
        self.show_results()

    def calc(self):# use Euler method for calc. 
        for i in range(self.stp):
            tmp_a = self.na[i] +(self.nb[i] - self.na[i]) / self.tau *self.dt
            tmp_b = self.nb[i] + (self.na[i] - self.nb[i]) / self.tau * self.dt
            self.t.append(round((self.t[i] + self.dt),2))
            self.na.append(tmp_a)
            self.nb.append(tmp_b)

    def show_results(self):# output calc results resorting to pylab.
        pl1 = pl.plot(self.t, self.na, color = "red", linewidth = 2.5, linestyle = "-", label = "Number of A")
        pl2 = pl.plot(self.t, self.nb, color = "blue", linewidth = 2.5, linestyle = "-", label = "Number of B")
        pl.title('Decay Process of Two Types of Nuclei')
        pl.xlabel('Time ($s$)')
        pl.ylabel('Number of nuclei')
        pl.legend((pl1[0], pl2[0]), ('Number of A', 'Number of B'), loc='best') 
        pl.show()
        self.store_results()



    def store_results(self):
        store_or_not = input('Store results?(For Windows, data will be stored at D disk.)\nY/N ->')
        if operator.eq(store_or_not,'Y') == True or operator.eq(store_or_not,'y') == True:
            if os.name == 'nt':
                myfile = open('D:\\nuclei_decay_data.txt', 'a', encoding='utf - 8')
            elif os.name == 'posix':
                myfile = open('nuclei_decay_data.txt', 'a', encoding='utf-8')

            print('Calculation at:', time.strftime('%Y-%m-%d %H:%M:%S', time.localtime(time.time())), file = myfile)
            print('NA: %s, NB: %s, time constant: %s (sec),time step: %s (sec), total time: %s (sec)' %(self.na[0], self.nb[0], self.tau, self.dt, self.time), file= myfile)
            print('Time(sec)\tNA\t\tNB', file= myfile)
            for i in range(len(self.t)):
                print('%.2f\t%.2f\t%.2f' %(self.t[i], self.na[i], self.nb[i]), file = myfile)
            myfile.write('----------------------------------- End ---------------------------------------\n')
            myfile.close()
            if os.name == 'nt':
                os.system('explorer /select, D:\\nuclei_decay_data.txt')
            print('Results saved.')

        elif operator.eq(store_or_not,'N') == True or operator.eq(store_or_not,'n') == True:
            print('Pass.')
            pass

        else:
            print(r'Wrong...')
            return self.store_results()
        print('Designd by N')
eg1 = EX_1_5()
