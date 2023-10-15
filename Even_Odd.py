def is_even(number):
    return number % 2 == 0

def is_odd(number):
    return number % 2 != 0

def is_positive(number):
    return number > 0

def is_negative(number):
    return number < 0

def is_prime(number):
    if number <= 1:
        return False
    for i in range(2, int(number**0.5) + 1):
        if number % i == 0:
            return False
    return True

def is_palindrome(text):
    clean_text = ''.join(c for c in text if c.isalnum()).lower()
    return clean_text == clean_text[::-1]

def is_divisible(number, divisor):
    return number % divisor == 0

def is_power_of_two(number):
    return number > 0 and (number & (number - 1)) == 0

def is_perfect_square(number):
    return number > 0 and int(number**0.5)**2 == number

def main():
    while True:
        print("Choose an option:")
        print("1. Check if a number is even")
        print("2. Check if a number is odd")
        print("3. Check if a number is positive")
        print("4. Check if a number is negative")
        print("5. Check if a number is prime")
        print("6. Check if a text is a palindrome")
        print("7. Check if a number is divisible by another number")
        print("8. Check if a number is a power of two")
        print("9. Check if a number is a perfect square")
        print("0. Exit")

        choice = input("Enter your choice: ")

        if choice == '0':
            break

        number = input("Enter a number or text: ")

        if choice == '1':
            result = is_even(int(number))
        elif choice == '2':
            result = is_odd(int(number))
        elif choice == '3':
            result = is_positive(int(number))
        elif choice == '4':
            result = is_negative(int(number))
        elif choice == '5':
            result = is_prime(int(number))
        elif choice == '6':
            result = is_palindrome(number)
        elif choice == '7':
            divisor = int(input("Enter a divisor: "))
            result = is_divisible(int(number), divisor)
        elif choice == '8':
            result = is_power_of_two(int(number))
        elif choice == '9':
            result = is_perfect_square(int(number))
        else:
            print("Invalid choice. Please enter a valid option.")
            continue

        print(f"Result: {result}")

if __name__ == "__main__":
    main()
