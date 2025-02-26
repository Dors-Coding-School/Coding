# Title: first_character
"""
Write a function that returns the first character of a given string.

first_character('hello') -> 'h'

first_character('world') -> 'w'

first_character('CodingDors') -> 'C'
"""


def first_character(s: str) -> str:
    first = s[0]
    return first


# Title: second_character
"""
Write a function that returns the second character of a given string.

second_character('hello') -> 'e'

second_character('world') -> 'o'

second_character('CodingDors') -> 'o'
"""


def second_character(s: str) -> str:
    second = s[1]
    return second


# Title: last_character
"""
Write a function that returns the last character of a given string.

last_character('hello') -> 'o'

last_character('world') -> 'd'

last_character('CodingDors') -> 's'
"""


def last_character(s: str) -> str:
    return s[-1]


# Title: concatenate_strings
"""
Write a function that concatenates two given strings.

concatenate_strings('hello', 'world') -> 'helloworld'

concatenate_strings('Coding', 'Dors') -> 'CodingDors'

concatenate_strings('apple', 'banana') -> 'applebanana'
"""


def concatenate_strings(s1: str, s2: str) -> str:
	return s1 + s2


# Title: repeat_string
"""
Write a function that repeats a given string n times.

repeat_string('hi', 3) -> 'hihihi' 

repeat_string('code', 2) -> 'codecode' 

repeat_string('a', 5) -> 'aaaaa'
"""


def repeat_string(s: str, n: int) -> str:
	return s * n


# Title: uppercase_first
"""
Write a function that returns the given string with its first character in uppercase.

uppercase_first('hello') -> 'Hello'

uppercase_first('coding') -> 'Coding'

uppercase_first('leo') -> 'Leo'
"""


def uppercase_first(s: str) -> str:
	first = s[0].upper()
	others = s[1:]
	return first + others


# Title: lowercase_first
"""
Write a function that returns the given string with its first character in lowercase.

lowercase_first('Hello') -> 'hello'

lowercase_first('CODING') -> 'cODING'

lowercase_first('LeO') -> 'leO'
"""


def lowercase_first(s: str) -> str:
	first = s[0].lower()
	others = s[1:]
	return first + others


# Title: replace_char
"""
Write a function that replaces all occurrences of a specified character in a given string with another character.

replace_char('hello', 'l', 'w') -> 'hewwo'

replace_char('APPLE', 'P', 'Z') -> 'AZZLE'

replace_char('banana', 'a', '4') -> 'b4n4n4'
"""


def replace_char(s: str, old_char: str, new_char: str) -> str:
	return s.replace(old_char, new_char)


# Title: remove_char
"""
Write a function that removes all occurrences of a specified character in a given string.

remove_char('hello', 'l') -> 'heo'

remove_char('apple', 'e') -> 'appl'

remove_char('BANANA', 'A') -> 'BNN'
"""


def remove_char(s: str, char_to_remove: str) -> str:
	return s.replace(char_to_remove, "")


# Title: string_length
"""
Write a function that returns the length of a given string.

string_length('hello') -> 5

string_length('code') -> 4

string_length('CodingDors') -> 10
"""


def string_length(s: str) -> int:
	return len(s)


# Title: substring
"""
Write a function that returns a substring of a given string, starting from the specified start index and ending with the specified end index.

substring('hello', 1, 2) -> 'el'

substring('CodingDors', 6, 9) -> 'Dors'

substring('applebananaorange', 5, 10) -> 'banana'
"""


def substring(s: str, start: int, end: int) -> str:
	sub = s[start:end+1]
	return sub


# Title: remove_whitespace_str
"""
Write a function that removes all leading and trailing whitespace from a given string.

remove_whitespace_str('     hello') -> 'hello'

remove_whitespace_str('apple     ') -> 'apple'

remove_whitespace_str('      CodingDors      ') -> 'CodingDors'
"""


def remove_whitespace_str(s: str) -> str:
	return s.replace(" ", "")


# Title: birthdate
"""
Given two strings 'day' and 'month', return a new string with the birth date. 

Hint: birth date should be in the format 'month/day'

birthdate('03', '07') -> '07/03'

birthdate('29', '06') -> '06/29'

birthdate('01', '05') -> '05/01'
"""


def birthdate(day: str, month: str) -> str:
	return month + "/" + day


# Title: formatted_time
"""
Given two strings 'hour' and 'minute', return a new string with the formatted time.

Hint: the time should be in the format 'hour:minute'

formatted_time('10', '15') -> '10:15'

formatted_time('05', '30') -> '05:30'

formatted_time('20', '00') -> '20:00'
"""


def formatted_time(hour: str, minute: str) -> str:
	return hour + ":" + minute


# Title: full_name
"""
Given two strings 'firstName' and 'lastName', return a new string with the full name.

Hint: the full name should be in the format 'firstName lastName'

full_name('John', 'Doe') -> 'John Doe'

full_name('Emma', 'Watson') -> 'Emma Watson'

full_name('Elon', 'Musk') -> 'Elon Musk'
"""


def full_name(firstName: str, lastName: str) -> str:
	return firstName + " " + lastName


# Title: year_day
"""
Given two strings 'day' and 'year', return a new string with the year and day of the year.

Hint: the output should be in the format 'year-day'

year_day('364', '2022') -> '2022-364'

year_day('1', '2030') -> '2030-1'

year_day('123', '2021') -> '2021-123'
"""


def year_day(day: str, year: str) -> str:
	return year + "-" + day


# Title: initials
"""
Write a function that takes two string parameters, 'firstName' and 'lastName'. The function should return a string that displays the initial of the first and last name.

Hint: The output should be in the format 'F.L.' where F is the first letter of firstName and L is the first letter of lastName.

initials('John', 'Doe') -> 'J.D.'

initials('Emma', 'Watson') -> 'E.W.'

initials('Elon', 'Musk') -> 'E.M.'
"""


def initials(firstName: str, lastName: str) -> str:
	initialFirst = firstName[0]
	initialLast = lastName[0]
	return initialFirst + '.' + initialLast + '.'


# Title: get_extension
"""
Write a function get_extension() that accepts a file name as a string and returns the file extension. The file name will always have an extension and will not contain any spaces.

Hint: all the extensions will end with a dot (.) and 3 letters.

get_extension('image.jpg') -> 'jpg'

get_extension('document.pdf') -> 'pdf'

get_extension('hello.txt') -> 'txt'
"""


def get_extension(file: str) -> str:
	extension = file[len(file)-3:]
	return extension


# Title: missing_chars
"""
Write a Python function that takes a string 's' and two integers 'a' and 'b', and returns a new string where the character at index 'a' and the character at index 'b' have been removed.  For example, if the string 's' is 'hello' and 'a' is 1 and 'b' is 3, the function should return the string 'hlo', where the characters at indices 1 and 3 (i.e. 'e' and 'l') have been removed.

missing_chars('hello', 1, 3) -> 'hlo'

missing_chars('coding', 0, 4) -> 'odig'
"""


def missing_chars(s: str,a: int,b: int)-> str:
    first = s[0:a]
    middle = s[a+1:b]
    last = s[b+1:]
    return first + middle + last


# Title: front_back
"""
Given a string 's', return a new string where the first and last chars have been exchanged.

front_back('code') → 'eodc'

front_back('a') → 'a'
"""


def front_back(s: str)-> str:
    first = s[0]
    last = s[-1]
    middle = s[1:-1]
    return last + middle + first


