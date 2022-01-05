from cs50 import get_int

def main():
    while True:
        height = get_int("Height: ")
        if height >= 0 and height <= 8:
            break

    for num_hashes in range(1, height + 1):

        num_spaces = height - num_hashes

        print(" " * num_spaces, end="")
        print("#" * num_hashes, end="")

        print("  ", end="")

        print("#" * num_hashes)


if __name__ == "__main__":
    main()