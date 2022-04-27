from models.student import Student
from models.teacher import Teacher
import random

class Classroom:

    def __init__(self, main_teacher, nb_places_max):
        self.students = []
        self.MAX_NB_PLACE = nb_places_max
        self.main_teacher = main_teacher

    # Méthodes
    def add_student(self, student):

        if isinstance(student, Student):
            if len(self.students) < self.MAX_NB_PLACE:
                self.students.append(student)
                print('Etudiant ajouté')
            else:
                print("Plus de place")
        else:
            print("Ce n'est pas un étudiant")

    def start_course(self, teacher: Teacher, course):
        teacher.teach(course)

        for student in self.students:
            if random.randint(0, 10) > 2:
                student.go_to_class(course)
            else:
                student.skip_class(course)
