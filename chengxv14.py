import pylab as pl
import math  as mt
g=9.8
l=9.8
q=0.5
ou_d=2/3
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


pl.subplot(121)
A = pendulum(0.5, 0.2)
A.run()
pl.plot(A.theta, A.omiga, 'r.', label='$F_D=0.5$')
pl.title('$ω$ versus $θ$')
pl.legend(loc="upper right", frameon=False)
pl.xlabel('$θ$(radians)')
pl.ylabel('$ω$(radians/s)')

pl.subplot(122)
A = pendulum(1.2, 0.2)
A.run()
pl.plot(A.theta, A.omiga, 'r.', label='$F_D=1.2$')
pl.title('$ω$ versus $θ$')
pl.legend(loc="upper right", frameon=False)
pl.xlabel('$θ$(radians)')
pl.ylabel('$ω$(radians/s)')

pl.show()
