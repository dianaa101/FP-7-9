from entities.Subject import Subject
from validator.EntityValidator import EntityValidator


class SubjectValidator(EntityValidator):
    def validate_subject(self, subject):
        """
        Validate a subject
        :param subject: The subject to be validated
        :raise ValueError: If the subject is not the correct type
        """
        super().validate_entity(subject)

        if not isinstance(subject, Subject):
            raise ValueError('Subject is not the correct type')

        es = ''

        try:
            self.validate_subject_name(subject.get_name())
        except ValueError as e:
            es = es + str(e) + '\n'

        try:
            self.validate_subject_teacher_name(subject.get_teacher_name())
        except ValueError as e:
            es = es + str(e) + '\n'

        if len(es) != 0:
            raise ValueError(es)

    def validate_subject_name(self, name):
        """
        Validate the subject's name
        :param name: The name of the subject to be validated
        :raise ValueError: If the subject name is not a string
        :raise ValueError: If the subject name is empty
        """
        if not isinstance(name, str):
            raise ValueError('Subject name is not the correct type')
        if len(name) == 0:
            raise ValueError('Subject name is empty')

    def validate_subject_teacher_name(self, teacher_name):
        """
        Validate the teacher's name of a subject
        :param teacher_name: The teacher's name to be validated
        :raise ValueError: If the teacher's name is not a string
        :raise ValueError: If the teacher's name is empty
        """
        if not isinstance(teacher_name, str):
            raise ValueError('Teacher name is not the correct type')
        if len(teacher_name) == 0:
            raise ValueError('Teacher name is empty')
