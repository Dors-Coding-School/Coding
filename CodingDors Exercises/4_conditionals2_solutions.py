# Title: should_take_umbrella
"""
The parameter 'is_raining' is True if it is raining, and the parameter 'is_sunny' is True if we have a sunny day. We should take an umbrella if it is not sunny or it is raining. Return True if we should take an umbrella.

should_take_umbrella(False, False) → False

should_take_umbrella(True, False) → True

should_take_umbrella(False, True) → False
"""


def should_take_umbrella(is_raining: bool, is_sunny: bool)->bool:
    if is_raining == True or is_sunny == False:
        return True
    else:
        return False


# Title: team_trouble
"""
Suppose we have a team of employees, and the parameters 'employee_a' and 'employee_b' indicate if each employee is present or absent from work. We are in trouble if both employees are absent or if both employees are present. Write a function to return True if we are in trouble.

team_trouble(False, False) → True

team_trouble(True, False) → False

team_trouble(True, True) → True
"""


def team_trouble(employee_a: bool, employee_b: bool)-> bool:
    if employee_a == True and employee_b == True:
        return True
    elif employee_a == False and employee_b == False:
        return True
    else:
        return False


# Title: sum_or_half_sum
"""
Write a Python function that takes two input integers 'a' and 'b', and returns their sum unless the two values are the same, in which case it should return half of their sum. For instance, if 'a' is 4 and 'b' is 5, the function should return 9. If 'a' and 'b' are both 3, the function should return 3.

sum_or_half_sum(4, 5) -> 9

sum_or_half_sum(3, 3) -> 3
"""


def sum_or_half_sum(a: int, b: int)-> int:
    if a != b:
        return a + b
    else:
        return a


# Title: absolute_difference
"""
Write a Python function that takes two input numbers 'a' and 'b', and returns the absolute difference between them. However, if the absolute difference is greater than 10, the function should return double the absolute difference instead. For instance, if 'a' is 4 and 'b' is 8, the function should return 4. If 'a' is 10 and 'b' is 25, the function should return 30.

absolute_difference(4, 8) -> 4

absolute_difference(10, 25) -> 30
"""


def absolute_difference(a: int, b: int)-> int:
    if abs(a - b) > 10:
        return abs(a - b) * 2
    else:
        return abs(a - b)


# Title: dog_trouble
"""
We have a playful dog that barks loudly at night. The 'hour' parameter is the current hour time in the range 0...23. We are in trouble if the dog is barking and the hour is before 6 or after 22. Return True if we are in trouble.

dog_trouble(True, 5) → True

dog_trouble(True, 7) → False

dog_trouble(False, 6) → False
"""


def dog_trouble(barking: bool, hour: int)-> bool:
    if barking == True and (hour <= 6 or hour >= 22):
        return True
    else:
        return False


# Title: near_ten
"""
Given an int 'n', return True if it is within 10 of 50. 
Note: abs(num) computes the absolute value of a number.

near_ten(48) → True

near_ten(55) → True

near_ten(5) → False
"""


def near_ten(n: int)->bool:
    c = abs(n - 50)
    if c <= 10:
        return True
    else:
        return False


# Title: hi_string
"""
Given a string 's', return a new string where "hi " has been added to the front. However, if the string already begins with "hi", return the string unchanged.

hi_string('Alice') → 'hi Alice'

hi_string('hi Bob') → 'hi Bob'

hi_string('') → 'hi'
"""


def hi_string(s: str)-> str:
	if s[0:2] == 'hi':
		return s
	else:
	  	return 'hi ' + s


# Title: front5
"""
Given a string 's', we'll say that the front is the first 5 chars of the string. If the string length is less than 5, the front is whatever is there. Return a new string which is 5 copies of the front.

front5('Python') → 'PythoPythoPythoPythoPytho'

front5('Chocolate') → 'ChocoChocoChocoChocoChoco'

front5('abc') → 'abcabcabcabcabc'
"""


def front5(s: str)-> str:
	first = s[:5]
	return first * 5


# Title: caught_speeding
"""
You are driving a little too fast, and a police officer stops you. Write a function to return the result, encoded as an int value: 0=no ticket, 1=small ticket, 2=big ticket. 

If speed is 60 or less, the result is 0. If speed is between 61 and 80 inclusive, the result is 1. If speed is 81 or more, the result is 2. Unless it is your birthday -- on that day, your speed can be 5 higher in all cases.

caught_speeding(60, False) → 0
caught_speeding(65, False) → 1
caught_speeding(100, True) → 2
"""


def caught_speeding(speed: int, is_birthday: bool) -> int:
  if is_birthday:
    speed -= 5
  if speed <= 60:
    return 0
  elif 61 <= speed <= 80:
    return 1
  else:
    return 2


# Title: alarm_clock
"""
Given a day of the week encoded as 0=Sun, 1=Mon, 2=Tue, ...6=Sat, and a boolean indicating if we are on vacation, return a string of the form "7:00" indicating when the alarm clock should ring. Weekdays, the alarm should be "7:00" and on the weekend it should be "10:00". Unless we are on vacation -- then on weekdays it should be "10:00" and weekends it should be "off".

alarm_clock(1, False) → '7:00'
alarm_clock(0, False) → '10:00'
alarm_clock(6, True) → 'off'
"""


def alarm_clock(day: int, vacation: bool) -> str:
	if vacation:
		if day == 0 or day == 6:
			return "off"
		else:
			return "10:00"
	else:
		if day == 0 or day == 6:
			return "10:00"
		else:
			return "7:00"


