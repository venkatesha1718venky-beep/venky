def calculate_grade(marks):
    if marks >= 90:
        return "A"
    elif marks >= 80:
        return "B"
    else:
        return "C"


for student_number in range(1, 6):
    print(f"\nStudent {student_number}")
    name = input("Enter the student's name: ")

    while True:
        try:
            marks = float(input("Enter marks (0-100): "))
            if 0 <= marks <= 100:
                break
            print("Marks must be between 0 and 100.")
        except ValueError:
            print("Please enter a valid number.")

    grade = calculate_grade(marks)
    print(f"{name} scored {marks:g} marks and received grade {grade}.")
