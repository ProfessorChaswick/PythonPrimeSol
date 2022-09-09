
import time
import math
import array

def convert(seconds):
	hours = seconds / 3600
	hoursRem = seconds % 3600 # Remainder from hours calculation
	minutes = hoursRem / 60
	seconds = hoursRem % 60   # Remainder from minutes calculation
	
	strHours = "hour"			# **********************************
	if int(hours) != 1:			# Make adjustments for English grammer
		strHours = "hours"		# plural or singular given when needed
	strMinutes = "minute"
	if int(minutes) != 1:
		strMinutes = "minutes"	# **********************************

	print ("%i %s, %i %s, %.2f seconds." % (hours, strHours, minutes, strMinutes, seconds))

numArray = array.array('I')
limit = input('enter number for top limit of search ->')# User input stored as a string
limit = int(limit) # Typecast to integer
sLimit = "{:,}".format(limit)
#print (sLimit)
uLim = math.floor(math.sqrt(limit))
#avoid squares of primes reporting as prime
uLim = int(uLim)
sLim = "{:,}".format(uLim)
#print (sLim)
startTime = time.time() # Remember time computation begins...

for x in range(0, limit+1): # Populate the array
	numArray.append(x)

for y in range(2, uLim):
	chk = y 
	chk = int(chk)
	#print "chk = %i and y = %i and numArray[chk] = %i" % (chk, y, numArray[chk])
	while (chk < limit):
		if(numArray[chk] % y == 0 and numArray[chk] != y):
			numArray[chk] = 0
		chk = chk + 1
endTime = time.time() # Remember when it ends
count = 0 # to count number of prime numbers - - -
		
for z in range(2, limit):
    if numArray[z] != 0:
        sNums = "{:,}".format(numArray[z])
        print ("%s is a prime number." % (sNums))
        count += 1 # counting prime numbers
fullTime = endTime - startTime
sCount = "{:,}".format(count)
print ("Elasped time = %.2f seconds" %(fullTime))
print ("there are %s prime numbers up to %s" % (sCount, sLimit))
print ("The floor of the square root of %s is %s." % (sLimit, sLim))
print ()
print ("%.2f seconds breaks out to..." %(fullTime))

convert(fullTime)