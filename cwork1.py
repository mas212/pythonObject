#==================
#static & class
#===================
class Cwork1:
	location = ''
	def __init__(self, location):

		self.location   = location

	def getLocation(self):
		return self.location

	@staticmethod
	def getPrice(price):
		return str(price)

work = Cwork1("ubud")
priceAll = work.getPrice(1000)
print(priceAll)
print(work.getLocation())
