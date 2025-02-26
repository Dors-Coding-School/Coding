# Title: return_two
"""
This is a problem to get you started on CodingDors. 

On the second line, write 'return 2' (without the single quotes) and click on Run.

Remember do not use print! All our problems require a return at the end of it.
"""


def return_two():
    return 2


# Title: return_n
"""
Write a function that takes one argument called 'n' and always returns n back.

An argument is a fancy programming word for an input. In the background we are sending different inputs to check if the code you wrote is correct.

For example,  

If the inputs is 2, we expect 2 back. If you don't understand check the "Show Solution" button.
"""


def return_n(n: int) -> int:
    return n


# Title: convert_seconds
"""
Given an integer 'n' that represents the minutes, return how many seconds that amount of minutes represent.

Hint: 1 minute = 60 seconds

convert_seconds(24) -> 1440
convert_seconds(59) -> 3540
convert_seconds(9) -> 540
"""


def convert_seconds(n: int)->int:
	return n * 60


# Title: convert_lb_to_kg
"""
Given a float 'n' that represents the weight in pounds (lb), return the weight converted to kilograms (kg).

Hint: 1 kg = lb * 0.453592

convert_lb_to_kg(10) -> 4.54
convert_lb_to_kg(180) -> 81.65
convert_lb_to_kg(220) -> 99.79
"""


def convert_lb_to_kg(lb: int)->float:
	return lb * 0.453592


# Title: convert_fahrenheit_to_celsius
"""
Given a float 'n' that represents the temperature in Fahrenheit, return the temperature converted to Celsius.

Hint: 1 Celsius = (Fahrenheit - 32) * 5/9

convert_fahrenheit_to_celsius(212) -> 100.0
convert_fahrenheit_to_celsius(194) -> 90.0
convert_fahrenheit_to_celsius(302) -> 150.0
"""


def convert_fahrenheit_to_celsius(n: float) -> float:
	return (n - 32) * 5/9


# Title: convert_celsius_to_kelvin
"""
Given a float 'n' that represents the temperature in Celsius, return the temperature converted to Kelvin.

Hint: 1 Kelvin = Celsius + 273.15

convert_celsius_to_kelvin(100) -> 373.15
convert_celsius_to_kelvin(170) -> 443.15
convert_celsius_to_kelvin(50) -> 323.15
"""


def convert_celsius_to_kelvin(n: int)->float:
	return n + 273.15


# Title: calculate_average
"""
Given 3 integers 'n1', 'n2' and 'n3', return the average of those 3 numbers.

calculate_average(5, 10, 15) -> 10.00
calculate_average(1, 1, 7) -> 3.00
calculate_average(-1, -5, -9) -> - 3.00
"""


def calculate_average(n1: int, n2: int, n3:int)->float:
	return (n1 + n2 + n3)/3


# Title: volume_of_cylinder
"""
Given an integer 'height' and an integer 'diameter', return the volume of a cylinder given its height and diameter. The volume will be in a format of a float.

Hint: the formula to calculate the volume of a cylinder is 3.14 * (diameter/2)^2 * height.

volume_of_cylinder(10, 4) -> 125.6
volume_of_cylinder(5, 2) -> 15.70
volume_of_cylinder(7, 4) -> 87.92
"""


def volume_of_cylinder(height: int, diameter: int)->float:
	return 3.14 * (diameter/2)**2 * height


# Title: calculate_area_of_circle
"""
Given an integer 'n' that represents the radius of a circle, return the area of the circle.

Hint: the formula to calculate the area of a circle is 3.14 * radius^2

calculate_area_of_circle(5) -> 78.5
calculate_area_of_circle(2) -> 12.56
calculate_area_of_circle(9) -> 254.34
"""


def calculate_area_of_circle(n: int)->float:
	return 3.14 * n**2


# Title: calc_bmi
"""
Given an integer 'weight' and an integer 'height', return the Body Mass Index (BMI) of the person. The BMI will be in a format of a float.

Hint: the formula to calculate BMI is weight / (height/100)^2.

calc_bmi(75, 180) -> 23.15
calc_bmi(90, 190) -> 24.93
calc_bmi(80, 170) -> 27.68
"""


