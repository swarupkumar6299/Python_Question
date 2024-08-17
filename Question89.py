student_mark = {
    "Jenny":92,
    "Arvind":67,
    "Harry":80,
    "Arjun":66,
    "Ankit":99,
    "Pream":34
}
student_grades={}
for student in student_mark:
    mark= student_mark[student]
    if mark>90:
        student_grades[student]="A+"
    elif mark >80:
        student_grades[student]="A"
    elif mark > 70:
        student_grades[student] = "B+"
    elif mark>60:
        student_grades[student] = "B"
    elif mark>50:
        student_grades[student] = "c"
    elif mark>40:
        student_grades[student] = "D"
    else:
        student_grades[student] = "F"
print(student_grades)
    
