import random
import string

def generate_password(length=16, use_upper=True, use_lower=True, use_digits=True, use_symbols=True):
    # Character pools
    characters = ""
    if use_lower:
        characters += string.ascii_lowercase
    if use_upper:
        characters += string.ascii_uppercase
    if use_digits:
        characters += string.digits
    if use_symbols:
        characters += string.punctuation
    
    if not characters:
        return "Error: No character types selected!"
    
    # Generate password
    password = ''.join(random.choice(characters) for _ in range(length))
    return password

def main():
    print("🔐 STRONG PASSWORD GENERATOR 🔐\n")
    
    try:
        length = int(input("Password length (default 16): ") or "16")
        if length < 8:
            print("Warning: Length too short — using 12 for security")
            length = 12
        
        print("\nInclude:")
        upper = input("Uppercase letters? (y/n, default y): ").lower() != 'n'
        lower = input("Lowercase letters? (y/n, default y): ").lower() != 'n'
        digits = input("Digits? (y/n, default y): ").lower() != 'n'
        symbols = input("Symbols (!@#$ etc)? (y/n, default y): ").lower() != 'n'
        
        password = generate_password(length, upper, lower, digits, symbols)
        
        print("\n" + "="*50)
        print(f"Generated Password ({length} chars):")
        print(f"{password}")
        print("="*50)
        print("\nCopy it now — stay safe out there 💪")
        
        again = input("\nGenerate another? (y/n): ").lower()
        if again == 'y':
            print("\n")
            main()
    
    except ValueError:
        print("Invalid input — use numbers for length.")

if __name__ == "__main__":
    main()