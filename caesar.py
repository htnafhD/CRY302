LETTERS = 'ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz'


def encrypt():
    text = input("Enter plain: ").strip()
    s = int(input("Shift: "))
    result = ""
    for i in range(len(text)):
        char = text[i]
        if (char.isupper()):
            result += chr((ord(char) + s - 65) % 26 + 65)
        else:
            result += chr((ord(char) + s - 97) % 26 + 97)
    print("Cipher: ", result)


def decrypt(LETTERS, key):
    decrypted_message = ""
    encrypted_message = input(
        "Enter encrypted message:").strip()

    for c in encrypted_message:
        if c in LETTERS:
            position = LETTERS.find(c)
            new_position = (position - key) % 26
            new_character = LETTERS[new_position]
            decrypted_message += new_character
        else:
            decrypted_message += c
    print("DECODE: ", decrypted_message)


def brute_force(LETTERS, encrypted_message, key):
    decrypted_message = ""
    for c in encrypted_message:
        if c in LETTERS:
            position = LETTERS.find(c)
            new_position = (position - key) % 26
            new_character = LETTERS[new_position]
            decrypted_message += new_character
        else:
            decrypted_message += c
    print('DECODE %s: %s' % (key, decrypted_message))


def egcd(a, b):
    if a == 0:
        return b, 0, 1
    else:
        g, x, y = egcd(b % a, a)
        return g, y - (b // a) * x, x


def inverse_mod(a, n):
    for x in range(1, n):
        if ((a % n) * (x % n)) % n == 1:
            return x
    return -1


def menu():
    print("1. Encrypt")
    print("2. Decrypt")
    print("3. BruteForce")
    print("4. Euclidean Algorithm")
    print("5. Modular Inverse")
    x = int(input("\nEnter choice: "))
    return x


def main():
    while True:
        z = menu()
        if z == 1:
            encrypt()
        elif z == 2:
            key = int(input("Shift: "))
            decrypt(LETTERS, key)
        elif z == 3:
            encrypted_message = input("Enter encrypted message:").strip()
            for i in range(1, 26):
                brute_force(LETTERS, encrypted_message, i)
        elif z == 4:
            a = int(input("Enter num a: "))
            b = int(input("Enter num b: "))
            print(egcd(a, b))
        elif z == 5:
            a = int(input("Enter num a: "))
            n = int(input("Enter num n: "))
            print(inverse_mod(a, n))
        else:
            return main()


if __name__ == "__main__":
    main()
