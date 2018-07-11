import operator
import random

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

class Dealership:
	def __init__(self, attributes):		
		self.attributes = attributes
		self.message = "Your vehicle is a {} {} from the year {}"		

	def random_vehicle(self):
		l = [random.choice(attr) for attr in self.attributes]
		return self.message.format(l[0], l[1], l[2])

attributes = [
	[
		'Ford',
		'GMC'
	],
	[
		'Supra',
		'Town Car'
	],
	[
		'1990',
		'2000'
	]
]


red_dealership = Dealership(attributes)
print (red_dealership)
print (red_dealership.random_vehicle())
