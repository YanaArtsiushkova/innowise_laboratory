students = []

menu = {
    '1.': 'Add a new student',
    '2.': 'Add grades for a student',
    '3.': 'Show report (all students)',
    '4.': 'Find top performer',
    '5.': 'Exit'
}

while True:
    print('--- Student Grade Analyzer ---')
    for key, value in menu.items():
        print(key, value)
    choice = input('Enter your choice: ')

    if choice == '1':
        new_student = input('Enter student name: ')
        name_exists = False                         #flag - does the name exist or not
        #Is the student on the list or not?
        for student in students:
            if student['name'].lower() == new_student.lower():
                name_exists = True
                break
        if name_exists:
            print('The student already exists')
        else:
            info = {'name': new_student, 'grades': []}
            students.append(info)

    elif choice == '2':
        name_student = input('Enter student name: ')
        name_found = None
        #find the name in the list
        for student in students:
            if student['name'].lower() == name_student.lower():
                name_found = student
                break
        if name_found is None:
            print('Student not found')
        else:
            print(f"Enter grades for {name_found['name']} (0–100). Type 'done' to finish.")
            while True:
                grade = input("Enter a grade (or 'done' to finish): ")
                if grade.lower() == 'done':
                    break
                try:
                    val = int(grade)                 #adding and checking the grade for the data type
                    if 0 <= val <= 100:
                        name_found['grades'].append(val)
                    else:
                        print('Grade must be between 0 and 100')
                except ValueError:
                    print('Invalid input. Please enter a number.')

    elif choice == '3':
        print('---Student Report---')
        if len(students) == 0:
            print('The list is empty')
        else:
            all_avg = []
            #Finding the average grade for each student
            for student in students:
                name = student['name']
                grade = student['grades']
                try:
                    avg = sum(grade)/len(grade)
                    print(f"{name}'s average grade is {avg}.")
                    all_avg.append(avg)
                except ZeroDivisionError:
                    print(f"{name}'s average grade is N/A.")
            if not all_avg:
                print('No grades')
            else:
                print('--------------------')
                print('Max Average: ', max(all_avg))
                print('Min Average: ', min(all_avg))
                print('Overall Average: ', sum(all_avg)/len(all_avg))

    elif choice == '4':
        if not students:
            print('The list is empty.')
        else:
            valid_students = [student for student in students if len(student['grades']) > 0]
            if not valid_students:
                print('No grades.')
            else:
                top_student = max(valid_students,
                    key=lambda s: sum(s['grades']) / len(s['grades'])
                )
                top_avg = sum(top_student['grades']) / len(top_student['grades'])
                print(
                    f"The student with the highest average is {top_student['name']} with a grade of {top_avg}"
                )
    elif choice == '5':
        break

    else:
        print('Invalid choice. Try again.')