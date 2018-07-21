from hello_world import String

number = 16
second_number = 0
first_array = [1,2,3]
second_array = [1,2]

p = String()

if number > 15:
    p.printer("1")

if first_array:
    p.printer("2")

if len(second_array) == 2:
    p.printer("3")

if len(first_array) + len(second_array) == 5:
    p.printer("4")

if first_array and first_array[0] == 1:
    p.printer("5")

if not second_number:
    p.printer("6")