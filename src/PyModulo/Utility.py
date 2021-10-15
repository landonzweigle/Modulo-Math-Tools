#! /usr/bin/python
# -*- coding: utf-8 -*-

def get_primes(n=100):
    _ret = []
    for i in range(2,n+1):
        if(is_prime(i)):
            _ret.append(i)
    return _ret

def slow_factor(n):
    return [j for j in range(2, n//2) if n%j==0]

def is_prime(n):
    return len([False for j in range(2, n//2) if n%j==0])==0
