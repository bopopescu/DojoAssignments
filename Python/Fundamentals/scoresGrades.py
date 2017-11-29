def scoresAndGrades():
    import random
    my_randoms = random.sample(xrange(60, 101), 10)

    for x in my_randoms:
        if 60 <= x <= 69:
            print "Score: {}; Your grade is D".format(x)
        elif 70 <= x <= 79:
            print "Score: {}; Your grade is C".format(x)
        elif 80 <= x <= 89:
            print "Score: {}; Your grade is B".format(x)
        elif 90 <= x <= 100:
            print "Score: {}; Your grade is A".format(x)
    print "End of the program. Bye!"

scoresAndGrades()