# class_static_methods_demo.py

class Calculator:
    # Class attribute
    calculation_type = "Arithmetic Operations"

    @staticmethod
    def add(a: float, b: float) -> float:
        """
        Static method to add two numbers.
        Does not require access to the class or instance.
        """
        return a + b

    @classmethod
    def multiply(cls, a: float, b: float) -> float:
        """
        Class method to multiply two numbers.
        Prints the class attribute 'calculation_type' before performing multiplication.
        """
        print(f"Calculation type: {cls.calculation_type}")
        return a * b


# Demonstration script (for testing purposes)
if __name__ == "__main__":
    # Using the static method
    sum_result = Calculator.add(10, 5)
    print(f"Addition Result: {sum_result}")

    # Using the class method
    product_result = Calculator.multiply(10, 5)
    print(f"Multiplication Result: {product_result}")