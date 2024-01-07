from entities.Entity import Entity


class EntityValidator:
    def validate_entity(self, entity):
        """
        Validate an entity
        :param entity: The entity to be validated
        :raise ValueError: If the entity is not the correct type
        """
        if not isinstance(entity, Entity):
            raise ValueError('Entity is not correct type')
        self.validate_id(entity.get_id())

    def validate_id(self, id_):
        """
        Validate the entity id
        :param id_: The id to be validated
        :raise ValueError: If the entity id is not a number
        """
        if not isinstance(id_, int):
            raise ValueError('Entity id is not a number')
