def main():
    # Get user input
    msg = input()
    # Call convert function
    result = convert(msg)
    # Print the result
    print(result)

def convert(msg):
    # Replace :) for happy emoji
    msg = msg.replace(":)", '🙂')
    # Replace :( for sad emoji
    msg = msg.replace(":(", '🙁')
    # Return string
    return msg

main()
