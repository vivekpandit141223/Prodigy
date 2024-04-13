# This is a Python program that can encrypt and decrypt text using the Caesar Cipher algorithm and it also allows users to input a message and a shift value to perform encryption
#and decryption of the text.

#This is the caeser_cipher function
def caesar_cipher(text, shift, mode):
    result = ""
    for char in text:
        if char.isalpha():
            if char.isupper():
                if mode == 'encrypt':
                    result += chr((ord(char) + shift - 65) % 26 + 65)
                elif mode == 'decrypt':
                    result += chr((ord(char) - shift - 65) % 26 + 65)
            elif char.islower():
                if mode == 'encrypt':
                    result += chr((ord(char) + shift - 97) % 26 + 97)
                elif mode == 'decrypt':
                    result += chr((ord(char) - shift - 97) % 26 + 97)
        else:
            result += char
    return result
# This is the main function
def main():
    message = input("Enter the message: ")
    shift = int(input("Enter the shift value (a number between 1 and 25): "))
    mode = input("Enter 'encrypt'  or 'decrypt' : ").lower()

    if mode != 'encrypt' and mode != 'decrypt':
        print("Invalid mode! Please enter 'encrypt' or 'decrypt'.")
        return

    if shift < 1 or shift > 25:
        print("Invalid shift value! Please enter a number between 1 and 25.")
        return

    result = caesar_cipher(message, shift, mode)
    print("Result:", result)


main()
