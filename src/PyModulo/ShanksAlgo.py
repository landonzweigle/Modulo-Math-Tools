#!/usr/bin/env python3.8
import sys

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

#a = setEntry(2,5)
#b = setEntry(2,7)
#print(a)
#print(a==b)
#print(a)

def find_inverse(g,p):
	#algorithm described in HPS 1.12
	def get_gcd_fast(a,b):
		u,g,x,y=1,a,0,b
		while(y!=0):
			q=g//y
			t=g%y
			s=u-(q*x)
			u,g=x,y
			x,y=s,t
		v=(g-(a*u))//b
		return {"GCD":g,"u":u,"v":v}
	return get_gcd_fast(g,p)["u"]

def power_mod(g,e,p):
	expBin = bin(e)[2:]
	#print(e, expBin[:-1])
	lastExp = g

	_ret = 1 if expBin[-1]=="0" else lastExp
	for b in reversed(expBin[:-1]):
		lastExp = (lastExp**2) % p
		if(b=='1'):
			_ret = (_ret * lastExp) % p
	return _ret

testMod=power_mod(3,129, (2**89)-1)
#print("Fast Exponent: %i"%testMod) 

def main(g, h, p):
	print("G:%s, H:%s, and P:%s "%(g, h, p))
	N = p - 1
	n = 1 + int(N**(1/2))
	print("n:", n)

	gInverse = find_inverse(g,p)
	print("g inverse = %s"%gInverse)

	L = [setEntry(power_mod(g,(i+1),p),i) for i in range(n)]
	M = [setEntry((h*power_mod(gInverse,n*(i+1),p))%p,i) for i in range(n)]
	print(L,M,sep='\n')

	intersec = set(L).intersection(M)
	print(intersec)

	mIdxs=setEntry.intersec[0]
	print("Intersection indexes: %s and %s"%(mIdxs.indexes[0],mIdxs.indexes[1]))

	x = (mIdxs.indexes[0]+1) + n*(mIdxs.indexes[1]+1)
	return x


if __name__ == "__main__":
	print("----------------MAIN----------------")
	hasArgs = (len(sys.argv)==4)
	g = int(sys.argv[1]) if hasArgs else 11
	h = int(sys.argv[2]) if hasArgs else 21
	p = int(sys.argv[3]) if hasArgs else 71
	x = main(g,h,p)
	print("DONE:")
	print("%i^(%i) ≡ %i mod %i"%(g,x,h,p))
