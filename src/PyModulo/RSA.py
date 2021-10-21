from math import log, log10, floor, ceil
from random import randrange
from numpy import base_repr
import warnings

from PyModulo import *
from PyModulo.Utility import *

class RSA:
	class PublicInfo:
		def __init__(self, N, e):
			self.N=N
			self.e=e

		def get_key(self):
			return self.N, self.e

	class PrivateInfo:
		def __init__(self, p, q, d, lowerN=None):
			self.p=p
			self.q=q
			self.d=d
			self.lowerN = lowerN if lowerN else (p-1)*(q-1) 

		def get_key(self):
			return self.p, self.q, self.d, self.lowerN

	def __init__(self, NDigitRange=(20,25), priInfo=None, pubInfo=None, printDebug=False):
		if(isinstance(pubInfo,RSA.PublicInfo) and priInfo==None):
			warnings.warn("Warning, RSA with only a public key can only encrypt messages!")

		if(not isinstance(priInfo, RSA.PrivateInfo)):
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

			lowerN = (p-1)*(q-1)

			debug("p=%i digits (digits: %i=%i desired)"%(p, len(str(p)), dp), output=printDebug)
			debug("q=%i digits (digits: %i=%i desired)"%(q, len(str(q)), dq), output=printDebug)
			debug("**Found p and q (p:%i, q:%i)"%(p,q), output=printDebug)
			debug("lowerN [(p-1)*(q-1)]=%i"%lowerN, output=printDebug)

			#find d:
			while((dInfo:=get_gcd_fast(d:=randrange(1,lowerN),lowerN))["GCD"]!=1):
				pass
			debug("found d=%i and :"%d, dInfo, output=printDebug)
		else:
			p, q, d, lowerN = priInfo.get_key()
			dInfo = get_gcd_fast(d,lowerN)

		if(not isinstance(pubInfo, RSA.PublicInfo)):
			N = p*q

			debug("N=%i (digits=%i)"%(N, len(str(N))), output=printDebug)
			debug("(p-1)*(q-1):", lowerN, output=printDebug)

			e = dInfo["u"] % lowerN
			debug("Found e:",e, output=printDebug)
		else:
			N, e = pubInfo.get_key()

		self.pubInfo = RSA.PublicInfo(N,e)
		self.priInfo = RSA.PrivateInfo(p, q, d, lowerN)

	def get_info(self):
		return {"N": self.pubInfo.N, "e": self.pubInfo.e, "p": self.priInfo.p, "q":self.priInfo.q, "d": self.priInfo.d, "lowerN":self.priInfo.lowerN}

	def encrypt_message(self, m, encoder=lambda x: int(x, 36)):
		mInt = encoder(m)
		return power_mod(mInt, self.pubInfo.e, self.pubInfo.N)

	def decrypt_message(self, m, decoder=lambda x: base_repr(x,base=36)):
		mInt = power_mod(m, self.priInfo.d, self.pubInfo.N)
		return decoder(mInt)





