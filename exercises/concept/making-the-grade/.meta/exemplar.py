def count_failed_students(student_marks):
    failed_marks = 0
    for mark in student_marks:
        if mark <=40:
            failed_marks += 1
    return failed_marks

def above_threshold(student_marks, threshold):
    above_marks = []
    for mark in student_marks:
        if mark >= threshold:
            above_marks.append(mark)
    return above_marks

def first_k_student_marks(student_marks, k):
    i = 0
    marks = []
    while i <= k:
        marks.append(student_marks[i])
        i += 1
    return marks

def perfect_score(student_info):
    for name, mark in student_info.items():
        if mark == 100:
            return name
    else:
        return "No hundreds"
