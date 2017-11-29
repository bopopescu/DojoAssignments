"""Create a function that takes in two lists and creates a single dictionary. 
The first list contains keys and the second list contains the values. Assume the lists will be of equal length.

Your first function will take in two lists containing some strings. Here are two example lists:
"""

def make_dict(list1, list2):

    new_dict = {}
    # your code here
    new_dict = zip(name,favorite_animal)
    new_dict = dict(new_dict)
    return new_dict

name = ["Anna", "Eli", "Pariece", "Brendan", "Amy", "Shane", "Oscar"]
favorite_animal = ["horse", "cat", "spider", "giraffe", "ticks", "dolphins", "llamas"]

print make_dict(name, favorite_animal)