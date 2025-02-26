# Title: alarm_clock

"""
Given a day of the week encoded as 0=Sun, 1=Mon, 2=Tue, ...6=Sat, and a boolean indicating if we are on vacation, return a string of the form "7:00" indicating when the alarm clock should ring. Weekdays, the alarm should be "7:00" and on the weekend it should be "10:00". Unless we are on vacation -- then on weekdays it should be "10:00" and weekends it should be "off".

alarm_clock(1, False) → '7:00'
alarm_clock(0, False) → '10:00'
alarm_clock(6, True) → 'off'
"""

def alarm_clock(day: int, vacation: bool) -> str:
    return

# Test your code (copy and past this block of code to test your solution)
print(alarm_clock((1, False)))  # Output: '7:00'
print(alarm_clock((5, False)))  # Output: '7:00'
print(alarm_clock((0, False)))  # Output: '10:00'
print(alarm_clock((6, False)))  # Output: '10:00'
print(alarm_clock((0, True)))  # Output: 'off'
print(alarm_clock((6, True)))  # Output: 'off'
print(alarm_clock((2, True)))  # Output: '10:00'
print(alarm_clock((3, True)))  # Output: '10:00'
