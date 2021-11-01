from math import sqrt, ceil, floor
from PyModulo import *
from itertools import count
import warnings

def pollard_factor(N, maxkBound=20, maxaBound=20, aStart=2, printLatex=None):
	a = aStart

	for i in range(maxaBound+1):
		a = aStart+i
		for j in range(2,maxkBound+1):
			a = power_mod(a,j,N)
			d = gcd_info(a-1,N)["GCD"]

			if(printLatex!=None):
				print("$%i^{%i!} - 1 \\equiv %i \\text{ mod %i}$ &  GCD($%i^{%i!} - 1$, N) = %i \\\\ \\hline"%(aStart+i,j,(a-1)%N, N, aStart+i,j, d) if printLatex else "%i^{%i!} - 1 = %i mod %i => GCD(a-1, N) = %i"%(aStart+i,j,(a-1)%N, N, d))

			if(d%N==0):
				break
			elif( 1 < d and d < N):
				return d, N//d
			elif(j==maxkBound):
				return


def square_factor(N, maxK=1000):
	sqrtN = ceil(sqrt(N))

	for k in (range(maxK+1) if maxK else count(start=1)):
		#print(k)
		altN = (sqrtN+k)**2
		iPow = altN-N
		i = sqrt(iPow)

		if(i==int(i)):
			print(iPow)
			if(iPow!=floor(i)**2):
				warnings.warn("Precision error. Returning nothing.")
				return
			return int((sqrtN+k)+i), int((sqrtN+k)-i)
