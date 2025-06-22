# robust_division_calculator.py

def safe_divide(numerator, denominator):
    """
    Performs division with error handling for division by zero and non-numeric inputs.

    Parameters:
        numerator (str or numeric): The number to be divided.
        denominator (str or numeric): The number to divide by.

    Returns:
        str: Result of division or appropriate error message.
    """
    try:
        # Convert inputs to float
        num = float(numerator)
        denom = float(denominator)

        result = num / denom
        return f"The result of the division is {result:.2f}"

    except ZeroDivisionError:
        return "Error: Cannot divide by zero."

    except ValueError:
        return "Error: Please enter numeric values only."

# main.py
import sys
from robust_division_calculator import safe_divide

def main():
    """
    Main function to handle command-line arguments and call the safe_divide function.
    Usage: python main.py <numerator> <denominator>
    """
    if len(sys.argv) != 3:
        print("Usage: python main.py <numerator> <denominator>")
        return

    numerator = sys.argv[1]
    denominator = sys.argv[2]

    result = safe_divide(numerator, denominator)
    print(result)

if __name__ == "__main__":
    main()