#Exercise_10: The Solar System
##We begin with the simplest situation,a sun and a single planet,and investigate a few of the properties of this model solar system.
##According to Newton's law of gravitation the magnitude of the force is given by<br/>

![](http://latex.codecogs.com/gif.latex?F_%7BG%7D%3D%5Cfrac%7BGM_%7BS%7DM_%7BE%7D%7D%7Br%5E%7B2%7D%7D)<br/>
##and we can obtain that:<br/>

![](http://latex.codecogs.com/gif.latex?%5Cfrac%7B%5Cmathrm%7Bd%7D%20v_%7Bx%7D%7D%7B%5Cmathrm%7Bd%7D%20t%7D%3D-%5Cfrac%7BGM_%7BS%7DM_%7BE%7Dx%7D%7Br%5E%7B3%7D%7D)<br/>

![](http://latex.codecogs.com/gif.latex?%5Cfrac%7B%5Cmathrm%7Bd%7Dx%7D%7B%5Cmathrm%7Bd%7D%20t%7D%3Dv_%7Bx%7D)<br/>

![](http://latex.codecogs.com/gif.latex?%5Cfrac%7B%5Cmathrm%7Bd%7Dv_%7By%7D%7D%7B%5Cmathrm%7Bd%7D%20t%7D%3D-%5Cfrac%7BGM_%7Bs%7Dy%7D%7Br%5E%7B3%7D%7D)<br/>

![](http://latex.codecogs.com/gif.latex?%5Cfrac%7B%5Cmathrm%7Bd%7Dy%7D%7B%5Cmathrm%7Bd%7D%20t%7D%3Dv_%7By%7D)<br/>
##and if we use astronomical units ,AU; and measure time in years, we find
![](http://latex.codecogs.com/gif.latex?GM_%7BS%7D%3Dv%5E%7B2%7Dr%3D4%5Cpi%20AU%5E%7B2%7D/yr%5E%7B2%7D)
##we next convert the equations of motion into difference equations in preparation for constructing a computational solution.We find

![](http://latex.codecogs.com/gif.latex?v_%7Bx%2Ci&plus;1%7D%3Dv_%7Bx%2Ci%7D-%5Cfrac%7B4%5Cpi%20%5E%7B2%7Dx_%7Bi%7D%7D%7Br_%7Bi%7D%5E%7B3%7D%7D%5CDelta%20t)<br/>

![](http://latex.codecogs.com/gif.latex?x_%7Bi&plus;1%7D%3Dx_%7Bi%7D&plus;v_%7Bx%2Ci&plus;1%7D%5CDelta%20t)<br/>

![](http://latex.codecogs.com/gif.latex?v_%7By-i&plus;1%7D%3Dv_%7By%2Ci%7D-%5Cfrac%7B4%5Cpi%5E2y_%7Bi%7D%7D%7Br_%7Bi%7D%5E%7B3%7D%7D%5CDelta%20t)<br/>

![](http://latex.codecogs.com/gif.latex?y_%7Bi&plus;1%7D%3Dy_%7Bi%7D&plus;v_%7By%2Ci&plus;1%7D%5CDelta%20t)<br/>

##and I imitate it by python ,and I gained that:
![](http://upload-images.jianshu.io/upload_images/3771733-3ed067606e468e7c.png?imageMogr2/auto-orient/strip%7CimageView2/2)
##Earth Orbiting the Sun

[code1](https://github.com/shuaishuaimin/computationalphysics_N2014301510032/blob/master/code1.py)

##we can use the animation of matplotlib to gain the cartoon,
##add follow codes:
[CODE2](https://github.com/shuaishuaimin/computationalphysics_N2014301510032/blob/master/CODE2%2Cpy)

##we get follow gif
![](http://upload-images.jianshu.io/upload_images/3771733-96110bd661cebad6.png?imageMogr2/auto-orient/strip%7CimageView2/2)
##Earth Orbiting the Sun
##If we consider the reduced mass
![](http://latex.codecogs.com/gif.latex?%5Cmu%20%3D%5Cfrac%7Bm_%7B1%7Dm_%7B2%7D%7D%7Bm_%7B1%7D&plus;m_%7B2%7D%7D)<>br/
##The orbital trajectory for a body of reduced mass is given in polar coordinates by
![](http://latex.codecogs.com/gif.latex?%5Cfrac%7B%5Cmathrm%7Bd%5E%7B2%7D%7Dt%20%7D%7B%5Cmathrm%7Bd%7D%20t%5E%7B2%7D%7D%28%5Cfrac%7B1%7D%7Br%7D%29&plus;%5Cfrac%7B1%7D%7Br%7D%3D-%5Cfrac%7B%5Cmu%20r%5E%7B2%7D%7D%7BL%5E%7B2%7D%7DF%28r%29)

###consider

![](http://latex.codecogs.com/gif.latex?%5Ctheta%20_%7B0%7D%3D0)

###we have
![](http://latex.codecogs.com/gif.latex?r%3D%28%5Cfrac%7BL%5E%7B2%7D%7D%7B%5Cmu%20GM_%7Bs%7DM_%7BP%7D%7D%29%5Cfrac%7B1%7D%7B1-ecos%5Ctheta%20%7D)


###so
![](http://latex.codecogs.com/gif.latex?v_%7Bmax%7D%3D%5Csqrt%7BGM_%7Bs%7D%7D%5Csqrt%7B%5Cfrac%7B%281&plus;e%29%7D%7Ba%281&plus;e%29%7D%281&plus;%5Cfrac%7BM_%7BP%7D%7D%7BM_%7BS%7D%7D%29%7D)<br/>
![](http://latex.codecogs.com/gif.latex?v_%7Bmin%7D%3D%5Csqrt%7BGM_%7Bs%7D%7D%5Csqrt%7B%5Cfrac%7B%281-e%29%7D%7Ba%281&plus;e%29%7D%281&plus;%5Cfrac%7BM_%7BP%7D%7D%7BM_%7BS%7D%7D%29%7D)<br/>

##Then let us suppose that the gravitational force is of the form
![](http://latex.codecogs.com/gif.latex?F_%7BG%7D%3D-%5Cfrac%7BGM_%7BS%7DM_%7BE%7D%7D%7Br%5E%7B3%7D%7D)

###then I get

![](http://latex.codecogs.com/gif.latex?v_%7Bx%2Ci&plus;1%7D%3Dv_%7Bx%2Ci%7D-%5Cfrac%7B4%5Cpi%20%5E%7B2%7Dx_%7Bi%7D%7D%7Br_%7Bi%7D%5E%7B%5Cbeta%20&plus;1%7D%7D%5CDelta%20t)<br/>

![](http://latex.codecogs.com/gif.latex?x_%7Bi&plus;1%7D%3Dx_%7Bi%7D&plus;v_%7Bx%2Ci&plus;1%7D%5CDelta%20t)<br/>

![](http://latex.codecogs.com/gif.latex?v_%7By%2Ci&plus;1%7D%3Dv_%7By%2Ci%7D-%5Cfrac%7B4%5Cpi%20%5E%7B2%7Dx_%7Bi%7D%7D%7Br_%7Bi%7D%5E%7B%5Cbeta%20&plus;1%7D%7D%5CDelta%20t)<br/>

![](http://latex.codecogs.com/gif.latex?y_%7Bi&plus;1%7D%3Dy_%7Bi%7D&plus;v_%7By%2Ci&plus;1%7D%5CDelta%20t)<br/>

###the picture
![](http://upload-images.jianshu.io/upload_images/3771733-b3c8d1a70c5f3c83.png?imageMogr2/auto-orient/strip%7CimageView2/2)

Beta=3.0 t=0.3yr v=1.7pi.png
![](http://upload-images.jianshu.io/upload_images/3771733-9bb9b0c44f39e2fe.png?imageMogr2/auto-orient/strip%7CimageView2/2)
Beta=2.5，t=1.5yr,v=1.7pi.png
![](http://upload-images.jianshu.io/upload_images/3771733-96110bd661cebad6.png?imageMogr2/auto-orient/strip%7CimageView2/2)
Beta=2.3,t=10yr,v=1.7pi.png


[CODE3](https://github.com/shuaishuaimin/computationalphysics_N2014301510032/blob/master/CODE3.py)
##then we get the animation
![](http://upload-images.jianshu.io/upload_images/3771733-e8b560da4bb803ae.gif?imageMogr2/auto-orient/strip)
Beta=3.0,v=2.0pi,t=200yr
##updating,just wait for a moment
