class Student:
    def __init__(self, name, surname):
        self.first_name = name
        self.last_name = surname
        self.group = None
        self.grades = {

        }

    def add_grade(self, class_, grade: int):
        if self.group and class_ in self.group.list_of_classes:
            try:
                self.grades[class_].append(grade)
            except KeyError:
                self.grades[class_] = [grade]
        else:
            print(f"There is no classes like {class_} in {self.first_name}'s schedule.")

    def count_final_grade(self):
        for k, grades in self.grades.items():
            print(str(k.name) + f': {sum(grades) / len(grades)}')


