#!/usr/bin/env python3

import codecs
from functools import reduce

"""
VENDOR
https://jhafranco.com/2012/01/29/rsa-implementation-in-python/
"""

def text2Int(text):
	"""Convert a text string into an integer"""
	return reduce(lambda x, y : (x << 8) + y, map(ord, text))

	
def int2Text(number, size):
	"""Convert an integer into a text string"""
	text = "".join([chr((number >> j) & 0xff) for j in reversed(range(0, size << 3, 8))])
	
	return text.lstrip("\x00")

def modSize(mod):
    """Return length (in bytes) of modulus"""
    modSize = len("{:02x}".format(mod)) // 2
    return modSize
 
def int2List(number, size):
	"""Convert an integer into a list of small integers"""
	
	return [(number >> j) & 0xff for j in reversed(range(0, size << 3, 8))]
 
def list2Int(listInt):
	"""Convert a list of small integers into an integer"""
	
	return reduce(lambda x, y : (x << 8) + y, listInt)

def printHexList(intList):
	"""Print ciphertext in hex"""
	for index, elem in enumerate(intList):
		print("{:02x} ".format(elem), end = "")
		if index % 32 == 0:
			print()
	print()
	
"""
Saját kód
"""

def hex_to_int(text):
	list = [text[i:i+2] for i in range(0, len(text), 2)]
	
	return [ord(codecs.decode(x, 'hex')) for x in list]
	

def get_hex_string(list):
	return "".join(["{:02x}".format(x) for x in list])