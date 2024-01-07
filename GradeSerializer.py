from entities.Grade import Grade


class GradeSerializer:
    def serialize(self, entity):
        return [
            entity.get_id(),
            entity.get_id_student(),
            entity.get_id_subject(),
            entity.get_value()
        ]

    def deserialize(self, parts):
        id_ = int(parts[0]),
        id_student = int(parts[1]),
        id_subject = int(parts[2]),
        value = int(parts[3])
        return Grade(id_, id_student, id_subject, value)