class Student:
    def __init__(self, imie, klasa):
        self.name = imie
        self.class_name = klasa
        self.subjects = {}


class Teacher:
    def __init__(self, imie, subject, classes):
        self.name = imie
        self.subject = subject
        self.classes = classes


class Tutor:
    def __init__(self, name, class_name):
        self.name = name
        self.class_name = class_name


class School:
    def __init__(self):
        self.students = []
        self.teachers = []
        self.tutors = []

    def create_student(self, name, class_name):
        self.students.append(Student(name, class_name))

    def create_teacher(self, name, subject, classes):
        self.teachers.append(Teacher(name, subject, classes))

    def create_tutor(self, name, class_name):
        self.tutors.append(Tutor(name, class_name))

    def manage(self):
        global subject
        while True:
            print("Dostepne opcje:")
            print("klasa")
            print("uczen")
            print("nauczyciel")
            print("wychowawca")
            print("koniec")

            command = input("Wybierz opcje: ")

            if command == "klasa":
                class_name = input("Podaj nazwe klasy: ")
                print("Uczniowie:")
                for student in self.students:
                    if student.class_name == class_name:
                        print(student.name)
                print("Wychowawca:")
                for tutor in self.tutors:
                    if tutor.class_name == class_name:
                        print(tutor.name)

            elif command == "uczen":
                name = input("Podaj imie i nazwisko ucznia: ")
                for student in self.students:
                    if student.name == name:
                        print("Lekcje:")
                        for subject in student.subjects:
                            print(subject)
                        print("Nauczyciele:")
                        for teacher in self.teachers:
                            if student.class_name in teacher.classes \
                                    and subject in teacher.subject:
                                print(teacher.name)

            elif command == "nauczyciel":
                name = input("Podaj imie i nazwisko nauczyciela: ")
                print("Klasy:")
                for teacher in self.teachers:
                    if teacher.name == name:
                        for class_name in teacher.classes:
                            print(class_name)

            elif command == "wychowawca":
                name = input("Podaj imie i nazwisko wychowawcy: ")
                print("Uczniowie:")
                for tutor in self.tutors:
                    if tutor.name == name:
                        for student in self.students:
                            if student.class_name == tutor.class_name:
                                print(student.name)

            elif command == "koniec":
                break


school = School()

while True:
    print("Dostepne opcje:")
    print("utworz")
    print("zarzadzaj")
    print("koniec")

    command = input("Wybierz opcje: ")

    if command == "utworz":
        while True:
            print("Dostepne opcje:")
            print("uczen")
            print("nauczyciel")
            print("wychowawca")
            print("koniec")

            command = input("Wybierz opcje: ")

            if command == "uczen":
                name = input("Podaj imie i nazwisko ucznia: ")
                class_name = input("Podaj nazwe klasy: ")
                school.create_student(name, class_name)

            elif command == "nauczyciel":
                name = input("Podaj imie i nazwisko nauczyciela: ")
                subject = input("Podaj nazwe przedmiotu: ")
                classes = []
                while True:
                    class_name = input("Podaj nazwe klasy "
                                       "(lub pusta linia aby zakonczyc): ")
                    if class_name == "":
                        break
                    classes.append(class_name)
                school.create_teacher(name, subject, classes)

            elif command == "wychowawca":
                name = input("Podaj imie i nazwisko wychowawcy: ")
                class_name = input("Podaj nazwe klasy: ")
                school.create_tutor(name, class_name)

            elif command == "koniec":
                break

    elif command == "zarzadzaj":
        school.manage()

    elif command.lower() == "koniec":
        print("Zamykanie")
        break
