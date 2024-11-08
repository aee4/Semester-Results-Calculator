def calculate_grade(mark):
    if 100 >= mark >= 80:
        return "A"
    elif 79.99 >= mark >= 75:
        return "B"
    elif 74.99 >= mark >= 70:
        return "B+"
    elif 69.99 >= mark >= 65:
        return "C+"
    elif 64.99 >= mark >= 60:
        return "C"
    elif 59.99 >= mark >= 55:
        return "D+"
    elif 54.99 >= mark >= 50:
        return "D"
    elif 49.99 >= mark >= 0:
        return "F"
    else:
        raise ValueError("Invalid mark")


def calculate_grade_point(mark):
    if 100 >= mark >= 80:
        return 4.0
    elif 79.99 >= mark >= 75:
        return 3.5
    elif 74.99 >= mark >= 70:
        return 3.0
    elif 69.99 >= mark >= 65:
        return 2.5
    elif 64.99 >= mark >= 60:
        return 2.0
    elif 59.99 >= mark >= 55:
        return 1.5
    elif 54.99 >= mark >= 50:
        return 1.0
    elif 49.99 >= mark >= 0:
        return 0.0
    


def calculate_weighted_gpa(mark):
    grade_point = calculate_grade_point(mark)
    return grade_point * 3.0

def semester_class(sgpa):
    if 4.00 >=  sgpa >= 3.60:
        return "First Class"
    elif 3.59 >= sgpa >= 3.00:
        return "Second Class Upper"
    elif 2.99 >= sgpa >= 2.50:
        return "Second Class Lower"
    elif 2.49 >= sgpa >= 2.00:
        return "Third Class "
    elif 1.99 >= sgpa >= 1.00:
        return "Pass"
    elif 0.99 >= sgpa >= 0.00:
        return "Fail"
  