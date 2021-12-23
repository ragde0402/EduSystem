class Group:
    def __init__(self, name, *args):
        """
        if you use it in different place you can create all list of students at the beginning
        :param name:
        :param args:
        """
        self.students = [*args]
        self.list_of_classes = []
        self.schedule = {'Monday': [],
                         'Tuesday': [],
                         'Wednesday': [],
                         'Thursday': [],
                         'Friday': []
                         }
        self.name = name

    def add_student(self, student):
        """
        Appends student object to the group
        :param student:
        :return:
        """
        self.students.append(student)
        student.group = self

    def remove_student(self, student):
        """
        removes student from the group and changes its assignment to None.
        :param student:
        :return:
        """
        self.students = [s for s in self.students if s != student]
        student.group = None

    def add_lesson(self, lesson, day):
        """
        add new lesson object to specified to the end of specified day
        :param lesson:
        :param day:
        :return:
        """
        if lesson not in self.list_of_classes:
            self.list_of_classes.append(lesson)
        self.schedule[day].append(lesson)

    def remove_lesson(self, lesson, day):
        """
        removes lesson object from specified day if there is none return print
        :param lesson:
        :param day:
        :return:
        """
        if self.schedule[day] == KeyError:
            print('wrong day')
        self.schedule[day] = [l for l in self.schedule[day] if l != lesson]


