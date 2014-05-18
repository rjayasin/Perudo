import random

def randomIndex(allRolls):
	x = random.randrange(1, len(allRolls)+1)
	print "Index:" + str(x)
	return allRolls[x]
