class Property:

	def __init__(self, name):
		self.name = name

	@property
	def infoWork(self):
		return self.name 

list = Property("mas212")
print(list.infoWork)
	
