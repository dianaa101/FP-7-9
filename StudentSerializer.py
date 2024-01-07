from entities.Student import Student


class StudentSerializer:
    def serialize(self, entity):
        return [
            entity.get_id(),
            entity.get_name()
        ]

    def deserialize(self, parts):
        id_ = int(parts[0])
        name = parts[1]
        return Student(id_, name)
