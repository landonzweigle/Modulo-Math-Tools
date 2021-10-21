#! /usr/bin/python
# -*- coding: utf-8 -*-

import sys
from PyModulo.PyModulo import *
#from PyModulo.Utility import *

class setEntry:
	intersec=[]
	class mIndex():
		def __init__(self, indexes):
			self.indexes=indexes
		def __repr__(self):
			return self.__str__()
		def __str__(self):
			return "%i-%i"%(self.indexes[0],self.indexes[1])

	def __init__(self, value, index):
		self.value = value
		self.index = index

	def __str__(self):
		return self.__repr__()

	def __repr__(self):
		return "%i@%s"%(self.value,self.index)

	def __hash__(self):
		return hash(self.value)

	def __eq__(self, other):
		if(self.value==other.value):
			sIdx=setEntry.mIndex([self.index, other.index])
			setEntry.intersec.append(sIdx)
			return True
		return False

def shanks_algorithm(g, h, p):
	#print("G:%s, H:%s, and P:%s "%(g, h, p))
	N = p - 1
	n = 1 + int(N**(1/2))
	#print("n:", n)

	gInverse = find_inverse(g,p)
	#print("g inverse = %s"%gInverse)

	L = [setEntry(power_mod(g,(i+1),p),i) for i in range(n)]
	M = [setEntry((h*power_mod(gInverse,n*(i+1),p))%p,i) for i in range(n)]
	#print(L,M,sep='\n')

	intersec = set(L).intersection(M)
	#print(intersec)

	mIdxs=setEntry.intersec[0]
	#print("Intersection indexes: %s and %s"%(mIdxs.indexes[0],mIdxs.indexes[1]))

	x = (mIdxs.indexes[0]+1) + n*(mIdxs.indexes[1]+1)
	return x
