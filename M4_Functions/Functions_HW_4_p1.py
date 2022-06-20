# Hometask: Refactor homeworks from module 2 and 3 using functional approach with decomposition.

import string
import random

# Homework 2:

# Defining range to count of dictionaries
dict_cnt_from = 2
dict_cnt_to = 5
# Defining count keys for dictionary
min_key_cnt = 3
max_key_cnt = 5
# Defining number range to be used for values in dictionary
min_value = 0
max_value = 100


def list_of_dictionaries():
    cnt_dicts = random.randint(dict_cnt_from, dict_cnt_to)
    list_dicts = []
    i = 1
    while i <= cnt_dicts:
        keys = random.sample(string.ascii_lowercase, k=random.randint(min_key_cnt, max_key_cnt))
        values = random.choices(range(min_value, max_value), k=len(keys))
        my_dict = {k: v for k, v in zip(keys, values)}
        i += 1
        list_dicts.append(my_dict)
    return list_dicts


list_of_dicts = list_of_dictionaries()

dict_max_values = {}
dict_has_duplicates = {}
dict_indexes = {}

for dic in list_of_dicts:
    for key in dic.keys():
        if key not in dict_max_values.keys():
            dict_max_values[key] = dic[key]
        if dic[key] > dict_max_values[key]:
            dict_max_values[key] = dic[key]


for dic in list_of_dicts:
    for key in dic.keys():
        if key not in dict_has_duplicates:
            dict_has_duplicates[key] = 0
        else:
            dict_has_duplicates[key] = 1


cnt = 1
for dic in list_of_dicts:
    for key, value in dic.items():
        if cnt == 1:
            dict_indexes[key] = key

        if cnt != 1 and key not in dict_indexes and dict_has_duplicates[key] == 0:
            dict_indexes[key] = key

        if cnt != 1 and key not in dict_indexes and dict_has_duplicates[key] != 0:
            dict_indexes[key] = key + '_' + str(cnt)

        if cnt != 1 and key in dict_indexes \
                and value == dict_max_values.get(key) \
                and key == dict_indexes.get(key):
            dict_indexes[key] = key + '_' + str(cnt)
    cnt += 1


def merge_dict():
    result_dict = {}
    for key, value in dict_indexes.items():
        result_dict[value] = dict_max_values.get(key)
    return result_dict


print("Merged dictionary:", merge_dict())
