def total(marks):
    return sum(marks)


def Average(marks):
    return sum(marks) / len(marks)


def percentage(marks):
    return (sum(marks) / (len(marks) * 100)) * 100


def grade(average):
    if average >= 90:
        return "A+"
    elif average >= 80:
        return "A"
    elif average >= 70:
        return "B"
    elif average >= 60:
        return "C"
    elif average >= 50:
        return "D"
    else:
        return "F"