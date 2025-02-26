# Title: sum_one_to_n
"""
Write a Python function that takes an integer n as input and calculates the sum of all integers from 1 to n, inclusive using a for loop. The function should the return the result.

sum_one_to_n(5) -> 15

sum_one_to_n(10) -> 55

sum_one_to_n(20) -> 210
"""


def sum_one_to_n(n: int):
	sum = 0
	for i in range(0, n+1):
	  sum = sum + i
	return sum


# Title: sum_one_to_n_while
"""
Write a Python function that takes an integer n as input and calculates the sum of all integers from 1 to n, inclusive, using a while loop.
 
sum_one_to_n_while(5) -> 15 

sum_one_to_n_while(10) -> 55 

sum_one_to_n_while(20) -> 210
"""


def sum_one_to_n_while(n: int):
	sum = 0
	i = 0
	while i <= n:
	  sum = sum + i
	  i = i + 1
	return sum


# Title: sum_to_n_even
"""
Write a Python function that takes an integer n as input and returns the sum of all even integers from 0 to n inclusive, using a for loop.
 
sum_to_n_even(5) -> 6

sum_to_n_even(10) -> 30

sum_to_n_even(1) -> 0
"""


def sum_to_n_even(n: int) -> int:
	sum = 0
	for i in range(n+1):
	  if i % 2 == 0:
	    sum += i
	return sum


# Title: sum_even_number_while
"""
Write a Python function that takes an integer n as input and returns the sum all even integers from 0 to n inclusive, using a while loop. 

sum_even_number_while(5) -> 6

sum_even_number_while(10) -> 30

sum_even_number_while(1) -> 0
"""


def sum_even_number_while(n: int) -> int:
	sum = 0
	i = 0
	while i <= n:
	  if i % 2 == 0:
	    sum += i
	  i += 1
	return sum


# Title: sum_odd_to_n_forloop
"""
Write a Python function that takes an integer n as input and returns the sum of all odd integers from 0 to n inclusive, using a for loop. 

sum_odd_to_n_forloop(5) -> 9

sum_odd_to_n_forloop(10) -> 25

sum_odd_to_n_forloop(1) -> 1
"""


def sum_odd_to_n_forloop(n: int) -> int:
	sum = 0
	for i in range(n+1):
	  if i % 2 != 0:
	    sum += i
	return sum


# Title: sum_to_n_odd_while
"""
Write a Python function that takes an integer n as input and returns the sum of all odd integers from 0 to n inclusive, using a while loop. 

sum_to_n_odd_while(5) -> 9

sum_to_n_odd_while(10) -> 25

sum_to_n_odd_while(1) -> 1
"""


def sum_to_n_odd_while(n: int) -> int:
	sum = 0
	i = 0
	while i <= n:
	  if i % 2 != 0:
	    sum += i
	  i += 1
	return sum


# Title: sum_reverse_n_for
"""
Write a Python function that takes an integer n as input and returns the sum of all numbers from n to 0 inclusive (reverse order), using a for loop.

sum_reverse_n_for(5) -> 15

sum_reverse_n_for(3) -> 6

sum_reverse_n_for(1) -> 1
"""


def sum_reverse_n_for(n: int) -> int:
	sum = 0
	for i in range(n, -1, -1):
	  sum += i
	return sum


# Title: sum_reverse_n_while
"""
Write a Python function that takes an integer n as input and returns the sum all numbers from n to 0 inclusive (reverse order), using a while loop.
 
sum_reverse_n_while(5) -> 15

sum_reverse_n_while(3) -> 6

sum_reverse_n_while(1) -> 1
"""


def sum_reverse_n_while(n: int) -> int:
	sum = 0
	while n > 0:
	  sum += n
	  n -= 1
	return sum


# Title: sum_reverse_n_even_for
"""
Write a Python function that takes an integer n as input and returns the sum of all even numbers from n to 0 inclusive, using a for loop.
 
sum_reverse_n_even_for(5) -> 6

sum_reverse_n_even_for(3) -> 2

sum_reverse_n_even_for(1) -> 0
"""


def sum_reverse_n_even_for(n: int) -> int:
	sum = 0
	for i in range(n, -1, -1):
	  if i % 2 == 0:
	    sum += i
	return sum


# Title: sum_reverse_n_even_while
"""
Write a Python function that takes an integer n as input and returns the sum of all even numbers from n to 0 inclusive, using a while loop.
 
sum_reverse_n_even_while(5) -> 6

sum_reverse_n_even_while(3) -> 2

sum_reverse_n_even_while(1) -> 0
"""


