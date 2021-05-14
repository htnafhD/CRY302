LETTERS = 'ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz'


def encrypt():
    text = input("Enter plain: ")
    s = int(input("Shift: "))
    result = ""
    for i in range(len(text)):
        char = text[i]
        if (char.isupper()):
            result += chr((ord(char) + s-65) % 26 + 65)
        else:
            result += chr((ord(char) + s - 97) % 26 + 97)
    print("Cipher: ", result)


def decrypt(LETTERS):
    result = ""
    encrypted_message = input(
        "Enter the message you would like to decrypt: ").strip()
    key = int(input("Enter key to decrypt: "))

    decrypted_message = ""

    for c in encrypted_message:
        if c in LETTERS:
            position = LETTERS.find(c)
            new_position = (position - key) % 26
            new_character = LETTERS[new_position]
            decrypted_message += new_character
        else:
            decrypted_message += c
    print(decrypted_message)


def brute_force(LETTERS):
    text = input("Enter plaint text:")
    for key in range(len(LETTERS)):
        translated = ''
        for symbol in text:
            if symbol in LETTERS:
                num = LETTERS.find(symbol)
                num = num - key
                if num < 0:
                    num = num + len(LETTERS)
                translated = translated + LETTERS[num]
            else:
                translated = translated + symbol
        print('DECODE #%s: %s' % (key, translated))


def menu():
    print("1. Encrypt")
    print("\n2. Decrypt")
    print("\n3. BruteForce\n")
    x = int(input("Enter choice:"))
    return x


def main():
    while True:
        z = menu()
        if z == 1:
            encrypt()
        elif z == 2:
            decrypt(LETTERS)
        elif z == 3:
            brute_force(LETTERS)
        else:
            return main()


if __name__ == "__main__":
    main()
