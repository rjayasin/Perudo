import random

def randomIndex(allRolls):
	x = random.randrange(1, len(allRolls)+1)
	print "Index:" + str(x)
	return allRolls[x]

def probOfWin(allRolls):
	atLeastOne = ((1 - (2.0/3.0)**len(allRolls)))*100
	print "The probability of at least one ??? is " str(atLeastOne)