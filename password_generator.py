import random
import string

def generate_password(length, use_upper, use_digits, use_symbols):
    characters = string.ascii_lowercase

    if use_upper:
        characters += string.ascii_uppercase
    if use_digits:
        characters += string.digits
    if use_symbols:
        characters += string.punctuation

    password = "".join(random.choice(characters) for _ in range(length))
    return password

def main():
    print("🔐 Welcome to Password Generator!")
    print("==================================")

    while True:
        try:
            length = int(input("\nEnter password length (min 6): "))
            if length < 6:
                print("❌ Length must be at least 6!")
                continue
            break
        except ValueError:
            print("❌ Please enter a valid number!")

    print("\nCustomize your password:")
    use_upper   = input("Include uppercase letters? (y/n): ").lower() == "y"
    use_digits  = input("Include numbers? (y/n): ").lower() == "y"
    use_symbols = input("Include symbols? (y/n): ").lower() == "y"

    password = generate_password(length, use_upper, use_digits, use_symbols)

    print("\n==================================")
    print(f"✅ Generated Password: {password}")
    print("==================================")

    again = input("\nGenerate another password? (y/n): ").lower()
    if again == "y":
        main()
    else:
        print("👋 Goodbye!")

main()
