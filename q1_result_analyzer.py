# Q1 - Student Result Analyzer
# This program takes a student's name, roll number and marks in 5 subjects,
# calculates total and average, assigns a grade, and shows which subjects
# the student failed in (below 40).


def analyze_result(name, roll, marks):
    total = sum(marks)
    average = total / len(marks)

    # Decide grade based on average
    if average >= 90:
        grade = "A"
    elif average >= 75:
        grade = "B"
    elif average >= 60:
        grade = "C"
    elif average >= 40:
        grade = "D"
    else:
        grade = "Fail"

    # Find subjects where marks are below 40
    failed_subjects = []
    for i in range(len(marks)):
        if marks[i] < 40:
            # Subject numbering starts from 1, not 0, for readability
            failed_subjects.append("Subject " + str(i + 1))

    # Print the report
    print(f"Student: {name} (Roll: {roll})")
    print(f"Total: {total}, Average: {average}")
    print(f"Grade: {grade}")

    if failed_subjects:
        print("Subjects below 40: " + ", ".join(failed_subjects))
    else:
        print("Subjects below 40: None")


def main():
    name = "Aarav"
    roll = 101
    marks = [88.5, 35.0, 76.0, 92.5, 48.0]

    analyze_result(name, roll, marks)

    print()  

    
    analyze_result("Priya", 102, [95.0, 91.0, 89.0, 93.0, 96.0])


if __name__ == "__main__":
    main()
