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
    def display_calculation_type(cls):
        """
        Class method that prints the class attribute 'calculation_type'.
        """
        print(f"Calculation Type: {cls.calculation_type}")

    @classmethod
    def create_multiplier(cls, factor: float):
        """
        Factory-style class method that returns a function to multiply a value by the given factor.
        Demonstrates usage of class context in a class method without calling it 'multiply'.
        """
        cls.display_calculation_type()  # Show the type before returning multiplier

        def multiplier(value: float) -> float:
            return value * factor

        return multiplier


# Demonstration script (for testing purposes)
if __name__ == "__main__":
    # Using the static method
    sum_result = Calculator.add(10, 5)
    print(f"Addition Result: {sum_result}")

    # Using a class method to get the calculation type
    Calculator.display_calculation_type()

    # Using another class method to create a multiplier function
    times_two = Calculator.create_multiplier(2)
    print(f"6 multiplied by 2 is: {times_two(6)}")