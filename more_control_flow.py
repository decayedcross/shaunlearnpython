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


