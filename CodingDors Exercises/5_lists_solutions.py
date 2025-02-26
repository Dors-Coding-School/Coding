# Title: first_element
"""
Write a function that returns the first element of a given list.

first_element([1,2,3,4,5]) -> 1

first_element([5,4,3,2,1]) -> 5

first_element([10,20,30,40,50]) -> 10
"""


def first_element(n: list) -> int:
	return n[0]


# Title: second_element
"""
Write a function that returns the second element of a given list.

second_element([1,2,3,4,5]) -> 2

second_element([5,4,3,2,1]) -> 4

second_element([10,20,30,40,50]) -> 20
"""


def second_element(n: list) -> int:
	return n[1]


# Title: last_element
"""
Write a function that returns the last element of a given list.

last_element([1,2,3,4,5]) -> 5

last_element([5,4,3,2,1]) -> 1

last_element([10,20,30,40,50]) -> 50
"""

def last_element(n: list) -> int:
	return n[-1]


# Title: list_length
"""
Write a function that returns the length of a given list.

list_length([2,5,8]) -> 3

list_length([11,3,2,9]) -> 4

list_length([0,2,4,6,8,9]) -> 6
"""


def list_length(n: list) -> int:
	return len(n)


# Title: concatenate_lists
"""
Write a function that concatenates two given lists.

concatenate_lists([1], [2]) -> [1,2]

concatenate_lists([3,4], [5]) -> [3,4,5]

concatenate_lists([2], [4,6,8]) -> [2,4,6,8]
"""


def concatenate_lists(n1: list, n2: list) -> list:
	return n1 + n2


# Title: repeat_list
"""
Write a function that repeats a given list n times.

repeat_list([1,2], 3) -> [1,2,1,2,1,2]

repeat_list([5,6,7]], 2) -> [5,6,7,5,6,7]

repeat_list([1], 5) -> [1,1,1,1,1]
"""


def repeat_list(l: list, n: int) -> list:
	return l * n


# Title: front_back_list
"""
Given a list 'n', return a new list where the first and last elements have been exchanged.

front_back_list([10,20,30]) → [30,20,10]

front_back_list([5,6,7]) → [7,6,5]

front_back_list([4,6,8]) → [8,6,4]
"""


def front_back_list(n: list) -> list:
	return [n[-1], n[1], n[0]] 


# Title: first_element_is_greater
"""
Write a function that checks if the first given element in the list is greater than or equal to the second given element.

first_element_is_greater([4,5]) -> True

first_element_is_greater([10, -10]) -> True

first_element_is_greater([1, 10]) -> False
"""


def first_element_is_greater(n: list) -> bool:
	if n[0] >= n[-1]:
	  return True
	else:
	  return False


# Title: first_element_is_smaller
"""
Write a function that checks if the first given element of the list is smaller than or equal to the second given element.

first_element_is_smaller([1, 3]) -> True

first_element_is_smaller([-10, -10]) -> True

first_element_is_smaller([7, 1]) -> False
"""


def first_element_is_smaller(n: list) -> bool:
	if n[0] <= n[-1]:
	  return True
	else:
	  return False


# Title: first_last9
"""
Given a list of integers, return True if the number 9 appears as either the first or last element in the list. The list will be of length 1 or more.

first_last9([1, 2, 9]) → True

first_last9([9, 1, 2, 3]) → True

first_last9([13, 9, 1, 2, 3]) → False
"""


def first_last9(n: list) -> bool:
	if n[0] == 9 or n[-1] == 9:
	  return True
	else:
	  return False


# Title: same_value
"""
Given a list of integers with 3 elements, return True if all the 3 elements are equal.


same_value([1, 2, 3]) → False
same_value([2, 2, 2]) → True
same_value([1, 2, 1]) → False
"""


def same_value(n: list) -> bool:
	if n[0] == n[1] == n[2]:
	  return True
	else:
	  return False


# Title: common_element
"""
Given 2 lists of integers, a and b, return True if they have the same first element or they have the same second element or they have the same last element. Both arrays will be length 3.

common_element([1,2,3], [4,5,3]) -> True
common_element([1,2,3], [4,5,6]) -> False
common_element([3,2,1], [0,2,4]) -> True
"""


