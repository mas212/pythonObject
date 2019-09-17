class Hero:

	#private class variabel
	__jumlah = 0;

	def __init__(self, name):
		self.name = name
		Hero.__jumlah += 1

	#method ini hanya berlaku pda object

	def getJumlah(self):
		return Hero.__jumlah 

	#method tidak berlaku pada object
	def getJumlah1():
		return Hero.__jumlah

	#method static (decorator)

	def getJumlah2():
		return Hero.__jumlah

sniper = Hero("jacmac")
print(Hero.getJumlah2())
