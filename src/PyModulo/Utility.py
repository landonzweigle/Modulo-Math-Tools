#! /usr/bin/python
# -*- coding: utf-8 -*-

from itertools import takewhile
from random import randrange
from math import floor, log10
from enum import Enum


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
def get_primes_SOE(n=100):
	firstN = range(2,n+1)
	isPrime=[True]*(n-1)

	digDict={}

	for i,p in enumerate(firstN):
		if(isPrime[i]):
			dp=len(str(p))

			digDict[dp] = digDict.get(dp,[])+[p]

			for pTest in range(2*p,n+1,p):

				isPrime[pTest-2]=False

	return [p for pList in digDict.values() for p in pList], digDict


def checkFirstPrimes(n):
    return len(pList)!=len(list(takewhile(lambda x: n!=x, pList)))

def slow_factor(n):
	return [j for j in range(2, n//2) if n%j==0]

def is_prime(n):
	return len([False for j in range(2, n//2) if n%j==0])==0




DEFAULT_FIRST_N_PRIMES=500
PRIME_LIST, PRIME_DIGITS = get_primes_SOE(DEFAULT_FIRST_N_PRIMES)