def common_element(a: list, b: list) -> bool:
	if a[0] == b[0]:
	  return True
	elif a[1] == b[1]:
	  return True
	elif a[2] == b[2]:
	  return True
	else:
	  return False


# Title: sum_all
"""
Given a list of integers length 3, return the sum of all the elements.


sum_all([1, 2, 3]) → 6
sum_all([5, 11, 2]) → 18
sum_all([7, 0, 0]) → 7
"""


def sum_all(n: list) -> int:
	sum = n[0] + n[1] + n[2]
	return sum


# Title: new_list
"""
Given three individual integers 'a', 'b', and 'c', the task is to formulate a list where each of these integers becomes an element.

new_list(3, 4, 5) -> [3, 4, 5]
new_list(1, 6, 12) -> [1, 6, 12]
new_list(21, 7, 14) -> [21, 7, 14]
"""


def new_list(a: int, b: int, c: int) -> list:
	return [a, b, c]


# Title: rotate_right
"""
Given a list of integers length 3, return a new list with the elements "rotated right" so [1, 2, 3] yields [3, 1, 2].


rotate_right([1, 2, 3]) → [3, 1, 2]
rotate_right([5, 11, 9]) → [9, 5, 11]
rotate_right([7, 0, 0]) → [0, 7, 0]
"""


def rotate_right(n: list) -> list:
	first = n[0]
	second = n[1]
	last = n[2]
	return [last, first, second]


# Title: reverse_list
"""
Given a list of integers length 3, return a new list with the elements in reverse order, so [1, 2, 3] becomes [3, 2, 1].


reverse_list([1, 2, 3]) → [3, 2, 1]
reverse_list([5, 11, 9]) → [9, 11, 5]
reverse_list([7, 0, 0]) → [0, 0, 7]
"""


def reverse_list(n: list) -> list:
	first = n[0]
	second = n[1]
	last = n[2]
	return [last, second, first]


# Title: min_end
"""
Given a list of integers length 3, figure out which is smaller, the first, second or last element in the list, and set all the other elements to be that value. Return the changed list.


min_end([1, 2, 3]) → [1, 1, 1]
min_end([11, 5, 9]) → [5, 5, 5]
min_end([2, 11, 3]) → [2, 2, 2]
"""


def min_end(n: list) -> list:
	if n[0] < n[1] and n[0] < n[2]:
	  min = n[0]
	elif n[1] < n[0] and n[1] < n[2]:
	  min = n[1]
	else:
	  min = n[2]
	  
	return [min, min, min]


# Title: compare_lists
"""
Given two lists of integers, 'a' and 'b', each consisting of three elements, return the list which has the larger value in the second position.

compare_lists([1, 4, 3], [2, 3, 5]) → [1, 4, 3]

compare_lists([1, 5, 9], [4, 2, 6]) → [1, 5, 9]

compare_lists([6, 3, 1], [2, 7, 0]) → [2, 7, 0]
"""


def compare_lists(a: list, b: list) -> list:
	if a[1] > b[1]:
	  return a
	else:
	  return b


# Title: make_ends
"""
Given two lists of integers 'a' and 'b', return a new list length 4 containing the first and last elements from the originals lists. The original list will be length 2 or more.

make_ends([1, 2, 3], [4, 5, 6]) → [1, 3, 4, 6]
make_ends([0, 2, 4], [1, 3, 5]) → [0, 4, 1, 5]
make_ends([7, 4, 6, 2], [-1, 0]) → [7, 2, -1, 0]
"""


def make_ends(a: list, b: list) -> list:
	return [a[0], a[-1], b[0], b[-1]]


# Title: even_list
"""
Given a list of integers length 3, return True if all the elements are even.

even_list([2, 5, 6]) → False
even_list([4, 8, 12]) → True
even_list([1, 3, 9]) → False
"""


def even_list(n: list) -> bool:
	if n[0] % 2 == 0 and n[1] % 2 == 0 and n[2] % 2 == 0:
	  return True
	else:
	  return False


