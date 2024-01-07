from entities.Entity import Entity


class Student(Entity):
    def __init__(self, id_, name):
        """
        Create a new student
        :param id_: The id of the student
        :param name: The name of the student
        """
        super().__init__(id_)

        self.__name = name

    def get_name(self):
        """
        Get the name of the student
        :return: The name of the student
        """
        return self.__name

    def set_name(self, name):
        """
        Set the name of the student
        :param name: The new name of the student
        """
        self.__name = name

    def set_multiple(self, name=None, id_=None):
        """
        Set multiple properties
        :param name: The new name of the student
        :param id_: The new id of the student
        """
        super().set_multiple(id_=id_)

        if name is not None:
            self.set_name(name)

    def __str__(self):
        s = super().__str__()
        s = s + f'Name: {self.__name}\n'
        return s