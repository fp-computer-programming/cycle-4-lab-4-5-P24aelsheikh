"""

*** You must write a comment for every chunk of code you write from now on along with your author tag***

Create a Python file named lab_4-5.py
Write a program that prompts one user for their first name, 
then a second user for their first name. Using the format method, 
output a string that follows this template.

Hello, person1. My name is person2.


"""
user1_name= input('Enter the first users first name: ')
user2_name= input('Enter the second users first name: ')
output_string = 'Hello, {}. My name is {}.'.format(user1_name, user2_name)
print(output_string)