#lowest and highest 
def find_lowest_highest(scores):
    if not scores:
        return None, None  
    lowest = highest = scores[0]  
    for score in scores:
        if score < lowest:
            lowest = score
        elif score > highest:
            highest = score

    return lowest, highest

no_students = 5
no_assignments = 7
no_quizzes = 5
no_exam = 1
# empty list
assignment_scores = [[] for i in range(no_assignments)]
quiz_scores = [[] for i in range(no_quizzes)]
exam_scores = []
# input
for i in range(no_students):
    print(f"Enter scores for Student {i + 1}:")
    
    #  assignment scores
    assignment_scores_student = [int(score) for score in input(f"Enter {no_assignments} assignment scores separated by spaces: ").split()]
    for i in range(no_assignments):
        assignment_scores[i].append(assignment_scores_student[i])
    
    #  quiz scores
    quiz_scores_student = [int(score) for score in input(f"Enter {no_quizzes} quiz scores separated by spaces: ").split()]
    for i in range(no_quizzes):
        quiz_scores[i].append(quiz_scores_student[i])
    
    #  exam score
    exam_score = int(input("Enter exam score: "))
    exam_scores.append(exam_score)

# assignment
print("\nAssignment Scores:")
for i in range(no_assignments):
    average_assignment_score = sum(assignment_scores[i]) / no_students
    lowest_assignment_score, highest_assignment_score = find_lowest_highest(assignment_scores[i])
    print(f"Assignment #{i + 1}:")
    print(f"Class Average: {average_assignment_score:.2f}")
    print(f"Lowest Score: {lowest_assignment_score}")
    print(f"Highest Score: {highest_assignment_score}")
    print()

# quiz
print("Quiz Scores:")
for i in range(no_quizzes):
    average_quiz_score = sum(quiz_scores[i]) / no_students
    lowest_quiz_score, highest_quiz_score = find_lowest_highest(quiz_scores[i])
    print(f"Quiz #{i + 1}:")
    print(f"Class Average: {average_quiz_score:.2f}")
    print(f"Lowest Score: {lowest_quiz_score}")
    print(f"Highest Score: {highest_quiz_score}")
    print()

# exam
average_exam_score = sum(exam_scores) / no_students
lowest_exam_score, highest_exam_score = find_lowest_highest(exam_scores)
print("Exam Scores:")
print(f"Class Average: {average_exam_score:.2f}")
print(f"Lowest Score: {lowest_exam_score}")
print(f"Highest Score: {highest_exam_score}")