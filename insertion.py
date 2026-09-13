employee = {
    "E1": {
        "emp_name": "Rahul",
        "designation": "Manager",
        "department": "HR",
        "salary": 60000
    },
    "E2": {
        "emp_name": "Priya",
        "designation": "Developer",
        "department": "IT",
        "salary": 75000
    },
    "E3": {
        "emp_name": "Aman",
        "designation": "Accountant",
        "department": "Finance",
        "salary": 55000
    },
    "E4": {
        "emp_name": "Sneha",
        "designation": "Developer",
        "department": "IT",
        "salary": 80000
    },
    "E5": {
        "emp_name": "Riya",
        "designation": "HR Executive",
        "department": "HR",
        "salary": 50000
    }
}
# 1. Print records of all employees
for emp_id in employee:
    print(emp_id, ":", employee[emp_id])
# 2. Print department of employee E4
print("\nDepartment of E4:", employee["E4"]["department"])
# 3. Find employee having maximum salary
max_salary = 0
max_employee = ""
for emp_id in employee:
    if employee[emp_id]["salary"] > max_salary:
        max_salary = employee[emp_id]["salary"]
        max_employee = emp_id
print("\nEmployee having maximum salary:")
print(max_employee, ":", employee[max_employee])
# 4. Insert a new employee
employee["E6"] = {
    "emp_name": "Karan",
    "designation": "Tester",
    "department": "IT",
    "salary": 65000
}
print("\nAfter inserting new employee:")
print(employee)