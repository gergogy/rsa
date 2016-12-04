#!/usr/bin/env python3

import exp

def fermat_test(base, prime):
	p1 = prime - 1
	
	if exp.fast(base, p1, prime) == 1:
		return True
	else:
		return False
		
def get_s_d(n):
	d = n - 1
	s = 0
	
	while not (d & 1): # addig megyünk amíg páratlan nem lesz
		d = d >> 1 # osztás kettővel
		s = s + 1 # megszámoljuk hányszor osztható kettővel
	
	return s, d

	
def miller_rabin_test(base, n, s, d):
	neg = n - 1
	m = exp.fast(base, d, n)
	# a^d kong. 1 (mod n) akkor prím, vagy
	if m == 1:
		return True

	# r {0, 1, ..., s-1}
	else:
		r = 1
		m = exp.fast(base, d, n)
		
		if m == -1 or m == neg:
			return True
			
		while r < s:
			m = exp.fast(m, 2, n)
		
			if m == -1 or m == neg:
				return True
			
			r = r + 1

	return False

def is_prime(number):
	for x in [2, 3, 5, 7, 11, 13, 17, 31, 127, 197, 241, 277, 733]:
		s, d = get_s_d(number)
		
		if not miller_rabin_test(x, number, s, d):
			return False
	
	return True
		

if __name__ == '__main__':
	print(fermat_test(12, 419))
	print(miller_rabin_test(11, 241))
	print(miller_rabin_test(15, 241))