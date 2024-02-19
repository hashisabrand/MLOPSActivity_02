# Import the StudentsInMLOps class
import pytest
from main import StudentsInMLOps

# Define test cases for the StudentsInMLOps class
class TestStudentsInMLOps:

    def test_initial_total_strength(self):
        mlops_class = StudentsInMLOps()
        assert mlops_class.getTotalStrength() == 0

    def test_enroll_students(self):
        mlops_class = StudentsInMLOps()
        mlops_class.enrollStudents(5)
        assert mlops_class.getTotalStrength() == 5

    def test_drop_students(self):
        mlops_class = StudentsInMLOps()
        mlops_class.enrollStudents(10)
        mlops_class.dropStudents(3)
        assert mlops_class.getTotalStrength() == 7

    def test_drop_students_invalid(self):
        mlops_class = StudentsInMLOps()
        mlops_class.enrollStudents(5)
        mlops_class.dropStudents(7)
        assert mlops_class.getTotalStrength() == 5  # Total strength should remain unchanged

    def test_get_class_name(self, capsys):
        mlops_class = StudentsInMLOps()
        mlops_class.getClassName()
        captured = capsys.readouterr()
        assert captured.out.strip() == 'StudentsInMLOps'


# Run the tests by executing `pytest` in the terminal
