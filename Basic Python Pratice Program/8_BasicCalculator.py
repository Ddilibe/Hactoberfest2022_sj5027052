#!/usr/bin/env python3

class Calculator:
	"""
		A Simple Calculator

		Args:
			No arguments

		Return:
			No specific returns. Look at the examples for more illustrations
	"""
	@classmethod
	def add(cls, *args):
		""" 
			Method in the simple calculator to calculate the addition
			The add method accepts a tuple of integers and floats

			Args:
				args: A tuple of values

			Return:
				(Integer) or (float)

			Example:
				>>> from Calculator import add
				>>> add(1,1)
				2
				>>>
				>>> add(32, 43)
				75
				>>>	add(23,45,2,84)
				154
		"""
		return sum(args)

	@classmethod
	def subtract(cls, *args):
		"""
			Method in the simple calculator for subtraction
			The subtract method accepts a tuple of integers and floats

			Args:
				args: A tuple of values

			Return:
				(Integer) or (float)

			Example:
				>>> from Calculator import subtract
				>>> subtract(1,1)
				0
				>>>
				>>> subtract(32, 43)
				-11
				>>>	subtract(23,45,2,84)
				-108
		"""
		if not (len(args) > 0):
			return (0)
		variable = args[0]
		for i in range(1, len(args)):
			variable -= args[i]
		return variable

	@classmethod
	def divide(cls, varia, varib):
		"""
			Method in the simple calculator for division
			The divide method accepts two arguments

			Args:
				varia: The first argument
				varib: The second argument

			Return:
				(Integer) or (Float)

			Example:
				>>> from Calculator import divide
				>>> divide(1,1)
				1
				>>>
				>>> divide(32, 43)
				0.7441860465
				>>>	divide(23,45,2,84)
				Traceback (most recent call last):
				...
				TypeError: Calculator.divide() takes 3 positional argument but 4 were given
		"""
		return (varia/varib)

	@classmethod
	def multiply(cls, *args):
		"""
			Method in the simple calculator for multiplication
			The multiply method accepts a tuple of values (Integers and floats)

			Args:
				args: A tuple of values

			Return:
				(Integer) or (float)

			Example:
				>>> from Calculator import multiply
				>>> multiply(1,1)
				1
				>>>
				>>> multiply(32, 43)
				1376
				>>>	multiply(23,45,2,84)
				173880
		"""
		if not (len(args) > 0):
			return 0
		variable = args[0]
		for i in range(1, len(args)):
			variable *= args[i]
		return variable

if __name__ == '__main__':
	new = Calculator()
	print(new.add(1,1))
	print(new.subtract(1,1))
	print(new.multiply(1,1))
	print(new.divide(1,1))
