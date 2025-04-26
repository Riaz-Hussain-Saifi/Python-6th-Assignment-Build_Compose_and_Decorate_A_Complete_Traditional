"""
Bank Class Implementation
This class use of class variables and class methods in Python.
Class variables are shared among all instances of the class.
"""

class Bank:
    """
    A class representing a bank with class variables and instance variables.
    Class variables are shared across all instances, while instance variables are unique to each instance.
    """
    
    # Class variable - shared among all instances
    bank_name = "National Bank of Pakistan"
    
    def __init__(self, branch_name):
        """
        Initialize a new Bank object with a branch name.
        Parameters:
            branch_name (str): The name of the bank branch
        """
        self.branch_name = branch_name  # Instance variable - unique to each instance
        
    @classmethod    
    def change_bank_name(cls, new_name):
        """
        Class method to change the bank name for all instances.
        Parameters:
            new_name (str): The new name for the bank
        """
        cls.bank_name = new_name
        
    def print_bank_name(self):
        """
        Method to print the bank name and branch name.
        Demonstrates accessing both class and instance variables.
        """
        print(f"The bank name is {Bank.bank_name}, branch name is {self.branch_name}")

# Example 1: Basic Usage
print("Example 1: Basic Bank Usage")
branch1 = Bank("Gulshan")
branch1.print_bank_name()

# Example 2: Creating Multiple Branches
print("\nExample 2: Multiple Branches")
branch2 = Bank("DHA")
branch2.print_bank_name()

# Example 3: Changing Bank Name
print("\nExample 3: Changing Bank Name")
Bank.change_bank_name("Alfalah")    # Change affects all instances
print("After changing bank name:")
branch1.print_bank_name()
branch2.print_bank_name()

# Example 4: Creating More Branches After Name Change
print("\nExample 4: New Branches After Name Change")
branch3 = Bank("Clifton")
branch4 = Bank("Karachi")
branch3.print_bank_name()
branch4.print_bank_name()

# Example 5: Accessing Class Variable Directly
print("\nExample 5: Direct Class Variable Access")
print(f"Current bank name: {Bank.bank_name}")

# Example 6: Creating Branches in a List
print("\nExample 6: List of Branches")
branches = [
    Bank("Lahore"),
    Bank("Islamabad"),
    Bank("Peshawar")
]

# Display all branch information
for branch in branches:
    branch.print_bank_name()
    
        
        
    
    