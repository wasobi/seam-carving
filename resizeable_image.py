import imagematrix
from array import *
import math

class ResizeableImage(imagematrix.ImageMatrix):
	"""
	Find the best seam
	"""
    def best_seam(self, dp=True):
    	gradient = _gradient(self)
    	if dp=True:
    		best = dynamic (gradient)
    	else:
    		# compute the best seam using the naive algorithm
    		_naive (gradient[0][0], energy)  
    	
	"""
	Remove the lowest energy seam from the image
	"""
    def remove_best_seam(self):
        self.remove_seam(self.best_seam())
    	
    """
    Calculate the lowest energy seam dynamically
    -- find the lowest adjacent energy, then add the to the total energy within the vertical seam
    -- takes an image map
    """
    def dynamic (_e_seam):
    # TO-DO
    # [ ]compute gradient at every pixel
    # [x]identify the lowest energy seam
    	# [x]sum of all of the energies along a path
    	# [x]find the smallest sum at the end of the path
    # [ ]retrace that path back to the first pixel in the path	
    
    inf = math.inf
    # _e_seam[i][j] is the energy of a given pixel
    		# energy of the pixels on the edge of the image will always be 10000
    	for i in range (self.height):
    		if i == 0:
    			i = 1 #skip the first row
    		for j in range (self.width):
    		# calculate the energy seam at the current pixel
    		# right edge
    		if j == 0 or j == self.width - 1:
    			_e_seam[i][j] = min(inf,_e_seam[i-1][j],_e_seam[i-1][j+1]) + _e_seam[i][j]
    		# left edge
    		elif j == self.width - 1:
    			_e_seam[i][j] = min(_e_seam[i-1][j-1],_e_seam[i-1][j],inf) + _e_seam[i][j]
    		else:
    			_e_seam[i][j] = min(_e_seam[i-1][j-2],_e_seam[i-1][j],_e_seam[i-1][j+1]) + _e_seam[i][j]
    
    
    """
    Create the image gradient by calculating the energy of each pixel
    Return the image as a 2 x 2 array
    """
    def _gradient (self):
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


