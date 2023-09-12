def wa(ascores, qscores, escore):
    aw, qw, ew = 0.4, 0.3, 0.3
    wavg = (sum(ascores) / len(ascores)) * aw + (sum(qscores) / len(qscores)) * qw + escore * ew
    return wavg

def assign_grade(wavg):
    if wavg >= 90: return 'A'
    elif wavg >= 80: return 'B'
    elif wavg >= 70: return 'C'
    elif wavg >= 60: return 'D'
    else: return 'F'

def display_report(s):
    wavg = wa(s["ascores"], s["qscores"], s["escore"])
    grade = assign_grade(wavg)
    print(f"Name: {s['name']}\nAssign Scores: {s['ascores']}\nQuiz Scores: {s['qscores']}\nExam Score: {s['escore']}\nWeighted Avg: {wavg:.2f}\nGrade: {grade}")

students = []

while True:
    print("\nStudent Record:\n1. Add Student\n2. Calculate Weighted Avg\n3. Calculate Class Avg, Lowest, and Highest Scores\n4. Exit")
    choice = input("Enter your choice: ")

    if choice == "1":
        s = {}
        s["name"] = input("Name: ")
        s["ascores"] = [int(score) for score in input("Assign Scores: ").split()]
        s["qscores"] = [int(score) for score in input("Quiz Scores: ").split()]
        s["escore"] = int(input("Exam Score: "))
        students.append(s)
        print("Student added!")

    elif choice == "2":
        for s in students: display_report(s)

    elif choice == "3":
        ascores_all, qscores_all, escores_all = [s["ascores"] for s in students], [s["qscores"] for s in students], [s["escore"] for s in students]
        num_assignments, num_quizzes = len(students[0]["ascores"]), len(students[0]["qscores"])

        for i in range(num_assignments):
            ascores_i = [s["ascores"][i] for s in students]
            print(f"Assign #{i + 1} - Class Avg: {sum(ascores_i) / len(ascores_i):.2f}, Lowest: {min(ascores_i)}, Highest: {max(ascores_i)}")

        for i in range(num_quizzes):
            qscores_i = [s["qscores"][i] for s in students]
            print(f"Quiz #{i + 1} - Class Avg: {sum(qscores_i) / len(qscores_i):.2f}, Lowest: {min(qscores_i)}, Highest: {max(qscores_i)}")

        print(f"Exam - Class Avg: {sum(escores_all) / len(escores_all):.2f}, Lowest: {min(escores_all)}, Highest: {max(escores_all)}")

    elif choice == "4":
        print("Exiting.")
        break

    else:
        print("Invalid choice. Select a valid option.")