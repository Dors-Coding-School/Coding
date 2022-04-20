# Variable to keep track
amount_due = 50

# Loop forever until we break at some point
while True:
    # Print the amount due
    print("Amount Due: ", amount_due)
    # Ask user to insert coin
    coin_inserted = int(input("Insert Coin: "))
    # Check if coin is 25, 10 or 5 cents
    if coin_inserted in [25, 10, 5]:
        # Subtract value from amount_due
        amount_due -= coin_inserted
        # Check if amount_due is less or equals to 0
        if amount_due <= 0:
            # Calculate the change owed
            change_owed = abs(amount_due)
            # Print the change owed
            print("Change Owed: ", change_owed)
            break
