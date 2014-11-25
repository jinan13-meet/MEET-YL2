class Animal():
	
	def __init__ (self, name, age):
		self.name = name
		self.age = age
	def dance (self, dance):
		print self.name + " " + "of" + " "+  str(self.age) + " " + "is dancing"
	def eat(self, food):
		print self.name +" " + "of" + " " + str(self.age) +" " + "is eating" +" " + food
class bird(Animal):
	def __init__(self, name, age,wings_color):
		Animal.__init__(self,name, age)
		self.wings_color = wings_color 
	
	def fly (self):
		print "bird" + " " + self.name + " " + str(self.age) + " " + self.wings_color
#class dog(Animal):
#	def __init__(self,name,age):
#	Animal.__init__(self,name,age)

#	def bark (self):




x = Animal("meet", 11)
x.dance("ballet")
y = Animal ("cat",2)
y.dance("samba")
y.eat("monkey")
z = Animal("dog", 5) 
z.eat("monkey")
l=bird("bamba", 8, "green")
l.fly()