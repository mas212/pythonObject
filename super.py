class Hero:
	def __init__(self, name, health):
		self.name 	= name
		self.health = health

	def getHealth(self): 
		print("{} hallo: {} ".format(self.name, self.health))


class Hero_itellegent(Hero):
	def __init__(self, name):
	    #fungsi super artinya mengambil fungsi kelas super 
		super().__init__(name, 100)
		super().getHealth()

class Hero_streng(Hero):
	def __init__(self, name):
		super().__init__(name, 77)

hari = Hero_itellegent("mas")
axa  = Hero_streng("jack")
