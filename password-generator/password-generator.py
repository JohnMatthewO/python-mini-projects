import random
import string

def get_preferences():
    print("Password Generator")
    print("-" * 40)

    length = int(input("Password length (Minimum 8): "))
    if length < 8:
        print("Setting length to minimum of 8!")
        length = 8
    
    use_uppercase = input("Include uppercase letters? (y/n): ").lower() == 'y'
    use_numbers = input("Include numbers? (y/n): ").lower() == 'y'
    use_symbols = input("Include symbols? (y/n): ").lower() == 'y'

    return length, use_uppercase, use_numbers, use_symbols

def build_character_pool(use_uppercase, use_numbers, use_symbols):
    pool = string.ascii_lowercase

    if use_uppercase:
        pool += string.ascii_uppercase
    if use_numbers:
        pool += string.digits
    if use_symbols:
        pool += string.punctuation

    return pool

def generate_password(length, pool):
    password = []

    for _ in range(length):
        password.append(random.choice(pool))

    random.shuffle(password)
    return ''.join(password)

def check_strength(use_uppercase, use_numbers, use_symbols, length):
    score = 0

    if length >= 12:
        score += 1
    if length >= 16:
        score += 1
    if use_uppercase:
        score += 1
    if use_numbers:
        score += 1
    if use_symbols:
        score += 1
    
    if score <= 2:
        return "Weak!!!"
    elif score <= 3:
        return "Medium!!"
    else:
        return "Strong!"

def main():
    while True:
        length, use_uppercase, use_numbers, use_symbols = get_preferences()

        pool = build_character_pool(use_uppercase, use_numbers, use_symbols)
        password = generate_password(length, pool)
        strength = check_strength(use_uppercase, use_numbers, use_symbols, length)

        print(f"Generated Password: {password}")
        print(f"Strength: {strength}")

        again = input("Generate another? (y/n)?: ").lower()
        if again != 'y':
            print("Bye!")
            break

main()