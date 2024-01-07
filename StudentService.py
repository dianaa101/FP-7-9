from entities.Student import Student
from repo.Repository import Repository
from validator.StudentValidator import StudentValidator
from utils import *


class StudentService:
    def __init__(self, repo: Repository, validator: StudentValidator):
        """
        Create a student service
        :param repo: The student repository
        """
        self.__repo = repo
        self.__validator = validator

    def create(self, name):
        """
        Create a student
        :param name: The name of the student
        :return: The created student
        """
        id_ = self.__repo.get_available_id()
        student = Student(id_, name)
        self.__validator.validate_student(student)
        self.__repo.add(student)
        return student

    def remove(self, id_):
        """
        Remove student by id
        :param id_: The id of the student
        :return: The removed student
        """
        return self.__repo.remove_by_id(id_)

    def get_all(self):
        """
        Get all the students
        :return: All the students
        """
        return self.__repo.get_all()

    def find_by_id(self, id_):
        """
        Find a student by id
        :param id_: The id of the student to be found
        :return: The found student
        """
        return self.__repo.find_by_id(id_)

    def update(self, id_, name):
        """
        Update a student's info
        :param id_: The id of the student
        :param name: The new name of the student
        :return: The updated info about the student
        """
        self.__validator.validate_student_name(name)
        return self.__repo.update_by_id(id_, name=name)

    def add_random(self, n):
        """
        Add random students
        :param n: Number of students to add
        :return: The added students
        """
        students = []
        for x in range(n):

            first_name = random_name_between(3, 10)
            last_name = random_name_between(3, 9)
            id_ = random.randint(0, 10000)
            id_ = self.__repo.get_available_id(preferred_id=id_)
            student = Student(id_, f'{first_name} {last_name}')
            self.__validator.validate_student(student)
            self.__repo.add(student)
            students.append(student)

        return students
