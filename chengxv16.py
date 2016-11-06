import pylab as pl
import math  as mt
g=9.8
l=9.8
q=0.5
ou_d=float(2/3)


class pendulum:
    def __init__(self,F_D,theta):
        self.theta=[theta]
        self.omiga=[0]
        self.t=[0]
        self.dt=0.01
        self.F_D=F_D
        self.omiga_need=[0]
        self.theta_need=[0]
    def run(self):

        while self.t[-1]<5000:
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

        a=len(self.theta)

        for i in range(a):
            if (self.t[i]*ou_d)%(2*mt.pi)<0.01 :
                self.theta_need.append(self.theta[i])
                self.omiga_need.append(self.omiga[i])
            elif abs(self.t[i]-mt.pi/4)<0.01:
                self.theta_need.append(self.theta[i])
                self.omiga_need.append(self.omiga[i])

    def draw(self):
        pl.plot(self.theta_need, self.omiga_need, 'r.')
        pl.title('$θ$ versus time')
        pl.legend(loc="upper right", frameon=False)
        pl.ylabel(r'$\omega$(radians/s)')
        pl.xlabel(r'$\theta$[randians]')
        pl.show()
A1=pendulum(1.2,0.2)
A1.run()
A1.draw()
