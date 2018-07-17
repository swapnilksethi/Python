from __future__ import print_function
x = raw_input('Enter Statement: ')
my_dict = {} 
for key in x:
  if key in my_dict:
     my_dict[key] += 1
  else:
     my_dict[key] = 1
del my_dict[' ']
print(my_dict)