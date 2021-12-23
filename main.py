from school import School
import random

if __name__ == "__main__":
    school = School()

### random data test code

    for x in range(2):
        school.create_group(f'group {x}')

    for x in range(10):
        school.create_student('John', f'{x + 1}')

    for student in school.students:
        group = random.choice(school.groups)
        group.add_student(student)

    for x in range(5):
        school.create_teacher('Teacher', f'{x}')

    for x in range(10):
        school.add_lesson(f'Lesson {x}', random.choice(school.teachers))

    for group in school.groups:
        for k, v in group.schedule.items():
            for x in range(random.randint(3, 7)):
                group.add_lesson(random.choice(school.lessons), k)
        print(group.name)
        for day, value in group.schedule.items():
            print(day)
            print([l.name for l in value])
        for student in group.students:
            for subject in group.list_of_classes:
                for r in range(random.randint(1, 3)):
                    student.add_grade(subject, random.randint(1, 6))
            print(student.first_name)
            print(student.last_name)
            print(student.grades)
            student.count_final_grade()
