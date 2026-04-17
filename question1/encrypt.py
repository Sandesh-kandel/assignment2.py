def read_file():
    with open("raw_text.txt", "r") as f:
        return f.read()


def write_file(filename, content):
    with open(filename, "w") as f:
        f.write(content)


def main():
    text = read_file()

    shift1 = int(input("Enter shift1: "))
    shift2 = int(input("Enter shift2: "))

    encrypted = ""
    for c in text:
        encrypted += encrypt_char(c, shift1, shift2)

    write_file("encrypted_text.txt", encrypted)

    decrypt_file(shift1, shift2)

    print("Encryption and decryption complete.")



def encrypt_char(c, shift1, shift2):
    if c.islower():
        if 'a' <= c <= 'm':
            shift = shift1 * shift2
            return chr((ord(c) - ord('a') + shift) % 26 + ord('a'))
        elif 'n' <= c <= 'z':
            shift = shift1 + shift2
            return chr((ord(c) - ord('a') - shift) % 26 + ord('a'))

    elif c.isupper():
        if 'A' <= c <= 'M':
            shift = shift1
            return chr((ord(c) - ord('A') - shift) % 26 + ord('A'))
        elif 'N' <= c <= 'Z':
            shift = shift2 ** 2
            return chr((ord(c) - ord('A') + shift) % 26 + ord('A'))

    return c   
        

def decrypt_char(c, shift1, shift2):
    if c.islower():
        if 'a' <= c <= 'm':
            shift = shift1 * shift2
            return chr((ord(c) - ord('a') - shift) % 26 + ord('a'))
        elif 'n' <= c <= 'z':
            shift = shift1 + shift2
            return chr((ord(c) - ord('a') + shift) % 26 + ord('a'))

    elif c.isupper():
        if 'A' <= c <= 'M':
            shift = shift1
            return chr((ord(c) - ord('A') + shift) % 26 + ord('A'))
        elif 'N' <= c <= 'Z':
            shift = shift2 ** 2
            return chr((ord(c) - ord('A') - shift) % 26 + ord('A'))

    return c


def decrypt_file(shift1, shift2):
    text = read_file_from("encrypted_text.txt")

    decrypted = ""
    for c in text:
        decrypted += decrypt_char(c, shift1, shift2)

    write_file("decrypted_text.txt", decrypted)

def read_file_from(filename):
    with open(filename, "r") as f:
        return f.read()    

def decrypt_char(c, shift1, shift2):
    if c.islower():
        if 'a' <= c <= 'm':
            shift = shift1 * shift2
            return chr((ord(c) - ord('a') - shift) % 26 + ord('a'))
        elif 'n' <= c <= 'z':
            shift = shift1 + shift2
            return chr((ord(c) - ord('a') + shift) % 26 + ord('a'))

    elif c.isupper():
        if 'A' <= c <= 'M':
            shift = shift1
            return chr((ord(c) - ord('A') + shift) % 26 + ord('A'))
        elif 'N' <= c <= 'Z':
            shift = shift2 ** 2
            return chr((ord(c) - ord('A') - shift) % 26 + ord('A'))

    # VERY IMPORTANT fallback
    return c  

if __name__ == "__main__":
    main()
    
