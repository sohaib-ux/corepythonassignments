def calculate_average(marks):
    return sum(marks) / len(marks)

def find_top_performer(students):
    averages = {student: calculate_average(marks) for student, marks in students.items()}
    top_performer = max(averages, key=averages.get)
    
    return averages, top_performer

students = {"John": [85, 78, 92], "Alice": [88, 79, 95], "Bob": [70, 75, 80]}
average_marks, top_performer = find_top_performer(students)

print(average_marks)
print(top_performer)
