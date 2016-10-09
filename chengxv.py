 import numpy as np    
 import pylab as pl    
 Number_A=[]    
 Number_B=[]    
 t=[]    
 print('the number of A atoms')    
 number_a=float(input())    
 Number_A.append(number_a)    
 print('the number of B atoms')    
 number_b=float(input())    
 Number_B.append(number_b)    
 print('the time of decay')    
 tdecay=float(input())    
 print('the time step')    
 dt=float(input())    
 t.append(0)    
 for i in range(100):    
     NA=Number_A[i]+((Number_B[i]-Number_A[i])/tdecay)*dt    
     NB=Number_B[i]+((Number_A[i]-Number_B[i])/tdecay)*dt    
     tadd=t[i]+dt    
     Number_A.append(NA)    
     Number_B.append(NB)    
     t.append(tadd)    
 t_max=t[-1]    
 pl.plot(t,Number_A,'r')    
 pl.plot(t,Number_B,'g')    
 pl.title('the decay between A and B')    
 pl.xlabel('the time of decay')    
 pl.ylabel('number of atoms')    
 pl.xlim(0.00,t_max)    
 pl.ylim(Number_B[0],Number_A[0])    
 pl.show()
