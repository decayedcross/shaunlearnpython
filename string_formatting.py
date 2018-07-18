#You will need to write a format string which prints out the data using the following syntax: Hello John Doe. Your current balance is $53.44.


class String_Mat():
	def __init__(self):
		pass

	def fmat(self, a, b, c, d):
		return("{0} {1} {2}. Your current balance is {3}".format(a, b, c, d))



p = String_Mat()

balance = p.fmat("Hello", "John", "Doe", 53.44)	

print(balance)


print("{0} {1} {2}. Your current balance is {3}".format("Hello", "John", "Doe", 53.44))



