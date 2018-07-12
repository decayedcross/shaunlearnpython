class VariablesAndTypes:
	def __init__(self):
		pass

	def is_string(self, s):
		if isinstance(s, str):
			return '{} is a string'.format(s)
		else:
			return '{} is not a string'.format(s)

	def is_float(self, f):
		if isinstance(f, float):
			return '{} is a float'.format(f)
		else:
			return '{} is not a float'.format(f)

	def is_int(self, i):
		if isinstance(i, int):
			return '{} is a int'.format(i)
		else:
			return '{} is not a int'.format(i)

vat = VariablesAndTypes()

my_string = vat.is_string('Hello')
my_float = vat.is_float(10.0)
my_int = vat.is_int(20)

print (my_string)
print (my_float)
print (my_int)

my_not_string = vat.is_string(20)
my_not_float = vat.is_float('Hello')
my_not_int = vat.is_int(10.0)

print (my_not_string)
print (my_not_float)
print (my_not_int)