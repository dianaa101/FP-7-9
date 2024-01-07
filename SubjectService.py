from entities.Subject import Subject
from repo.Repository import Repository
from validator.SubjectValidator import SubjectValidator


class SubjectService:
    def __init__(self, repo: Repository, validator: SubjectValidator):
        """
        Create a subject service
        :param repo: The subject repository
        """
        self.__repo = repo
        self.__validator = validator

    def create(self, name, teacher_name):
        """
        Create a subject
        :param name: The name of the subject
        :param teacher_name: The teacher's name responsible for the subject
        :return: The created subject
        """
        id_ = self.__repo.get_available_id()
        subject = Subject(id_, name, teacher_name)
        self.__validator.validate_subject(subject)
        self.__repo.add(subject)
        return subject

    def remove(self, id_):
        """
        Remove subject by id
        :param id_: The id of the subject to be removed
        :return: The removed subject
        """
        return self.__repo.remove_by_id(id_)

    def get_all(self):
        """
        Get all the subjects
        :return: All the subjects
        """
        return self.__repo.get_all()

    def find_by_id(self, id_):
        """
        Find subject by id
        :param id_: The id of the subject to be found
        :return: The found subject
        """
        return self.__repo.find_by_id(id_)

    def update(self, id_, name, teacher_name):
        """
        Update a subject
        :param id_: The id of the subject
        :param name: The new name of the subject
        :param teacher_name: The teacher's new name responsible for the subject
        :return: The updated subject
        """
        if name is not None:
            self.__validator.validate_subject_name(name)
        if teacher_name is not None:
            self.__validator.validate_subject_teacher_name(teacher_name)
        return self.__repo.update_by_id(id_, name=name, teacher_name=teacher_name)
