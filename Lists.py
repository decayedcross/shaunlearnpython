#In this exercise, you will need to add numbers and strings to the correct lists using the "append" list method. You must add the numbers 1,2, and 3 to the "numbers" list, and the words 'hello' and 'world' to the strings variable.

#You will also have to fill in the variable second_name with the second name in the names list, using the brackets operator []. Note that the index is zero-based, so if you want to access the second item in the list, its index will be 1.


class List:
	def __init__(self):
		pass	

	def app(self, l, value):		
		l.append(value)
		return l		

	def second_names(self, l):		
		self.message = "The second name on the names list is {}"	
		second_name = self.select_index(l, 1)
		return self.message.format(second_name)

	def select_index(self, l, index):
		return l[index]

names = [
	"John", "Eric", "Jessica"
]

numbers = []

string = []


# write your code here

a = List()

names = a.select_index(names, 1)

second_name = a.second_names(names)

numbers = a.app(numbers, 1)
numbers = a.app(numbers, 2)
numbers = a.app(numbers, 3)

string = a.app(string, "hello")
string = a.app(string, "world")

print(second_name)
print(numbers)
print(string)




