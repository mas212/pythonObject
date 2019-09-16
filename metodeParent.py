class Cwork:
	location = ''

	def __init__(self, location):

		self.location   = location

	def getLocation(self):
		return self.location

class Fasilitas(Cwork):
	def setFasilitas(self, fasilitas_name):
		self.fasilitas_name = fasilitas_name
		return self.fasilitas_name



working = Fasilitas("Ubud")
print(working.getLocation() +
	 " this price per hours " 
	 + working.setFasilitas("internet"))
