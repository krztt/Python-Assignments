import math



# prompt the user of their grades
def get_grades():
    print('Enter the grades of your 3 programming project:')
    grades = list()
    count = 0
    while count < 3 :
        program_grade = int(input(f'Program {count + 1} grade: '))
        count += 1
        grades.append(program_grade)
    print('Is this the correct scores?')
    for i in range(len(grades)):
        print("Program", (i +1 ), ":", grades[i])
    while True:
        choice = input('Y/N ').strip().upper()
        if choice == 'Y':
        # math functions
            sum = math.fsum(grades)
            average = sum/3

            print('Computed Average(rounded):', math.ceil(average))
            if average >= 75:
                print('You have passed')
            else:
                print('Sorry, your grades are below the passing grade')
            return grades
        elif choice == 'N':
            return get_grades()
        else:
            print('Error, type Y or N')

get_grades()

