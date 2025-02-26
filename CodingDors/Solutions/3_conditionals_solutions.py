# Title: is_even
"""
Write a function that checks if a given number is even.

is_even(5) -> False

is_even(10) -> True

is_even(99) -> False
"""


def is_even(n: int) -> bool:
	if n % 2 == 0:
		return True
	else:
		return False


# Title: is_positive
"""
Write a function that checks if a given number is positive.

is_positive(1) -> True

is_positive(-10) -> False

is_positive(19) -> True
"""


def is_positive(n: int) -> bool:
	if n > 0:
		return True
	else:
		return False


# Title: is_divisible
"""
Write a function that checks if a given number is divisible by another number.

is_divisible(8, 2) -> True

is_divisible(5, 3) -> False

is_divisible(21, 7) -> True
"""


def is_divisible(x: int, y: int) -> bool:
	if x % y == 0:
		return True
	else:
		return False


# Title: maximum
"""
Write a function that returns the maximum of two numbers.

maximum(1, 3) -> 3

maximum(7, -3) -> 7

maximum(10, -10) -> 10
"""


def maximum(x: int, y: int) -> int:
	if x > y:
		return x
	else:
		return y


# Title: minimum
"""
Write a function that returns the minimum of two numbers.

minimum(3, 7) -> 3

minimum(-3, -7) -> -7

minimum(10, 110) -> 10
"""


def minimum(x: int, y: int) -> int:
	if x < y:
		return x
	else:
		return y


# Title: absolute_value
"""
Write a function that returns the absolute value of a number.

absolute_value(8) -> 8

absolute_value(-19) -> 19

absolute_value(-37) -> 37
"""


def absolute_value(n: int) -> int:
	return abs(n)


# Title: greater_number
"""
Write a function that returns the greater number of three given numbers.

greater_number(1, 2, 3) -> 3

greater_number(-1, -2, -3) -> -1

greater_number(10, 15, 7) -> 15
"""


def greater_number(x: int, y: int, z: int) -> int:
	if x > y and x > z:
		return x
	elif y > x and y > z:
		return y
	else:
		return z


# Title: is_negative
"""
Write a function that checks if a given number is negative.

is_negative(5) -> False

is_negative(-5) -> True

is_negative(-21) -> True
"""


def is_negative(n: int) -> bool:
	if n < 0:
		return True
	else:
		return False


# Title: is_odd
"""
Write a function that checks if a given number is odd.

is_odd(8) -> False

is_odd(9) -> True

is_odd(-21) -> True
"""


def is_odd(n: int) -> bool:
	if n % 2 != 0:
		return True
	else:
		return False


# Title: is_leap_year
"""
Write a function that checks if a given year is a leap year.

Hint: A leap year is divisible by 4 but not divisible by 100

is_leap_year(2020) -> True

is_leap_year(2021) -> False

is_leap_year(1996) -> True
"""


def is_leap_year(year: int) -> bool:
	div_by_4 = year % 4
	div_by_100 = year % 100
	
	if div_by_4 == 0 and div_by_100 != 0:
		return True
	else:
		return False


# Title: is_vowel
"""
Write a function that checks if a given character is a vowel.

is_vowel('a') -> True

is_vowel('b') -> False

is_vowel('u') -> True
"""


def is_vowel(char: str) -> bool:
	char = char.lower()
	
	if char == 'a' or char == 'e' or char == 'i' or char == 'o' or char == 'u':
		return True
	else:
		return False


# Title: is_consonant
"""
Write a function that checks if a given character is a consonant.

is_consonant('c') -> True

is_consonant('a') -> False

is_consonant('z') -> True
"""


def is_consonant(char: str) -> bool:
	char = char.lower()
	
	if char != 'a' and char != 'e' and char != 'i' and char != 'o' and char != 'u':
		return True
	else:
		return False


# Title: is_uppercase
"""
Write a function that checks if a given character is uppercase.

is_uppercase('a') -> False

is_uppercase('A') -> True

is_uppercase('Z') -> True
"""


def is_uppercase(char: str) -> bool:
	if char.isupper():
		return True
	else:
		return False


# Title: is_lowercase
"""
Write a function that checks if a given character is lowercase.

is_lowercase('a') -> True

is_lowercase('A') -> False

is_lowercase('z') -> True
"""


def is_lowercase(char: str) -> bool:
	if char.islower():
		return True
	else:
		return False


# Title: is_same_letter
"""
Write a function that checks if two given characters are the same letter, regardless of their case.

is_same_letter('a', 'A') -> True

is_same_letter('a', 'b') -> False

is_same_letter('C', 'C') -> True
"""


def is_same_letter(char1: str, char2: str) -> bool:
	char1 = char1.lower()
	char2 = char2.lower()
	
	#or you could you upper() for both variables
	
	if char1 == char2:
		return True
	else:
		return False


# Title: is_digit
"""
Write a function that checks if a given character is a digit.

is_digit(1) -> True

is_digit('a') -> False

is_digit('!') -> False
"""


def is_digit(char: str) -> bool:
	if char.isdigit():
		return True
	else:
		return False


# Title: is_alphabetic
"""
Write a function that checks if a given character is alphabetic.

is_alphabetic('g') -> True

is_alphabetic('1') -> False

is_alphabetic('?') -> False
"""


def is_alphabetic(char: str) -> bool:
	if char.isalpha():
		return True
	else:
		return False


# Title: is_alphanumeric
"""
Write a function that checks if a given character is alphanumeric.

is_alphanumeric('a') -> True

is_alphanumeric('1') -> True

is_alphanumeric('.') -> False
"""


def is_alphanumeric(char: str) -> bool:
	if char.isalnum():
		return True
	else:
		return False


# Title: is_greater_or_equal
"""
Write a function that checks if the first given number is greater than or equal to the second given number.

is_greater_or_equal(3, 3) -> True

is_greater_or_equal(-10, -21) -> True

is_greater_or_equal(1, 10) -> False
"""


def is_greater_or_equal(x: int, y: int) -> bool:
	if x >= y:
		return True
	else:
		return False


# Title: is_smaller_or_equal
"""
Write a function that checks if the first given number is smaller than or equal to the second given number.

is_smaller_or_equal(1, 3) -> True

is_smaller_or_equal(-10, -10) -> True

is_smaller_or_equal(7, 1) -> False
"""


def is_smaller_or_equal(x: int, y: int) -> bool:
	if x <= y:
		return True
	else:
		return False


