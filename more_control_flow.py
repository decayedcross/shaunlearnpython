#4.1
### NOTES ###

# if - statement is used for conditional execution
# elif - not required in if statement, can be more than 1, short for else if.
# else - not required in if statement

x = 420

if x == 420:
	print('blaze it')
elif x == 1252:
	print('ninja blaze')
elif x == 2:
	print('TWOOO CHAINS')
else:
	print('this is a SHIT number, GTFO')



#4.2
### NOTES ###

#for - loops through the content of a given list or string

four_point_two = ['lesson', 'four', 'point', 'two']

for length in four_point_two:
	print(length, 'is', len(length), 'characters long')


#4.3
### NOTES ###

#range - if you need a range of numbers in a list or string, it may bheave as a list but it is not


#We say such an object is iterable, that is, suitable as a target for functions and constructs that expect something from which they can obtain successive items until the supply is exhausted. 
# We have seen that the for statement is such an iterator. The function list() is another; it creates lists from iterables:

for four_point_three in range(len(four_point_two)):
	print(four_point_three, (four_point_two[four_point_three]))


#4.4 (first version)
#for blaze in range(415, 421):
#	if blaze == 420:
#		print(blaze, 'blaze it')
#		break
#	else:
#		print(blaze, 'is a usless number')


#4.4
### NOTES ###

#break - break the loop
#continue - after finding w/e you want in the and make an action continue con through the loop

for blaze in range(415, 423):
	if blaze == 421:
		print(blaze,'we\'ve gone to far')
		break
	else:
		if blaze == 420:
			print(blaze, 'blaze it')
			continue
		print(blaze, 'is a usless number')

#4.4 (elif version)
for blaze in range(415, 423):
	if blaze == 421:
		print(blaze,'we\'ve gone to far')
		break
	elif blaze == 420:
		print(blaze, 'blaze it')
		continue
	print(blaze, 'is a usless number')

#4.5

#pass - skip


#4.6
def fib(n):    # write Fibonacci series up to n
    """Print a Fibonacci series up to n."""
    a, b = 0, 1
    while a < n:
        print(a, end=' ')
        a, b = b, a+b
    print()

# Now call the function we just defined:
fib(2000)

def blaze(a, b):
	for blaze in range(a, b):
		if blaze == 421:
			print(blaze,'we\'ve gone to far')
			break
		else:
			if blaze == 420:
				print(blaze, 'blaze it')
				continue
			print(blaze, 'is a usless number')

c = blaze(415, 423)






#def introduces a function and must allways be followed by the function name and parenthesized with any parameters inside the paranthasieze 

#The first statement of the function body can optionally be a string literal; this string literal is the function’s documentation string, or docstring. 


#The execution of a function introduces a new symbol table used for the local variables of the function. 
#More precisely, all variable assignments in a function store the value in the local symbol table; whereas variable references first look in the local symbol table, 
#then in the local symbol tables of enclosing functions, then in the global symbol table, and finally in the table of built-in names. 
#Thus, global variables cannot be directly assigned a value within a function (unless named in a global statement), although they may be referenced.

#The actual parameters (arguments) to a function call are introduced in the local symbol table of the called function when it is called; 
#thus, arguments are passed using call by value (where the value is always an object reference, not the value of the object). [1] 
#When a function calls another function, a new local symbol table is created for that call.

#A function definition introduces the function name in the current symbol table.
# The value of the function name has a type that is recognized by the interpreter as a user-defined function. 
# This value can be assigned to another name which can then also be used as a function. This serves as a general renaming mechanism:



#The return statement returns with a value from a function. return without an expression argument returns None. Falling off the end of a function also returns None.
#The statement result.append(a) calls a method of the list object result. 
#A method is a function that ‘belongs’ to an object and is named obj.methodname, where obj is some object (this may be an expression),
# and methodname is the name of a method that is defined by the object’s type. Different types define different methods.
#  Methods of different types may have the same name without causing ambiguity. (It is possible to define your own object types and methods, using classes, see Classes) 
#  The method append() shown in the example is defined for list objects; it adds a new element at the end of the list.
#   In this example it is equivalent to result = result + [a], but more efficient.