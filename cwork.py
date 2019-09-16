class Cwork:
	location = ''
	price 	 = ''

	def __init__(self, location, price):

		self.location   = location
		self.price 		= price

	def getLocation(self):
		return self.location

	def getPrice(self):
		return self.price

class Fasilitas(Cwork):
	def setFasilitas(self, fasilitas_name):
		self.fasilitas_name = fasilitas_name
		return self.fasilitas_name


working = Fasilitas("Ubud", "1000.000")
print(working.getLocation() +
	 " this price per hours " 
	 + working.getPrice() +
	  " Fasilitas "
	 + working.setFasilitas("internet"))
