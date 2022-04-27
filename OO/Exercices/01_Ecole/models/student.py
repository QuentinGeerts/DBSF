class Student:

    def __init__(self, lastname, firstname):
        self.lastname = lastname
        self.firstname = firstname
        self.matricule = lastname[:4] + firstname[:3]

    def skip_class(self, course):
        print(f"{self.lastname} {self.firstname} sèche le cours de {course}.")

    def go_to_class(self, course):
        print(f"{self.lastname} {self.firstname} suit le cours de {course}.")