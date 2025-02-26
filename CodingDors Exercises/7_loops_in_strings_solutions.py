# Title: count_char
"""
Write a function that counts the occurrences of a specified character in a given string.

count_char('hello', 'l') -> 2

count_char('code', 'd') -> 1

count_char('banana', 'a') -> 3
"""


def count_char(s: str, char_to_count: str) -> int:
	count = 0
	
	for i in s:
	  if i.lower() == char_to_count.lower():
	    count = count + 1
	return count


# Title: count_lower_letters
"""
Write a function that counts the number of lowercase letters present in a given string 's'.

count_lower_letters("Hello World") → 8
count_lower_letters("LOWERCASE") → 0
count_lower_letters("MixedCase123") → 5
"""


def count_lower_letters(s: str) -> int:
	count = 0
	for i in s:
	  if i.islower() == True:
	    count = count + 1
	return count


# Title: count_vowels_str
"""
Write a function that counts the number of vowels in a given string.

count_vowels_str('hello') -> 2

count_vowels_str('codingDORS') -> 3

count_vowels_str('APPLEbanana') -> 5
"""


def count_vowels_str(s: str) -> int:
	vowels = ['a', 'e', 'i', 'o', 'u']
	count = 0
	
	for i in s:
	  if i.lower() in vowels:
	    count = count + 1
	return count


# Title: count_consonants_str
"""
Write a function that counts the number of consonants in a given string.

count_consonants_str('hello') -> 3

count_consonants_str('codingDORS') -> 7

count_consonants_str('APPLEbanana') -> 6
"""


def count_consonants_str(s: str) -> int:
	vowels = ['a', 'e', 'i', 'o', 'u']
	count = 0
	
	for i in s:
	  if i.lower() not in vowels:
	    count = count + 1
	return count


# Title: find_char
"""
Write a function that returns the index of the first occurrence of a specified character in a given string or -1 if the character is not present.

find_char('banana', 'b') -> 0

find_char('hello', 'l') -> 2

find_char('code', 'a') -> -1
"""


def find_char(s: str, char_to_find: str) -> int:
  for i in range(len(s)):
  	if char_to_find.lower() in s[i].lower():
  	   return i
  
  return -1


# Title: contains_special_chars
"""
Write a function that checks if the string contains either an exclamation mark (!) or a question mark (?). The function should return True if either (or both) of these characters are present, and False otherwise.

contains_special_chars("Hello! Welcome") → True
contains_special_chars("What is your name") → False
contains_special_chars("How are you?") → True
"""


def contains_special_chars(s: str) -> bool:
	for i in s:
	  if i == '!' or i == '?':
	    return True
	return False


# Title: find_uppercase_position
"""
Write a function that returns the position (index) of the first uppercase letter in a given string 's'. If there are no uppercase letters in the string, the function should return -1.

find_uppercase_position("hello World") → 6
find_uppercase_position("nouppercasehere") → -1
find_uppercase_position("CodingDors") → 0
"""


def find_uppercase_position(s: str) -> int:
	for i in range(len(s)):
	  if s[i].isupper():
	    return i
	return -1


# Title: extract_uppercase
"""
Write a function that extracts all the uppercase letters from the given string 's' and return them as a new string in the order they appear.

extract_uppercase("Hello World") → "HW"
extract_uppercase("nouppercasehere") → ""
extract_uppercase("CODINGDORS") → "CODINGDORS"
"""


def extract_uppercase(s: str) -> str:
    word = ''
    for i in s:
      if i.isupper():
        word = word + i
    return word


# Title: replace_a_with_four
"""
Write a function that returns a new string where every instance of the letter 'a' (both uppercase and lowercase) in the given string 's' is replaced with the number '4'.

replace_a_with_four("Banana") → "B4n4n4"
replace_a_with_four("Apples are Amazing!") → "4pples 4re 4m4zing!"
replace_a_with_four("CodingDors") → "CodingDors"
"""


def replace_a_with_four(s: str) -> str:
	word = ''
	for i in s:
	  if i.lower() == 'a':
	    word = word + '4'
	  else:
	    word = word + i
	return word


# Title: replace_upper
"""
Write a function that returns a new string where every uppercase letter from the given string 's' is replaced with an underscore (_).

replace_upper("helloWorld") → "hello_orld"
replace_upper("replaceUppeR") → "replace_ppe_"
replace_upper("cOdInG") → "c_d_n_"
"""


def replace_upper(s: str) -> str:
	word = ''
	for i in s:
	  if i.isupper():
	    word = word + '_'
	  else:
	    word = word + i
	return word