# Title: love_six
"""
The number 6 is a truly great number. Given two int values, a and b, return True if either one is 6. Or if their sum or difference is 6.

love_six(6, 4) → True
love_six(4, 5) → False
love_six(1, 5) → True
"""


def love_six(a: int, b: int) -> bool:
	if a == 6 or b == 6 or a + b == 6 or abs(a - b) == 6:
		return True
	else:
	  	return False


# Title: in_one_to_ten
"""
Given a number n, return True if n is in the range 1..10, inclusive. Unless "outside_mode" is True, in which case return True if the number is less or equal to 1, or greater or equal to 10.

in_one_to_ten(5, True) → True
in_one_to_ten(11, False) → False
in_one_to_ten(1, True) → True
"""


def in_one_to_ten(n: int, outside_mode: bool) -> bool:
	if outside_mode and (n <= 1 or n >= 10):
		return True
	else:
		if 1 < n < 10:
			return True
		else:
			return False


# Title: near_ten_bool
"""
Given a non-negative number "num", return True if num is within 2 of a multiple of 10. Note: (a % b) is the remainder of dividing a by b, so (7 % 5) is 2.

near_ten_bool(12) → True
near_ten_bool(19) → True
near_ten_bool(23) → False
"""


def near_ten_bool(num: int) -> bool:
	if num % 10 >= 8 or num % 10 <= 2:
		return True
	else:
	  	return False


# Title: teen_sum
"""
Given 2 ints, a and b, return their sum. However, "teen" values in the range 13..19 inclusive, are extra lucky. So if either value is a teen, just return 19.

teen_sum(10, 13) → 19 
teen_sum(2, 3) →  5
teen_sum(9, 0) → 9
"""


def teen_sum(a: int, b: int) -> int:
	if 13 <= a <= 19 or 13 <= b <= 19:
		return 19
	else:
		return a + b


# Title: answer_cell
"""
Your cell phone rings. Return True if you should answer it. Normally you answer, except in the morning you only answer if it is your mom calling. In all cases, if you are asleep, you do not answer.

answer_cell(False, True, True) → False
answer_cell(True, True, True) → False
answer_cell(False, False, False) → True
"""


def answer_cell(is_morning: bool, is_mom: bool, is_asleep: bool) -> bool:
	if is_asleep:
		return False
	elif is_morning and not is_mom:
		return False
	return True


# Title: tea_party
"""
We are having a party with amounts of tea and candy. Return the int outcome of the party encoded as 0=bad, 1=good, or 2=great. A party is good (1) if both tea and candy are at least 5. However, if either tea or candy is at least double the amount of the other one, the party is great (2). However, in all cases, if either tea or candy is less than 5, the party is always bad (0).

tea_party(5, 5) → 1
tea_party(10, 5) → 2
tea_party(4, 5) → 0
"""


def tea_party(tea: int, candy: int) -> int:
	if tea < 5 or candy < 5:
		return 0
	elif tea >= 2 * candy or candy >= 2 * tea:
		return 2
	else:
	  	return 1


# Title: fizz_string
"""
Given a string str, if the string starts with "f" return "Fizz". If the string ends with "b" return "Buzz". If both the "f" and "b" conditions are true, return "FizzBuzz". In all other cases, return the string unchanged.

fizz_string('fizz') → 'Fizz'
fizz_string('buzzb') → 'Buzz'
fizz_string('fizzb') → 'FizzBuzz'
fizz_string('abcdefg') → 'abcdefg'
"""


def fizz_string(s: str) -> str:
	if s[0] == "f" and s[-1] == "b":
		return "FizzBuzz"
	elif s[0] == "f":
		return "Fizz"
	elif s[-1] == "b":
		return "Buzz"
	else:
	  	return s


# Title: max_mod5
"""
Given two int values, return whichever value is larger. However, if the two values have the same remainder when divided by 5, then the return the smaller value. However, in all cases, if the two values are the same, return 0.

max_mod5(10, 5) → 5
max_mod5(20, 15) → 15
max_mod5(10, 10) → 0
"""


def max_mod5(a: int, b: int) -> int:
	ra = a % 5
	rb = b % 5
	if ra == rb:
		if a > b:
			return b
		elif a < b:
			return a
		else:
			return 0
	else:
		if a > b:
			return a
		else:
			return b


# Title: grade_convertor
"""
Write a function grade_convertor(grade) that takes a grade as a percentage (0-100) and returns a string: "Fail" if the grade is less than 40, "Pass" if the grade is between 40 and 60, and "Excellent" if the grade is more than 60.

grade_convertor(30) -> 'Fail'
grade_convertor(40) -> 'Pass'
grade_convertor(60) -> 'Excellent'
"""


def grade_convertor(grade: int) -> str:
	if grade < 40:
		return 'Fail'
	elif 40 <= grade < 60:
		return 'Pass'
	else:
		return 'Excellent'


# Title: check_temperature
"""
Write a function check_temperature(temp) that takes a temperature as input (in Fahrenheit) and returns "Hot" if the temperature is above 80 degrees, "Warm" if the temperature is between 60 and 80 degrees, "Cool" if the temperature is between 40 and 60 degrees, and "Cold" if the temperature is below 40 degrees.

check_temperature(30) -> 'Cold'
check_temperature(40) -> 'Cool'
check_temperature(60) -> 'Warm'
check_temperature(80) -> 'Hot'
"""


def check_temperature(temp: int) -> str:
	if temp < 40:
		return 'Cold'
	elif 40 <= temp < 60:
		return 'Cool'
	elif 60 <= temp < 80:
		return 'Warm'
	else:
		return 'Hot'


