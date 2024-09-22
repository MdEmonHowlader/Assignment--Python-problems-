def grade(score):
    if score >= 90 and score<=100:
        return "A"
    elif score >= 80 and score < 90:
        return "B"
    elif score >=70 and score < 80:
        return "C"
    elif score >= 60 and score <70:
        return "D"
    elif score >=0 and score <60:
        return "F"
    else:
        return "Invalid score."
score =float(input("Enter the student's score (0-100): "))
g=grade(score)
print(f"The student's grade is: {g}")