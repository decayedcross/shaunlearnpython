import operator

class Calc:
	def __init__(self, name):
		self.name = name
		self.my_message = '{} your answer is {}'
		self.ops = {
			"+":operator.add,
			"-":operator.sub,
			"*":operator.mul,
			"/":operator.truediv
		}

	def calculate(self, op, num_one, num_two):
		return self.my_message.format(self.name, self.ops[op](num_one, num_two))

my_calc_class = Calc('Shaun')

answer_one = my_calc_class.calculate('/', 1, 2)
print (answer_one)