#! /usr/bin/python
# -*- coding: utf-8 -*-

from PyModulo.Utility import *
import warnings

def is_congruent(a, b, n):
	return ((a-b)%n)==0

#if i is negative returns i%n. 
#if i is postitive returns i%-n.
def flipped_congruence(i, n):
	return i%(-i*n//abs(i))

#yeah its that simple... Probably should enfore just using a%n but whatever.
def abs_congruence(a, n):
	return a%n

def eth_root(e, c, p, debug=False):
	factors = slow_factor(p)
	pTwo = p-1 if(len(factors)==0) else (factors[0]-1)*(factors[1]-1)
	gcdRes = get_gcd_fast(e, pTwo)
	if(gcdRes["GCD"]!=1):
		raise Exception("GCD(%s, %s)!=1"%(e, pTwo))
	#Ensure we have the positive inverse:
	eInverse = gcdRes["u"] % pTwo

	if(debug):
		print("Factors: %s \npTwo: %s \neInverse: %s"%(factors,pTwo,eInverse))

	return power_mod(c, eInverse, p)


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

def rand_n_digit_prime(n, amnt=1):
	digMin = 10**(n-1)
	digMax = 10**(n)-1

	oddRange=(digMax-digMin)//2

	failed=[]
	primes=[]
	foundPrimes=0
	while(foundPrimes!=amnt):
		#generate only odd numbers:
		p = 2*randrange(0, oddRange+1)+digMin+1
		if(p not in failed and miller_rabin(p)):
				foundPrimes+=1
				primes.append(p)
		else:
			failed.append(p)

	return (primes if amnt>1 else primes[0]) if len(primes) > 0 else None

def miller_rabin(p, nTrials=25):
	q=p-1
	k=0
	while(q%2==0):
		q>>=1
		k+=1

	if(q%2==0):
		return False

	for i in range(nTrials):
		a = randrange(2, p)

		if(is_congruent(power_mod(a, q, p),1,p)==False):
			satisfies=True
			for j in range(k):
				aPow=power_mod(a,2**j * q, p)

				if(is_congruent(aPow,-1,p)==True):
					satisfies=False
					break

			if(satisfies):
				return False
	return True


#return g^-1 mod p
def find_inverse(g,p):
	return get_gcd_fast(g,p)["u"]

def power_mod(g,e,p):
	expBin = bin(e)[2:]

	if(e<0):
		gcdInfo = get_gcd_fast(g,p)
		if(gcdInfo["GCD"]!=1):
			raise Exception("e (%i) is negative, but g (%i) does not have an inverse mod p (%i)."%(e,g,p))
		else:
			g = gcdInfo["u"]

	lastExp = g
	_ret = 1 if expBin[-1]=="0" else lastExp
	for b in reversed(expBin[:-1]):
		lastExp = (lastExp**2) % p
		if(b=='1'):
			_ret = (_ret * lastExp) % p

	return _ret

def get_multiplicative_order(a,p):
    if(get_gcd_fast(a,p)["GCD"]!=1):
        return []
    return [i for i in range(1,p) if (a**i)%p==1][0]

def is_primitive_root(g,p):
    return get_multiplicative_order(g,p)==p-1
