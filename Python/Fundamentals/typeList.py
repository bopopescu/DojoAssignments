l = ['magical','unicorns']

newString = ""
sum = 0
for x in l:
    if isinstance(x, str):
        newString += x + " "
    elif isinstance(x, (int, float)):
        sum += x

if all(isinstance(x, str) for x in l):
    print "The list you entered is of string type"

if all(isinstance(x, (int,float)) for x in l):
    print "The list you entered is of integer type"

if any(isinstance(x, (int, float)) for x in l) and isinstance(x, str):
    print "The list you entered is of mixed type"

print "String: " + newString
print "Sum: ", sum