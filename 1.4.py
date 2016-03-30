#!/usr/bin/python

from pprint import pprint

def replace(s,len):
	tmp = s[:len].split(" ")
	result = ""
	for item in tmp:
		if item != "":
			result = result+item+"%20"
		
	return result[:-3]

print replace("asd fasd fadsf a sdf at  ees d fs df   sdf sdf   dasfhuadsf asdfad    asdfaesdfs    ",80)