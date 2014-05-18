import random

players = raw_input("How many players? :")
timeRolled = int(players)*5

def diceRoll():
	dice = []
	for x in range(int(timeRolled)):
		gen = random.randrange(1, 7)
		dice.append(gen)
	return dice

rolls = diceRoll();
print len(rolls) , " many rolls"

print rolls
print rolls[0:5]
print rolls[5:10]
print rolls[10:15]