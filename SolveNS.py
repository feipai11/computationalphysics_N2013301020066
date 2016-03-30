##!/public/usrs/liuhj6/anaconda/bin/python

import numpy as np
import time

class SolveNS:
	
	def Init(self, nnodes, x_min, x_max, nlevel):
		
		self.nnodes = nnodes
		self.x_min = x_min
		self.x_max = x_max
		self.step = float(x_max - x_min) / nnodes

		#Calculate all the nodes
		self.x = np.zeros(nnodes)
		self.x[0] = x_min
		for ix in range(1,self.nnodes):
			self.x[ix] = self.x[ix-1] + self.step

		#Initialize the Hamiltonian
		self.Ham = np.zeros([nnodes, nnodes])

		#Set the first n level which needs to be calculated
		self.nlevel = nlevel

		self.CalHam()
		self.SolveEnAndWave()

	def Poten(self,x):
		##Calculate the Potential
		#############################################
		# one dimentional infinite potential
		#if( x==self.x_min or x==self.x_max ):
	    #	return 10000
		#else:
		#	return 0.0
		#############################################

		#############################################
		# one dimentional harmonic potential
		return 0.5*x**2
		#############################################

	def CalHam(self):

		#Calculate the Hamiltonian matrix
		self.Ham[0,0] = 1.0/self.step**2 + self.Poten(self.x[0])
		self.Ham[0,1] = -0.5*self.step**2
		self.Ham[self.nnodes-1,self.nnodes-2] = -0.5*self.step**2
		self.Ham[self.nnodes-1,self.nnodes-1] = 1.0/self.step**2 + self.Poten(self.x[-1])

		for inodes in range(1,self.nnodes-2):
			for jnodes in range(3):
				self.Ham[inodes, inodes] = 1.0/self.step**2 + self.Poten(self.x[inodes])
				self.Ham[inodes, inodes-1] = -0.5 / self.step**2
				self.Ham[inodes, inodes+1] = -0.5 / self.step**2
				
	def SolveEnAndWave(self):
		
		# Solve the eigenvalues and wavefunctions
		self.eig, self.wave = np.linalg.eig(self.Ham)

		# Store the wavefunction to output
		wave = np.zeros([self.nnodes,self.nlevel+1])

		# save the original eigvalues: keep the original order to find the correct wavefunction
		eig = self.eig
		# Convert to list to use the function eig.index(eig) to locate the index
		eig = eig.tolist()

		# Sort the eigenvalues
		self.eig.sort()

		print "  The first %d eigenvalues :" % self.nlevel
		nlevel = min(self.nlevel, self.nnodes)
		for ilevel in range(nlevel):
			print " %8.4f " % self.eig[ilevel] ,
		print 

		# build the eig list
		wave[:,0] = self.x
		for ilevel in range(1,nlevel+1):
			index = eig.index(self.eig[ilevel])
			wave[:,ilevel:ilevel+1]=self.wave[:,index:index+1]
	
		np.savetxt('wavefun.dat',wave,fmt='%12.6f',delimiter='')

start = time.clock()
mySolve = SolveNS()
mySolve.Init(2000, -10, 10, 10)
finish = time.clock()
print "  Elapsed time %12.6f s" % (finish - start)
