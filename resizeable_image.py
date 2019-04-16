import imagematrix
from array import *

class ResizeableImage(imagematrix.ImageMatrix):
    def best_seam(self, dp=True):
    	best = {}
    	if dp=True:
    		best = dynamic (self)
    	else:
    		_naive ()
        

    def remove_best_seam(self):
        self.remove_seam(self.best_seam())
    	
    
    def dynamic (self):
    		# energy of the pixels on the edge of the image will always be 10000
    	for i in range (self.height):
    		for j in range (self.width):
    		# compute gradient at every pixel
    		# create energy map
    		# identify the lowest energy seam
    			# sum of all of the energies along a path
    			# find the smallest sum at the end of the path
    			# retrace that path back to the first pixel in the path	
    
    
    """
    Create the image gradient by calculating the energy of each pixel
    Return the image as a 2 x 2 array
    """
    def _gradient (self,i):
    	gradient = []
    	for i in range (self.height):
    		for j in range (self.width):
    			# calculate the energy of each pixel
    			# return the gradient of the image
    	return gradient
    	
	"""
	Find and return the minimum energy
	"""
    def min (a,b,c):
    	if a < b and a < c:
    		return a
    	elif a > b and b < c:
    		return b
    	else:
    		return c