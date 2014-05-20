import random

def randomIndex(allRolls):
	x = random.randrange(1, len(allRolls)+1)
	print "Index:" + str(x)
	return allRolls[x]

def probOfWin(allRolls):
	for x in range (1, 11):
		atLeastSome = (((1 - (2.0/3.0)**len(allRolls)))*100)/x
		#2/3 probability because 2/6 outcomes = win
		print "The probability of at least " + str(x) + " winning die is " + str(atLeastSome) + "%."