#Creating a Calculator by creating pakages & Modules
#This is a simple calculator that can perform basic arithmetic operations
#Also Contain Power, Square Root, Factorial functions and exponential
#It is organized into packages and modules for better structure
#Trignomatric functions are also included
#Can use Math Library for advanced calculations
#Start creating
#Calculator.py

from arithmetic.sum import sum
from arithmetic.Subtract import Subtract
from arithmetic.multiply import multiply
from arithmetic.divide import divide
from arithmetic.modulus import modulus
from number_check.prime_number import prime_number
from number_check.even_odd import even_odd
from power import power
from power import sq_root as square_root
from power import cube_root
from factorial import factorial
from trigonometric import trigonometric
def main():
    print("Welcome to the Calculator!")
    print("Select operation:")
    print("1. Add")
    print("2. Subtract")
    print("3. Multiply")
    print("4. Divide")
    print("5. Modulus")
    print("6. Power")
    print("7. Square Root")
    print("8. Cube Root")
    print("9. Trigonometric Functions")
    print("10. Check if a number is Prime")
    print("11. Check if a number is Even or Odd")
    print("12. Factorial")
    print("13. Exit")
    
    
    choice = input("Enter choice (1-13): ")
    # Check if the choice is valid
    if choice not in [str(i) for i in range(1, 14)]:
        print("Invalid choice!")
        return
    # Perform the selected operation
    print("You selected option:", choice)
    
        
    if choice == '1':
        num1 = float(input("Enter first number: "))
        num2 = float(input("Enter second number: "))
        print(f"The sum is: {sum(num1, num2)}")
    elif choice == '2':
        num1 = float(input("Enter first number: "))
        num2 = float(input("Enter second number: "))
        print(f"The difference is: {Subtract(num1, num2)}")
    elif choice == '3':
        num1 = float(input("Enter first number: "))
        num2 = float(input("Enter second number: "))
        print(f"The product is: {multiply(num1, num2)}")
    elif choice == '4':
        num1 = float(input("Enter first number: "))
        num2 = float(input("Enter second number: "))
        if num2 != 0:
            print(f"The quotient is: {divide(num1, num2)}")
        else:
            print("Error! Division by zero.")
    elif choice == '5':
        num1 = float(input("Enter first number: "))
        num2 = float(input("Enter second number: "))
        print(f"The modulus is: {modulus(num1, num2)}")
    elif choice == '6':
        base = float(input("Enter base: "))
        exponent = float(input("Enter exponent: "))
        print(f"{base} raised to the power of {exponent} is: {power(base, exponent)}")
    elif choice == '7':
        num = float(input("Enter number: "))
        print(f"The square root of {num} is: {square_root(num)}")
    elif choice == '8':
        num = float(input("Enter number: "))
        print(f"The cube root of {num} is: {cube_root(num)}")
    elif choice == '9':
        angle = float(input("Enter angle in degrees: "))
        print("Trigonometric Functions:")
        print(f"Sine: {trigonometric.sine(angle)}")
        print(f"Cosine: {trigonometric.cosine(angle)}")
        print(f"Tangent: {trigonometric.tangent(angle)}")
    elif choice == '10':
        num = int(input("Enter a number: "))
        if prime_number(num):
            print(f"{num} is a prime number.")
        else:
            print(f"{num} is not a prime number.")
    elif choice == '11':
        num = int(input("Enter a number: "))
        print(f"{num} is {even_odd(num)}.")
    elif choice == '12':
        num = int(input("Enter a number: "))
        print(f"The factorial of {num} is: {factorial(num)}")
    elif choice == '13':
        print("Exiting the calculator. Goodbye!")
        print("Thank you for using the calculator!")
        return
    else:
        print("Invalid choice! Please select a valid operation.")
    
main()
while True:
    cont = input("Do you want to perform another operation? (yes/no): ").lower()
    if cont == 'yes':
        main()
    elif cont == 'no':
        print("Exiting the calculator. Goodbye!")
        print("Thank you for using the calculator!")
        break    