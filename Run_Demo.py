# run_demo.py
# Run this file to see all outputs in your terminal:
#   python run_demo.py

from student_data import students
from filter import filter_students_by_major
from data_processing import format_student_data, display_students
from set_operations import unique_majors
from data_generator import student_generator

# ─────────────────────────────────────────────
print("=" * 50)
print("1. ALL STUDENTS")
print("=" * 50)
display_students(students)

# ─────────────────────────────────────────────
print("\n" + "=" * 50)
print("2. FILTER BY MAJOR: Computer Science")
print("=" * 50)
cs_students = filter_students_by_major(students, "Computer Science")
display_students(cs_students)

# ─────────────────────────────────────────────
print("\n" + "=" * 50)
print("3. FILTER BY MAJOR: Mathematics")
print("=" * 50)
math_students = filter_students_by_major(students, "Mathematics")
display_students(math_students)

# ─────────────────────────────────────────────
print("\n" + "=" * 50)
print("4. UNIQUE MAJORS (set comprehension)")
print("=" * 50)
majors = unique_majors(students)
print(majors)

# ─────────────────────────────────────────────
print("\n" + "=" * 50)
print("5. GENERATOR - Mathematics students (one at a time)")
print("=" * 50)
gen = student_generator(students, "Mathematics")
print(next(gen))
print(next(gen))
print(next(gen))

print("\n✅ All done! Everything is working.")