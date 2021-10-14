#!/usr/bin/env python
# coding: utf-8

def is_prime(n):
    return len([False for j in range(2, n) if n%j==0])==0

def get_primes(n=100):
    _ret = []
    for i in range(2,n+1):
        if(is_prime(i)):
            _ret.append(i)
    return _ret

def get_multiplicative_order(a,p):
    if(get_gcd_fast(a,p)["GCD"]!=1):
        return []
    return [i for i in range(1,p) if (a**i)%p==1][0]

def is_primitive_root(g,p):
    return get_multiplicative_order(g,p)==p-1

def all_primitive_roots(p):
    unitsPMinusOne=0
    primitiveRoots=[]

    for g in range(1,p):
        if(is_primitive_root(g,p)):
            primitiveRoots.append(g)
        if(g<p and get_gcd_fast(g,p-1)["GCD"]==1):
            unitsPMinusOne+=1
    return {"PRIMITIVE_ROOTS":primitiveRoots, "UNITS(p-1)":unitsPMinusOne}


def search_primes_with_primitive_root(a,n=100):
    root_primes=[]
    primes=get_primes(n)
    for prime in primes:
        if(a<prime and is_primitive_root(a,prime)):
            root_primes.append(prime)
    return root_primes 

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



def main():
	roots229 = all_primitive_roots(229)
	print("There are %i Primitive Roots Modulo 229 being %s [%i=φ(228)=%i]"%(len(roots229["PRIMITIVE_ROOTS"]),roots229["PRIMITIVE_ROOTS"],len(roots229["PRIMITIVE_ROOTS"]), roots229["UNITS(p-1)"]))

	twoPrimitivePrimes = search_primes_with_primitive_root(2)
	print("for every prime less than 100, 2 is a primitive root of these: %s"%twoPrimitivePrimes)   

	threePrimitivePrimes=search_primes_with_primitive_root(3)
	print("for every prime less than 100, 3 is a primitive root of these: %s"%threePrimitivePrimes)

	fourPrimitivePrimes=search_primes_with_primitive_root(4)
	print("for every prime less than 100, 4 is a primitive root of these: %s"%fourPrimitivePrimes)


if __name__=="__main__":
	main()
