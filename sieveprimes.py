#!/usr/bin/python
import sys
import math

if (len(sys.argv) < 3):
	print "Please enter a lower and upper bound!"
	exit()

low_bound = int(sys.argv[1])

if (low_bound < 1):
	print "enter bound > 1"
	exit()

upper_bound = int(sys.argv[2])

if (upper_bound < low_bound):
	print "upper bound must be greater than or equal to lower bound"
	exit()

#Create number list
numlist = [0] * (low_bound-1)
for i in xrange(low_bound, upper_bound+1):
	numlist.append(i)

k = 1
count = 0

while (k < math.sqrt(upper_bound)):
	if (numlist[k] == 0):
		m = k+1
	else:
		m = numlist[k]
	i = m
	while ((i * m) < upper_bound+1):
		if (numlist[i * m - 1] != 0):
			numlist[i * m -1] = 0
		i += 1
	k = m

for x in range(low_bound-1, upper_bound	):
	if (numlist[x] != 0 and numlist[x] != 1):
		print "Prime: " , numlist[x]
		primenum = numlist[x]
		count += 1
print "# of Primes: ", count
