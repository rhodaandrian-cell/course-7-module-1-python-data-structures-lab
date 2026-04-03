# data_generator.py
# Uses generator expressions for memory-efficient processing of large student datasets.

def student_generator(students, major):
    """
    Return a generator expression that lazily yields students filtered by major.

    Unlike list comprehensions, generator expressions do not load all results
    into memory at once. Instead, they yield one item at a time, making them
    far more memory-efficient for large datasets.

    Args:
        students (list): A list of student tuples in the form (ID, Name, Major).
        major (str): The major to filter students by.

    Returns:
        generator: A generator that yields student tuples matching the given major.

    Example:
        >>> gen = student_generator(students, "Mathematics")
        >>> next(gen)
        (102, 'Bob Smith', 'Mathematics')
        >>> next(gen)
        (105, 'Eve Lewis', 'Mathematics')
    """
    return (student for student in students if student[2] == major)