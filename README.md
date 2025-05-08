# 💳 Card Validator

A simple Python script to validate credit or debit card numbers using the **Luhn Algorithm** and identify the card type (e.g., Visa, MasterCard, American Express, LankaPay, UnionPay).

## 📦 Features

- Command-line interface with a formatted welcome message
- Supports card numbers with spaces or dashes
- Automatically cleans and reverses the input
- Uses the **Luhn Algorithm** for validation
- Identifies card type:
  - ✅ Visa
  - ✅ MasterCard
  - ✅ American Express
  - ✅ UnionPay
  - ✅ LankaPay

## 🧠 How It Works

1. User enters a card number.
2. The input is cleaned (spaces/dashes removed).
3. The number is reversed and processed.
4. The **Luhn Algorithm** calculates the checksum.
5. If valid, the card type is displayed.

## 🧰 Technologies Used

- Python 3

## ▶️ How to Run

### Requirements

- Python 3.x

### Steps

1. Save the script as `card_validator.py`
2. Open a terminal in the script’s directory
3. Run the script using:

```bash
python card_validator.py
```

## 📝 Example

```bash
==============================
|        Card Validator      |
==============================

Welcome! Let's validate your card number.

Please follow the instructions below:
- Enter your credit or debit card number.
- You can include spaces or dashes, but they will be automatically removed.
- Example: 4111 1111 1111 1111 or 4111-1111-1111-1111

Enter your credit or debit card number: 4111 1111 1111 1111
✅ Valid Card - Visa

Would you like to validate another card? (yes/no): no

Thank you for using Card Validator! Goodbye.
```

## 🔢 Example Test Card Numbers

| Card Type         | Example Number         | 
|-------------------|------------------------|
| Visa              | 4111 1111 1111 1111    |
| MasterCard        | 5555 5555 5555 4444    | 
| American Express  | 3782 822463 10005      | 
| UnionPay          | 6200 0000 0000 0005    | 
| LankaPay          | 3571110000000000       | 

⚠️ These are test numbers and do not work for real transactions.
