# Task 1

def new_list(n):

    for i in range(1, n + 1): # This has 0(n ) time complexity

        print(i**2) # this is a 0(1) time complexity



new_list(8) # Overall we have a 0(n) time complexity 


print('='*75)



# Task 2

def merge_list():

    list_1 = ["john", "blake", "matt"]

    list_2 = ["tiffany", "debbie", "sofia"] # The two lists have 0(1)time complexity

    combine_list = list_1 + list_2 # The combine list is also 0(1) complexity

    print(combine_list) # Overall the function is 0(1) complexity


merge_list()



