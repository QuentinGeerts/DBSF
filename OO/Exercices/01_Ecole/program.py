# from package.fichier import class/methode [, ...]
from models.classroom import Classroom
from models.student import Student
from models.teacher import Teacher
import datetime

if __name__ == "__main__":
    print(__name__)
    quentin = Teacher("Geerts", "Quentin", datetime.datetime(2021, 3, 15),"quentin.geerts@bstorm.be")

    print(quentin.hire_date)

    class1 = Classroom(quentin, 2)

    student1 = Student("De Niro", "Robert")
    student2 = Student("Roberts", "Julia")
    student3 = Student("Clark", "Kent")

    class1.add_student(student1)
    class1.add_student(student2)
    class1.add_student(student3)


    class1.start_course(quentin, "Python OO")
