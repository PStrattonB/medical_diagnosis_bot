"""
For our project, we have 2 main goals: to diagnose a patient’s state of dehydration and to keep track of and print all diagnoses. We can phrase them in above format like this:

We want to diagnose a patient’s state of dehydration based on a short questionnaire given:

    The questions are all binary questions (only 1 of 2 possible choices)
    The response to a given question will determine which question is asked next/which diagnosis to return
    The final dehydration diagnoses are either no dehydration, some dehydration, or severe dehydration

We want to print out a list of all saved patients and their diagnoses given:

    We are storing a list of all previous patients and diagnoses
    The list is accessible to us
    We can add new diagnoses to the list

Project Design:

Which language to use?
How do we want the program to run? (text-based, GUI, etc.)
How we want to structure the code
Which data structures we want to use

 Tools such as UML diagrams and flowcharts are particularly helpful at this stage.

Let’s apply this planning to our project. We know that we have 2 goals:

    1.To run and store a new diagnosis
    2.To display a list of previous diagnoses


Although these share some components, they are two separate functionalities so we’ll need at least one function for each
 and likely some helper functions, especially when performing a new diagnosis. We’ll also need a list to store patients
 and diagnoses; to keep things simple, we’ll just use a list of strings formatted as:

“Patient_name – diagnosis”

our program will repeat these two steps continuously:

    Display a prompt or ask the user a question
    Process the user’s text response and move to the next step

This diagram outlines 3 sets of logic that we’ll need to implement:

    Is the patient irritable/lethargic or do they have a normal appearance?
    Are the patient’s eyes normal/slightly sunken or are they very sunken?
    Is the patient’s skin pinch normal or slow?
"""

# Testing Phase

"""
Unit tests test the performance of individual functions or small blocks of code. These are used to model all possible 
input-output scenarios and ensure that each individual part of the code will hold up under expected and unexpected 
conditions. When writing the tests for an individual function or block of code, we want to consider all possible 
input-output combinations to make sure that the code is robust and has no single point of failure. Unit tests provide a 
quantitative measure of how well a program is performing.

Integration tests test how functions work together when performing a task or set of functionality. They are used to 
target procedures or overarching functionality and consider the results of a series of functions running together rather 
than looking at each individual function. Integration tests provide a more qualitative measure of how well a program is 
performing.



"""