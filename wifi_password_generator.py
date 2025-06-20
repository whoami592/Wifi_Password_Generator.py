import random
import string

def print_banner():
    banner = """
    ╔══════════════════════════════════════════════╗
    ║      WiFi Password Generator                 ║
    ║      Coded by Pakistani Ethical Hacker       ║
    ║      Mr Sabaz Ali Khan                      ║
    ╚══════════════════════════════════════════════╝
    """
    print(banner)

def generate_password(length=12):
    characters = string.ascii_letters + string.digits + string.punctuation
    password = ''.join(random.choice(characters) for _ in range(length))
    return password

def main():
    print_banner()
    
    try:
        length = int(input("Enter desired password length (8-50): "))
        if length < 8 or length > 50:
            print("Please choose a length between 8 and 50 characters.")
            return
            
        num_passwords = int(input("How many passwords do you want to generate? "))
        if num_passwords <= 0:
            print("Please enter a positive number.")
            return
            
        print("\nGenerated WiFi Passwords:")
        print("-" * 30)
        for i in range(num_passwords):
            password = generate_password(length)
            print(f"Password {i+1}: {password}")
            
    except ValueError:
        print("Invalid input! Please enter numbers only.")

if __name__ == "__main__":
    main()