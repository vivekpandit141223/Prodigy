import re


#This function will check the complixicity of the password
def assess_password_strength(password):
    length = len(password)
    uppercase = any(char.isupper() for char in password)
    lowercase = any(char.islower() for char in password)
    digit = any(char.isdigit() for char in password)
    special_char = bool(re.match(r'[!@#$%^&*()\-_=+{};:,<.>/?\[\]\\\|`~]', password))

    strength = 0

    if length >= 8:
        strength += 1
    if uppercase:
        strength += 1
    if lowercase:
        strength += 1
    if digit:
        strength += 1
    if special_char:
        strength += 1

    if strength <= 2:
        return "Weak"
    elif strength <= 4:
        return "Moderate"
    else:
        return "Strong"

def main():
    password = input("Enter your password: ")
    strength = assess_password_strength(password)
    print("Password strength:", strength)


main()
