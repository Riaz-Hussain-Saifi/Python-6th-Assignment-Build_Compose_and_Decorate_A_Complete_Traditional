"""
Student Class Implementation 
This class use of self in Python classes.
It creates a Student object with name and marks attributes.
"""

class Student:
    """
    A class to represent a student with name and marks.
    This class shows how to use instance variables and methods.
    """
    
    def __init__(self, name, marks):
        """
        Initialize a new Student object.
        Parameters:
            name (str): The name of the student
            marks (int): The marks obtained by the student
        """
        self.name = name    # Instance variable for student's name
        self.marks = marks  # Instance variable for student's marks

    def display(self):
        """
        Display the student's information.
        This method shows how to access instance variables using self.
        """
        print(f"Student name: {self.name}")    # Accessing name using self
        print(f"Student marks: {self.marks}")  # Accessing marks using self

# Example usage of the Student class
if __name__ == "__main__":
    # Example 1: Creating and displaying a student
    print("Example 1: Basic Student Creation")
    student1 = Student("Riaz", 94)
    student1.display()
    
    # Example 2: Creating multiple students
    print("\nExample 2: Multiple Students")
    student2 = Student("Ali", 85)
    student3 = Student("Sarah", 92)
    student2.display()
    student3.display()
    
    # Example 3: Direct attribute access
    print("\nExample 3: Direct Attribute Access")
    print(f"Name: {student1.name}")
    print(f"Marks: {student1.marks}")
    
    # Example 4: Modifying attributes
    print("\nExample 4: Modifying Attributes")
    student1.marks = 96  # Updating marks
    print(f"Updated marks for {student1.name}: {student1.marks}")
    
    # Example 5: Creating a list of students
    print("\nExample 5: List of Students")
    students = [
        Student("Waseem", 88),
        Student("Taha", 95),
        Student("Nimra", 82)
    ]
    
    # Display all students in the list
    for student in students:
        student.display() 