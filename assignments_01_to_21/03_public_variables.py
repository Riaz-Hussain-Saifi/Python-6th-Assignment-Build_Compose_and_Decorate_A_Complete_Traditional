"""
Car Class Implementation
This class use of public variables in Python classes.
Public variables can be accessed directly from outside the class.
""" 
 
class Car:
    """
    A class representing a car with public variables.
    Public variables can be accessed and modified from anywhere.
    """
    
    def __init__(self, brand):
        """
        Initialize a new Car object with a brand.
        Parameters:
            brand (str): The brand name of the car
        """
        self.brand = brand   # Public variable - can be accessed from outside the class
        
    def start(self):
        """
        Method to start the car.
        Accessing public variable within the class.
        """
        print(f"{self.brand} car started")

# Example 1: Basic Usage
print("Example 1: Basic Car Usage")
my_car = Car("Toyota")
print(f"Car brand: {my_car.brand}")  # Accessing public variable
my_car.start()  # Calling method that uses public variable

# Example 2: Creating Multiple Cars
print("\nExample 2: Multiple Cars")
car1 = Car("Honda")
car2 = Car("BMW")
print(f"First car brand: {car1.brand}")
print(f"Second car brand: {car2.brand}")

# Example 3: Modifying Public Variable
print("\nExample 3: Modifying Public Variable")
my_car.brand = "Lexus"  # Directly modifying public variable
print(f"Updated car brand: {my_car.brand}")
my_car.start()

# Example 4: Creating Cars in a List
print("\nExample 4: List of Cars")
cars = [
    Car("Ford"),
    Car("Tesla"),
    Car("Audi")
]

# Display all car brands
for car in cars:
    print(f"Car brand: {car.brand}")
    car.start()

# Example 5: Dynamic Brand Assignment
print("\nExample 5: Dynamic Brand Assignment")
brands = ["Mercedes", "Porsche", "Ferrari"]
for brand in brands:
    car = Car(brand)
    print(f"Created car with brand: {car.brand}")
    car.start()
        
        