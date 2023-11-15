import db.database as db

SORTKEYDB = {'water':0,
			'bos':1,
			'tuin':2,
			'zee':3}

SORTKEYCON = {'water':0,
			'bos':2,
			'tuin':3,
			'zee':1}

def orderscores(scores):

	print(scores)

	lijst = []
	
	for key, value in scores.items():
			lijst.append((key,value))

	lijst.sort(key=lambda entry: SORTKEYCON[entry[0]])

	lijst = (list(map(lambda tup: tup[1],lijst)))
	
	return lijst	


def orderscoresDB(scores):	
	lijst = []
	for key, value in scores.items():
		lijst.append((key,value))	

	lijst.sort(key=lambda entry: SORTKEYDB[entry[0]])

	return lijst	







class player:
	def __init__(self, naam, water=0, zee=0, bos=0, tuin=0):
		self.__naam = naam # private
		self.__scores = {
			'water': water,
			'zee' : zee,
			'bos' : bos,
			'tuin' : tuin
			}
	
	def get_naam(self): 
		return self.__naam	



	

		

		

	def get_scores(self):
		op = []
		for key, value in self.__scores.items():
			op.append((key,value))
		return op	
		

	

	def dagupdate(self):
		
		lijst = []
		for key, value in self.__scores.items():
			lijst.append((key,value))

		

		lijst.sort(key=lambda entry: SORTKEYDB[entry[0]])

		lijst = (list(map(lambda tup: tup[1],lijst)))

		db.dagupdate_db(self.__naam,lijst)



	def print_scores(self):
		lijst = orderscoresDB(self.__scores)

		op = self.__naam +"\n"
		
		for item in lijst:

			op += (item[0]+" : " + str(item[1]) + " \n")

		print(op)

	def update_scores(self,habitat,punten):
		self.__scores[habitat] = self.__scores[habitat] + punten


	
			




	



	
			
		



			


		




	