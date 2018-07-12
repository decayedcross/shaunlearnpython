class VariablesAndTypes:
	def __init__ (self, mystring, myfloat, myint):
		self.mystring = mystring
		self.myfloat = myfloat
		self.myint = myint
		return 	


mystring = "hello"
myfloat = 10.0
myint =  20

fullstring = VariablesAndTypes("hello", 10.0, 20)



# testing code
if mystring == "hello":
    print("String: " + mystring)
if isinstance(myfloat, float) and myfloat == 10.0:
    print("Float: " + myfloat)
if isinstance(myint, int) and myint == 20:
    print("Integer: " + myint)


   