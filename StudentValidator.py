from entities.Student import Student
from validator.EntityValidator import EntityValidator


class StudentValidator(EntityValidator):
    def validate_student(self, student):
        super().validate_entity(student)
        if not isinstance(student, Student):
            raise ValueError('Student is not correct type')
        self.validate_student_name(student.get_name())

    def validate_student_name(self, name):
        """
        Validate a student's name
        :param name: The name of the student to be validated
        :raise ValueError: If the student name is not a string
        :raise ValueError: If the student name is empty
        """
        if not isinstance(name, str):
            raise ValueError('Student name is not a string')
        if len(name) == 0:
            raise ValueError('Student name empty')