# Title: triple_char
"""
Given a string 's', return a new string where for every char in the original, there are three chars.

triple_char('The') → 'TTThhheee'
triple_char('Abc') → 'AAAbbbccc'
triple_char('code') → 'cccooodddeee'
"""


def triple_char(s: str) -> str:
	word = ''
	for i in s:
	  word = word + (i * 3)
	return word


# Title: hi_ho
"""
Return True if the string "hi" and "ho" appear the same number of times in the given string.

hi_ho('hiho') → True
hi_ho('hihi') → False
hi_ho('1hi1hohello') → True
"""


def hi_ho(s: str) -> bool:
	count_hi = 0
	count_ho = 0
	# Count the 'hi's and 'ho's
	for i in range(len(s)-1):
	  if s[i:i+2] == 'hi':
	    count_hi += 1
	  elif s[i:i+2] == 'ho':
	    count_ho += 1
	# Check if they are the same
	if count_hi == count_ho:
	  return True
	else:
	  return False


# Title: count_code_times
"""
Return the number of times that the string "code" appears anywhere in the given string.

count_code_times('aaacodebbb') → 1
count_code_times('codexxcode') → 2
count_code_times('cozexxcope') → 0
"""


def count_code_times(s: str) -> int:
	count = 0
	for i in range(len(s)-3):
	  if s[i:i+4] == 'code':
	    count += 1
	return count


# Title: swap_case
"""
Write a function that returns a new string with the case of each character in the given string swapped.

swap_case('hello') -> 'HELLO'

swap_case('CODE') -> 'code'

swap_case('aPpLe') -> 'ApPlE'
"""


def swap_case(s: str) -> str:
	word = ''
	
	for i in s:
	  if i.isupper():
	    word = word + i.lower()
	  else:
	    word = word + i.upper()
	return word


# Title: reverse_string
"""
Write a function that takes a string as input and returns the string reversed.

reverse_string('hello') -> 'olleh'

reverse_string('code') -> 'edoc'

reverse_string('banana') -> 'ananab'
"""


def reverse_string(s: str) -> str:
	word = ''
	for i in range(len(s)-1, -1, -1):
	  word = word + s[i]
	return word


# Title: reverse_swap
"""
Write a function that returns a new string that is the reverse of the given string 's', and where the case of each letter in the original string is swapped (i.e., lowercase letters become uppercase and uppercase letters become lowercase).

reverse_swap("Hello") → "OLLEh"
reverse_swap("wOrLd123!") → "!321DlRoW"
reverse_swap("sWAP mE") → "eM pawS"
"""


def reverse_swap(s: str) -> str:
	word = ''
	for i in range(len(s)-1, -1, -1):
	  if s[i].isupper():
	    word += s[i].lower()
	  else:
	    word += s[i].upper()
	return word


# Title: has_matching
"""
Given two strings 's1' and 's2', write a function that determines if the two strings share at least one letter in the same position. The function should return True if they do and False otherwise.

Assume that both strings will have the same length.

has_matching("apple", "abcde") → True
has_matching("hello", "world") → True
has_matching("dance", "lover") → False
"""


def has_matching(s1: str, s2: str) -> bool:
	for i in range(len(s1)):
	  if s1[i] == s2[i]:
	    return True
	return False


# Title: check_first_number
"""
Given a string 's', determine if the first number appearing in the string is 0. The function should return False if the first number in the string is 0. If the string does not contain any numbers or if the first number appearing isn't 0, it should return True.

check_first_number("Hello") → True
check_first_number("Hell0") → False
check_first_number("H3ll0") → True
"""


def check_first_number(s: str) -> bool:
	for i in s:
	  if i.isdigit():
	    if i == '0':
	      return False
	    else:
	      return True
	# If we don't have any number, we need the next line
	return True


# Title: valid_vanity_plate
"""
Given a string 's', determine if, after the first appearance of a number in the string, there are any letters. For a string to be considered valid, once numbers start appearing, they should not be followed by any letters.

valid_vanity_plate("ABC123") → True
valid_vanity_plate("AB12CD") → False
valid_vanity_plate("A1B2") → False
"""


def valid_vanity_plate(s: str) -> bool:
	for i in range(len(s)):
	  if s[i].isdigit():
	    if s[i:].isdigit():
	      return True
	    else:
	      return False
	# If we don't have any number, we should return True
	return True


# Title: split_string
"""
Write a function that splits a given string into a list of words using a specified delimiter.

split_string('apple,banana,orange', ',') -> ['apple', 'banana', 'orange']

split_string('red.green.blue', '.') -> ['red', 'green', 'blue']

split_string('python/java/html', '/') -> ['python', 'java', 'html']
"""


def split_string(s: str, delimiter: str) -> list:
	return s.split(delimiter)


