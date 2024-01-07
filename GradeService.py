from entities.Grade import Grade
from repo.Repository import Repository
from validator.GradeValidator import GradeValidator


class GradeService:
    def __init__(self, repo: Repository, validator: GradeValidator, student_repo: Repository, subject_repo: Repository):
        """
        Create a grade service
        :param repo: The repository of the grade
        """
        self.__repo = repo
        self.__validator = validator
        self.__student_repo = student_repo
        self.__subject_repo = subject_repo

    def create(self, student, subject, value):
        """
        Create a grade
        :param student: The name of the student
        :param subject: The subject of the grade
        :param value: The value of the grade
        :return: The created grade
        """
        id_student = student.get_id()
        id_subject = subject.get_id()
        id_ = self.__repo.get_available_id()
        grade = Grade(id_, id_student, id_subject, value)
        self.__validator.validate_grade(grade)
        self.__repo.add(grade)
        return grade

    def get_all(self):
        """
        Get all the grades
        :return: All the grades
        """
        return self.__repo.get_all()

    def remove_grades_for_student(self, student):
        """
        Remove grades for student.
        :param student: The student to remove the grades for
        """
        grades = self.__repo.get_all()
        student_id = student.get_id()
        for x in grades:
            if student_id == x.get_id_student():
                self.__repo.remove_by_id(x.get_id())

    def remove_grades_for_subject(self, subject):
        """
        Remove grades for subject.
        :param subject: The subject to remove the grades for.
        """
        grades = self.__repo.get_all()
        subject_id = subject.get_id()
        for x in grades:
            if subject_id == x.get_id_subject():
                self.__repo.remove_by_id(x.get_id())

    def get_filtered_by_subject(self, searched_subject_id):
        grades = self.__repo.get_all()
        filtered_grades = []

        for grade in grades:
            if searched_subject_id != grade.get_id_subject():
                continue

            filtered_grades.append(grade)

        return filtered_grades

    def get_grades_for_subject(self, searched_subject_id):
        """
        Get grades for subject.
        :param searched_subject_id: The id of the subject to look for
        :return: The grades for the subject
        """
        grades = self.get_filtered_by_subject(searched_subject_id)

        def sort_fn(grade):
            student = self.__student_repo.find_by_id(grade.get_id_student())
            return student.get_name(), grade.get_value()

        grades.sort(key=sort_fn)

        return grades

    def get_student_avg_grade(self, student_id, subject_id=None):
        s = 0
        n = 0
        grades = self.__repo.get_all()
        for grade in grades:
            if student_id != grade.get_id_student():
                continue
            if subject_id is not None and subject_id != grade.get_id_subject():
                continue
            s = s + grade.get_value()
            n = n + 1
        if n == 0:
            return 0
        return s / n

    def get_top_20p_avg_grades(self):
        students = self.__student_repo.get_all()
        avg_grades = []
        for student in students:
            avg_grade = self.get_student_avg_grade(student.get_id())
            avg_grades.append([student.get_name(), avg_grade])
        avg_grades.sort(key=lambda y: y[1], reverse=True)

        n = len(avg_grades) * 0.2
        n = max(n, 1)

        return avg_grades[:n]

    def stat_1(self, searched_subject):
        students = self.__student_repo.get_all()
        avg_grades = []
        for student in students:
            avg_grade = self.get_student_avg_grade(student.get_id(), subject_id=searched_subject.get_id())
            if avg_grade >= 5:
                continue
            avg_grades.append([student.get_name(), avg_grade])
        avg_grades.sort(key=lambda y: (-y[1], y[0]))

        return avg_grades
