class Basic_String:
	def __init__(self):
		pass

	def printer(self, message, s):
		print(message, s)
		return
	
	def form_printer(self, message, a):
		print(message.format(s.count(a)))

s = "Hey there! what should this string be?"


p = Basic_String()

# Length should be 20
p.printer("Length of s =", len(s))

# First occurrence of "a" should be at index 8
p.printer("The first occurrence of the letter a =", s.index("a"))

# Number of a's should be 2
p.form_printer("a occurs {} times" , "a")

# Slicing the string into bits
p.printer("The first five characters are", s[:5])
p.printer("The next five characters are", s[5:10])
p.printer("The thirteenth character is", s[12])
p.printer("The characters with odd index are", s[1::2])
p.printer("The last five characters are", s[-5:])

# Convert everything to uppercase
p.printer("String in uppercase:", s.upper())

# Convert everything to lowercase
p.printer("String in lowercase:", s.lower())

# Check how a string starts
if s.startswith("Str"):
    print("String starts with 'Str'. Good!")
    p.printer("String starts with 'Str'. Good!")

# Check how a string ends
if s.endswith("ome!"):
    print("String ends with 'ome!'. Good!")
    p.printer("String in lowercase:", s.lower())

# Split the string into three separate strings,
# each containing only a word
p.printer("Split the words of the string: ", s.split(" "))