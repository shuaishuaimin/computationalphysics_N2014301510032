
#完成作业1.5

Consider again a decay problem with two types of nuclei of type A into ones of type B, while nuclei of type B, while nuclei of type B decay into ones of type A. Strictly speaking, this is not a "decay" process,since it is possible for the type B nuclei to turn back into type A nuclei. A better analogy would be a resonance in which a system can tunnel or move back and forth between two states A and B which have equal energies. The corresponding rate equations are <br/>
![](http://latex.codecogs.com/gif.latex?%5Cfrac%7B%5Cmathrm%7Bd%7DNa%20%7D%7B%5Cmathrm%7Bd%7D%20t%7D%3D%5Cfrac%7BNb%7D%7B%5Ctau%7D-%5Cfrac%7BNa%7D%7B%5Ctau%7D)<br/>
![](http://latex.codecogs.com/gif.latex?%5Cfrac%7B%5Cmathrm%7Bd%7DNb%20%7D%7B%5Cmathrm%7Bd%7D%20t%7D%3D%5Cfrac%7BNa%7D%7B%5Ctau%7D-%5Cfrac%7BNb%7D%7B%5Ctau%7D)<br?>
 
 （1.0）
where for simplicity we have assumed that the two types of decay are characterized by the same time constant,τ. Solve this system of equatiions for the numbers of nuclei, NA=100, NB=0, etc., and take τ=1s. Show that your numercial results are consistent with the idea that the system reaches a steady state in which NA and NB are constant. In such a steady state, the time derivatives dNA/dt and dNB/dt should vanish.

#方程的解析

假设原子的衰变方程<br/> 
![](http://latex.codecogs.com/gif.latex?%5Cfrac%7BdN%7D%7Bdt%7D%3D-%5Cfrac%7BN%7D%7B%5Ctau%7D)<br/>

 (1.1) 

对N做泰勒展开得到<br/> 
![](http://latex.codecogs.com/gif.latex?N%28%5CDelta%20t%29%3DN%280%29&plus;%5Cfrac%7BdN%7D%7Bdt%7D%5Ccdot%5CDelta%20t&plus;%5Cfrac%7B1%7D%7B2%7D%5Ccdot%5Cfrac%7Bd%5E2N%7D%7Bdt%5E2%7D%5CDelta%20t&plus;%5Ccdots)<br/> 
 
取前两项得<br/>
 
又有 <br/>
 
 （1.2） 
##再由式(1.1)得<br/>
![](http://latex.codecogs.com/gif.latex?N%28t&plus;%5CDelta%20t%29-N%28t%29%5Capprox%20N%28t%29-%5Cfrac%7B%5Cmathrm%7Bd%7D%20N%7D%7B%5Cmathrm%7Bd%7D%20t%7D%5Ccdot%20%5CDelta%20t)<br/>
题目解析<br/>

由上面分析知 令<br/>
由（1.2）知  <br/>
由（1.0）知  <br/>
同理可知  <br/>

##以下是在python中的代码模拟
[程序](https://github.com/shuaishuaimin/computationalphysics_N2014301510032/blob/master/chengxv.py)
