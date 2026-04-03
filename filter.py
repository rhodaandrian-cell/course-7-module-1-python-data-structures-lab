# filter.py
# Provides filtering functionality for student records using list comprehensions.

def filter_students_by_major(students, major):
    """
    Filter a list of students by their major using a list comprehension.

    Args:
        students (list): A list of student tuples in the form (ID, Name, Major).
        major (str): The major to filter by.

    Returns:
        list: A filtered list of student tuples whose major matches the given major.

    Example:
        >>> filter_students_by_major(students, "Mathematics")
        [(102, 'Bob Smith', 'Mathematics'), (105, 'Eve Lewis', 'Mathematics'), ...]
    """
    return [student for student in students if student[2] == major]