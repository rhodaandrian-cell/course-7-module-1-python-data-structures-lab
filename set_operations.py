# set_operations.py
# Uses set comprehensions to track unique student attributes such as majors.

def unique_majors(students):
    """
    Return a set of unique majors from a list of students using set comprehension.

    Set comprehensions automatically eliminate duplicates, making them ideal
    for tracking unique values across a dataset.

    Args:
        students (list): A list of student tuples in the form (ID, Name, Major).

    Returns:
        set: A set of unique major names found among the students.

    Example:
        >>> unique_majors([(101, "Alice", "CS"), (102, "Bob", "Math"), (103, "Charlie", "CS")])
        {'CS', 'Math'}
    """
    return {student[2] for student in students}