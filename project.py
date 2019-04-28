from stedent import Student
import os
import sys


def admin_li():
    while 1:
        os.system('cls')
        print(green, "Logged as in 'admin' ")
        print(endc)
        print("--Main Menu")
        print("  |- 1) Student Management ")
        print("  |- 2) Course Management ")
        print("  |- 3) Exit ")
        choose = input("\nchoose(1_3):")

        if choose == '1':
            os.system('cls')
            print("--Student Management Menu")
            print("  |- 1) List all Student ")
            print("  |- 2) Browse a Student ")
            print("  |- 3) Search Student ")
            print("  |- 4) Add a Student ")
            print("  |- 5) Edit a Student ")
            print("  |- 6) Remove a Student ")
            print("  |- 7) Back ")

            ch = input("\nchoose(1_7):")

            if ch == '1':
                os.system('cls')
                students = Student()
                print("student number, fname, lname, avg\n")
                print(students.show_all_students())
                input("\npress any key to back:")
                continue

            elif ch == '2':
                os.system('cls')
                students = Student()
                student_number = input("Enter student number: ")
                print(students.show_a_student(student_number))
                input("\npress any key to back:")
                continue

            elif ch == '3':
                os.system('cls')
                students = Student()
                student_number = input("Enter student number: ")
                print(students.show_search(student_number))
                input("\npress any key to back:")
                continue

            elif ch == '4':
                os.system('cls')
                add_std = Student()
                student_number = input("Enter student number: ")
                fname = input("Enter student first name: ")
                lname = input("Enter student last name: ")
                avg = input("Enter student average: ")

                if add_std.add(student_number, fname, lname, avg):
                    print( green + "you added a student successfully." + endc)

                else:
                    print(red + "this student number is already exists!!" + endc)
                input("\npress any key to back:")
                continue

            elif ch == '5':
                os.system('cls')
                chek_edit = Student()
                student_number = input("Enter student number to edit: ")
                print(chek_edit.show_a_student(student_number))
                if chek_edit.chek_edit(student_number):
                    new_student_number = input("Enter new student number: ")
                    new_fname = input("Enter student first name: ")
                    new_lname = input("Enter student last name: ")
                    new_avg = input("Enter student average: ")
                    edit = Student()
                    edit.edit(student_number, new_student_number, new_fname, new_lname, new_avg)
                    print(green + "you edited student successfully." + endc)
                    input("\npress any key to back:")
                input("\npress any key to back:")

            elif ch == '6':
                os.system('cls')
                remove_std = Student()
                student_number = input("Enter student number to remove: ")
                print(remove_std.show_a_student(student_number))
                x = input(red + "are you sure you want to delete(y|n)? " + endc)
                if x == 'y':
                    remove = Student()
                    remove.remove(student_number)
                    print("Student deleted!")
                    input("\npress any key to back:")
                elif x == 'n':
                    continue

            elif ch == '7':
                continue

            else:
                print("You entered a wrong number. Please try again.")
                continue

        if choose == '2':
            os.system('cls')
            print("--Course Management Menu")
            print("  |- 1) List all Course")
            print("  |- 2) Browse a Course")
            print("  |- 3) Search Course")
            print("  |- 4) Add a Course")
            print("  |- 5) Edit a Course ")
            print("  |- 6) Remove a Course ")
            choose = input("\nchoose(1_6):")
        if choose == '3':
           a = input(red + "are you sure(y/n)?" + endc)
           if a == 'y':
             os.system('cls')
             sys.exit(0)
           if a == 'n':
              continue


def manager_li():
    pass


def teacher_li():
    pass


def student_li():
    pass


if __name__ == "__main__":

    os.system('cls')
    print("================== Welcome ==================\n")
    print("---Login\n")
    endc = '\033[0m'
    green = '\033[1;32;40m'
    red = '\033[31m'

    while 1:
        # use = input("\tEnter your username:")
        # password = input("\tEnter your password:")
        use = 'admin'
        password = '1234'
        login = Student()
        flag = login.login(use, password)
        flag = int(flag)

        if flag == 0:
            os.system('cls')
            print(red, "\nError:Username or Password do not match!!")
            print(endc)

        elif flag == 1:
            admin_li()

        elif flag == 2:
            os.system('cls')
            print(green, "Logged as in 'course manager' ")
            print(endc)
            manager_li()
            break

        elif flag == 3:
            os.system('cls')
            print(green, "Logged as in 'student' ")
            print(endc)
            student_li()
            break
        elif flag == 4:
            os.system('cls')
            print(green, "Logged as in 'teacher' ")
            print(endc)
            teacher_li()
            break
        else :
            print("Error! Flag is not correct.")
            continue
