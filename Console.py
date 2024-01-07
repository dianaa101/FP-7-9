from service.GradeService import GradeService
from service.StudentService import StudentService
from service.SubjectService import SubjectService


class Console:
    def __init__(self, student_service: StudentService, subject_service: SubjectService, grade_service: GradeService):
        self.__student_service = student_service
        self.__subject_service = subject_service
        self.__grade_service = grade_service

    def run(self):
        print("""
1. Add student
2. Update student
3. Show students
4. Delete student
5. Add subject
6. Update subject
7. Show subjects
8. Delete subject
9. Add grade
10. Show grades
11. Show grades for subject
12. Find student
13. Find subject
14. Show avg grades for top 20% students
15. Add random
16. Get students with grade lower than 5 sorted
17. Exit
""")
        while True:
            try:
                o = int(input("o: "))
            except ValueError:
                continue
            match o:
                case 1:
                    self.add_student()
                case 2:
                    self.update_student()
                case 3:
                    self.show_students()
                case 4:
                    self.delete_student()
                case 5:
                    self.add_subject()
                case 6:
                    self.update_subject()
                case 7:
                    self.show_subjects()
                case 8:
                    self.delete_subject()
                case 9:
                    self.add_grade()
                case 10:
                    self.show_grades()
                case 11:
                    self.show_grades_for_subject()
                case 12:
                    self.find_student()
                case 13:
                    self.find_subject()
                case 14:
                    self.show_avg_grades_for_top_20p_students()
                case 15:
                    self.add_random()
                case 16:
                    self.get_students_with_grade_lower_than_5_sorted()
                case 17:
                    break

    def find_subject(self):
        try:
            id_ = int(input('Subject ID: '))
            subject = self.__subject_service.find_by_id(id_)
            print(subject)
        except ValueError as e:
            print(e)

    def find_student(self):
        try:
            id_ = int(input('Student ID: '))
            student = self.__student_service.find_by_id(id_)
            print(student)
        except ValueError as e:
            print(e)

    def show_grades_for_subject(self):
        try:
            subject_id = int(input('Subject ID: '))
            subject = self.__subject_service.find_by_id(subject_id)
            print(subject)
            grades = self.__grade_service.get_grades_for_subject(subject_id)
            for grade in grades:
                student = self.__student_service.find_by_id(grade.get_id_student())
                print(f'Grade: {student.get_name()}, {grade.get_value()}')
        except ValueError as e:
            print(e)

    def show_grades(self):
        grades = self.__grade_service.get_all()
        for grade in grades:
            print(grade)

    def add_grade(self):
        try:
            subject_id = int(input('Subject ID: '))
            subject = self.__subject_service.find_by_id(subject_id)
            student_id = int(input('Student ID: '))
            student = self.__student_service.find_by_id(student_id)
            value = int(input('Value: '))
            grade = self.__grade_service.create(student, subject, value)
            print(f'Grade: {student.get_name()}, {grade.get_value()}, {subject.get_name()}')
        except ValueError as e:
            print(e)

    def delete_subject(self):
        try:
            id_ = int(input('Subject ID: '))
            subject = self.__subject_service.remove(id_)
            self.__grade_service.remove_grades_for_subject(subject)
            print(subject)
        except ValueError as e:
            print(e)

    def show_subjects(self):
        subjects = self.__subject_service.get_all()
        for x in subjects:
            print(x)

    def update_subject(self):
        try:
            id_ = int(input('Subject ID: '))
            name = input('Subject Name: ')
            teacher_name = input('Teacher name: ')
            if len(name) == 0:
                name = None
            if len(teacher_name) == 0:
                teacher_name = None
            subject = self.__subject_service.update(id_, name, teacher_name)
            print(subject)
        except ValueError as e:
            print(e)

    def add_subject(self):
        try:
            name = input('Subject Name: ')
            teacher_name = input('Teacher Name: ')
            subject = self.__subject_service.create(name, teacher_name)
            print(subject)
        except ValueError as e:
            print(e)

    def delete_student(self):
        try:
            id_ = int(input('Student ID: '))
            student = self.__student_service.remove(id_)
            self.__grade_service.remove_grades_for_student(student)
            print(student)
        except ValueError as e:
            print(e)

    def show_students(self):
        students = self.__student_service.get_all()
        for x in students:
            print(x)

    def update_student(self):
        try:
            id_ = int(input('Student ID: '))
            name = input('Student Name: ')
            if len(name) == 0:
                name = None
            student = self.__student_service.update(id_, name)
            print(student)
        except ValueError as e:
            print(e)

    def add_student(self):
        try:
            name = input('Student Name: ')
            student = self.__student_service.create(name)
            print(student)
        except ValueError as e:
            print(e)

    def show_avg_grades_for_top_20p_students(self):
        avg_grades = self.__grade_service.get_top_20p_avg_grades()
        for avg_grade in avg_grades:
            print(f'Average grade: {avg_grade[0]} {avg_grade[1]}')

    def get_students_with_grade_lower_than_5_sorted(self):
        try:
            subject_id = int(input('Subject ID: '))
            subject = self.__subject_service.find_by_id(subject_id)
            print(subject)
            avg_grades = self.__grade_service.stat_1(subject)
            for avg_grade in avg_grades:
                print(f'Average grade: {avg_grade[0]}, {avg_grade[1]}')
        except ValueError as e:
            print(e)
            
    def add_random(self):
        try:
            n = int(input('Nr. of students: '))
            students = self.__student_service.add_random(n)
            for x in students:
                print(x)
        except ValueError as e:
            print(e)
