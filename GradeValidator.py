from entities.Grade import Grade
from validator.EntityValidator import EntityValidator


class GradeValidator(EntityValidator):
    def validate_grade(self, grade):
        """
        Validate grade
        :param grade: The grade to be validated
        :raise ValueError: If the grade is not the correct type
        """
        super().validate_entity(grade)
        if not isinstance(grade, Grade):
            raise ValueError('Grade is not the correct type')
        self.validate_grade_value(grade.get_value())

    def validate_grade_value(self, value):
        """
        Validate the grade's value
        :param value: The value of the grade to be validated
        :raise ValueError: If the grade value is not a number
        :raise ValueError: If the grade value is not between 1 and 10
        """
        if not isinstance(value, int):
            raise ValueError('Grade value is not the correct type')
        if value < 1 or value > 10:
            raise ValueError('Grade value is not between 1-10')
