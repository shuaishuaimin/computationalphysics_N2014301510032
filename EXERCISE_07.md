#Excercise_07

##Exercise 3.12

In constructing the Poincaré section in Figure 3.9 we plotted points only at times that were in phase with the drive force; that is, at times , where  is an integer. At these values of  the driving force passed through zero [see(3.18)]. However, we could jusi as easily have chosen to make the plot at times corresponding to a maximum of the drive force, or at times out-of-phase with this force, etc. Construct the Poincaré sections for these cases and compare them with Figure 3.9.

##Exercise 3.13

Write a program to calculate and compare the behavior of two, nearly identical pendulums. Use it to calculate the divergence of two nearby trajectories in the chaotic regime, as in Figure 3.7, and make a qualitative estimate of the corresponding Lyapunov exponent from the slope of a plot of  as a function of  .

##Exercise 3.14

Repeat the previous problem, but give the two pendulums slightly different damping factors. How does the value of the Lyapunov exponent compare with that found in Figure 3.7?

###1. 理论推导

        过去我们已经学习了一些单摆的基础知识，在无阻尼和驱动力且摆角很小的情况下单摆的动力学方程近似为
![](http://latex.codecogs.com/gif.latex?%5Cfrac%7B%5Cmathrm%7Bd%7D%5E2%20%5Ctheta%20%7D%7B%5Cmathrm%7Bd%7D%20t%5E2%7D%3D-%5Cfrac%7Bg%7D%7Bl%7D%5Ccdot%20%5Ctheta)

        显然， 这种情况下单摆近似地做简谐运动，有
        
   ![](http://latex.codecogs.com/gif.latex?%5Ctheta%20%3D%5Ctheta%20o%20sin%28%5COmega%20t&plus;%5Cphi%20%29)

        如果我们考虑阻尼，单摆的动力学方程会变为
  ![](http://latex.codecogs.com/gif.latex?%5Cfrac%7B%5Cmathrm%7Bd%7D%5E2%20%5Ctheta%20%7D%7B%5Cmathrm%7Bd%7D%20t%5E2%7D%3D-%5Cfrac%7Bg%7D%7Bl%7D%5Ctheta%20-q%5Cfrac%7B%5Cmathrm%7Bd%7D%20%5Ctheta%20%7D%7B%5Cmathrm%7Bd%7D%20t%7D)

        这时，单摆将会做阻尼振动，有
  ![](http://latex.codecogs.com/gif.latex?%5Ctheta%20%28t%29%3D%20%7B%5Ctheta%20_%7B0%7D%7D%5Ccdot%20e%5E%7B-%5Cfrac%7Bqt%7D%7B2%7D%7Dsin%28%20%5Csqrt%7B%5COmega%20%5E%7B2%7D-%5Cfrac%7Bq%5E%7B2%7D%7D%7B4%7D%7Dt&plus;%5Cphi%20%29)

        此时单摆将做振幅逐渐减小的周期性阻尼振动，经过较长时间后，振幅几乎为零，可以认为振动停止。然而，如果有驱动力，情况又将大不一样，单摆的运动学     方程变为

![](http://latex.codecogs.com/gif.latex?%5Cfrac%7B%5Cmathrm%7Bd%7D%5E2%20%5Ctheta%20%7D%7B%5Cmathrm%7Bd%7D%20t%5E2%7D%3D-%5Cfrac%7Bg%7D%7Bl%7D%5Ctheta%20-q%5Cfrac%7B%5Cmathrm%7Bd%7D%20%5Ctheta%20%7D%7B%5Cmathrm%7Bd%7D%20t%7D&plus;F_%7BD%7Dsin%28%5COmega%20_%7BD%7Dt%29)
        这时单摆做受迫振动，有<br/>
      ![](http://latex.codecogs.com/gif.latex?%5Ctheta%20%28t%29%3D%5Ctheta%20_%7B0%7Dsin%28%5COmega%20_%7BD%7D&plus;%5Cphi%20%29)         

其中<br/>

  ![](http://latex.codecogs.com/gif.latex?%5Ctheta%20_%7B0%7D%3D%5Cfrac%7BF_%7BD%7D%7D%7B%5Csqrt%7B%28%5COmega%20%5E%7B2%7D-%5COmega%20_%7BD%7D%5E%7B2%7D%29%5E%7B2%7D&plus;q%28%5COmega%20_%7BD%7D%5E%7B2%7D%29%7D%7D)<br/>
        然而，在摆角较大时，近似不再成立，我们必须设法求解如下非线性方程<br/>
![](http://latex.codecogs.com/gif.latex?%5Cfrac%7B%5Cmathrm%7Bd%7D%5E2%20%5Ctheta%20%7D%7B%5Cmathrm%7Bd%7D%20t%5E2%7D%3D-%5Cfrac%7Bg%7D%7Bl%7Dsin%28%5Ctheta%20%29%20-q%5Cfrac%7B%5Cmathrm%7Bd%7D%20%5Ctheta%20%7D%7B%5Cmathrm%7Bd%7D%20t%7D&plus;F_%7BD%7Dsin%28%5COmega%20_%7BD%7Dt%29)<br/>

###2.算法探讨

        我们如果依然采用欧拉法，将得到发散的解，显然这与实际不符，在此我们采用欧拉-克罗默方法求数值解，步骤如下
![](http://latex.codecogs.com/gif.latex?%5Comega%20_%7Bi&plus;1%7D%3D%5Comega%20_%7Bi%7D-%5B%5Cfrac%7Bg%7D%7Bl%7Dsin%5Ctheta%20_%7Bi%7D-q%5Comega%20_%7Bi%7D&plus;F_%7BD%7Dsin%28%5COmega%20_%7BD%7Dt_%7Bi%7D%29%5D%5CDelta%20t)
![](http://latex.codecogs.com/gif.latex?%5Ctheta%20_%7Bi&plus;1%7D%3D%5Ctheta%20_%7Bi%7D&plus;%5Comega%20_%7Bi&plus;1%7D%5CDelta%20t)
![](http://latex.codecogs.com/gif.latex?t_%7Bi&plus;1%7D%3Dt_%7Bi%7D&plus;%5CDelta%20t)

注意，若不在区间内，我们须通过加或减使其落入区间内。

###代码如下所示

[代码](https://github.com/shuaishuaimin/computationalphysics_N2014301510032/blob/master/chengxv21.py)

##得到的图像

![](https://github.com/Damonphysics/computationalphysics_N2014301020007/blob/master/figure_1-2.png?raw=true)
##下面考虑3.12题

###先考虑在一般情况下任意时间的图像，代码如下

[代码2]（https://github.com/shuaishuaimin/computationalphysics_N2014301510032/blob/master/chengxv14.py）

###得到的图像

![](https://github.com/Damonphysics/computationalphysics_N2014301020007/blob/master/figure_1-4.png?raw=true)

###当FD=0.5时，庞加莱界面上大致是一封闭曲线，可以认为运动是准周期的;而当FD=1.2时，庞加莱截面上是一些成片的具有分形结构的密集点，运动变为混沌的

###考虑在特定的时间点附近的omega和theta的分布情况，代码如下

[代码3]（）
