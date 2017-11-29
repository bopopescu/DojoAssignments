first_row = "x 1 2 3 4 5 6 7 8 9 10 11 12"
print first_row

for row in range(1, 13): 
    display_string = ''
    for column in range(0, 13):
        if column is 0:
            display_string += str(row) + ' '
        else:    
            display_string += str(column * row) + ' '
    print display_string    
