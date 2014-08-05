import random
import probability

def populateDiceList():
	dice = []
	for x in range(int(timeRolled)):
		gen = random.randrange(1, 7)
		dice.append(gen)
	return dice

def returnMode(inputList):
	from collections import Counter
	data = Counter(inputList)	#Kind of a dict, [(number, occurrences)] 
	for x, y in data.most_common(1): 
		return (x, y) #return mode and occurrences separately
	#Unfortunately, this will only return the lowest dice value for mode. 

#aces in Perudo are wildcards, the number 1 
def countAces(inputList):
	return inputList.count(1)

def removeAces(inputList):
	return [value for value in inputList if value != 1]

def handSlicing(allRolls, playerNum):
	#what a painful sounding function name!
	return allRolls[((playerNum-1)*5):(playerNum*5)]

def isWagerTrue(aces, dieValue, dieWager, allRolls):
	actualCount = allRolls.count(dieValue)
	print "There actually were", actualCount + aces
	if dieWager <= actualCount + aces:
		verdict = True
	else:
		verdict = False
	print "This wager is", verdict


players = raw_input("How many players? : ")	
timeRolled = int(players)*5

probThreshhold = 20.00
#This translates to % in probOfWin function.
#Needs to adjust based on number of remaining dice...
rolls = populateDiceList();
print rolls
for x in range(1, int(players)+1):
	currentHand = handSlicing(rolls, x)
	handMode, handModeTimes = returnMode(removeAces(currentHand))
	acesInHand = countAces(currentHand)
	allOfTheAces = countAces(rolls)
	handTotal = acesInHand + handModeTimes
	totalWager = probability.probOfWin(rolls, probThreshhold) + handTotal
	print "Player " + str(x) + "\'s hand:", currentHand
	print "Number of aces in hand:", acesInHand
	print "This player should wager on", handMode, "which appears", handTotal, "times."
	print "My wager is", totalWager, str(handMode) + "\'s."
	isWagerTrue(allOfTheAces, handMode, totalWager, rolls)
	print "\n"
