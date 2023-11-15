
SORTKEY = {'water':0,
			'bos':1,
			'tuin':2,
			'zee':3}


scores = {'tuin':10,
			'zee':20,
			'bos':30,
			'water':40}

lijst = []


		
for key, value in scores.items():
			lijst.append((key,value))

print(lijst)			
		


lijst.sort(key=lambda entry: SORTKEY[entry[0]])

print(lijst)

print(lijst[3][1])

# personen = [ ("Jan", 172), ("Fatima", 165), ("Igor", 168), ("Rune", 176), ("Anja",
# 174)]
# naam = lambda persoon: persoon[0]
# lengte = lambda persoon: persoon[1]
# personen = sorted(key=naam, reverse=True)

# print(personen)


# student_tuples = [
#     ('john', 'A', 15),
#     ('jane', 'B', 12),
#     ('dave', 'B', 10),
# ]

# ftie = lambda student: student[2]

# sorted(student_tuples, key=ftie) 

# print(student_tuples)
