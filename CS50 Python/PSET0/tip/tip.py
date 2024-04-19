def main():
    dollars = dollars_to_float(input("How much was the meal? "))
    percent = percent_to_float(input("What percentage would you like to tip? "))
    tip = dollars * percent
    print(f"Leave ${tip:.2f}")


def dollars_to_float(d):
    # Remove "$" from string d
    without_dollar_sign_d = d.replace("$","")
    # Convert string into float
    without_dollar_sign_d = float(without_dollar_sign_d)
    # Return float to store in variable dollars (line 2)
    return without_dollar_sign_d


def percent_to_float(p):
    # Remove "%" from string p
    without_percentage_sign_p = p.replace("%","")
    # Convert string into float
    without_percentage_sign_p = float(without_percentage_sign_p)
    # Convert number to percentage
    p_times_100 = without_percentage_sign_p / 100
    # Return float to store in variable percent (line 3)
    return p_times_100


main()
