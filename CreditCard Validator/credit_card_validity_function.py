def check_card_type(card_number):
    card_type = ""
    if card_number[0] == "4" and 13 <= len(card_number) <= 16:
        card_type = "Visa Card"
    elif card_number[0] == "5" and 13 <= len(card_number) <= 16:
        card_type = "MasterCard"
    elif card_number[0] == "6" and 13 <= len(card_number) <= 16:
        card_type = "Discover Card"
    elif card_number[0] == "3" and card_number[1] == "7" and 13 <= len(card_number) <= 16:
        card_type = "American Express Card"
    else:
        card_type = "Invalid Card"
    return card_type

def add_all_odd(card_number):
    add_all_odd = 0
    for number in range(len(card_number) - 1, 0, -2):
        add_all_odd += int(card_number[number])
    return add_all_odd

def sum_second_digits(card_number):
    sum_second_digits = 0
    double_second_numbers = 0
    for count in range(len(card_number)-2, -1 , -2):
        double_second_numbers = int(card_number[count]) * 2
        if double_second_numbers > 9:
            double_second_numbers -= 9
        sum_second_digits += double_second_numbers
    return sum_second_digits
def get_total_sum(sum_one, sum_two):
    total_sum = sum_one + sum_two
    return total_sum
def check_validity(total_sum):
    status = ""
    if (total_sum % 10 == 0):
        status = "The card is valid"
    else:
        status = "The card is invalid"
    return status

def card_digit_length(card_number):
    return len(card_number)

def print_card_info(card_type, card_number, card_digit_length, status):
    card_info = f"""
    +++++++++++++++++++++++++++++++++++++++++++++++
    ++ Credit card type: {card_type}
    ++ Credit card number: {card_number}
    ++ Credit card digit length: {card_digit_length}
    ++ Validity status: {status}
    +++++++++++++++++++++++++++++++++++++++++++++++
    """
    print(card_info)