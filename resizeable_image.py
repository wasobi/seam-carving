import imagematrix
from array import *
import math

class ResizeableImage(imagematrix.ImageMatrix):
    def best_seam(self, dp=True):
    	best = {}
    	if dp=True:
    		best = dynamic (self)
    	else:
    		_naive ()
        

    def remove_best_seam(self):
        self.remove_seam(self.best_seam())
    	
    
    def dynamic (self,seam):
    inf = math.inf
    
    _e_seam = []
    i = 2 # start at the second row
    		# energy of the pixels on the edge of the image will always be 10000
    	for i in range (self.height):
    		for j in range (self.width):
    		#calculate the energy seam at the current pixel
    		if j == 0:
    			_e_seam[i][j] = min(inf,j,j+1)
    		elif j == self.width - 1:
    			_e_seam[i][j] = min(j-1,j,inf)
    		else:
    			_e_seam[i][j] = min(j-1,j,j+1)
    		
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


