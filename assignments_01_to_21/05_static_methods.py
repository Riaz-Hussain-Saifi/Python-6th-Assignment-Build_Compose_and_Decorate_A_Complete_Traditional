"""
MathUtils Class Implementation
This class use of static methods in Python.
Static methods are utility functions that belong to a class but don't access or modify class or instance data.
"""
 
class MathUtils:
    """
    A class containing utility methods for mathematical operations.
    Static methods are used here as they don't need to access class or instance data.
    """
    
    @staticmethod
    def add(a, b):
        """
        Static method to add two numbers.
        Parameters:
            a (int/float): The first number
            b (int/float): The second number
        Returns:
            int/float: The sum of a and b
        """
        return a + b

# Example 1: Basic Usage
print("Example 1: Basic Addition")
result = MathUtils.add(5, 3)
print(f"Sum of 5 and 3 is: {result}")  # Output: Sum of 5 and 3 is: 8

# Example 2: Using with Different Data Types
print("\nExample 2: Different Data Types")
print(f"Sum of 2.5 and 3.7 is: {MathUtils.add(2.5, 3.7)}")  # Output: Sum of 2.5 and 3.7 is: 6.2

# Example 3: Using in a Loop
print("\nExample 3: Using in a Loop")
numbers = [(1, 2), (3, 4), (5, 6)]
for num1, num2 in numbers:
    print(f"Sum of {num1} and {num2} is: {MathUtils.add(num1, num2)}")

# Example 4: Using with Negative Numbers
print("\nExample 4: Negative Numbers")
print(f"Sum of -5 and 3 is: {MathUtils.add(-5, 3)}")  # Output: Sum of -5 and 3 is: -2

# Example 5: Using in a List Comprehension
print("\nExample 5: List Comprehension")
pairs = [(10, 20), (30, 40), (50, 60)]
sums = [MathUtils.add(x, y) for x, y in pairs]
print(f"List of sums: {sums}")  # Output: List of sums: [30, 70, 110]
