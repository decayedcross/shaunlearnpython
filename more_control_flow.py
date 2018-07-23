#4.1
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

