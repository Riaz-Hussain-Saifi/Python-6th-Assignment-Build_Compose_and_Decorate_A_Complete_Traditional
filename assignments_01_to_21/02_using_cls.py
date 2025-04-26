"""
Counter Class Implementation
This class use of class methods (@classmethod) and class variables in Python.
It shows how to track the number of objects created from a class.
"""
 
class Counter:
    # Class variable - shared among all instances
    # This variable keeps track of total objects created
    count = 0
    
    def __init__(self):
        """
        Constructor method that increments the class variable count
        whenever a new Counter object is created
        """
        Counter.count += 1
        
    @classmethod
    def get_count(cls):
        """
        Class method to get the total number of Counter objects created
        @classmethod decorator allows us to access class variables using 'cls'
        """
        print(f"Number of objects created: {cls.count}")

# Example 1: Basic Usage
print("Example 1: Basic Counter Usage")
c1 = Counter()
c2 = Counter()
c3 = Counter()
c4 = Counter()
Counter.get_count()  # Should display 4

# Example 2: Creating more objects
print("\nExample 2: Creating More Objects")
c5 = Counter()
c6 = Counter()
Counter.get_count()  # Should display 6

# Example 3: Accessing class variable directly
print("\nExample 3: Direct Class Variable Access")
print(f"Total count from class variable: {Counter.count}")

# Example 4: Creating objects in a loop
print("\nExample 4: Creating Objects in a Loop")
for i in range(3):
    Counter()
Counter.get_count()  # Should display 9

# Example 5: Resetting the counter
print("\nExample 5: Resetting Counter")
Counter.count = 0
Counter.get_count()  # Should display 0
        
        