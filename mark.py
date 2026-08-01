def calculate_grade(marks):
    if marks >= 90:
        return "A"
    elif marks >= 75:
        return "B"
    elif marks >= 60:
        return "C"
    else:
        return "Fail"
def average(marks_list):
    return sum(marks_list) / len(marks_list)
if __name__ == "__main__":
    marks = [80, 85, 81]
    avg = average(marks)
    print("Marks:", marks)
    print("Average:", avg)
    print("Grade:", calculate_grade(avg))

    
