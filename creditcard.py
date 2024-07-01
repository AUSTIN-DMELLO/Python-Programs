import re
def validate_credit_card(card_number):
    pattern = r'^([456]\d{3}-?\d{4}-?\d{4}-?\d{4})$'
    if re.match(pattern, card_number):
        card_number = card_number.replace('-', '')
        for i in range(len(card_number) - 3):
            if card_number[i] == card_number[i + 1] == card_number[i + 2] == card_number[i + 3]:
                return False
        return True
    else:
        return False
def main():
    credit_cards = [
        "4578-3456-0978-5069",
        "6234-2221-1234-8900",
        "1234-4567-3456",
        "5678-7777-1345-3456",
        "4567 5678 3333-4589w"
    ]
    for card_number in credit_cards:
        if validate_credit_card(card_number):
            print(f"{card_number}: Valid")
        else:
            print(f"{card_number}: Invalid")
if __name__ == "__main__":
    main()
