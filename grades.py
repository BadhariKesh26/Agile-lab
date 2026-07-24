
def get_grade(mark):
    """Return the grade for a given mark."""
    if mark >= 90:
        return 'A'
    elif mark >= 80:
        return 'B'
    elif mark >= 70:
        return 'C'
    elif mark >= 60:
        return 'D'
    else:
        return 'F' 


def get_valid_mark(subject_name):
    """Prompt user for a valid mark (0-100) for the given subject."""
    while True:
        try:
            mark = float(input(f"Enter marks for {subject_name}: "))
            if 0 <= mark <= 100:
                return mark
            else:
                print("❌ Marks must be between 0 and 100. Please try again.")
        except ValueError:
            print("❌ Invalid input. Please enter a numeric value.")


def main():
    print("=" * 40)
    print("        GRADE CALCULATOR")
    print("=" * 40)

    # Get marks for 3 subjects
    subject1 = get_valid_mark("Subject 1")
    subject2 = get_valid_mark("Subject 2")
    subject3 = get_valid_mark("Subject 3")

    # Calculate individual grades
    grade1 = get_grade(subject1)
    grade2 = get_grade(subject2)
    grade3 = get_grade(subject3)

    # Calculate overall percentage and grade
    total_marks = subject1 + subject2 + subject3
    percentage = total_marks / 3
    overall_grade = get_grade(percentage)

    # Display results
    print("\n" + "=" * 40)
    print("            RESULTS")
    print("=" * 40)
    print(f" Subject 1: {subject1:.2f}  →  Grade {grade1}")
    print(f" Subject 2: {subject2:.2f}  →  Grade {grade2}")
    print(f" Subject 3: {subject3:.2f}  →  Grade {grade3}")
    print("-" * 40)
    print(f" Total Marks     : {total_marks:.2f} / 300")
    print(f" Overall Percentage: {percentage:.2f}%")
    print(f" Overall Grade   : {overall_grade}")
    print("=" * 40)


if __name__ == "__main__":
    main()

