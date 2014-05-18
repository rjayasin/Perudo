import random
import probability

players = raw_input("How many players? :")
timeRolled = int(players)*5

def populateDiceList():
	dice = []
	for x in range(int(timeRolled)):
		gen = random.randrange(1, 500)
		dice.append(gen)
	return dice

rolls = populateDiceList();
print rolls
this = probability.randomIndex(rolls)
print "random index " + str(this)

# print len(rolls) , " many rolls"

# print rolls
# print rolls[0:5]
# print rolls[5:10]
# print rolls[10:15]

