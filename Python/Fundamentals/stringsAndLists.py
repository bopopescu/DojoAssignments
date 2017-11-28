words = "It's thanksgiving day. It's my birthday, too!"

print words.find('day')
print words.replace("day", "month")

x = [2,54,-2,7,12,98]

print min(x)
print max(x)

x = ["hello",2,54,-2,7,12,98,"world"]

print x[0]
print x[-1]
newList = [x[0], x[-1]]
print newList

x = [19,2,54,-2,7,12,98,32,10,-3,6]

x.sort()
firstHalf = x[0:len(x)/2]
x[0:len(x)/2] = [firstHalf]
print x