# create a 2D array to store the marks of 5 students in 3 subjects and perform the following operations on marks array. 1. find the maximium , minimum and avg marks . 2. find the student id(0-5) who score maximum marks in sub2. 3. find max marks subject wise. 4. find avg marks sub wise. 5. add 10 marks for all students who score less than 50 in sub2. 6.find out no. of students whose score more than 80 in sub3. 7. find the min number of marks of student2. 8. find max marks of student 4
import numpy as np
marks = np.array([[60, 70, 80],
                  [90, 85, 75],
                  [70, 39, 90],
                  [85, 95, 80],
                  [95, 45, 95]])
print("Marks Array: ")
print(marks)
# 1. find the maximum marks.
print("\n Maximum marks:",np.max(marks))
# 2. find the minimum marks.
print("\n Minimum marks:",np.min(marks))
# 3. find the average marks.
print("\n Average marks:",np.mean(marks))
# 4. find the student id(0-5) who score maximum marks in sub2.
max_sub2 = np.argmax(marks[:, 1])
print("\n Student id with maximum marks in sub2:", max_sub2)
# 5. find max marks subject wise.
max_subject_wise = np.max(marks, axis=0)
print("\n Maximum marks subject wise:", max_subject_wise)
# 6. find avg marks sub wise.
avg_subject_wise = np.mean(marks, axis=0)
print("\n Average marks subject wise:", avg_subject_wise)
# 7. add 10 marks for all students who score less than 50 in sub2.
marks[marks[:, 1] < 50, 1] += 10
print("\n Marks after adding 10 to students with less than 50 in sub2:")
print(marks)
# 8. find out no. of students whose score more than 80 in sub3.
count_sub3 = np.sum(marks[:, 2] > 80)
print("\n Number of students with marks more than 80 in sub3:", count_sub3)
# 9. find the min number of marks of student2.
min_student2 = np.min(marks[1])
print("\n Minimum marks of student2:", min_student2)
# 10. find max marks of student 4
max_student4 = np.max(marks[3])
print("\n Maximum marks of student4:", max_student4)