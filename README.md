# Student Data Management System - Full Code Example

```python
# ── student_data.py ────────────────────────────────────────────────────────────
# Student records stored as a list of tuples: (ID, Name, Major)
students = [
    (101, 'Alice Johnson', 'Computer Science'),
    (102, 'Bob Smith', 'Mathematics'),
    (103, 'Charlie Davis', 'Physics'),
    (104, 'Diana Prince', 'Biology'),
    (105, 'Eve Lewis', 'Mathematics'),
    (106, 'Frank Wright', 'Computer Science'),
    (107, 'Grace Hall', 'Physics'),
    (108, 'Hank Green', 'Biology')
]

# ── filter.py ────────────────────────────────────────────────────────────────
# Filter students by a specific major using list comprehension
def filter_students_by_major(students, major):
    return [student for student in students if student[2] == major]

# Example:
# cs_students = filter_students_by_major(students, "Computer Science")
# print(cs_students)


# ── data_processing.py ───────────────────────────────────────────────────────
# Format a single student record
def format_student_data(student):
    return f"ID: {student[0]} | Name: {student[1]} | Major: {student[2]}"

# Display multiple students
def display_students(students):
    for student in students:
        print(format_student_data(student))

# Example:
# display_students(students)


# ── set_operations.py ───────────────────────────────────────────────────────
# Track unique majors across all students
def unique_majors(students):
    return {student[2] for student in students}

# Example:
# print(unique_majors(students))


# ── data_generator.py ───────────────────────────────────────────────────────
# Memory-efficient generator for filtering students by major
def student_generator(students, major):
    return (student for student in students if student[2] == major)

# Example:
# gen = student_generator(students, "Mathematics")
# print(next(gen))
# print(next(gen))