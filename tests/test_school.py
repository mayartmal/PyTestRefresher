import pytest
from source.school import Classroom, Student, Teacher, TooManyStudents

@pytest.fixture
def classroom():
    return Classroom(
        teacher=Teacher("Minerva McGonagall"),
        students=[Student("Harry Potter"), Student("Hermione Granger"), Student("Ron Weasley")],
        course_title="Transfiguration"
    )

@pytest.fixture
def student():
    return Student("Draco Malfoy")

@pytest.mark.parametrize("student_name", [
    "Luna Lovegood",
    "Neville Longbottom",
    "Ginny Weasley"
])

def test_add_student(classroom, student_name):
    student = Student(student_name)
    classroom.add_student(student)
    assert student in classroom.students

def test_add_student_raises_too_many_students(classroom):
    for i in range(8):
        classroom.add_student(Student(f"Student {i}"))
    with pytest.raises(TooManyStudents):
        classroom.add_student(Student("Seamus Finnigan"))

def test_remove_student(classroom):
    classroom.remove_student("Hermione Granger")
    assert not any(student.name == "Hermione Granger" for student in classroom.students)

def test_remove_student_not_in_class(classroom):
    classroom.remove_student("Draco Malfoy")  # Should not raise an error
    assert len(classroom.students) == 3  # No change in size

def test_change_teacher(classroom):
    new_teacher = Teacher("Severus Snape")
    classroom.change_teacher(new_teacher)
    assert classroom.teacher.name == "Severus Snape"