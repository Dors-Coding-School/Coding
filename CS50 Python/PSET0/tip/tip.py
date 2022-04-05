def main():
    dollars = dollars_to_float(input("How much was the meal? "))
    percent = percent_to_float(input("What percentage would you like to tip? "))
    tip = dollars * percent
    print(f"Leave ${tip:.2f}")


def dollars_to_float(d):
    # TODO
    without_dollar_sign_d = d.replace("$","")
    return float(without_dollar_sign_d)


def percent_to_float(p):
    # TODO
    without_percentage_sign_p = p.replace("%","")
    p_times_100 = float(without_percentage_sign_p) / 100
    return p_times_100


main()