def sum_reverse_n_even_while(n: int) -> int:
	sum = 0
	while n > 0:
	  if n % 2 == 0:
	    sum += n
	  n -= 1
	return sum


# Title: sum_reverse_n_odd_for
"""
Write a Python function that takes an integer n as input and returns the sum of all odd numbers from n to 0, using a for loop.
 
sum_reverse_n_odd_for(5) -> 9

sum_reverse_n_odd_for(3) -> 4

sum_reverse_n_odd_for(1) -> 1
"""


def sum_reverse_n_odd_for(n: int) -> int:
	sum = 0
	for i in range(n, -1, -1):
	  if i % 2 != 0:
	    sum += i
	return sum


# Title: sum_reverse_n_odd_while
"""
Write a Python function that takes an integer n as input and returns the sum of all odd numbers from n to 1 inclusive, using a while loop.
 
sum_reverse_n_odd_while(5) -> 9

sum_reverse_n_odd_while(3) -> 4

sum_reverse_n_odd_while(1) -> 1
"""


def sum_reverse_n_odd_while(n: int) -> int:
	sum = 0
	while n > 0:
	  if n % 2 != 0:
	    sum += n
	  n -= 1
	return sum


# Title: sum_one_to_n_step
"""
Write a Python function that takes an integer n as input and calculates the sum of all integers from 3 to n, inclusive using a for loop. The function should the return the result.

sum_one_to_n_step(15) -> 45

sum_one_to_n_step(10) -> 18

sum_one_to_n_step(20) -> 63
"""


def sum_one_to_n_step(n: int) -> int:
	sum = 0
	for i in range(3, n+1, 3):
	  sum += i
	return sum


# Title: sum_one_to_n_step_while
"""
Write a Python function that takes an integer n as input and calculates the sum of all integers from 3 to n, inclusive using a while loop. The function should the return the result.

sum_one_to_n_step_while(15) -> 45

sum_one_to_n_step_while(10) -> 18

sum_one_to_n_step_while(20) -> 63
"""


def sum_one_to_n_step_while(n: int) -> int:
	sum = 0
	i = 3
	while i <= n:
	  sum += i
	  i += 3
	return sum


# Title: sum_sequence
"""
Given 2 integers 'x' and 'y', return the sum of all integers in the range of x and y. 

sum_sequence(1, 100) -> 5050 

sum_sequence(5, 36) -> 501
"""


def sum_sequence(x: int, y: int) -> int:
  sum = 0
  for i in range(x, y+1):
    sum = sum + i
  return sum


# Title: return_quarters
"""
Given an integer called 'change', use a while loop to determine how many quarters will be given as 'change'. 

return_quarters(76) -> 3 

return_quarters(29) -> 1
"""


def return_quarters(change: int) -> int:
	quarter = 0
	while change >= 25:
	  quarter = quarter + 1
	  change = change - 25
	return quarter


# Title: count_digits
"""
Given a integer 'n', return how many digits 'n' has. 

count_digits(3278) -> 4 

count_digits(67766776) -> 8
"""


def count_digits(n: int) -> int:
	n_of_digits = 0
	while n > 0:
	  n_of_digits = n_of_digits + 1
	  n = n // 10
	return n_of_digits


# Title: sum_digits
"""
Given a integer 'n', return the sum of the digits. 

sum_digits(3278) -> 20 

sum_digits(67766776) -> 52
"""


def sum_digits(n: int) -> int:
	sum = 0
	while n > 0:
	  lastDigit = n % 10
	  sum = sum + lastDigit
	  n = n // 10
	return sum


# Title: sum_every_other_digit
"""
Given an integer 'n', return the sum of every other digit starting from the last digit. 

sum_every_other_digit(3278) -> 10 

sum_every_other_digit(1039) -> 9
"""


def sum_every_other_digit(n: int) -> int:
	sum = 0
	while n > 0:
	  lastDigit = n % 10
	  sum = sum + lastDigit
	  n = n // 100
	return sum


# Title: sum_every_other_digit_two
"""
Given an integer 'n', return the sum of every other digit starting from second to last digit. 

sum_every_other_digit_two(3278) -> 10 

sum_every_other_digit_two(1039) -> 4
"""


def sum_every_other_digit_two(n: int) -> int:
	sum = 0
	n = n // 10
	
	while n > 0:
	  lastDigit = n % 10
	  sum = sum + lastDigit
	  n = n // 100
	return sum


