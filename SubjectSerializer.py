from entities.Subject import Subject


class SubjectSerializer:
    def serialize(self, entity):
        return [
            entity.get_id(),
            entity.get_name(),
            entity.get_teacher_name()
        ]

    def deserialize(self, parts):
        id_ = int(parts[0]),
        name = parts[1],
        teacher_name = parts[2]
        return Subject(id_, name, teacher_name)