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

