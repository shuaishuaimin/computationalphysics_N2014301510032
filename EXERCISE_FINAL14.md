#TOTAL:The random walk model: the drunkard and diffusion
##                                                                                                                          陈有民2014301510032
##The summery：

There are many random process in nature. It's often known as a kind of many-body problem. We know that many-body problem can be simplified to a mean-field mathod or solved by statistic method. Actually, random process is can be determinate in microscopes, but we don't bother to solve all the motions of internal particles. Because we can understand the physics in the process in macroscopes, as well as it's easy to solve if we adopt the statistics mathod. Here, a one-dimensional random model was calculated, and we can get some useful conclusion.

##The psudocode：

As a random model, how to generate a series of random number is very important. Fortunately, python-numpy can generate random number through the function 'np.random.random()'. This time I didn't use class to complete the work. It's just an operation on a 500x100 array, but his next position being linked with the last position. That's the only rule we should obey.

##The result:

·first, we have learned that diffusion can be explained by randon walk model no matter it is a atom diffusion or electron and ion diffusion. We have a gineral conclusion that  ,where the x is the average farest distance an atom diffused at time t. So a one-dimensional random walk have been done,and this is the result: 
![](https://www.zybuluo.com/feipai11/note/404621)
We can easily find that the squre distance is directly proportional to the time, that is exactly the diffusion theory tell us. In this progrem, I make 500 sample to do this experimental, that is the statistic average od the distance. Well, now we can say the diffusion is actually the random walk of the part icles. The driven force of the motions is the entrapy.
·Second, a one-dimensional walk with different probability(0.25 go left and 0.75 go right) are also simulated. And this is the result: 
![](https://www.zybuluo.com/feipai11/note/404621)
WOW! The realtion is diffrernt at all: the distance is directly proportional to the time, and the square distance is quadratic to the time! with the probability different in different direction, we say that there is a external field so particles have a mean velocity in a direction, this model can explain the motions of particles in a external field(such as election in electric field) with resistance. Actually this is not an diffusion at all. The driven force of the motions is the external field.
##The conclusion:

This pragram modeled the motion of a drunkard, and gained the relation between the random walk model and the diffusion. And we find that electric current can be explained by the random walk model with different probability in different directions.


##[program](https://github.com/shuaishuaimin/computationalphysics_N2014301510032/blob/master/program.py)
