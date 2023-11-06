# =============================================================================
# Proj2_Hooker_Carson.py
# This program...

# author: Carson Hooker, Brennan Chan, Sara Vladisavljevich
# last modified: 11/2/23
# =============================================================================

import datetime

class Person():
    
    def __init__(self, name):
        """Assumes name is a string. Creates a person"""
        self.name = name
        self.birthday = None
        
    def set_birthday(self, birthdate):
        """Assumes birthdate if of type datetime.date"""
        self.birthday = birthdate
        
    def get_age_days(self):
        """Returns self's current age in days"""
        if self.birthday == None:
            raise ValueError
        return (datetime.date.today() - self.birthday).days
    
    def get_age_years(self):
        """Return self's current age in years"""
        if self.birthday == None:
            raise ValueError
        return self.get_age_days() / 365
    
    def get_birthday(self):
        """Returns self's birthday"""
        return self.birthday
    
    def get_name(self):
        """Return self's name"""
        return self.name

# The `Student` class represents a student and includes methods for changing the major, adding
# assignments to the gradebook, printing student information, and printing the gradebook.
class Student(Person):
    
    def __init__(self, name, id_number, classification):
        """
        The function initializes a student object with a name, id number, classification, major, and an
        empty gradebook.
        
        Vars:
            name: The name of the student
            id_number: The id_number parameter is used to store the unique identification number of
                the student. This number is typically assigned by the educational institution and is used to
                identify the student in various administrative and academic processes
            classification: The "classification" parameter in the `__init__` method is used to
                specify the classification of the student. It could be a string representing the student's
                classification, such as "Freshman", "Sophomore", "Junior", or "Senior"
        """
        
        super().__init__(name)
        self.id_number = id_number
        self.classification = classification
        self.major = None
        self.gradebook = {}
        
    def change_major(self, major):
        """
        The `change_major` function changes the major of a student, while the `add_assignment` function
        adds an assignment to the gradebook with a corresponding score.
        
        Args:
            self(self): self
            major(string): The major parameter is a string that represents the new major for the student
        """
        # does this matter if its public or not?
        self.major = major
        
    def add_assignment(self, assignment_name, score):
        """
        The function adds an assignment to the gradebook and assigns it a score.
        
        Args: 
            assignment_name (string): The name of the assignment that you want to add to the gradebook
            score (int): The score parameter represents the score or grade that is assigned to the
                assignment. It is a numerical value that indicates the performance or achievement of the student
                on the assignment
        """
        
        self.gradebook[assignment_name] = score

    def student_info(self):
        """
        The function "student_info" prints out the information of a student, including their name, ID
        number, classification, and major.
        """
        
        print("Student Information:")
        print(f"\tStudent's Name: {self.name}")
        print(f"\tStudent's ID Number: {self.id_number}")
        print(f"\tStudent's Classification: {self.classification}")
        print(f"\tStudent's Major: {self.major}")

    def print_gradebook(self):
        """Prints the gradebook with all assignment and scores"""
        
        print(f"{self.name}'s Gradebook:")
        for assignment, score in self.gradebook.items():
            print(f"\t{assignment}: {score}%")

# examples / driver 
PersonA = Person("Fauna")
PersonA.set_birthday(datetime.date(2014, 3, 18))
print('Person Name',PersonA.get_name() + ':')
print('\tBirthday',PersonA.get_birthday())
print('\tAge in Days:',PersonA.get_age_days())
print('\tAge in Years:',PersonA.get_age_years())

StudentA = Student("Andrew", "999226755", "Senior")
StudentA.change_major("Mathematics")
# show polymorphism
StudentA.set_birthday(datetime.date(1979, 7, 21))
StudentA.student_info()
StudentA.add_assignment("Homework", 99.7)
StudentA.add_assignment("Participation", 100)
StudentA.add_assignment("Final", 92)
StudentA.print_gradebook()
print("\tBirthday",StudentA.get_birthday())

StudentB = Student("Samantha", "999568332", "Sophomore")
StudentB.change_major("Anthropology")
StudentB.student_info()
StudentB.add_assignment("Annotated Bibliography 1", 95)
StudentB.add_assignment("Rough Draft 1", 90)
StudentB.add_assignment("Essay 1", 87.5)
StudentB.print_gradebook()

StudentC = Student("Natalie", "999720365", "Senior")
StudentC.change_major("Speech Pathology")
StudentC.student_info()
StudentC.add_assignment("Observation Reflection 1", 95)
StudentC.add_assignment("Project 1", 98)
StudentC.add_assignment("Midterm", 94)
StudentC.print_gradebook()

StudentD = Student("Todd", "999220045", "Freshman")
StudentD.change_major("Business")
StudentD.student_info()
StudentD.add_assignment("Quiz 1", 80)
StudentD.add_assignment("Quiz 2", 75)
StudentD.add_assignment("Quiz 3", 90)
StudentD.print_gradebook()