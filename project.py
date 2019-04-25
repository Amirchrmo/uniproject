from stedent import Student
import os
import sys


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

    if flag == 1:
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
                choose = input("\nchoose(1_6):")
                if choose == '1':
                    students = Student()
                    print("student number, fname, lname, avg\n")
                    print(students.show_all_students())
                    input("\npress any key to back:")
                    choose = 0
                if choose == '2':
                    students = Student()
                    student_number = input("Enter student number: ")
                    print(students.show_a_student(student_number))
                    input("\npress any key to back:")
                    choose = 0
                if choose == '3':
                    students = Student()
                student_number = input("Enter student number: ")
                print(students.search(student_number))
                input("\npress any key to back:")
                choose = 0
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


    if flag == 2:
       os.system('cls')
       print(green, "Logged as in 'course manager' ")
       print(endc)
       break
    if flag == 3:
        os.system('cls')
        print(green, "Logged as in 'student' ")
        print(endc)
        break
    if flag == 4:
        os.system('cls')
        print(green, "Logged as in 'teacher' ")
        print(endc)
        break
