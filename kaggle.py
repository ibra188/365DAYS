import numpy as np
from math import pi, log

#help(math.log(32, 2)) # help function to find out what the log function does.
#help(math) # help function to find out what the math module does.


print("Pi to 4 decimal places is = {:.4f}".format(pi)) # print the value of pi to 4 decimal places.
print(log(32, 2)) # log the base 2 of 32.

print(pi, log(4, 2))
# list in python
companies = ['Google', 'Facebok', 'Amazon', 'Microsoft', 'Apple', 'IBM']
print(companies[3], companies[-2]) 

number_list = [[1,2,3], [4,6,12]]
print(number_list[1], number_list[-1])

#list are mutable
companies[1] = "AfriFam"
print(companies)

# list funzione
print(len(companies))
print(sorted(companies))

prime_numbers = [2,4, 3,6]
print(sum(prime_numbers), min(prime_numbers), max(prime_numbers))

#apending in list
city_list = ['conegliano', 'san vendemiano', 'padova', 'treviso']
city_list.append('belluno')
print(city_list)

# Searching lists
print(city_list.index('conegliano')) 