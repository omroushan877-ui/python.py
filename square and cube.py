# Program to calculate square and cube of a number
def calculate_square_and_cube(number):
    """Calculate the square and cube of a number"""
    square = number ** 2
    cube = number ** 3
    return square, cube

# Main program
if __name__ == "__main__":
    try:
        # Get input from user
        num = float(input("Enter a number: "))
        
        # Calculate square and cube
        square, cube = calculate_square_and_cube(num)
        
        # Display results
        print(f"\nNumber: {num}")
        print(f"Square: {square}")
        print(f"Cube: {cube}")
        
    except ValueError:
        print("Error: Please enter a valid number!")