#encapsulation
#private variable c and can be accessed within class and its derivatives only
#protected variable d and can be accessed within class and its derivatives only and are accessed with classcall._className__variableName
class India(): 
	def __init__(self):
		self.a="hello"
		self._c="hey"
		self.__d="namaste"

obj=India()
print(obj.a)
print(obj._c)
print(obj._India__d)

   
  	
