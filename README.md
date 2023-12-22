# Case Study: Automated Student Grade Calculation (ASGC)

Problem Statement:
A high school teacher wants to automate the process of calculating grades for their students. They have a set of assignments, quizzes, and a final exam that contribute to the students' final grades. The teacher needs a program that can take in the scores for each student and calculate their final grade based on a predetermined weighting system.

Solution:
To solve this problem, the teacher decides to write a Python program that includes functions to handle various aspects of grade calculation.

Function 1: Calculate Weighted Average
This function calculates the weighted average of all assignments, quizzes, and the final exam scores based on predetermined weights.
Inputs: List of assignment scores, list of quiz scores, final exam score
Output: Weighted average score

Function 2: Assign Letter Grade
This function takes the calculated weighted average and assigns a letter grade based on the school's grading scale.
Inputs: Weighted average score
Output: Letter grade (A, B, C, etc.)

Invalid: sobra sa 100
A: 90-100
B: 80-89
C: 70-79
D: 60-69
F: 0-59
Invalid: mababa sa 0


Function 3: Display Student Report
This function displays a student's name, scores for each assignment and quiz, final exam score, weighted average, and letter grade.
Inputs: Student's name, assignment scores, quiz scores, final exam score
Output: Printed student report