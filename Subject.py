from entities.Entity import Entity


class Subject(Entity):
    def __init__(self, id_, name, teacher_name):
        """
        Create a new subject
        :param id_: The id of the subject
        :param name: The name of the subject
        :param teacher_name: The teacher's name
        """
        super().__init__(id_)

        self.__name = name
        self.__teacher_name = teacher_name

    def get_name(self):
        """
        Get the name of the subject
        :return: The name of the subject
        """
        return self.__name

    def set_name(self, name):
        """
        Set the name of the subject
        :param name: The new name of the subject
        """
        self.__name = name

    def get_teacher_name(self):
        """
        Get the name of the teacher
        :return: The name of the teacher
        """
        return self.__teacher_name

    def set_teacher_name(self, teacher_name):
        """
        Set the name of the teacher
        :param teacher_name: The new name of the teacher
        """
        self.__teacher_name = teacher_name

    def set_multiple(self, name=None, teacher_name=None, id_=None):
        """
        Set multiple properties
        :param name: The new name of the subject
        :param teacher_name: The new name of the teacher
        :param id_: The new id of the teacher
        """
        super().set_multiple(id_=id_)
        if name is not None:
            self.set_name(name)
        if teacher_name is not None:
            self.set_teacher_name(teacher_name)

    def __str__(self):
        s = super().__str__()
        s = s + f'Name: {self.__name}\n'
        s = s + f'Teacher\'s Name: {self.__teacher_name}\n'
        return s