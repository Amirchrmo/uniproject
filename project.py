from stedent import Student
from course import Course
import os
import sys

use = ''
password = ''

def admin_li():
    while 1:
        os.system('cls')
        print(green, "Logged as in 'admin' ")
        print(endc)
        print("--Main Menu")
        print("  |- 1) Student Management ")
        print("  |- 2) Course Management ")
        print("  |- 3) Change Username ")
        print("  |- 4) Exit ")
        choose = input("\nchoose(1_4):")

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
                choose = 0
                continue

            elif ch == '2':
                students = Student()
                courses = Course()
                student_number = input("Enter student number: ")
                print(students.show_a_student(student_number))

                with open("student_courses.txt") as file:
                    sac = file.readlines()

                for item in sac:
                    i = item.split(",")
                    if (i[0] == student_number):
                        showc = (courses.show_a_course(i[1].strip())).strip()
                        print("\t" + showc[2:])


                input("\npress any key to back:")
                choose = 0
                continue

            elif ch == '3':
                students = Student()
                student_number = input("Enter student number: ")
                print(students.search(student_number))
                input("\npress any key to back:")
                choose = 0
                continue

            elif ch == '7':
                continue

            else :
                print("You entered a wrong number. Please try again.")
                continue

        elif choose == '2':
            os.system('cls')
            print("--Course Management Menu")
            print("  |- 1) List all Course")
            print("  |- 2) Browse a Course")
            print("  |- 3) Search Course")
            print("  |- 4) Add a Course")
            print("  |- 5) Edit a Course ")
            print("  |- 6) Remove a Course ")
            ch = input("\nchoose(1_6):")

            if ch == '1':
                students = Course()
                # print("student number, fname, lname, avg\n")
                print(students.show_all_courses())
                input("\npress any key to back:")
                choose = 0
                continue

            elif ch == '2':
                students = Course()
                student_number = input("Enter course number: ")
                print(students.show_a_course(student_number))
                input("\npress any key to back:")
                choose = 0
                continue

            elif ch == '3':
                students = Course()
                cnumber = input("Enter course number: ")
                print(students.search(cnumber))
                input("\npress any key to back:")
                choose = 0
                continue

            elif ch == '7':
                continue

            else :
                print("You entered a wrong number. Please try again.")
                continue
        elif choose == '3':
            users = []
            with open("users.txt") as File:
                users = File.readlines()

            for inum, item in enumerate(users):
                i = (item.split(","))
                if(use == i[0].strip()):
                    pass4ch = input("Please Enter your password :")
                    if(i[1].strip() == pass4ch):
                        newUsername = input("Please enter your new Username:")
                        newPassword = input("Please enter your new Password:")

                        users[inum] = "{}, {}, {}".format(newUsername, newPassword, i[2].strip())
                        with open("users.txt", "w") as File:
                            for item in users:
                                File.write(item + "\n")
                else:
                    continue

        elif choose == '4':
           a = input(red + "are you sure(y/n)?" + endc)
           if a == 'y':
             os.system('cls')
             sys.exit(0)
           if a == 'n':
             continue
        else:
            print("Error please try again !")
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
        use = input("\tEnter your username:")
        password = input("\tEnter your password:")
        # use = 'admin'
        # password = '1234'
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
