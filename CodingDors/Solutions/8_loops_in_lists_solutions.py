# Title: print_to_n_for_loop
"""
Write a Python function that takes an integer n as input and returns a list that contains all numbers from 0 to n inclusive, using a for loop.
 
print_to_n_for_loop(5) -> [0, 1, 2, 3, 4, 5]

print_to_n_for_loop(3) -> [0, 1, 2, 3]

print_to_n_for_loop(1) -> [0, 1]
"""


def print_to_n_for_loop(n: int):
	numbers = []
	for i in range(0, n+1):
	  numbers.append(i)
	return numbers


# Title: print_to_n_even
"""
Write a Python function that takes an integer n as input and returns a list that contains all even integers from 0 to n inclusive, using a for loop.
 
print_to_n_even(5) -> [0, 2, 4]

print_to_n_even(10) -> [0, 2, 4, 6, 8, 10]

print_to_n_even(1) -> [0]
"""


def print_to_n_even(n: int):
	even = []
	for i in range(0, n+1):
	  if i % 2 == 0:
	    even.append(i)
	return even


# Title: print_odd_to_n_forloop
"""
Write a Python function that takes an integer n as input and returns a list that contains all odd integers from 0 to n inclusive, using a for loop. 

print_odd_to_n_forloop(5) -> [1, 3, 5]

print_odd_to_n_forloop(10) -> [1, 3, 5, 7, 9]

print_odd_to_n_forloop(1) -> [1]
"""


def print_odd_to_n_forloop(n: int):
	odd = []
	for i in range(0, n+1):
	  if i % 2 != 0:
	    odd.append(i)
	return odd


# Title: print_one_to_n_while
"""
Write a Python function that takes an integer n as input and returns a list that contains all the integers from 1 to n, inclusive, using a while loop. 

print_one_to_n_while(5) -> [1, 2, 3, 4, 5]

print_one_to_n_while(10) ->  [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

print_one_to_n_while(0) -> []
"""


def print_one_to_n_while(n: int):
	numbers = []
	i = 1
	while i <= n:
	  numbers.append(i)
	  i = i + 1
	return numbers


# Title: print_even_number_while
"""
Write a Python function that takes an integer n as input and returns a list that contains all even integers from 0 to n inclusive, using a while loop. 

print_even_number_while(5) -> [0, 2, 4]

print_even_number_while(10) -> [0, 2, 4, 6, 8, 10]

print_even_number_while(1) -> [0]
"""


def print_even_number_while(n: int):
	numbers = []
	i = 0
	while i <= n:
	  if i % 2 == 0:
	    numbers.append(i)
	  i = i + 1
	return numbers


# Title: print_to_n_odd_while
"""
Write a Python function that takes an integer n as input and returns a list that contains all odd integers from 0 to n inclusive, using a while loop. 

print_to_n_odd_while(5) -> [1, 3, 5]

print_to_n_odd_while(10) -> [1, 3, 5, 7, 9]

print_to_n_odd_while(1) -> [1]
"""


def print_to_n_odd_while(n: int):
	numbers = []
	i = 0
	while i <= n:
	  if i % 2 != 0:
	    numbers.append(i)
	  i = i + 1
	return numbers


# Title: reverse_n_for
"""
Write a Python function that takes an integer n as input and returns a list that contains all numbers from n to 0 inclusive (reverse order), using a for loop.
 
reverse_n_for(5) -> [5,4, 3, 2, 1, 0]

reverse_n_for(3) -> [3, 2, 1, 0]

reverse_n_for(1) -> [1, 0]
"""


def reverse_n_for(n: int):
	numbers = []
	for i in range(n, -1, -1):
	  numbers.append(i)
	return numbers


# Title: reverse_n_while
"""
Write a Python function that takes an integer n as input and returns a list that contains all numbers from n to 0 inclusive (reverse order), using a while loop.
 
reverse_n_while(5) -> [5, 4, 3, 2, 1, 0]

reverse_n_while(3) -> [3, 2, 1, 0]

reverse_n_while(1) -> [1, 0]
"""


def reverse_n_while(n: int):
	numbers = []
	while n >= 0:
	  numbers.append(n)
	  n = n - 1
	return numbers


# Title: reverse_n_even_for
"""
Write a Python function that takes an integer n as input and returns a list that contains all even numbers from n to 0 inclusive, using a for loop.
 
reverse_n_even_for(5) -> [4, 2, 0]

reverse_n_even_for(3) -> [2, 0]

reverse_n_even_for(1) -> [0]
"""


def reverse_n_even_for(n: int):
	numbers = []
	for i in range(n, -1, -1):
	  if i % 2 == 0:
	    numbers.append(i)
	return numbers


# Title: reverse_n_even_while
"""
Write a Python function that takes an integer n as input and returns a list that contains all even numbers from n to 0 inclusive, using a while loop.
 
reverse_n_even_while(5) -> [4, 2, 0]

reverse_n_even_while(3) -> [2, 0]

reverse_n_even_while(1) -> [0]
"""


def reverse_n_even_while(n: int):
	numbers = []
	while n >= 0:
	  if n % 2 == 0:
	    numbers.append(n)
	  n = n - 1
	return numbers


