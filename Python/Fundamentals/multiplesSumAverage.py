# For loop from 1 to 1001. Finds and prints all odd numbers.
for x in range (1, 1001):
    if x % 2 == 0:
        #print x

# For loop from 5 to 1,000,001. Finds and prints multiples of five.
for fives in range(5, 1000001):
    if fives % 5 == 0:
        print fives

# Sums up all values in the list
a = [1,2,5,10,255,3]
print sum(a)

# Takes sum of all values and divides by the length of list
a = [1,2,5,10,255,3]
print sum(a)/len(a)
