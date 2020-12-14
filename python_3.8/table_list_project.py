"""print an aligned table from a list of strings"""

table_data = [['apples', 'oranges', 'cherries', 'banana'],
              ['Alice', 'Bob', 'Carol', 'David'],
              ['dogs', 'cats', 'moose', 'goose']]

def print_table(table):

    # create a list zeros euql to the length of the input list
    col_widths = [0] * len(table)

    # find longest word in each sublist and set col_width to largest value
    count = 0
    while count < len(table):
        for item in table[count]:
            if len(item) > col_widths[count]:
                col_widths[count] = len(item)
        count += 1


    # print function
    for word in range(len(table[0])):
        for item in range(len(table)):
            print(table[item][word].rjust(col_widths[item]), end= ' ')
        print()

    
print_table(table_data)
