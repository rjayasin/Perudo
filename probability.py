import random

def randomIndex(allRolls):
	x = random.randrange(1, len(allRolls)+1)
	print "Index:" + str(x)
	return allRolls[x]

def probOfWin(allRolls, threshold):
	for x in range (1, 21):
		probNow = ((1 - (2.0/3.0)**(len(allRolls)-5))*100)/x
		probNext = ((1 - (2.0/3.0)**(len(allRolls)-5))*100)/(x + 1)
		#2/3 probability because 2/6 outcomes = win
		#Will definitely revise the above probability calculations later. 
		# print ("The probability of at least " + str(x) 
		# 		+ " winning die is " + str(probNow) + "%.")
		if threshold > probNext: #this condition doesn't have to be compound!
			return x
