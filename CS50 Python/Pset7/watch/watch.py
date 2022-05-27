import re

def main():
    print(parse(input("HTML: ")))


def parse(s):
    iframe = re.search(r"(<iframe)(.)*(></iframe>)",s)
    if iframe:
        searched = re.search(r"(http(s)*?://(?:www\.)?youtube\.com/embed/)([a-z_A-Z_0-9_]+)", s)
        if searched:
            str = searched.group()
            matches = re.match(r"^(http(s)*?://(?:www\.)?youtube\.com/embed/)([a-z_A-Z_0-9_]+)$", str)
            return "https://youtu.be/" + matches.groups()[2]


if __name__ == "__main__":
    main()
