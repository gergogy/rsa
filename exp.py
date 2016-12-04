#!/usr/bin/env python3
	
def fast(base, exp, mod):
	n = 1
	
	while exp:
		if exp & 1: # szorzás csak 2 hatványai esetén
			n = n * base % mod
			
		exp = exp >> 1
		base = base * base % mod # az eredményt mindig négyzetre kell emelni és modulo mod
	
	return n


if __name__ == '__main__':
	print("test fast")
	print(fast(12, 418, 419))
	print(fast(11, 15, 241))
	print(fast(129, 97, 171))
	