#!/usr/bin/env python3

import exp
import gcd
import prime
import random
import rsa_string as STR
import codecs
import base64
import time

global hardness
global p
global q
global e
global phi_n
global d
global PK
global SK
global state
global sys_rand

def definitions():
	global hardness, menu, e, sys_rand, state
	
	hardness = 1536
	e = 65537
	state = 0
	menu = [
		'generate_primes',
		'generate_keys',
		'enc',
		'enc_string',
		'dec',
		'dec_string',
		'test',
		'show',
		'exit'
	]
	sys_rand = random.SystemRandom()


def calculate_phi_n():
	global phi_n, p, q
	
	phi_n = (p-1) * (q-1)

	
def calculate_d():
	global phi_n, d, e
	
	d = gcd.extended(phi_n, e)[4]
	
	if d < 0:
		d = d % phi_n

		
def get_odd_random_number():
	global hardness, sys_rand
	
	a = sys_rand.getrandbits(hardness)
	
	while not (a & 1):
		a = sys_rand.getrandbits(hardness)

	return a

	
def generate_primes():
	global p, q, state, hardness
	
	print("Bitlength:", hardness)
	print("Generate p...")
	start = time.time()
	a = get_odd_random_number()
	
	while not prime.is_prime(a):
		a = get_odd_random_number()
	print("%s seconds" % (time.time()- start))
	print("Generate q...")
	start = time.time()
	b = get_odd_random_number()
	
	while a == b or not prime.is_prime(b):
		b = get_odd_random_number()
	
	print("%s seconds" % (time.time()- start))
	p, q = a, b
	
	state = 1

	
	
def check_state():
	global state
	
	if not state:
		print('please generate primes...')
		return False
	elif state == 1:
		print('please generate keys...')
		return False
		
	return True

	
def generate_keys():
	global p, q, PK, SK, d, e, state
	
	if not state:
		print('please generate primes...')
		return
	
	print("Calculate n...")
	n = p * q
	
	print("PK done")
	PK = (n, e)
	
	print("Calculate phi(n)...")
	calculate_phi_n()
	
	print("Calculate d...")
	calculate_d()
	
	print("SK done")
	SK = (n, d)
	
	state = 2
	
def encrypt(m):
	global PK
	
	if not check_state():
		return
	
	return exp.fast(m, PK[1], PK[0])

	
def decrypt(c):
	global p, q, SK
	
	if not check_state():
		return
	
	e1 = SK[1] % (p - 1)
	c1 = exp.fast(c, e1, p)
	e2 = SK[1] % (q - 1)
	c2 = exp.fast(c, e2, q)
	
	ext = gcd.extended(p, q)
	
	return (c1 * ext[4] * q + c2 * ext[3] * p) % SK[0]
	
	
def print_menu():
	global menu
	
	print("Commands:")
	for item in menu:
		print(" >", item)
	
def navigation():
	global menu

	while True:
		print_menu()
		
		item = str(input("> "))
		
		if item in menu:
			eval(item + "()")

			
def show():
	global p, q, phi_n, PK, SK
	
	if not check_state():
		return
	
	print("p:", p)
	print("q:", q)
	print("PK:", PK)
	print("SK:", SK)
	print("phi_n:", phi_n)

	
def enc_string():
	global PK
	
	if not check_state():
		return
	
	ptext = str(input("Message: "))
	size = STR.modSize(PK[0])
	output = []
	
	while ptext:
		nbytes = min(len(ptext), size - 1)
		aux1 = STR.text2Int(ptext[:nbytes])
		assert aux1 < PK[0]
		aux2 = exp.fast(aux1, PK[1], PK[0])
		output += STR.int2List(aux2, size + 2)
		ptext = ptext[size:]
	
	s = str(base64.b64encode(bytearray(STR.get_hex_string(output), 'utf8')))[2:-1]
	
	print("Encrypted message:")
	print(s)

	
def dec_string():
	global SK, p, q
	
	if not check_state():
		return
	
	ctext = STR.hex_to_int(base64.b64decode(input("Encrypted message: ")))
	size = STR.modSize(SK[0])
	output = ""
	
	while ctext:
		aux3 = STR.list2Int(ctext[:size + 2])
		assert aux3 < SK[0]
		c1 = exp.fast(aux3, SK[1] % (p - 1), p)
		c2 = exp.fast(aux3, SK[1] % (q - 1), q)
		ext = gcd.extended(p, q)
		aux4 = (c1 * ext[4] * q + c2 * ext[3] * p) % SK[0]
		output += STR.int2Text(aux4, size)
		ctext = ctext[size + 2:]
	
	print("Message:")
	print(output)

	
def enc():
	
	if not check_state():
		return
	
	message = int(input("Number: "))
	
	print("Encrypted number:")
	print(encrypt(message))


def dec():
	
	if not check_state():
		return
	
	message = int(input("Encrypted number: "))
	
	print("Number:")
	print(decrypt(message))


def test():
	global p, q, e
	
	p = int(input("p: "))
	q = int(input("q: "))
	e = int(input("e: "))
	generate_keys()

	
if __name__ == '__main__':
	definitions()
	navigation()
	
	
	
	
	
