
#完成作业1.5

Consider again a decay problem with two types of nuclei of type A into ones of type B, while nuclei of type B, while nuclei of type B decay into ones of type A. Strictly speaking, this is not a "decay" process,since it is possible for the type B nuclei to turn back into type A nuclei. A better analogy would be a resonance in which a system can tunnel or move back and forth between two states A and B which have equal energies. The corresponding rate equations are 
 
 （1.0）
where for simplicity we have assumed that the two types of decay are characterized by the same time constant,τ. Solve this system of equatiions for the numbers of nuclei, NA=100, NB=0, etc., and take τ=1s. Show that your numercial results are consistent with the idea that the system reaches a steady state in which NA and NB are constant. In such a steady state, the time derivatives dNA/dt and dNB/dt should vanish.

#方程的解析

假设原子的衰变方程<br/>

 (1.1) 

对N做泰勒展开得到<br/> 
 
取前两项得<br/>
 
又有 <br/>
 
 （1.2） 
##再由式(1.1)得<br/>


题目解析<br/>

由上面分析知 令<br/>
由（1.2）知  <br/>
由（1.0）知  <br/>
同理可知  <br/>

##以下是在python中的代码模拟
[程序](https://github.com/shuaishuaimin/computationalphysics_N2014301510032/blob/master/chengxv.py)
