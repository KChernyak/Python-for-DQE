# TASK
# Create a python script:
# create list of 100 random numbers from 0 to 1000
# sort list from min to max (without using sort())
# calculate average for even and odd numbers
# print both average result in console

# 1. Define value range from 0 to 1000

num_range = range(0, 1000)

# Import random method and
import random

# Generating 100 values in list from 0 to 1000 and printing result
value_list = random.sample(num_range, 100)

# print("Random list of values: ", value_list)

# 2. Sorting for the random values from min to max without using sort()
# a. Assigning each value from 100 values in list number from 0 to 99
for i in range(len(value_list)):
    # b. Comparison first value in list with the next one.
    # If next value greater than previous one than it moves it further. Than compares it with the next one.
    # It happens in a loop till the end of the cycle
    for s in range(len(value_list) - 1):
        if value_list[s] > value_list[s + 1]:
            value_list[s], value_list[s + 1] = value_list[s + 1], value_list[s]

# Printing (displaying) sorted list
print("Sorted random list: ", value_list)

# 3. Calculating average for even and odd numbers
# a. Separating list with 100 random values (value_list) to list with odd and list with even elements

odd_value_list = []   # list with odd values
even_value_list = []  # list of even values

for number in value_list:
    if number % 2 == 1:  # sorting out if number in list odd than append it to odd list
        odd_value_list.append(number)
    if number % 2 == 0:  # sorting out if number in list even than append it to even list
        even_value_list.append(number)

print("List with odd values: ", odd_value_list)
print("List with even values: ", even_value_list)

# b. Calculation of avg value for odd and even lists and printing the average value for each list
# (in addition added round function to restrict digits after comma

avg_odd = sum(odd_value_list)/len(odd_value_list)
print("The average of list with odd values is ", round(avg_odd,2))

avg_even = sum(even_value_list)/len(even_value_list)
print("The average of list with even values is ", round(avg_even,2))
