# odd/even

#def oddEven():
    #for i in range(1, 2001):
        #if(i % 2 != 0):
            #print "Number is {}. This is an odd number.".format(i)
        #else:
            #print "Number is {}. This is an even number.".format(i)

# multiply
def multiply(a, b):
    new = []
    for each in a:
        each = each * b
        new.append(each)
    return new
a = [2,4,10,16]
b = multiply(a, 5)
print b

def layered_multiples(arr):
    new_array = []
    for i in arr:
        new_array += ([[1] * i])
    return new_array
x = layered_multiples(multiply([2,4,5],3))
print x