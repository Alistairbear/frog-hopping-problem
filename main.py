probabilityTable = []

# the function f is not used, it was my first attempt at solving the problem
# I thought I'd leave it in as if it was my working out
def f(n, jumps):
	if n == 1:
		return 1
	elif n == 0:
		return 1
	else:
		result = 0
		for i in range(0, n):
			result  += f(i, jumps + 1) * jumps
		result = result / n
		return result

# this is a working solution (as far as I can tell)
def f2(currentProbability, n, jumps):
	global probabilityTable
	if n == 0:
		# when at the bottom of a probability branch, add the probability to the relevant total
		probabilityTable[jumps] += currentProbability
	else:
		for i in range(0, n):
			f2(currentProbability / n, i, jumps + 1)

def printTable(probabilityTable):
	for i in range(0, len(probabilityTable)):
		print(str(i) + " | ", end="")
	print()
	for i in range(0, len(probabilityTable)):
		print("====", end="")
	print()
	for i in range(0, len(probabilityTable)):
		print(str(probabilityTable[i]) + " | ", end="")
	print()

# shows calculated probabilities from 5 to 29 (takes a long time to calculate all of them, not sure exactly how long)
for i in range(5, 30):
	probabilityTable = [0.0] * (i + 1) # initialise a float array of length i
	print("for n = " + str(i))
	f2(1, i, 0)

	result = 0 # result is the expected value
	for i in range(0, len(probabilityTable)):
		result += i * probabilityTable[i]
	print("expected value = " + str(result))
	
