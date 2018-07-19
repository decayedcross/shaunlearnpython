





s = "Hey there! what should this string be?"
# Length should be 20
print("Length of s =", len(s))

# First occurrence of "a" should be at index 8
print("The first occurrence of the letter a =", s.index("a"))

# Number of a's should be 2
print("a occurs {} times".format(s.count("a")))

# Slicing the string into bits
print("The first five characters are", s[:5])
print("The next five characters are", s[5:10])
print("The thirteenth character is", s[12])
print("The characters with odd index are", s[1::2])
print("The last five characters are", s[-5:])

# Convert everything to uppercase
print("String in uppercase:", s.upper())

# Convert everything to lowercase
print("String in lowercase:", s.lower())

# Check how a string starts
if s.startswith("Str"):
    print("String starts with 'Str'. Good!")

# Check how a string ends
if s.endswith("ome!"):
    print("String ends with 'ome!'. Good!")

# Split the string into three separate strings,
# each containing only a word
print("Split the words of the string: ", s.split(" "))