#! /usr/bin/python
# -*- coding: utf-8 -*-

from itertools import takewhile
from random import randrange
from math import floor, log10, sqrt
from enum import Enum
from collections import defaultdict

class COLORS(Enum):
    RED="\033[31m"
    GREEN="\033[32m"
    BLUE="\033[34m"
    WHITE="\033[37m"
    BLACK="\u001b[38;5;16m"
    ORANGE="\u001b[38;5;178m"

def debug(msg="", color=None, output=True):
	if(output):
		if(color != None and not isinstance(color, COLORS)):
			raise Exception("Debug expected color but %s was given."%type(color))
		else:
			if(color!=None):
				color=color.value
				end="\033[0m"
			else:
				color=""
				end=""
		print("%s%s%s"%(color,msg,end))



def get_primes_naive(n=100):
	_ret = []
	for i in range(2,n+1):
		if(is_prime(i)):
			_ret.append(i)
	return _ret

#Implements the Sieve of Eratosthenes.
#returns a list of primes, and a dict, where the key is the number of digits and the value is a list of primes with that many digits.
def get_primes_SOE(n=100, retFull=True, retDict=False):
	if(not retFull and not retDict):
		raise Exception("get_primes_SOE argument error: one of retFull or retDict must be true. If both are false nothing will be returned.")

	firstN = range(2,int(sqrt(n))+1)
	isPrime=[True]*(n-1)

	for i,p in enumerate(firstN):
		if(isPrime[i]):
			for pTest in range(p**2,n+1,p):
				isPrime[pTest-2]=False

	primes = [i+2 for i, prime in enumerate(isPrime) if prime]

	if(retDict):
		digDict = defaultdict(int)
		for p in primes:
			digDict[len(str(p))]+=1
		if(retFull):
			return primes, digDict
		else:
			return digDict
	elif(retFull):
		return primes


def check_first_primes(n):
    return len(PRIME_LIST)!=len(list(takewhile(lambda x: n!=x, PRIME_LIST)))

def slow_factor(n):
	return [j for j in range(2, n//2) if n%j==0]

def is_prime(n):
	return len([False for j in range(2, n//2) if n%j==0])==0


DEFAULT_FIRST_N_PRIMES=500
PRIME_LIST, PRIME_DIGITS = get_primes_SOE(DEFAULT_FIRST_N_PRIMES, retDict=True)
