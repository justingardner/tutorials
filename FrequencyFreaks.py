# Functions from FrequencyFreaks Colab notebook to use in other notebooks
# See: https://colab.research.google.com/drive/1Yxj-Cld8uV3uNQ28WNcgH0udZVqJbdgy?usp=sharing

def getMeshPoints(nPoints):
    # first create a linearly spaced set of x and y points between -1 and 1
    x = np.linspace(-1,1,nPoints)
    y = np.linspace(-1,1,nPoints)
    
    # keep the extents for use with imshow
    extents = [np.min(x),np.max(x),np.min(y),np.max(y)]

    # now create the mesh of x and y (these will now both be 2D matrices of x and y values)
    x, y = np.meshgrid(x, y, indexing='xy')

    # and return the computed values
    return x, y, extents

# function that makes a gaussian
def makeGaussian(x,y,sigma):
    # there it is!
    gaussian = np.exp(-(x**2+y**2)/(2*sigma**2))
    
    # return 
    return gaussian

# function to make a grating
def makeGrating(x, y, orientation, spatialPhase, spatialFrequency):
    # we wil convert orientation and spatialPhase into radians
    orientation = np.pi*orientation/180
    spatialPhase = np.pi*spatialPhase/180

    # we need to convert spatial frequency into cycles/image
    # remember that we made the extents in getMeshPoints
    # to go from -1 to 1, so we want that to go from -pi to pi
    spatialFrequency = spatialFrequency * np.pi

    # make the grating
    grating = np.cos(spatialFrequency*(x*np.cos(orientation)+y*np.sin(orientation))+spatialPhase)

    # and return
    return grating

