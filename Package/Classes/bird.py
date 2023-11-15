class bird:
	def __init__(self, naam, habitat):
		self.__naam = naam # private
		self.__habitat = habitat
	
	def get_naam(self): # getter voor brand
		return self.__naam
	
