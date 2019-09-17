class Hero:

	def __init__(self, name, health):
		self.name 	= name
		self.health = health


class Hero_intellegent(Hero):
	pass

lina = Hero("mas212", 100)
dev = Hero_intellegent("sekolahpintar", 90)
print(lina.name)
print(dev.__dict__)