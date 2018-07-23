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

#for - loops through the content of a given list or string in numerical order, starting with 0

four_point_two = ['lesson', 'four', 'point', 'two']

for length in four_point_two:
	print(length, 'is', len(length), 'characters long')


#4.3
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



	Python’s for statement iterates over the items of any sequence (a list or a string), in the order that they appear in the sequence. For example (no pun intended):

If you need to modify the sequence you are iterating over while inside the loop (for example to duplicate selected items), it is recommended that you first make a copy. 
Iterating over a sequence does not implicitly make a copy. The slice notation makes this especially convenient:

