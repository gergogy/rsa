#!/usr/bin/env python3

def simple(a, b):
	while b:
		a, b = b, a % b
		
	return a

def extended(a, b):
	k = 0
	r_old = a
	r = b
	x = 0
	x_old = 1
	y = 1
	y_old = 0
	
	while r != 0:
		q = r_old // r
		x_old, x = x, x * q + x_old
		y_old, y = y, y * q + y_old
		r_old, r = r, r_old % r
		k = k + 1
	
	if k & 1:
		X = (-1) * x_old
		Y = y_old
	else:
		X = x_old
		Y = (-1) * y_old
	
	return r_old, x_old, y_old, X, Y
	
	
if __name__ == '__main__':
	case = (1, 26, 1987, -26, 1987)
	
	print("extended(a, b) = (gcd, xi, yi, X, Y)")
	print ("Test: extended(49140, 643) =", case)
	print("Test passed:", case == extended(49140, 643))
	print(extended(13,7))
	
	