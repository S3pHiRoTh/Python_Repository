"""
- Project : Py Calculate (Py_Calculate_Main.py)
- Project description : A simple calculator program.
- Language : Python
- Coded by : A.Taylor
- Coder Name : S3pHiRoTh
"""

#	Import python's operator module
import operator as op
from sys import exit

class Calc(object) :
	operands = {'+' : op.add, '-' : op.sub, '*' : op.mul,
						'/' : op.floordiv}
		
	def __init__(self) :
		self.title("\n\n\t\t Py Calculate. By S3pHiRoTh (A.Taylor)\n\n")
		self.main(0)
		
	def title(self, title) :
		print(title)
		return
		
	def main(self, j= 0) :
		while(j != 1):
			a = int(input("Enter your first integer for your sum : "))
			b = int(input("Enter your second integer for your sum : "))
			op = input("Now choose your operator (+,-,* or /) : ")
			calc_sum = self.operands[op]
			output = calc_sum(a, b)
			print("\nThe answer to your sum is %i \n"%(output))
			q = input("Would you like to quit Py Calculate? Or Calculate another sum? (y to quit the program or n to continue) : ")
			if(q == "y"):
				j = 1
				input("Thanks for using Py Calculate! Press enter to continue.")
				exit()
			elif(q == "n"):
				c = Calc()
		
class runapp(object) :
	
	def __init__(self) :
		self.call_class()
		
	def call_class(self) :
		i = Calc()		
		