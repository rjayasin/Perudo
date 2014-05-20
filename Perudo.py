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

#aces in Perudo are wildcards, the number 1 
def countAces(inputList):
	return inputList.count(1)

def removeAces(inputList):
	return [value for value in inputList if value != 1]

def handSlicing(allRolls, playerNum):
	#what a painful sounding function name!
	return allRolls[((playerNum-1)*5):(playerNum*5)]


players = raw_input("How many players? :")	
timeRolled = int(players)*5

rolls = populateDiceList();
print rolls
for x in range(1, int(players)+1):
	print "Player " + str(x) + "\'s hand: " + str(handSlicing(rolls, x))


print "Aces removed " + str(removeAces(rolls))
print "# of aces: " + str(countAces(rolls))
# rollsNoAces = removeAces(rolls)
# handMode, handModeTimes = returnMode(rollsNoAces)
# print "The mode without aces is " + str(handMode) + ", " + str(handModeTimes) + " times."
# probability.probOfWin(rolls)


