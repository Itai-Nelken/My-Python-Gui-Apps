#!/bin/python3

import sys

class print_color():
	def red(text):
		print("\033[31m",text,"\033[0m")
	def green(text):
		print("\033[32m",text,"\033[0m")

class errors:
	def exit(exit_code):
		sys.exit(exit_code)
	def error(text):
		print("\033[1;31m",text,"\033[0m")
		exit(1)


try:
	arg1=sys.argv[1]
except IndexError:
	errors.error("ERROR: no color provided!")
try:
	arg2=sys.argv[2]
except IndexError:
	errors.error("ERROR: no text provided!")

if arg1=="red":
	print_color.red(arg2)
elif arg1=="green":
	print_color.green(arg2)
else:
	errors.error("ERROR: invalid color!")
