#! /usr/bin/python
# -*- coding: utf-8 -*-

from PyModulo.__init__ import *


if __name__ == "__main__":
	print(find_inverse(3,10))
	print(flipped_congruence(-5, 32), flipped_congruence(flipped_congruence(-5, 32), 32))
	print(shanks_algorithm(156, 116, 593))
	print(get_gcd_fast(423,191))
