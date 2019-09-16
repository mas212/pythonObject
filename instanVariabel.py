class Hero:
	#class variabel
	jumlah = 0

	def __init__(self, inputName, inputPower, inputArmor, inputHealth):
	    #instant variabel
		self.inputName = inputName
		self.power 	   = inputPower
		self.armor 	   = inputArmor
		self.health    = inputHealth
		Hero.jumlah += 1
		print("nama na adalah", inputName)

	def getName(self):
		return self.inputName

	def getHealth(self, up):
		self.health = up
		return self.health

hero1 = Hero("mas212", "90", "80", "30")
print(Hero.jumlah)
print(hero1.inputName + " power " + hero1.power + " armor" + hero1.armor + " health " + hero1.health)
print(hero1.getName())
print(hero1.getHealth(100))