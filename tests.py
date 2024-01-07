from entities.Entity import Entity
from entities.Grade import Grade
from entities.Student import Student
from entities.Subject import Subject
from repo.Repository import Repository
from service.GradeService import GradeService
from service.StudentService import StudentService
from service.SubjectService import SubjectService
from validator.EntityValidator import EntityValidator
from validator.GradeValidator import GradeValidator
from validator.StudentValidator import StudentValidator
from validator.SubjectValidator import SubjectValidator


def test_entity():
    e = Entity(0)
    assert e.get_id() == 0
    e.set_id(1)
    assert e.get_id() == 1
    e.set_multiple(id_=5)
    assert e.get_id() == 5


def test_student():
    e = Student(0, 'Cosmin')
    assert e.get_name() == 'Cosmin'
    e.set_name('Screech')
    assert e.get_name() == 'Screech'
    e.set_multiple(name='Cake')
    assert e.get_name() == 'Cake'


def test_subject():
    e = Subject(0, 'Mathematics', 'Diana')
    assert e.get_name() == 'Mathematics'
    e.set_name('Mathematical Analysis')
    assert e.get_name() == 'Mathematical Analysis'
    e.set_multiple(name='Maths')
    assert e.get_name() == 'Maths'

    assert e.get_teacher_name() == 'Diana'
    e.set_teacher_name('Cosmin')
    assert e.get_teacher_name() == 'Cosmin'
    e.set_multiple(teacher_name='Maria')
    assert e.get_teacher_name() == 'Maria'


def test_grade():
    e = Grade(0, 1, 2, 10)
    assert e.get_id_student() == 1
    e.set_id_student(2)
    assert e.get_id_student() == 2

    assert e.get_id_subject() == 2
    e.set_id_subject(3)
    assert e.get_id_subject() == 3

    assert e.get_value() == 10
    e.set_value(9)
    assert e.get_value() == 9

    e.set_multiple(id_student=3, id_subject=4, value=8)
    assert e.get_id_student() == 3
    assert e.get_id_subject() == 4
    assert e.get_value() == 8


def test_repo():
    repo = Repository()
    e = Entity(0)
    repo.add(e)
    es = repo.get_all()
    assert len(es) == 1
    assert es[0] == e

    ef = repo.find_by_id(0)
    assert ef == e

    repo.update_by_id(0, id_=1)
    assert e.get_id() == 1

    er = repo.remove_by_id(1)
    assert er == e


def test_student_validator():
    validator = StudentValidator()
    student = Student(1, "Cosmin")
    validator.validate_student(student)

    student = Student(1, 1)
    try:
        validator.validate_student(student)
        assert False
    except ValueError:
        pass


def test_student_service():
    repo = Repository()
    validator = StudentValidator()
    service = StudentService(repo, validator)
    s = service.create('Cosmin')
    assert s.get_name() == 'Cosmin'
    ss = service.get_all()
    assert len(ss) == 1
    assert ss[0] == s
    s = service.update(s.get_id(), 'Screech')
    assert s.get_name() == 'Screech'
    service.remove(s.get_id())
    ss = service.get_all()
    assert len(ss) == 0


def test_subject_service():
    repo = Repository()
    validator = SubjectValidator()
    service = SubjectService(repo, validator)
    s = service.create('Mathematics', 'Berinde')
    assert s.get_name() == 'Mathematics'
    assert s.get_teacher_name() == 'Berinde'
    ss = service.get_all()
    assert len(ss) == 1
    assert ss[0] == s
    s = service.update(s.get_id(), 'Chemistry', 'Cake')
    assert s.get_name() == 'Chemistry'
    assert s.get_teacher_name() == 'Cake'
    service.remove(s.get_id())
    ss = service.get_all()
    assert len(ss) == 0


