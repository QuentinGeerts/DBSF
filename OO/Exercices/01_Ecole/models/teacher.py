class Teacher:

    def __init__(self, lastname, firstname, hire_date, email):
        self.lastname = lastname
        self.firstname = firstname
        self.hire_date = hire_date
        self.email = email

    def teach(self, course):
        print(f"{self.lastname} {self.firstname} donne le cours de {course}")