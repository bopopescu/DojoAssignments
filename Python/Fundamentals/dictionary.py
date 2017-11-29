about_me = {"name": "Maria", "age": "33", "country of birth": "The United States", "favorite language": "Python"}

def description():
    for key,data in about_me.iteritems():
        print "My {} is {}".format(key, data)

description()
