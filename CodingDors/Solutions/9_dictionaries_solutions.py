# Title: create_dictionary
"""
Given a string 'name' and an integer 'age', return a dictionary with the pair of key 'name' and value 'age' added. 

Hint: Dictionaries are used to store data values in key:value pairs.

create_dictionary(gi', 25) -> {'gi': 25}
create_dictionary('leo', 41) -> {'leo': 41}
create_dictionary('rod', 12) -> {'rod': 12}
"""


def create_dictionary(name, age):
  new_dict = {name: age}
  return new_dict


# Title: add_element_dictionary
"""
Given a dictionary called 'students', a string 'name' and an integer 'age', return the dictionary 'student' with the pair of key 'name' and value 'age' added. 

Hint: Dictionaries are used to store data values in key:value pairs.

add_element_dictionary({'leo': 12}, 'gi', 25) -> {'leo':12, 'gi': 25}
add_element_dictionary({'fe': 27}, 'leo', 41) -> {'fe': 27,'leo': 41}
add_element_dictionary({}, 'rod', 12) -> {'rod': 12}
"""


def add_element_dictionary(students, name, age):
	students[name] = age
	return students


# Title: return_value
"""
We have a dictionary 'd' that contains as key the fruit and the value its price. Given a string 'fruit', return the price of this fruit in the dictionary.

return_value({'apple': 0.5, 'banana': 0.25, 'cherry': 0.75}, 'apple') -> 0.5
return_value({'apple': 0.5, 'banana': 0.25, 'cherry': 0.75}, 'cherry') -> 0.75
"""


def return_value(d, fruit):
	price = d[fruit]
	return price


# Title: find_person
"""
Given a dictionary 'd' and a string 'name', return True if the given name exist in our dictionary. Otherwise, False. 

find_person({'Gi': 123, 'Leo': 456}, 'Gi') -> True 

find_person({'Gi': 123, 'Leo': 456}, 'Ana') -> False
"""


def find_person(d: dict,name: str) -> bool:
	if name in d:
	  return True
	else:
	  return False


# Title: dictionary_size
"""
Given a dictionary, return the number of key-value pairs it contains.

dictionary_size({}) -> 0
dictionary_size({'name': 'Gi'}) -> 1
dictionary_size({'a':1, 'b':4, 'c': 7}) -> 3
"""


def dictionary_size(d):
	return len(d)


# Title: update_value
"""
Given a dictionary, a key, and a value, update the value associated with the key in the dictionary. If the key does not exist, add the key-value pair to the dictionary.

update_value({}, 'name', 'Gi') -> {'name': 'Gi'}
update_value({'name': 'Gi'}, 'name', 'Leo') -> {'name': 'Leo'}
update_value({'name': 'Gi'}, 'age', 25) -> {'name': 'Gi', 'age': 25}
"""


def update_value(d, key, value):
	if key in value:
	  d[key] = value
	  return d
	else:
	  d[key] = value
	  return d
	  
	# Since we'll change the value either way, 
	# you can do only as follow:
	d[key] = value
	return d


# Title: sum_values_dict
"""
Given a dictionary with integer values, return the sum of all the values.

sum_values_dict({'a': 1}) -> 1
sum_values_dict({'a': 1, 'b': 7}) -> 8
sum_values_dict({'a': 1, 'b': 7, 'c': 9}) -> 17
"""


def sum_values_dict(d):
	sum = 0
	for key in d:
	  sum += d[key]
	return sum


# Title: square_values
"""
Given a dictionary with integer values, return a new dictionary with the values squared.

square_values({'a':1}) -> {'a': 1}
square_values({'a':1, 'b': 5}) -> {'a': 1, 'b': 25}
square_values({'a':1, 'b': 5, 'c': 9}) -> {'a': 1, 'b': 25, 'c': 9}
"""


def square_values(d):
	for key in d:
	  d[key] = d[key] ** 2
	return d


# Title: common_keys
"""
Given two dictionaries, return True if at least one of the keys that are present in both dictionaries.

common_keys({'a': 1}, {'a': 2}) -> True
common_keys({'a': 1}, {'b': 2}) -> False
common_keys({'a': 1, 'b': 2}, {'c': 3, 'b': 3}) -> True
"""


def common_keys(d1, d2):
	for key in d1:
	  if key in d2:
	    return True
	return False


# Title: capitalize_keys
"""
Given a dictionary with string keys, create a new dictionary with the same key-value pairs, but with the keys capitalized.

capitalize_keys({'name': 'gi'}) -> {'Name': 'gi'}
capitalize_keys({'sport': 'soccer'}) -> {'Sport': 'soccer'}
capitalize_keys({'name': 'gi', 'sport': 'soccer'}) -> {'Name': 'gi', 'Sport': 'soccer'}
"""


def capitalize_keys(d):
  new_d = {}
  for key in d:
    new_d[key.title()] = d[key]
  return new_d


# Title: capitalize_values
"""
Given a dictionary with string values, create a new dictionary with the same key-value pairs, but with the values capitalized.

capitalize_values({'name': 'gi'}) -> {'name': 'Gi'}
capitalize_values({'sport': 'soccer'}) -> {'sport': 'Soccer'}
capitalize_values({'name': 'gi', 'sport': 'soccer'}) -> {'name': 'Gi', 'sport': 'Soccer'}
"""


