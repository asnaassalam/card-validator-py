#Welcome Message
def print_welcome_message():
    box_width = 30
    text = "Card Validator"
    padding = (box_width - len(text) - 2) // 2
    print("=" * box_width)
    print("|" + " " * padding + text + " " * (box_width - len(text) - padding - 2) + "|")
    print("=" * box_width)
    print("\nWelcome! Let's validate your card number.")
    print("\nPlease follow the instructions below:")
    print("\nInstructions:")
    print("- Enter your credit or debit card number.")
    print("- You can include spaces or dashes, but they will be automatically removed.")
    print("- Example: 4111 1111 1111 1111 or 4111-1111-1111-1111")

#Reverse the card number
reverse_card_numbers_list = []
def reverse_card_numbers(card_number):
    reverse_card_numbers_list.clear()
    card_number_length = len(card_number) - 1
    while card_number_length >= 0:
        reverse_card_numbers_list.append(card_number[card_number_length])
        card_number_length = card_number_length - 1
    return reverse_card_numbers_list

#Applying Luhn Algorithm
def luhn_algorithm(card_number):
    odd_sum = 0
    even_sum = 0
    for index, value in enumerate(reverse_card_numbers(card_number)):
        if index % 2 == 0 or index == 0:
            odd_sum = odd_sum + int(value)
        else:
            check_sum = int(value) * 2
            if check_sum > 9:
                check_sum = check_sum - 9
                even_sum = even_sum + check_sum
            else:
                even_sum = even_sum + check_sum
    total =  odd_sum + even_sum
    return total

#Find the Card Type
def card_type(card_number):
    if int(card_number[0]) == 4 and (len(reverse_card_numbers_list) == 13 or len(reverse_card_numbers_list) == 16 or len(reverse_card_numbers_list) == 19):
        print("✅ Valid Card - Visa")
    elif int(card_number[0:6]) == 357111 and len(reverse_card_numbers_list) == 16:
        print("✅ Valid Card - LankaPay")
    elif int(card_number[0:2]) == 62 and (len(reverse_card_numbers_list) == 16 or len(reverse_card_numbers_list) == 19):
        print("✅ Valid Card - UnionPay")
    elif (int(card_number[0:2]) in range(51, 56) or int(card_number[0:4]) in range(2221, 2721)) and len(reverse_card_numbers_list) == 16:
        print("✅ Valid Card - MasterCard")
    elif int(card_number[0:2]) == 34 or int(card_number[0:2]) == 37 and len(reverse_card_numbers_list) == 15:
        print("✅ Valid Card - American Express")

#Check the card length and validate the card
def validate_card(card_number):
    if 12 < len(card_number) < 20 and luhn_algorithm(card_number) % 10 == 0:
        card_type(card_number)
    else:
        print("❌ Invalid Card")

#Main Function
def main():
    while True:

        # User input
        card_number = input("\nEnter your credit or debit card number: ").strip().replace("-", "").replace(" ", "")

        validate_card(card_number)

        repeat = input("\nWould you like to validate another card? (yes/no): ").strip().lower()
        if repeat != 'yes':
            print("\nThank you for using Card Validator! Goodbye.")
            break

print_welcome_message()
main()