# Title: reverse_n_odd_while
"""
Write a Python function that takes an integer n as input and returns a list that contains all odd numbers from n to 1 inclusive, using a while loop.
 
reverse_n_odd_while(5) -> [5, 3, 1]

reverse_n_odd_while(3) -> [3, 1]

reverse_n_odd_while(1) -> [1]
"""


def reverse_n_odd_while(n: int):
	numbers = []
	while n >= 0:
	  if n % 2 != 0:
	    numbers.append(n)
	  n = n - 1
	return numbers


# Title: reverse_n_odd_for
"""
Write a Python function that takes an integer n as input and returns a list that contains all odd numbers from n to 0, using a for loop.
 
reverse_n_odd_for(5) -> [5, 3, 1]

reverse_n_odd_for(3) -> [3, 1]

reverse_n_odd_for(1) -> [1]
"""


def reverse_n_odd_for(n: int):
	numbers = []
	for i in range(n, -1, -1):
	  if i % 2 != 0:
	    numbers.append(i)
	return numbers


# Title: count_odds_list
"""
Return the number of odd integers in the given list. Note: the % "mod" operator computes the remainder, e.g. 5 % 2 is 1.


count_odds_list([2, 1, 2, 3, 4]) → 2
count_odds_list([2, 2, 5]) → 1
count_odds_list([1, 3, 5]) → 3
"""


def count_odds_list(l: list) -> int:
	sum = 0
	for i in range(len(l)):
	  if l[i] % 2 != 0:
	    sum += 1
	return sum


# Title: has33_list
"""
Given a list of integers, return True if the list contains a 3 next to a 3 somewhere.

has33_list([1, 3, 3]) → True
has33_list([1, 3, 1, 3]) → False
has33_list([3, 1, 3]) → False
"""


def has33_list(l: list) -> bool:
	for i in range(len(l)-1):
	  if l[i] == l[i+1] == 3:
	    return True
	return False


# Title: list456
"""
Given a list of integers, return True if the sequence of numbers 4, 5, 6 appears in the list somewhere.

list456([1, 4, 5, 6, 1]) → True
list456([1, 4, 5, 4, 6]) → False
list456([1, 1, 2, 4, 5, 6]) → True
"""


def list456(l: list) -> bool:
	for i in range(len(l)-2):
	  if l[i] == 4 and l[i+1] == 5 and l[i+2] == 6:
	    return True
	return False


# Title: has_matching_list
"""
Given two lists 'l1' and 'l2', write a function that determines if the two lists share at least one letter in the same position. The function should return True if they do and False otherwise.

Assume that both lists will have the same length.

has_matching_list(["a","p","p","l","e"], ["a","b","c","d","e"]) → True
has_matching_list(["h","e","l","l","o"], ["w","o","r","l","d"]) → True
has_matching_list(["d","a","n","c","e"], ["l","o","v","e","r"]) → False
"""


def has_matching_list(l1: list, l2: list) -> bool:
	for i in range(len(l1)):
	  if l1[i] == l2[i]:
	    return True
	return False


# Title: check_first_number_list
"""
Given a list 'l', determine if the first number appearing in the list is 0. The function should return False if the first number in the list is 0. If the list does not contain any numbers or if the first number appearing isn't 0, it should return True.

check_first_number_list(["H","e","l","l","o"]) → True
check_first_number_list(["H","e","l","l","0"]) → False
check_first_number_list(["H","3","l","l","0"]) → True
"""


def check_first_number_list(l: list) -> bool:
	for i in range(len(l)):
	  if str(l[i]).isdigit():
	    if str(l[i]) == '0':
	      return False
	    else:
	      return True
	return True


# Title: sort_list
"""
Given a list of integers, return a the same list sorted in ascending order.

sort_list([25, 12, 22, 11]) -> [11, 12, 22, 25]
sort_list([-5, 0, -2, 3, 2, 1]) -> [-5, -2, 0, 1, 2, 3]
"""


def sort_list(l: list) -> list:
	return sorted(l)


# Title: sum_matrix_elements
"""
Given a 2-dimensional list (matrix) of integers, write a Python function that calculates and returns the sum of all its elements using loops.

sum_matrix_elements([[1, 2, 3], [4, 5, 6], [7, 8, 9]]) -> 45
sum_matrix_elements([[10]]) -> 10
"""


def sum_matrix_elements(matrix):
	total = 0
	for row in matrix:
	  for num in row:
	    total += num
	return total


# Title: has_letter_a_matrix
"""
Given a 2-dimensional list (matrix) where each element is a single letter, write a Python function that determines if the letter 'a' exists in the matrix. If the letter 'a' is found, the function should return True, otherwise, it should return False.

has_letter_a_matrix([['b', 'c', 'd'], ['e', 'f', 'g'], ['h', 'i', 'a']]) -> True
has_letter_a_matrix([['b', 'c', 'd'], ['e', 'f', 'g'], ['h', 'i', 'j']]) -> False
"""


def has_letter_a_matrix(matrix):
	for row in matrix:
	  for num in row:
	    if num == 'a':
	      return True
	return False


