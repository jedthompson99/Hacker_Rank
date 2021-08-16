def main():
    number_students = int(input())
    students = []
    grades = []

    for i in range(number_students):
        name = input('Student Name: ')
        grade = float(input("Grade: "))
        grades.append(grade)
        students.append([name, grade])

    second_lowest_grade = sorted(grades)[1]
    second_lowest_students = sorted(
        [student[0] for student in students if student[1] == second_lowest_grade])
    for student in second_lowest_students:
        print(student)


if __name__ == '__main__':
    main()
