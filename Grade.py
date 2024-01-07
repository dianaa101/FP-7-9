from entities.Entity import Entity


class Grade(Entity):
    def __init__(self, id_, id_student, id_subject, value):
        """
        Create a new grade
        :param id_: The id of the grade
        :param id_student: The id of the student
        :param id_subject: The id of the subject
        :param value: The value of the grade
        """
        super().__init__(id_)

        self.__id_student = id_student
        self.__id_subject = id_subject
        self.__value = value

    def get_id_student(self):
        """
        Get the id of the student
        :return: The id of the student
        """
        return self.__id_student

    def set_id_student(self, id_student):
        """
        Set the id of the student
        :param id_student: The new id
        """
        self.__id_student = id_student

    def get_id_subject(self):
        """
        Get the id of the subject
        :return: The id of the subject
        """
        return self.__id_subject

    def set_id_subject(self, id_subject):
        """
        Set the id of the subject
        :param id_subject: The new id of the subject
        """
        self.__id_subject = id_subject

    def get_value(self):
        """
        Get the value of the grade
        :return: The value of the grade
        """
        return self.__value

    def set_value(self, value):
        """
        Set the value of the grade
        :param value: The new value of the grade
        """
        self.__value = value

    def set_multiple(self, id_student=None, id_subject=None, value=None, id_=None):
        """
        Set multiple properties
        :param id_student: The new id of the student
        :param id_subject: The new id of the subject
        :param value: The value of the grade
        :param id_: The new id of the grade
        """
        super().set_multiple(id_=id_)
        if id_student is not None:
            self.set_id_student(id_student)
        if id_subject is not None:
            self.set_id_subject(id_subject)
        if value is not None:
            self.set_value(value)
