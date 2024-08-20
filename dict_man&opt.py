dict_1 = {
'pie': 'apple',
'ice_cream': 'moose tracks',
'cobbler': 'peach',
'cake': None
}

dict_2 = {
'dinner': 'turkey',
'ice_cream': 'vanilla',
'appetizer': 'soup',
'cobbler': 'peach'
}


def merge_dict():

    dict_1.update(dict_2) # this is a 0(1) time complexity

    print(dict_1)



merge_dict() # Overall we have a 0(1) time complexity 

print('='*75)


# Task 2

def intersect():
   
   for items in dict_1: # This has 0(n ) time complexity

      if items in dict_2 and dict_1[items] == dict_2[items]: # This has 0(1) time complexity

         
         print(items) # Overall this has an 0(n) time complexity



intersect()