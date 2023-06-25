#!/usr/bin/python3
def add(a,b):
	return a + b
def sub(a,b):
	return(a - b)
def mul(a,b):
	return a * b
def div(a,b):
	if (b == 0):
		print("Error: Division by Zero")
		return
	if isinstance(a, int) and isinstance(b, int):
		return a // b
	elif isinstance(a, float) or isinstance(b, float):
		return a / b
	else:
		print("Invalid operands")
def pow(a,b):
	return a ** b

import math

print("Available Operators are: +, -, *, /, **, sin, tan, cos, log, ln, log10, log2,sqrt")
operator = input("Enter operator: ")
if operator in ["sin", "tan", "cos", "log", "ln", "log10", "log2", "sqrt"]:
	a = input("Enter number: ")
	a = float(a)
	result = 0
	if operator == "sin":
		result = math.sin(a)
	elif operator == "tan":
		result = math.tan(a)
	elif operator == "cos":
		result = math.cos(a)
	elif operator == "log":
		result = math.log(a)
	elif operator == "ln":
		result = math.ln(a)
	elif operator == "log10":
		result = math.log10(a)
	elif operator == "log2":
		result = math.log2(a)
	elif operator == "sqrt":
		result = math.sqrt(a)
	print(result)
else:
	a = input("Enter Number: ")
	b = input("Enter Number: ")
	result = 0

	try:
		if  "." in a or "." in b:
			a = float(a)
			b = float(b)
		else:
			a = int(a)
			b = int(b)
		if operator == "+":
			result = add(a, b)
		elif operator == "-":
			result = sub(a, b)
		elif operator == "*":
			result = mul(a, b)
		elif operator == "/":
			result = div(a, b)
		elif operator == "**":
			result = pow(a, b)
		else:
			print("Invalid Operator")
		print(result)
	except ValueError:
		print("Invalid Number")
