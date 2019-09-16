class Hero:
	def __init__(self, inputName, inputPower, inputArmor):
		self.inputName = inputName
		self.power 	   = inputPower
		self.armor 	   = inputArmor

hero1 = Hero("mas212", "90", "80")
print(hero1.inputName + " power " + hero1.power + " armor" + hero1.armor)