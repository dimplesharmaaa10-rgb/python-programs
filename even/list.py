# Python program to create a list of 10 students' names and their marks, then find the student with maximum and minimum marks. No duplicate values are taken in any list.
students = ["Amit", "Rahul", "Priya", "Neha", "Riya", "Arjun", "Karan", "Sneha", "Vikash", "Anjali"]
marks = [85, 90, 78, 88, 95, 76, 82, 91, 69, 87]
max_marks = max(marks)
min_marks = min(marks)
max_student = students[marks.index(max_marks)]
min_student = students[marks.index(min_marks)]
print("Student with Maximum Marks:")
print(max_student, "scored", max_marks)
print("\nStudent with Minimum Marks:")
print(min_student, "scored", min_marks)
