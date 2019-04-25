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
                students = Student()
                print("student number, fname, lname, avg\n")
                print(students.show_all_students())
                input("\npress any key to back:")
                continue

            elif ch == '2':
                students = Student()
                student_number = input("Enter student number: ")
                print(students.show_a_student(student_number))
                input("\npress any key to back:")
                continue

            elif ch == '3':
                students = Student()
                student_number = input("Enter student number: ")
                print(students.search(student_number))
                input("\npress any key to back:")
                continue

            elif ch == '4':
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
            elif ch == '7':
                continue

            else :
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
            print(red, "\nEror:Username or Password do not match!!")
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
