def calculate_weighted_average(assignments, quizzes, final_exam):
    """
    Calculate the weighted average based on predetermined weights.

    Inputs:
    - assignments (list): List of assignment scores.
    - quizzes (list): List of quiz scores.
    - final_exam (float): Final exam score.

    Output:
    - float: Weighted average score.
    """
    # Predetermined weights
    assignment_weight = 0.4
    quiz_weight = 0.3
    final_exam_weight = 0.3

    # Calculate weighted average
    weighted_average = (sum(assignments) / len(assignments)) * assignment_weight + \
                       (sum(quizzes) / len(quizzes)) * quiz_weight + \
                       final_exam * final_exam_weight

    return weighted_average


def assign_letter_grade(weighted_average):
    """
    Assign a letter grade based on the school's grading scale.

    Input:
    - weighted_average (float): Calculated weighted average score.

    Output:
    - str: Letter grade (A, B, C, etc.).
    """
    if weighted_average < 0 or weighted_average > 100:
        return "Invalid"
    elif weighted_average >= 90:
        return "A"
    elif weighted_average >= 80:
        return "B"
    elif weighted_average >= 70:
        return "C"
    elif weighted_average >= 60:
        return "D"
    else:
        return "F"


def display_student_report(name, assignments, quizzes, final_exam):
    """
    Display a student's report including scores and letter grade.

    Inputs:
    - name (str): Student's name.
    - assignments (list): List of assignment scores.
    - quizzes (list): List of quiz scores.
    - final_exam (float): Final exam score.
    """
    weighted_average = calculate_weighted_average(assignments, quizzes, final_exam)
    letter_grade = assign_letter_grade(weighted_average)

    # Display student report
    print(f"Student: {name}")
    print(f"Assignments: {assignments}")
    print(f"Quizzes: {quizzes}")
    print(f"Final Exam: {final_exam}")
    print(f"Weighted Average: {weighted_average}")
    print(f"Letter Grade: {letter_grade}")


# Example usage:
student_name = input("Enter student's name: ")
assignment_scores = [float(score) for score in input("Enter assignment scores separated by spaces: ").split()]
quiz_scores = [float(score) for score in input("Enter quiz scores separated by spaces: ").split()]
final_exam_score = float(input("Enter final exam score: "))

display_student_report(student_name, assignment_scores, quiz_scores, final_exam_score)