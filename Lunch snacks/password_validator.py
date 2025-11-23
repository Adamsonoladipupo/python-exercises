def password_validator(user_input):
    message = ""
    if user_input == "":
        message = "No password entered"
    for letter in user_input:
        if letter.islower() or letter.isupper() or letter.isdigit():
            message = "your password strenght WEAK"
        if letter.islower() and letter.isupper() and letter.isdigit():
            message = "your password strength Medium"
    return message


user_input = input("Please enter your password: ")
print(password_validator(user_input))