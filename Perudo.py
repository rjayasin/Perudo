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
	data = Counter(inputList)
	return data.most_common(1)

def countAces(inputList):
	return inputList.count(1)

def removeAces(inputList):
	return [value for value in inputList if value != 1]


players = raw_input("How many players? :")
timeRolled = int(players)*5

rolls = populateDiceList();
print rolls

print removeAces(rolls)


print countAces(rolls)

# this = probability.randomIndex(rolls)
# print "random index " + str(this)
# print len(rolls) , " many rolls"
# print rolls
# print rolls[0:5]
# print rolls[5:10]
# print rolls[10:15]

