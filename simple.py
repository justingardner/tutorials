# simple.py
#
#      usage: simple
#         by: justin gardner
#       date: 03/22/16
#    purpose: library of routines for simulating simple/complex cells
#

# import necessary libraries
import matplotlib.pyplot as plt
import numpy as np

##################
#    xycoords    #
##################
def xycoords(xDeg=10,yDeg=10,pixPerDeg=10):
    '''Function generates x and y coordinates for
       use with grating/gaussian'''
    # setup x and y coordinates
    x = np.linspace(-xDeg/2,xDeg/2,xDeg*pixPerDeg)
    y = np.linspace(-yDeg/2,yDeg/2,yDeg*pixPerDeg)
    x,y = np.meshgrid(x,y)
    # return values
    return(x,y)

#####################
#    gabor patch    #
#####################
def grating(xDeg=10,yDeg=10,sf=1,orient=0,phase=0,pixPerDeg=10):
    '''Function to generate a 2D sinusoidal grating
       Returns a 2D grating

       xDeg, yDeg: Size of patch in degrees
       sf: spatial frequence in degrees
       orient: orienation in degrees
       phase: phase in degrees
       pixPerDeg: Number pixels per degree

       Example:
       z,x,y = simple.grating()
       fig = plt.figure()
       ax = fig.add_subplot(111)
       ax.imshow(z,cmap="gray")'''
    # get x,y coords
    x,y = xycoords(xDeg,yDeg,pixPerDeg)
    # phase in radians
    phase = np.radians(phase)
    # orientation weights
    orient = np.radians(orient)
    a=np.cos(orient)*sf*2*np.pi
    b=np.sin(orient)*sf*2*np.pi
    # compute 2D sinusoid
    z = np.cos(a*x+b*y+phase)
    # return values
    return(z)

########################
#    gaussian patch    #
########################
def gaussian(xDeg=10,yDeg=10,xStd=1,yStd=1,xCenter=0,yCenter=0,pixPerDeg=10,minVal=0.01):
    '''Function to generate a 2D gaussian
       Returns a 2D gaussian

       xDeg, yDeg: Size of patch in degrees
       xStd, yStd: Std in degrees
       xCenter, yCenter: Center of gaussian in degres
       pixPerDeg: Number pixels per degree
       minVal: Clipping value so that gaussian goes to zero (otherwise values are always some small number)

       Example:
       z,x,y = simple.gaussian()
       fig = plt.figure()
       ax = fig.add_subplot(111)
       ax.imshow(z,cmap="gray")'''
    # get x,y coords
    x,y = xycoords(xDeg,yDeg,pixPerDeg)
    # compute 2D gaussian
    z = np.exp(-(((x-xCenter)**2)/(2*(xStd**2))+((y-yCenter)**2)/(2*(yStd**2))))
    # clip out small values so that we can fade completely to gray
    z = (z<minVal).choose(z,0)
    # return values
    return(z)
