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

def makeGaussian(x,y,sigma):
  # there it is!
  gaussian = np.exp(-(x**2+y**2)/(2*sigma**2))
  
  # return 
  return gaussian

def makeGrating(x, y, orientation,spatialFrequency):
  # we wil convert orientation into radians
  orientation = np.pi*orientation/180

  # we need to convert spatial frequency into cycles/image
  # remember that we made the extents in getMeshPoints
  # to go from -1 to 1, so we want that to go from -pi to pi
  spatialFrequency = spatialFrequency * np.pi

  # make the grating
  grating = np.cos(spatialFrequency*(x*np.cos(orientation)+y*np.sin(orientation)))

  # and return
  return grating
 def getImage(filename,imageSize):
  # first load the image
  img = iio.imread(filename)

  # make graycale by averaging across color dimensions
  img = img.mean(2)

  # get a square of the image
  imgSquareSize = np.min(img.shape);
  img =img[0:imgSquareSize,0:imgSquareSize]

  # interpolate to preferred size 
  fun = interpolate.interp2d(np.linspace(0,1,imgSquareSize),np.linspace(0,1,imgSquareSize),img,kind='linear')
  img = fun(np.linspace(0,1,imageSize),np.linspace(0,1,imageSize))

  # normalize values to between -1 and 1
  # just because this is a typical and easy way to 
  # think about values of an image 0 is gray -1 is black and 1 is white
  # just like for a sinewave grating!
  img = (img - img.min())/(img.max() - img.min())
  img = 2 * img - 1

  # return the image
  return img 