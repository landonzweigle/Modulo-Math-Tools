#! /usr/bin/python
# -*- coding: utf-8 -*-

from PyModulo.Utility import *

def is_congruent(a,b, n):
	return (a-b%n)==0

#if i is negative returns i%n. 
#if i is postitive returns i%-n.
def flipped_congruence(i, n):
	return i%(-i*n//abs(i))



def eth_root(e, c, p):
	factors = slow_factor(p)
	pTwo = p-1 if(len(factors)==0) else (factors[0]-1)*(factors[1]-1)
	gcdRes = get_gcd_fast(e, pTwo)
	if(gcdRes["GCD"]!=1):
		raise Exception("GCD(%s, %s)!=1"%(e, pTwo))
	#Ensure we have the positive inverse:
	eInverse = gcdRes["u"] % pTwo
	
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

#return g^-1 mod p
def find_inverse(g,p):
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

def get_multiplicative_order(a,p):
    if(get_gcd_fast(a,p)["GCD"]!=1):
        return []
    return [i for i in range(1,p) if (a**i)%p==1][0]

def is_primitive_root(g,p):
    return get_multiplicative_order(g,p)==p-1