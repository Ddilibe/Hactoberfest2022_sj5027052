#!/usr/bin/env python

class Permutation:
	"""
		Permutation class for calculating the permutation of two numbers
		This class only accepts integers

		Args:
			numa: The first Number
			numb: The second number

		Return:
			Integers

		Formular:
			1. Arrangement without replacement
				(a)P(b) = a!/(a-b)! = a(a - 1)(a - 2)...(a - b + 1)
				The equation above is read as a permutation b is a factorial
				divided by a minus b factorial
			2. Arrangement with replacement
				(a)P(b) = a^b
				The equation above is read as a permutation b is a to the power b

		Example:
			>>>	import Permutation
			>>>
			>>> print("Example 1 (without replacement) ")
			Example 1 (without replacement)
			>>>
			>>>	new = Permutation(6, 3)
			>>> new.permutate()
			120
			>>>
			>>>	print("Example 2 (with replacement) ")
			Example 2 (with replacement)
			>>>
			>>>	new = Permutation(6, 3)
			>>> new.permutate()
			216


	"""
	def __init__(self, numa, numb):
		""" Initialization Function """
		error =  "Permutation only accepts integer arguments"
		if isinstance(numa, int):
			self.numa = numa
		else:
			raise TypeError(error)
		if isinstance(numb, int):
			self.numb = numb
		else:
			raise TypeError(error)

	def numerator(self):
		""" Method for calculation the numerator """
		j = 1
		for i in range(1, self.numa+1):
			j *= i
		return j

	def denominator(self):
		""" Method for calculating the denominator """
		j, k = 1, self.numa - self.numb
		for i in range(1, k+1):
			j *= i
		return j

	def permutate(self, replace=False):
		""" Method for calculating the permutation """
		if replace:
			return int(self.numerator()/self.denominator())
		else:
			return self.numa ** self.numb

	def __str__(self):
		""" Method for giving detail about the permutation """
		return "The permutation of {} to {} is {}".\
			format(self.numa, self.numb, self.permutate())

if __name__ == '__main__':
	# Testing the new class
	new_value = Permutation(23.2, 3)
	print(new_value.numerator())
	print(new_value.denominator())
	print(new_value.permutate(replace=True))
	print(new_value)
