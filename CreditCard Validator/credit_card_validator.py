from credit_card_validity_function import *

print("Welcome, this app help you validate your credit card number")
card_number = input("Enter your credit card number: ")
card_type = check_card_type(card_number)
card_digit_length = card_digit_length(card_number)
status = check_validity(sum_second_digits(card_number))

print_card_info(card_type, card_number, card_digit_length, status)
