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
import matplotlib.animation as animation

# some global variables that control
# the overall size of the stimulus in degrees
# and how many pixels per degree to use
global xDeg, yDeg, pixPerDeg
xDeg=10
yDeg=10
pixPerDeg=10

##################
#    xycoords    #
##################
def xycoords():
    '''Function generates x and y coordinates for
       use with grating/gaussian'''
    # get globals
    global xDeg,yDeg,pixPerDeg
    # setup x and y coordinates
    x = np.linspace(-xDeg/2,xDeg/2,xDeg*pixPerDeg)
    y = np.linspace(-yDeg/2,yDeg/2,yDeg*pixPerDeg)
    x,y = np.meshgrid(x,y)
    # return values
    return(x,y)

#######################
#    grating patch    #
#######################
def grating(sf=1,orient=0,phase=0):
    '''Function to generate a 2D sinusoidal grating
       Returns a 2D grating

       sf: spatial frequence in degrees
       orient: orienation in degrees
       phase: phase in degrees

       Example:
       z,x,y = simple.grating()
       fig = plt.figure()
       ax = fig.add_subplot(111)
       ax.imshow(z,cmap="gray")'''
    # get x,y coords
    x,y = xycoords()
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
def gaussian(xStd=1,yStd=1,xCenter=0,yCenter=0,minVal=0.01):
    '''Function to generate a 2D gaussian
       Returns a 2D gaussian

       xStd, yStd: Std in degrees
       xCenter, yCenter: Center of gaussian in degres
       minVal: Clipping value so that gaussian goes to zero (otherwise values are always some small number)

       Example:
       z,x,y = simple.gaussian()
       fig = plt.figure()
       ax = fig.add_subplot(111)
       ax.imshow(z,cmap="gray")'''
    # get x,y coords
    x,y = xycoords()
    # compute 2D gaussian
    z = np.exp(-(((x-xCenter)**2)/(2*(xStd**2))+((y-yCenter)**2)/(2*(yStd**2))))
    # clip out small values so that we can fade completely to gray
    z = (z<minVal).choose(z,0)
    # return values
    return(z)

#######################
#    spot stimulus    #
#######################
def spot(xCenter=0,yCenter=0,xWidth=1,yWidth=1,spotColor=1):
    '''Function to make a square spot
       Returns a 2D image with spot at defined location
       
       xCenter,yCenter: Position of square spot in degrees
       xWidth,yWidth: Size of square spot in degrees
       spotColor: Color of spot (1 for white, -1 for black)
       
       Example:
    z = simple.spot()
    fig = plt.figure()
    ax = fig.add_subplot(111)
    ax.imshow(z,cmap="gray",vmin=-1,vmax=1)'''
    # get x,y coords
    x,y = xycoords()
    # set everything to zero first
    z = np.zeros(x.shape)
    # Set a square patch to the spotColor
    z = ((x-xCenter<xWidth) & (x-xCenter>-xWidth) & (y-yCenter<yWidth) & (y-yCenter>-yWidth)).choose(z,spotColor)
    # return z
    return(z)

################
#    imshow    #
################
def imshow(im):
    '''Displays the image in an inline plt using matplotlib
    im should be a 2D array of values between -1 and 1

    Example:
    gabor = simple.gaussian()*simple.grating(orient=30)
    simple.imshow(gabor)'''
    # set up figure
    fig = plt.figure()
    ax = fig.add_subplot(111)
    ax.axis('off')
    # display image with gray colormap interpeting values as between -1 and 1
    ax.imshow(im,cmap="gray",vmin=-1,vmax=1)

#######################
#    makeAnimation    #
#######################
class makeAnimation(object):
    '''make an animation object that can be used to display a 3D set of images where
       the z-dimension is frames of movie

       example:
       nFrames = 50;
       iFrame = 0;
       driftingGrating = np.zeros((100,100,nFrames))
       for iPhase in np.linspace(0,360,nFrames):
           driftingGrating[:,:,iFrame] = simple.grating(phase=iPhase)
           iFrame = iFrame+1
       a = makeAnimation(driftingGrating)
       plt.show()'''
    # initialize the animation with a 3D sequence of images
    def __init__(self,imseq):
        # keep the 3D image sequence
        self.imseq = imseq
        # number of frames
        self.nFrames = imseq.shape[2]
        # first frame = is 0
        self.frameNum = 0
        # put up figure
        self.fig = plt.figure()
        ax = self.fig.add_subplot(111)
        ax.axis('off')
        # draw the first image
        self.im = plt.imshow(imseq[:,:,self.frameNum],cmap="gray",vmin=-1,vmax=1)
        # start the animation
        self.ani = animation.FuncAnimation(self.fig,self.update,interval=50,blit=True)
    # update function
    def update(self,*args):
        # update frame number
        self.frameNum = (self.frameNum + 1) % self.nFrames
        # and display image
        self.im.set_array(self.imseq[:,:,self.frameNum])
        return(self.im)


