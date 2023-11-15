import db.database as db
import Classes.players as players



def reset():
	db.clearScoreTable()
	db.startScoreTable()



def makeAllPlayers():
	Spelers = []
	lijstSpelers = db.geefSpelers()
	for naam in lijstSpelers:
		scores = db.getPlayerScore(naam)
		

		speler = makePlayer(naam,scores)
		Spelers.append(speler)
	return Spelers	





def makePlayer(name,scores):
	lijst = players.orderscores(scores)
	speler = players.player(name,lijst[0],lijst[1],lijst[2],lijst[3])
	return speler


	


