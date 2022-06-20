# Description
# Write a code, which will:
#
# 1. create a list of random number of dicts (from 2 to 10)
# - dict's random numbers of keys should be letter (all 26 letters),
# - dict's values should be a number (0-100),
# - example: [{'a': 5, 'b': 7, 'g': 11}, {'a': 3, 'c': 35, 'g': 42}]
#
# 2. get previously generated list of dicts and create one common dict:
# - if dicts have same key, we will take max value, and rename key with dict number with max value
# - if key is only in one dict - take it as is,
# - example: {'a_1': 5, 'b': 7, 'c': 35, 'g_2': 42}
#
# Each line of code should be commented with description.

# 1. Creation a list of random number of dicts (from 2 to 10)
import string  # to access lower case characters
import random  # to access  the method random

dict_number = random.randint(2, 10)  # define a random count of dicts

print("Count of dictionaries: ", dict_number)  # displaying number to check count of dicts

list_dicts = []
letters = string.ascii_lowercase  # generate list of letters as a key and get the lower cases ascii letters
i = 1
while i <= dict_number:  # creating a loop with random count of dictionaries
    keys = random.sample(letters, k=random.randint(3, 26))  # where range is number of required rand_letter
    values = random.choices(range(0, 100), k=len(keys))  # list of numbers as value in range 0-100
    my_dict = {key: value for key, value in zip(keys, values)}  # Generate dictionary with key as letter,value as number
    i += 1
    list_dicts.append(my_dict)  # appending generated dict into list

print("My random list of dictionaries: ", list_dicts)  # displaying list of dictionaries

# 2. Creation a common dict

dict_max_values = {}  # key: max_value
dict_indexes = {}  # key: number_of_dict
dict_has_duplicates = {}  # 0 or 1 in case if key has duplicate, but first value is bigger
result_dict = {}  # Merged dictionary

for dic in list_dicts:
    for key in dic.keys():
        if key not in dict_max_values.keys():
            dict_max_values[key] = dic[key]
        if dic[key] > dict_max_values[key]:
            dict_max_values[key] = dic[key]

# print('Dict with keys and max values: ', dict_max_values)

for i in list_dicts:
    for key in i.keys():
        if key not in dict_has_duplicates:
            dict_has_duplicates[key] = 0
        else:
            dict_has_duplicates[key] = 1

# print('Keys which have duplicates: ', dict_has_duplicates)

cnt = 1
for i in list_dicts:
    for key, value in i.items():
        if cnt == 1:
            dict_indexes[key] = key

        elif cnt != 1 and key not in dict_indexes and dict_has_duplicates[key] == 0:
            dict_indexes[key] = key

        elif cnt != 1 and key not in dict_indexes and dict_has_duplicates[key] != 0:
            dict_indexes[key] = key + '_' + str(cnt)

        elif cnt != 1 and key in dict_indexes \
                and value == dict_max_values.get(key) \
                and key == dict_indexes.get(key):
            dict_indexes[key] = key + '_' + str(cnt)
    cnt += 1

# print('keys with indexes:', dict_indexes)

for key, value in dict_indexes.items():
    result_dict[value] = dict_max_values.get(key)

print('Merged dict with keys and max values: ', result_dict)