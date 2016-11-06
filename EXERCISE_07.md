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


        如果我们考虑阻尼，单摆的动力学方程会变为


        这时，单摆将会做阻尼振动，有


        此时单摆将做振幅逐渐减小的周期性阻尼振动，经过较长时间后，振幅几乎为零，可以认为振动停止。然而，如果有驱动力，情况又将大不一样，单摆的运动学方程变为


        这时单摆做受迫振动，有


其中


        然而，在摆角较大时，近似不再成立，我们必须设法求解如下非线性方程


###2.算法探讨

        我们如果依然采用欧拉法，将得到发散的解，显然这与实际不符，在此我们采用欧拉-克罗默方法求数值解，步骤如下




注意，若不在区间内，我们须通过加或减使其落入区间内。

###代码如下所示
