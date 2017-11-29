def stars(list):
    for x in list:
        print ("*" * x)

stars([4,6,1,3,5,7,25])




def stars_two(list):
    for x in list:
        if type(x) is int:
            print ("*" * x)
        else:
            print (str.lower(x[0]) * len(x))

stars_two([4, "Tom", 1, "Michael", 5, 7, "Jimmy Smith"])