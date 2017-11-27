#Tests if integer is greater than or equal to 100
x = -105
if x >= 100:
    print "That's a big number!"
else:
    print "That's a small number"

#Tests if string is greater than or equal to 50 characters
y = "Tell me and I forget. Teach me and I remember. Involve me and I learn."
if len(y) >= 50:
    print "Long sentence."
else:
    print "Short sentence."

#Tests if length of list is greater than or equal to 10
z = [4,34,22,68,9,13,3,5,7,9,2,12,45,923]
if len(z) >= 10:
    print "Big list!"
else:
    print "Short list."
