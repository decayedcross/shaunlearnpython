#The target of this exercise is to create two lists called x_list and y_list, which contain 10 instances of the variables x and y, respectively. 
#You are also required to create a list called big_list, which contains the variables x and y, 10 times each, by concatenating the two lists you have created.


class Operations:
	def __init__(self):
		pass

	def x(self, x_number):		
		return [object()] * x_number

	def add_list(self, a_list, b_list):
		return a_list + b_list

# TODO: change this code

basic = Operations()

x_list = basic.x(10)
y_list = basic.x(10)

big_list = basic.add_list(x_list, y_list)

print(x_list, "\n \n",  y_list, "\n \n", big_list)
