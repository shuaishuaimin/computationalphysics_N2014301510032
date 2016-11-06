import pylab as pl
import math  as mt
g=9.8
l=9.8
q=0.5
ou_d=2/3

'''
print('The l ->')
l=float(input())
print('The q ->')
q=float(input())
print('The ou_d ->')
ou_d=float(input())
print('F_D->')
F_D=float(input())
print('theta->')
theta=float(input())
'''

class pendulum:
    def __init__(self,F_D,theta):
        self.theta=[theta]
        self.omiga=[0]
        self.t=[0]
        self.dt=0.04
        self.F_D=F_D
    def run(self):

        while self.t[-1]<60:
            omiga_new=self.omiga[-1]-((g/l)*mt.sin(self.theta[-1])+q*self.omiga[-1]-self.F_D*mt.sin(ou_d*self.t[-1]))*self.dt
            self.omiga.append(omiga_new)
            theta_new=(self.theta[-1]+self.omiga[-1]*self.dt)
            if theta_new>mt.pi:
                theta_new=theta_new-2*mt.pi
            if theta_new<-(mt.pi):
                theta_new=theta_new+2*mt.pi
            self.theta.append(theta_new)
            t_new=self.t[-1]+self.dt
            self.t.append(t_new)



sub1=pl.subplot(251)
A=pendulum(0,0.2)
A.run()
sub1.plot(A.t,A.theta,'g',label='$F_D=0$')
sub1.set_title('$θ$ versus time')
sub1.legend(loc="upper right",frameon=False)
pl.ylabel('$θ$(radians)')
pl.xlabel('time(s)')

sub2=pl.subplot(252)
A=pendulum(0.5,0.2)
A.run()
sub2.plot(A.t,A.theta,'g',label='$F_D=0.5$')
sub2.set_title('$θ$ versus time')
sub2.legend(loc="upper right",frameon=False)
pl.ylabel('$θ$(radians)')
pl.xlabel('time(s)')

sub3=pl.subplot(253)
A=pendulum(1.0,0.2)
A.run()
sub3.plot(A.t,A.theta,'g',label='$F_D=1.0$')
sub3.set_title('$θ$ versus time')
sub3.legend(loc="upper right",frameon=False)
pl.ylabel('$θ$(radians)')
pl.xlabel('time(s)')

sub4=pl.subplot(254)
A=pendulum(1.5,0.2)
A.run()
sub4.plot(A.t,A.theta,'g',label='$F_D=1.5$')
sub4.set_title('$θ$ versus time')
sub4.legend(loc="upper right",frameon=False)
pl.ylabel('$θ$(radians)')
pl.xlabel('time(s)')

sub5=pl.subplot(255)
A=pendulum(2.0,0.2)
A.run()
sub5.plot(A.t,A.theta,'g',label='$F_D=2.0$')
sub5.set_title('$θ$ versus time')
sub5.legend(loc="upper right",frameon=False)
pl.ylabel('$θ$(radians)')
pl.xlabel('time(s)')

sub6=pl.subplot(256)
A=pendulum(0,0.2)
A.run()
sub6.plot(A.t,A.omiga,'b',label='$F_D=0$')
sub6.set_title('$θ$ versus time')
sub6.legend(loc="upper right",frameon=False)
pl.ylabel('$θ$(radians)')
pl.xlabel('time(s)')

sub7=pl.subplot(257)
A=pendulum(0.5,0.2)
A.run()
sub7.plot(A.t,A.omiga,'b',label='$F_D=0.5$')
sub7.set_title('$θ$ versus time')
sub7.legend(loc="upper right",frameon=False)
pl.ylabel('$θ$(radians)')
pl.xlabel('time(s)')

sub8=pl.subplot(258)
A=pendulum(1.0,0.2)
A.run()
sub8.plot(A.t,A.omiga,'b',label='$F_D=1.0$')
sub8.set_title('$θ$ versus time')
sub8.legend(loc="upper right",frameon=False)
pl.ylabel('$θ$(radians)')
pl.xlabel('time(s)')

sub9=pl.subplot(259)
A=pendulum(1.5,0.2)
A.run()
sub9.plot(A.t,A.omiga,'b',label='$F_D=1.5$')
sub9.set_title('$θ$ versus time')
sub9.legend(loc="upper right",frameon=False)
pl.ylabel('$θ$(radians)')
pl.xlabel('time(s)')

sub10=pl.subplot(2,5,10)
A=pendulum(2.0,0.2)
A.run()
sub10.plot(A.t,A.omiga,'b',label='$F_D=2.0$')
sub10.set_title('$θ$ versus time')
sub10.legend(loc="upper right",frameon=False)
pl.ylabel('$θ$(radians)')
pl.xlabel('time(s)')

pl.show()
