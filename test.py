from main import StudentsInMLOps

def test_enroll_students():
    mlops_class = StudentsInMLOps()
    mlops_class.enroll_students(5)
    assert mlops_class.get_total_strength() == 5

def test_drop_students():
    mlops_class = StudentsInMLOps()
    mlops_class.enroll_students(10)
    mlops_class.drop_students(3)
    assert mlops_class.get_total_strength() == 7

def test_drop_students_invalid():
    mlops_class = StudentsInMLOps()
    mlops_class.enroll_students(5)
    mlops_class.drop_students(8)  # Trying to drop more students than enrolled
    assert mlops_class.get_total_strength() == 5  # Total strength should remain unchanged

def test_get_class_name():
    mlops_class = StudentsInMLOps()
    assert mlops_class.get_class_name() == "MLOps"

if __name__ == "__main__":
    # Run the tests
    test_enroll_students()
    test_drop_students()
    test_drop_students_invalid()
    test_get_class_name()

    print("All tests passed successfully.")
