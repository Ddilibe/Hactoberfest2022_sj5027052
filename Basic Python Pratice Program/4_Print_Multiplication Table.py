#!/usr/bin/env python

class Multiplication:
	"""
		Class for displaying the multiplication table

		Args:
			@hori: The argument indicates the number of columns that would be shown
			@veri: The argument indicates the number of lines that would be shown

		Return:
			No Return

		Example:
			>>> import Multiplication
			>>> new_table = Multiplication(3, 5)
			>>> new_table.table()

			The multiplication table of 3 against 5

			0       0       0
			1       2       3
			2       4       6
			3       6       9
			4       8       12
			5       10      15
			>>>
			>>>
			>>> print("Testing with a string")
			>>> another_table = Multiplication("3", 4)
			>>> another_table.create()
			Traceback (most recent call last):
  			...
  			raise TypeError(error)
  			TypeError: Multiplication table needs integer for displaying table
  			>>> 
	"""
	def __init__(self, hori, veri):
		""" Initialization Class """
		error = "Multiplication table needs integer for displaying table"
		self.verify_int(hori, error)
		self.verify_int(veri, error)
		self.hori, self.veri, self.new_dictionary = hori, veri, {}

	def verify_int(self, insert, error):
		""" Method for verifing that the input is an integer """
		if not isinstance(insert, int):
			raise TypeError(error)

	def table(self):
		""" Method for displaying the table """
		print("\n\nThe multiplication table of {} against {} \n".format(self.hori, self.veri))
		if not self.new_dictionary:
			self.create()
		for i in self.new_dictionary:
			value = self.new_dictionary[i]
			value = [str(i) for i in value]
			value = "\t".join(value)
			print(f"{value}")

	def create(self):
		""" Method for filling up the dictionary and creating the table """
		for i in range(self.veri+1):
			self.new_dictionary[i] = [j*i for j in range(1, self.hori+1)]

if __name__ == '__main__':
	""" Test running the function """
	new_table = Multiplication(3, 5)
	new_table.create()
	new_table.table()
