# data_processing.py
# Handles formatting and displaying of student records.

def format_student_data(student):
    """
    Format a single student tuple into a readable string.

    Args:
        student (tuple): A student tuple in the form (ID, Name, Major).

    Returns:
        str: A formatted string representing the student's details.

    Example:
        >>> format_student_data((101, "Alice Johnson", "Computer Science"))
        'ID: 101 | Name: Alice Johnson | Major: Computer Science'
    """
    student_id, name, major = student
    return f"ID: {student_id} | Name: {name} | Major: {major}"


def display_students(students):
    """
    Print the details of all students in the list.

    Iterates through each student and prints their formatted details
    using the format_student_data function.

    Args:
        students (list): A list of student tuples in the form (ID, Name, Major).

    Returns:
        None
    """
    for student in students:
        print(format_student_data(student))