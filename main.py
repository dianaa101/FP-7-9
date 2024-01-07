from entities.StudentSerializer import StudentSerializer
from repo.FileRepository import FileRepository
from repo.Repository import Repository
from service.GradeService import GradeService
from service.StudentService import StudentService
from service.SubjectService import SubjectService
from tests import run_tests
from ui.Console import Console
from validator.GradeValidator import GradeValidator
from validator.StudentValidator import StudentValidator
from validator.SubjectValidator import SubjectValidator

run_tests()

student_repo = Repository()
# student_serializer = StudentSerializer()
# student_repo = FileRepository('studens.txt', student_serializer)
student_validator = StudentValidator()
student_service = StudentService(student_repo, student_validator)

subject_repo = Repository()
subject_validator = SubjectValidator()
subject_service = SubjectService(subject_repo, subject_validator)

grade_repo = Repository()
grade_validator = GradeValidator()
grade_service = GradeService(grade_repo, grade_validator, student_repo, subject_repo)

console = Console(student_service, subject_service, grade_service)
console.run()

