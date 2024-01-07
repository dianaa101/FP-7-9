class Entity:
    def __init__(self, id_):
        """
        Create an entity
        :param id_: The id of the entity
        """
        self.__id_ = id_

    def get_id(self):
        """
        Get id
        :return: The id of the entity
        """
        return self.__id_

    def set_id(self, id_):
        """
        Set the id
        :param id_: The new id of the entity
        """
        self.__id_ = id_

    def set_multiple(self, id_=None):
        """
        Set multiple properties
        :param id_: The new id of the entity
        """
        if id_ is not None:
            self.set_id(id_)

    def __str__(self):
        s = f'Id: {self.__id_}\n'
        return s