def capitalize_values(d):
	for key in d:
	  d[key] = d[key].title()
	return d


# Title: merge_dictionaries
"""
Given two dictionaries, merge them into a single dictionary. If a key exists in both dictionaries, sum the values.

merge_dictionaries({'a': 5, 'b': 3}, {'a': 2, 'c': 7}) -> {'a': 7, 'b': 3, 'c': 7}
merge_dictionaries({'apple': 10}, {'banana': 5, 'apple': 2}) -> {'apple': 12, 'banana': 5}
"""


def merge_dictionaries(d1, d2):
	new_dict = {}
	for key in d1:
	  if key in d2:
	    new_dict[key] = d1[key] + d2[key]
	  else:
	    new_dict[key] = d1[key]
	for key2 in d2:
	  if key2 not in new_dict:
	    new_dict[key2] = d2[key2]
	return new_dict


# Title: invert_dictionary
"""
Given a dictionary, return a new dictionary with keys and values swapped.

invert_dictionary({'a': 1, 'b': 2}) -> {1: 'a', 2: 'b'}
invert_dictionary({'apple': 'fruit', 'carrot': 'vegetable'}) -> {'fruit': 'apple', 'vegetable': 'carrot'}
invert_dictionary({}) -> {}
"""


def invert_dictionary(d):
	new_dict = {}
	for key in d:
	  old_value = d[key]
	  new_dict[old_value] = key
	return new_dict


# Title: filter_by_value
"""
Given a dictionary and a value, return a new dictionary containing only the key-value pairs with the given value.

filter_by_value({'a': 1, 'b': 2, 'c': 1}, 1) -> {'a': 1, 'c': 1}
filter_by_value({'apple': 'fruit', 'carrot': 'vegetable', 'banana': 'fruit'}, 'fruit') -> {'apple': 'fruit', 'banana': 'fruit'}
"""


def filter_by_value(d, value):
	new_d = {}
	for key in d:
	  if d[key] == value:
	    new_d[key] = value
	return new_d


# Title: keys_of_max_value
"""
Given a dictionary with integer values, return a list of keys with the maximum value.

keys_of_max_value({'a': 1, 'b': 2, 'c': 1}) -> ['b']
keys_of_max_value({'apple': 3, 'banana': 5, 'cherry': 5}) -> ['banana', 'cherry']
"""


def keys_of_max_value(d):
	keys_list = []
	max_value = max(d.values())
	for key in d:
	  if d[key] == max_value:
	    keys_list.append(key)
	return keys_list


# Title: sorted_keys
"""
Given a dictionary, return a list of its keys sorted in ascending order.

sorted_keys({'c': 1, 'a': 2, 'b': 1}) -> ['a', 'b', 'c']
sorted_keys({'banana': 5, 'apple': 3, 'cherry': 7}) -> ['apple', 'banana', 'cherry']
"""


def sorted_keys(d):
	keys_list = sorted(d.keys())
	return keys_list


# Title: remove_key
"""
Given a dictionary and a key, return a new dictionary with the specified key removed.

remove_key({'a': 1, 'b': 2, 'c': 3}, 'a') -> {'b': 2, 'c': 3}
remove_key({'apple': 'fruit', 'banana': 'fruit', 'carrot': 'vegetable'}, 'banana') -> {'apple': 'fruit', 'carrot': 'vegetable'}
"""


def remove_key(d, key):
	d.pop(key)
	return d


# Title: dict_intersection
"""
Given two dictionaries, return a new dictionary containing the key-value pairs that are present in both dictionaries.

dict_intersection({'a': 1, 'b': 2, 'c': 3}, {'a': 1, 'b': 2, 'd': 4}) -> {'a': 1, 'b': 2}
dict_intersection({'apple': 'fruit', 'carrot': 'vegetable'}, {'banana': 'fruit', 'apple': 'fruit'}) -> {'apple': 'fruit'}
"""


def dict_intersection(d1, d2):
	new_d = {}
	for key in d1:
	  if key in d2 and d1[key] == d2[key]:
	    new_d[key] = d1[key]
	return new_d


# Title: count_values
"""
Given a dictionary, return a new dictionary where the keys are the unique values from the input dictionary and the values are the number of occurrences of each unique value.

count_values({'a': 1, 'b': 2, 'c': 1, 'd': 2, 'e': 3}) -> 1: 2, 2: 2, 3: 1}
count_values({'apple': 'fruit', 'carrot': 'vegetable', 'banana': 'fruit'}) -> {'fruit': 2, 'vegetable': 1}
"""


def count_values(d):
	result = {}
	for value in d.values():
	  if value in result:
	    result[value] += 1
	  else:
	    result[value] = 1
	return result


# Title: nested_value
"""
Given a nested dictionary and a list of keys, return the value at the specified depth in the nested dictionary. If any key is not present, return False.

nested_value({'a': {'b': {'c': 1}}}, ['a', 'b', 'c']) -> 1
nested_value({'key': 'value'}, ['key', 'missing']) -> False
nested_value({'fruit': {'apple': {'color': 'red'}}}, ['fruit', 'apple', 'color']) -> 'red'
"""


def nested_value(d, keys):
	for key in keys:
	  if key in d:
	    d = d[key]
	  else:
	    return False
	return d


