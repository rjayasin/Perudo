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
	data = Counter(inputList)	#Kind of a dict, [(number, occurrances)] 
	for x, y in data.most_common(1): 
		return x #this will return only the mode itself

def countAces(inputList):
	return inputList.count(1)

def removeAces(inputList):
	return [value for value in inputList if value != 1]


players = raw_input("How many players? :")	
timeRolled = int(players)*5

rolls = populateDiceList();
print rolls
print "Aces removed " + str(removeAces(rolls))
print "# of aces: " + str(countAces(rolls))
rollsNoAces = removeAces(rolls)
print "The mode without aces is " + str(returnMode(rollsNoAces))


# this = probability.randomIndex(rolls)
# print "random index " + str(this)
# print len(rolls) , " many rolls"
# print rolls
# print rolls[0:5]
# print rolls[5:10]
# print rolls[10:15]

