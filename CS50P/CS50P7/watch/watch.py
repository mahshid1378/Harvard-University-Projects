import sys
import re


def main():
    print(parse(input("HTML: ")))


def parse(s):
    match = re.search(r'<iframe.*?src="(.*?)"', s)
    if match:
        url = match.group(1)
        youtube_url = re.sub(r'^https?://(www\.)?youtube\.com/embed/', 'https://youtu.be/', url)
        return youtube_url
    else:
        return None


if __name__ == "__main__":
    main()