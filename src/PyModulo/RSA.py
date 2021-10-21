from math import log, log10, floor, ceil
from random import randrange
from numpy import base_repr

from PyModulo import *
from PyModulo.Utility import *

class RSA:
	class PublicInfo:
		def __init__(self, N, e):
			self.N=N
			self.e=e

	class PrivateInfo:
		def __init__(self, p, q, d):
			self.p=p
			self.q=q
			self.d=d

	def __init__(self, NDigitRange=(20,25), printDebug=False):
		minDig, maxDig = NDigitRange

		dnMin, dnMax = (ceil((minDig+1)/2), floor((maxDig+1)/2))
		debug(dnMin, dnMax, output=printDebug)

		diff = dnMax-dnMin
		debug("diff:", diff, output=printDebug)

		#the number of digits in the first number:
		dp = randrange(dnMin,dnMax+diff+1)
		p = rand_n_digit_prime(dp)

		#the number of digits in the second number:
		dq =randrange(dnMin,dnMax*2-dp+1)
		q = rand_n_digit_prime(dq)

		debug("p=%i digits (digits: %i=%i desired)"%(p, len(str(p)), dp), output=printDebug)
		debug("q=%i digits (digits: %i=%i desired)"%(q, len(str(q)), dq), output=printDebug)

		debug("**Found p and q (p:%i, q:%i)"%(p,q), output=printDebug)

		N=p*q

		debug("N=%i (digits=%i)"%(N, len(str(N))), output=printDebug)

		barN = (p-1)*(q-1)
		debug("(p-1)*(q-1):", barN, output=printDebug)
		#find e:
		#e = randrange(1,barN)
		while((gcdE:=get_gcd_fast(e:=randrange(1,barN),barN))["GCD"]!=1):
			pass

		d = gcdE["u"]
		debug("Found e:",e, output=printDebug)
		debug("e info:",gcdE, output=printDebug)
		debug("d (e inverse):", d, output=printDebug)

		self.pubInfo = RSA.PublicInfo(N,e)
		self.priInfo = RSA.PrivateInfo(p,q,d)

	def get_info(self):
		return {"N": self.pubInfo.N, "e": self.pubInfo.e, "p": self.priInfo.p, "q":self.priInfo.q, "d": self.priInfo.d}

	def encrypt_message(self, m, encoder=lambda x: int(x, 36)):
		mInt = encoder(m)
		return power_mod(mInt, self.priInfo.d, self.pubInfo.N)

	def encrypt_message(self, m, decoder=lambda x: base_repr(x)):
		mInt = power_mod(m, self.priInfo.d, self.pubInfo.N)
		return decoder(mInt, 36)





