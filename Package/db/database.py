import sqlite3 # stap 1: importeren

import sys

import settings


SCORECOLUMNS = ("water","bos","tuin","zee")


def dicInfo(scores):
	return dict(zip(SCORECOLUMNS, scores))

	
	
def pdata():
	print(settings.DATABASE)
	print(DATABASE)


# import Classes.bird as bird

# def maakVogels():

# 	allevogels = []

# 	dbconnectie = sqlite3.connect("C:\\Users\\Stijn\\testProject\\TestDb\\birds.db") 

# 	mijncursor = dbconnectie.cursor() # Stap 3: cursor maken

# 	mijnquery = "SELECT Name_Dutch, Habitat FROM birds"

# 	mijncursor.execute(mijnquery)

# 	rows = mijncursor.fetchall()
	
# 	for row in rows:
# 		vogel = bird.bird(row[0],row[1])
# 		allevogels.append(vogel)
			

# 	dbconnectie.close()

# 	return allevogels

# def maakSpelers():

# 	allespelers = []

# 	dbconnectie = sqlite3.connect("C:\\Users\\Stijn\\testProject\\TestDb\\birds.db") 

# 	mijncursor = dbconnectie.cursor() # Stap 3: cursor maken

# 	mijnquery = "SELECT Name_Dutch, Habitat FROM birds"

# 	mijncursor.execute(mijnquery)

# 	rows = mijncursor.fetchall()
	
# 	for row in rows:
# 		vogel = bird.bird(row[0],row[1])
# 		allevogels.append(vogel)
			

# 	dbconnectie.close()

# 	return allevogels


def startScoreTable():

	spelers = geefSpelers()


	for speler in spelers:
		
		dbconnectie = sqlite3.connect("C:\\Users\\Stijn\\testProject\\TestDb\\birds.db") 

		mijncursor = dbconnectie.cursor() 

		sqlite_insert = """INSERT INTO scores
			(Player,Waterscore,Bosscore, Tuinscore, Zeescore)
			VALUES (?, 0, 0, 0,0);"""

		data_tuple = (speler,)

		mijncursor.execute(sqlite_insert,data_tuple)

		dbconnectie.commit()


		dbconnectie.close()

def clearScoreTable():

	dbconnectie = sqlite3.connect("C:\\Users\\Stijn\\testProject\\TestDb\\birds.db") 

	mijncursor = dbconnectie.cursor() 

	sqlite_insert = """DELETE FROM scores;"""

	mijncursor.execute(sqlite_insert)

	dbconnectie.commit()

	dbconnectie.close()



def dagupdate_db(name,score):
	import sqlite3
	with sqlite3.connect("C:\\Users\\Stijn\\testProject\\TestDb\\birds.db") as dbconnectie:
		mijncursor = dbconnectie.cursor()
		query = """
 		UPDATE scores set Waterscore =?,
 						Bosscore = ?,
 						Tuinscore = ?,
 						Zeescore = ?
 		WHERE Player LIKE ? 
 		"""
		
		parameters = (score[0],score[1],score[2],score[3],name)

		

		mijncursor.execute(query, parameters)

		dbconnectie.commit()

		dbconnectie.close()
	

def reset():
	clearScoreTable()
	startScoreTable()
		


def geefSpelers():

	spelers = []

	dbconnectie = sqlite3.connect("C:\\Users\\Stijn\\testProject\\TestDb\\birds.db") 

	mijncursor = dbconnectie.cursor()

	mijnquery = "SELECT Player FROM Players"

	mijncursor.execute(mijnquery)

	rows = mijncursor.fetchall()

	for row in rows:
		spelers.append(row[0])

	return spelers
	
	dbconnectie.close()



def getPlayerScore(naam):

	scores = []

	dbconnectie = sqlite3.connect("C:\\Users\\Stijn\\testProject\\TestDb\\birds.db") 

	mijncursor = dbconnectie.cursor()

	mijnquery = """
	SELECT Waterscore,Bosscore,Tuinscore,Zeescore 
	FROM scores
	WHERE Player LIKE ?
	"""

	parameters = (naam,)

	mijncursor.execute(mijnquery, parameters)

	rows = mijncursor.fetchall()

	scores = rows[0]

	op = dicInfo(scores)

	return op
	
	dbconnectie.close()


# def getVelden():


# 	dbconnectie = sqlite3.connect("C:\\Users\\Stijn\\testProject\\TestDb\\birds.db") 

# 	mijncursor = dbconnectie.cursor()

# 	PRAGMA table_info(table_name)

# 	mijnquery = "PRAGMA table_info(table_name)"

# 	mijncursor.execute(mijnquery)

# 	rows = mijncursor.fetchall()

# 	for row in rows:
# 		spelers.append(row[0])

# 	return spelers
	
# 	dbconnectie.close()





# def VogelBijSpeler(vogel):
# 	dbconnectie = sqlite3.connect("C:\\Users\\Stijn\\testProject\\TestDb\\birds.db") 

# 	mijncursor = dbconnectie.cursor()

# 	mijnquery = "SELECT Name_Dutch, Habitat FROM birds"


# def UpdatePlayerScore():

# 	dbconnectie = sqlite3.connect("C:\\Users\\Stijn\\testProject\\TestDb\\birds.db") 

# 	mijncursor = dbconnectie.cursor()

# 	mijnquery = """
	
# 	"""

# 	parameters = ("TomVogels",)


	

# 	mijncursor.execute(mijnquery)

	



# 	dbconnectie.close()
  

  	

#   	# dbconnectie.commit()
	



















