class Repository:
    def __init__(self):
        """
        Create a repo.
        """
        self._data = []

    def add(self, entity):
        """
        Add an entity to the repo
        :param entity: The entity to be added
        :raise ValueError: If the id of the entity already exists
        """
        for x in self._data:
            if x.get_id() == entity.get_id():
                raise ValueError(f'Id: {entity.get_id()} already exists')
        self._data.append(entity)

    def get_available_id(self, preferred_id=None):
        """
        Get the first available id
        :return: The found id
        """
        ids = []
        # Populate the 'ids' list with existing IDs
        for x in self._data:
            id_ = x.get_id()
            ids.append(id_)

        # Initialize the ID to 0, or set it to the preferred ID if provided
        id_ = 0
        if preferred_id is not None:
            id_ = preferred_id

        # Check if the current 'id_' is not in use
        while True:
            if id_ not in ids:
                return id_
            # If the current 'id_' is in use, increment it and repeat the process
            id_ = id_ + 1

    def get_all(self):
        """
        Get all the entities
        :return All the entities
        """
        return self._data[:]

    def find_by_id(self, id_):
        """
        Find an entity by id
        :param id_: The id to be found
        :return: The found entity
        :raise ValueError: If the id of the entity does not exist
        """
        for x in self._data:
            if x.get_id() == id_:
                return x
        raise ValueError(f'Id: {id_} was not found')

    def remove_by_id(self, id_):
        """
        Remove an entity by id
        :param id_: The id of the entity
        :return: The removed entity
        :raise ValueError: If the id of the entity does not exist
        """
        searched_ids = self.get_all()
        for x in searched_ids:
            if x.get_id() == id_:
                self._data.remove(x)
                return x
        raise ValueError(f'Id: {id_} does not exist')

    def update_by_id(self, searched_id, *args, **kwargs):
        """
        Update an entity by id using given arguments
        :param searched_id:
        :param id_: The id of the entity to be updated
        :param args: Leftover positional arguments
        :param kwargs: Leftover named arguments *boom*
        :raise ValueError: If the id of the entity does not exist
        :return: The updated entity
        """
        for x in self._data:
            if x.get_id() == searched_id:
                x.set_multiple(*args, **kwargs)
                return x
        raise ValueError(f'Id {searched_id} does not exist!')