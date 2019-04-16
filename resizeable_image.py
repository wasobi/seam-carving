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
    		# compute the best seam dynamically (loops)
    		dynamic(gradient)
    	else:
    		# compute the best seam using the naive algorithm (recursion)
    		naive(0,0, energy)  
    	
	"""
	Remove the lowest energy seam from the image
	"""
    def remove_best_seam(self):
        self.remove_seam(self.best_seam())
    	
    """
    Calculate the lowest energy seam dynamically
    -- find the lowest adjacent energy, then add the to the total 
    energy within the vertical seam
    -- takes an image map
    """
    def dynamic (map):
    # TO-DO
<<<<<<< HEAD
    # [x]compute gradient at every pixel
    # [x]identify the lowest energy seam
    	# [x]sum of all of the energies along a path
    	# [x]find the smallest sum at the end of the path
    # [x]retrace that path back to the first pixel in the path
    	# [x]find the first pixel of the min seam
    	# [ ]retrace path
=======
    # [ ]compute gradient at every pixel
    # [x]identify the lowest energy seam
    	# [x]sum of all of the energies along a path
    	# [x]find the smallest sum at the end of the path
    # [ ]retrace that path back to the first pixel in the path	
>>>>>>> master
    
    inf = math.inf
    # _e_seam[i][j] is the energy of a given pixel
    	# energy of the pixels on the edge of the image will always be 10000
    	for i in range (self.height):
    		if i == 0:
    			i = self.height-1 #skip the first row
    		for j in range (self.width):
    		# calculate the energy seam at the current pixel
    		# right edge
<<<<<<< HEAD
    		if j == 0:
    			map[i][j] = _min(inf,map[i-1][j],map[i-1][j+1]) + map[i][j]
    		# left edge
    		elif j == self.width - 1:
    			map[i][j] = _min(map[i-1][j-1],map[i-1][j],inf) + map[i][j]
    		else:
    			map[i][j] = _min(map[i-1][j-2],map[i-1][j],map[i-1][j+1]) + map[i][j]
=======
    		if j == 0 or j == self.width - 1:
    			_e_seam[i][j] = _e_seam[i][j] + min(inf,_e_seam[i-1][j],_e_seam[i-1][j+1])
    		# left edge
    		elif j == self.width - 1:
    			_e_seam[i][j] = _e_seam[i][j] + min(_e_seam[i-1][j-1],_e_seam[i-1][j],inf)
    		else:
    			_e_seam[i][j] = _e_seam[i][j] + min(_e_seam[i-1][j-2],_e_seam[i-1][j],_e_seam[i-1][j+1])
>>>>>>> master
    
    	# locate the start of the lowest energy seam
        for j in range(self.width):
    		if map[self.height-1][j] < map[self.height-1][j+1]:
    			min_seam = map[self.height-1][j]
    		else:
    			min_seam = map[self.height-1][j+1]
    			
    	# follow the path along the lowest energy seam
    		for i range(self.height):
    			
    			
    	return gradient[self.height-1].index(min_seam)
    
    """
    Calculate the lowest energy recursively
    """
    def naive (gradient, i, j)
    	# depth first search on the gradient
    	# if left edge
    	# if right edge
    	# if last row
    	# else
    		# min(left,right,middle)
    		# get energy of current
    		# update energy (energy + min)
    return
    
    """
    Calculate the lowest energy recursively
    """
    def _naive (pixel, energy)
    
    
    return
    
    """
    Create the image gradient by calculating the energy of each pixel
    Return the image as a 2 x 2 array
    """
    def _gradient (self):
    	# initialize an energy map (filled with zeros)
    	gradient = np.zeros((self.width,self.height),dtype = np.int)
    	for i in range (self.height):
    		for j in range (self.width):
    			# calculate the energy of a pixel
    			gradient[i][j] = self.energy(i,j)
    	# return the gradient of the image
    	return gradient
    	
	"""
	Find and return the minimum energy
	"""
    def _min (a,b,c):
    	if a < b and a < c:
    		return a
    	elif a > b and b < c:
    		return b
    	else:
    		return c


