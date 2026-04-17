def read_file():
    with open("raw_text.txt", "r") as f:
        return f.read()


def write_file(filename, content):
    with open(filename, "w") as f:
        f.write(content)


def main():
    text = read_file()
    print(text)  # just to check


if __name__ == "__main__":
    main()
