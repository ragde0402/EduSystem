from group import Group
from student import Student
from lesson import Lesson
from teacher import Teacher


class School:
    def __init__(self):
        self.groups = []
        self.lessons = []
        self.students = []
        self.teachers = []

    def remove_group(self, class_: object):
        """
        updates list of existing groups in school and updating students.group to None for each from the group.
        :param class_:
        :return:
        """
        self.groups = [c for c in self.groups if c != class_]
        for student in self.students:
            if student.group == class_:
                student.group = None

    def add_lesson(self, name, person: object, duration=1):
        """
        creates new lesson with the lecturer. Add those classes to the list of classes.
        :param name:
        :param person:
        :param duration:
        :return:
        """
        lesson = Lesson(name, duration, person)
        self.lessons.append(lesson)

    def remove_lesson(self, lesson: object):
        """
        removes classes from the list of all avalialible classes in school.
        :param lesson:
        :return:
        """
        self.lessons = [l for l in self.lessons if lesson != l]

    def create_group(self, name):
        """
        creates new group. At the begining it is empty. You need to use some group methods to add students and
        activities to it
        :param name:
        :return:
        """
        group = Group(name)
        self.groups.append(group)

    def create_student(self, name, last_name):
        """
        creates a person who is just a student you need to append him to group and it will have access to all activities
        from his group of assignment
        :param name:
        :param last_name:
        :return:
        """
        student = Student(name, last_name)
        self.students.append(student)

    def create_teacher(self, first_name, last_name):
        """
        lecturer of the lessons/activities.
        :param first_name:
        :param last_name:
        :return:
        """
        teacher = Teacher(first_name, last_name)
        self.teachers.append(teacher)