def calc_bmi(weight: int, height: int)->float:
	return weight / (height/100)**2


# Title: return_hello
"""
Given a string 's', return a new string with the word "hello" in front. 

return_hello("Gi") -> "hello Gi" 

return_hello("Leo") -> "hello Leo"
"""


def return_hello(s: str)-> str:
	return 'hello ' + s


# Title: return_person_details
"""
Write a Python function that takes two input strings 'name' and 'age', and returns a new string in the following format: '''name'' is ''age'''. For instance, if the name is 'Maria' and the age is 20, the function should return 'Maria is 20'.

return_person_details('Maria', 20) -> 'Maria is 20'

return_person_details('Gi', 25) -> 'Gi is 25'
"""


def return_person_details(name: str,age: str)->str:
    return name + " is " + age


# Title: title_movie
"""
Write a Python function that takes a string 'movie' and returns a new string with every word in the movie name capitalized. For instance, if the movie name is 'the lord of the rings', the function should return 'The Lord Of The Rings'.

title_movie('the lord of the rings') -> 'The Lord Of The Rings'

title_movie('star wars') -> 'Star Wars'
"""


def title_movie(movie: str)-> str:
    upper = movie.title()
    return upper


# Title: upper_movie
"""
Write a Python function that takes a string 'movie' and returns a new string with every character in the movie name converted to uppercase. For instance, if the movie name is 'The Lord of the Rings', the function should return 'THE LORD OF THE RINGS'.

upper_movie('The Lord of the Rings') -> 'THE LORD OF THE RINGS'

upper_movie('star wars') -> 'STAR WARS'
"""


def upper_movie(movie: str)->str:
    final = movie.upper()
    return final


# Title: lower_movie
"""
Write a Python function that takes a string 'movie' and returns a new string with every character in the movie name converted to lowercase. For instance, if the movie name is 'The Lord of the Rings', the function should return 'the lord of the rings'.

lower_movie('The Lord of the Rings') -> 'the lord of the rings'

lower_movie('STAR WARS') -> 'star wars'
"""


def lower_movie(movie: str)->str:
    result = movie.lower()
    return result


# Title: remove_whitespace
"""
Given a string 's', return a new string without leading or trailing whitespace. 

remove_whitespace("     hi there") -> "hi there" 

remove_whitespace("hello world       ") -> "hello world"
"""


def remove_whitespace(s: str)->str:
    result = s.strip()
    return result


# Title: replace_words
"""
Write a Python function that takes three input strings 'a', 'b', and 'c', and returns a new string obtained by replacing all occurrences of the string 'b' in the string 'a' with the string 'c'. For instance, if the string 'a' is 'the quick brown fox jumps over the lazy dog', string 'b' is 'fox', and string 'c' is 'cat', the function should return 'the quick brown cat jumps over the lazy dog'.

replace_words('the quick brown fox jumps over the lazy dog', 'fox', 'cat') -> 'the quick brown cat jumps over the lazy dog'
"""


def replace_words(a: str,b:str,c: str)->str:
    jump = a.replace(b, c)
    return jump


# Title: round_floats
"""
Given a float 'n', return the number with only two decimal places. 

round_floats(3.141) -> 3.14 

round_floats(75.123456) -> 75.12
"""


def round_floats(n: float)->float:
    result = round(n, 2)
    return result


# Title: remove_letter_g
"""
Write a Python function that takes a string 's' and returns a new string obtained by removing all occurrences of the letter 'g' from the string. For instance, if the string is 'going to the grocery store', the function should return 'oin to the rocery store'.

remove_letter_g('going to the grocery store') -> 'oin to the rocery store'
"""


def remove_letter_g(s: str)->str:
    return s.replace("g","")


# Title: convert_miles
"""
Given an integer 'n', return the kilometers that this number of miles represents. Hint: 1 mile = 1.60934 kilometers. 

convert_miles(1) -> 1.60934 

convert_miles(0.4) -> 0.643736
"""


def convert_miles(n: float)->float:
    return n * 1.60934


