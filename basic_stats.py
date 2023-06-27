# Author: Alyce Harlan
# GitHub username: chaynz22
# Date: 26 June 2023
# Description: This program allows the user to create Student entries including their names and grades.
# The user is then able to access some basic statistics concerning the grades of those students.

import statistics

class Student:
    '''Defines an individual student entry and it's attributes: name and grade'''
    def __init__(self, name, grade):
        self._name = name
        self._grade = grade
    def get_student_name(self):
        '''Returns student's name'''
        return self._name
    def get_grade(self):
        '''Returns Student's Grade'''
        return self._grade

s1 = Student("Sarah", 78) #test code, defines a student with name Sarah and grade 78
print("Student name = ", s1.get_student_name()) #test, prints student name
print("Student grade= ", s1.get_grade()) #test, prints student grade

def basic_stats():
    '''Calculates the statistics for a given set of students'''
    statistics.mean()
    statistics.mode()
    statistics.median()
