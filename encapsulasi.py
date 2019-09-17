class Hero:
	def __init__(self, name, health, attackPower):
		self.__name = name
		self.__health = health
		self.__attackPower = attackPower

	def getName(self):
		return self.__name

	def getHealth(self):
		return self.__health

	def attacked(self, attackedFull):
		self.__health = attackedFull


ml = Hero("bajol", 90, 70)
print(ml.__dict__)
print(ml.getName())
print(ml.getHealth())
print(ml.attacked(10))

