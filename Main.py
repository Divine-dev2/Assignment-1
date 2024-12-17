import math

first_name = input('Please enter your first name: ')

def calculate_volume_sphere():
    radius = float(input('Please enter the radius of the sphere: '))
    if radius <= 0:
        print("Radius must be a positive number.")
        return
    volume = (4 / 3) * math.pi * radius ** 3
    print(f'The volume of the sphere is {volume:.2f}')

def calculate_triangle_area():
    side_a = float(input('Please enter the first side of the triangle: '))
    side_b = float(input('Please enter the second side of the triangle: '))
    side_c = float(input('Please enter the third side of the triangle: '))
    s = (side_a + side_b + side_c) / 2  
    area = math.sqrt(s * (s - side_a) * (s - side_b) * (s - side_c))
    print(f'The area of the triangle using Heron\'s formula is {area:.2f}')

def calculate_median():
    numbers = input('Enter numbers separated by commas: ')
    nums_list = sorted([float(num) for num in numbers.split(',')])
    if not nums_list:
        print("No numbers provided. Please try again.")
        return
    n = len(nums_list)
    if n % 2 == 1:
        median = nums_list[n // 2]
    else:
        median = (nums_list[n // 2 - 1] + nums_list[n // 2]) / 2
    print(f'The median of the numbers is {median}')

def calculate_compound_interest():
    principal = float(input('Please enter the principal amount: '))
    rate = float(input('Please enter the annual interest rate (as a percentage): '))
    time = float(input('Please enter the time (in years): '))
    n = int(input('Please enter the number of times interest is compounded per year: '))
    accumulated_amount = principal * (1 + rate / (100 * n)) ** (n * time)
    compound_interest = accumulated_amount - principal
    print(f'The total accumulated amount is {accumulated_amount:.2f}')
    print(f'The compound interest is {compound_interest:.2f}')

def calculate_acceleration():
    initial_velocity = float(input('Please enter the initial velocity (in m/s): '))
    final_velocity = float(input('Please enter the final velocity (in m/s): '))
    time = float(input('Please enter the time (in seconds): '))
    if time == 0:
        print("Time cannot be zero. Please enter a valid time.")
        return
    acceleration = (final_velocity - initial_velocity) / time
    print(f'The acceleration is {acceleration:.2f} m/s²')

def main_menu():
    print("\nChoose an option from the following:")
    print("a) Calculate the Volume of a Sphere")
    print("b) Calculate the Area of a Triangle")
    print("c) Calculate the Median of Numbers")
    print("d) Calculate Compound Interest")
    print("e) Calculate Acceleration")

    choice = input("Enter your choice (a, b, c, d, e): ").lower()

    if choice == 'a':
        calculate_volume_sphere()
    elif choice == 'b':
        calculate_triangle_area()
    elif choice == 'c':
        calculate_median()
    elif choice == 'd':
        calculate_compound_interest()
    elif choice == 'e':
        calculate_acceleration()
    else:
        print("Invalid choice. Please select a valid option.")

main_menu()

print(f'Thank you {first_name} for using my App')
