def main():
    fraction = input("Fraction: ")
    fraction_converted = convert(fraction)
    output = gauge(fraction_converted)
    print(output)

def convert(fraction):
    while True:
        try:
            # Try to split the fuel
            numerator, denominator = fraction.split("/")
            # Convert into integers
            new_numerator = int(numerator)
            new_denominator = int(denominator)
            # Calculate the percentage
            f = new_numerator / new_denominator
            # Check if its less than 1 and stop the loop
            if f <= 1:
                # Multiply percentage by 100
                p = int(f * 100)
                return p
            else:
                fraction = input("Fraction: ")
                pass
        except (ValueError,ZeroDivisionError):
            raise

def gauge(percentage):
    # Check if percentage is less than 1, return E
    if percentage <= 1:
        return "E"
    # Check if percentage is greater than 99, return F
    elif percentage >= 99:
        return "F"
    # Otherwise, return the %
    else:
        return str(percentage) + "%"


if __name__ == "__main__":
    main()
