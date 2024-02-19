class StudentsInMLOps:
    def __init__(self):
        self.total_strength = 0
        self.class_name = "MLOps"

    def enroll_students(self, count):
        """
        Enroll students in the MLOps class.

        Parameters:
        - count (int): The number of students to enroll.
        """
        self.total_strength += count

    def drop_students(self, count):
        """
        Drop students from the MLOps class.

        Parameters:
        - count (int): The number of students to drop.
        """
        if count > self.total_strength:
            print("Error: Cannot drop more students than the total strength.")
        else:
            self.total_strength -= count

    def get_total_strength(self):
        """
        Get the total strength of students in the MLOps class.

        Returns:
        - int: Total strength of students.
        """
        return self.total_strength

    def get_class_name(self):
        """
        Get the name of the class.

        Returns:
        - str: Name of the class.
        """
        return self.class_name


# Example Usage:
if __name__ == "__main__":
    mlops_class = StudentsInMLOps()

    mlops_class.enroll_students(10)
    print(f"Total Strength: {mlops_class.get_total_strength()}")  # Output: 10

    mlops_class.drop_students(3)
    print(f"Total Strength: {mlops_class.get_total_strength()}")  # Output: 7

    class_name = mlops_class.get_class_name()
    print(f"Class Name: {class_name}")  # Output: MLOps
