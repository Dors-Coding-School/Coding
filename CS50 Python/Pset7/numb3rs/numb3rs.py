import re

def main():
    print(validate(input("IPv4 Address: ")))

def validate(ip):
    if re.search(r"^[0-9_]+\.[0-9_]+\.[0-9_]+\.[0-9_]+$", ip):
        split_ip = ip.split(".")
        for piece in split_ip:
            if int(piece) > 255:
                return False
        return True
    else:
        return False

if __name__ == "__main__":
    main()
