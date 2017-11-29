def coinTosses():
    heads = 0
    tails = 0
    import random

    for i in range(1,5001):
        coin = random.randint(1,2)
        if coin == 1:
            tails += 1
            print "Attempt #{}: Throwing a coin... It's a tail! ... Got {} head(s) so far and {} tail(s) so far".format(i, heads, tails)
        if coin ==2:
            heads += 1
            print "Attempt #{}: Throwing a coin... It's a head! ... Got {} head(s) so far and {} tail(s) so far".format(i, heads, tails)

coinTosses()