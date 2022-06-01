import re

def main():
    print(parse(input("HTML: ")))


def parse(s):
    if re.search(r"<iframe(.)*><\/iframe>", s):
        url_pattern = re.search(r"(http(s)*:\/\/(www\.)*youtube\.com\/embed\/)([a-z_A-Z_0-9]+)", s)
        if url_pattern:
            split_url = url_pattern.groups()
            return "https://youtu.be/" + split_url[3]


if __name__ == "__main__":
    main()