def test_grade_service():
    repo_students = Repository()
    repo_subjects = Repository()
    repo_grades = Repository()
    validator = GradeValidator()
    service = GradeService(repo_grades, validator, repo_students, repo_subjects)
    student = Student(0, 'Cosmin')
    repo_students.add(student)
    subject = Subject(0, 'Mathematics', 'Cake')
    repo_subjects.add(subject)
    grade = service.create(student, subject, 6)
    assert grade.get_value() == 6
    assert grade.get_id_student() == 0
    assert grade.get_id_subject() == 0

    grades = service.get_all()
    assert len(grades) == 1
    assert grades[0].get_value() == grade.get_value()


def test_find_grades():
    repo_students = Repository()
    repo_subjects = Repository()
    repo_grades = Repository()
    validator = GradeValidator()
    service = GradeService(repo_grades, validator, repo_students, repo_subjects)
    student = Student(1, 'Cosmin')
    repo_students.add(student)
    subject = Subject(2, 'English', 'Screech')
    repo_subjects.add(subject)
    grade = service.create(student, subject, 10)
    assert grade.get_value() == 10
    assert grade.get_id_student() == 1
    assert grade.get_id_subject() == 2
    grades = service.get_grades_for_subject(subject.get_id())
    assert len(grades) == 1
    assert grades[0].get_value() == grade.get_value()


def test_grade_service_get_top_20p_avg_grades():
    repo_students = Repository()
    repo_subjects = Repository()
    repo_grades = Repository()
    validator = GradeValidator()
    service = GradeService(repo_grades, validator, repo_students, repo_subjects)

    student0 = Student(0, 'Cosmin')
    repo_students.add(student0)

    student1 = Student(1, 'Screech')
    repo_students.add(student1)

    student2 = Student(2, 'Cake')
    repo_students.add(student2)

    student3 = Student(3, 'Diana')
    repo_students.add(student3)

    subject0 = Subject(0, 'Maths', 'Cake')
    repo_subjects.add(subject0)

    subject1 = Subject(1, 'FP', 'Screech')
    repo_subjects.add(subject1)

    service.create(student0, subject1, 10)
    service.create(student0, subject1, 4)
    service.create(student0, subject0, 5)
    service.create(student0, subject0, 6)
    service.create(student1, subject0, 7)
    service.create(student1, subject0, 3)
    service.create(student0, subject0, 3)
    avg_grades = service.get_top_20p_avg_grades()
    assert len(avg_grades) == 1
    assert avg_grades[0][0] == student0.get_name()
    assert avg_grades[0][1] == 5.6


def test_stat_1():
    repo_students = Repository()
    repo_subjects = Repository()
    repo_grades = Repository()
    validator = GradeValidator()
    service = GradeService(repo_grades, validator, repo_students, repo_subjects)

    student0 = Student(0, 'Cosmin')
    repo_students.add(student0)

    student1 = Student(1, 'Ana')
    repo_students.add(student1)

    subject0 = Subject(0, 'Maths', 'Cake')
    repo_subjects.add(subject0)

    subject1 = Subject(1, 'FP', 'Screech')
    repo_subjects.add(subject1)

    service.create(student0, subject1, 10)
    service.create(student0, subject1, 4)
    service.create(student0, subject0, 5)

    service.create(student0, subject0, 2)
    service.create(student1, subject0, 4)
    service.create(student1, subject0, 3)
    service.create(student0, subject0, 3)

    avg_grades = service.stat_1(subject0)
    assert len(avg_grades) == 2
    assert avg_grades[0][0] == student1.get_name()
    assert avg_grades[1][0] == student0.get_name()
    assert avg_grades[0][1] == 3.5
    assert avg_grades[1][1] == 10 / 3


def run_tests():
    test_entity()
    test_student()
    test_subject()
    test_grade()
    test_repo()
    test_student_validator()
    test_student_service()
    test_subject_service()
    test_grade_service()
    test_find_grades()
    test_stat_1()
    test_grade_service_get_top_20p_avg_grades()
