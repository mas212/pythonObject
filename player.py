#=====
# Class & Object
#=====
class Player:
	name = "harri"
	age = ''

	def getName(self):
		return self.name

	def getAge(self, age):
		self.age = age
		return self.age

#call Object
ball = Player()
ball_name = ball.getName()
print(ball_name)

ball_age = ball.getAge('12')
print(ball_age)
