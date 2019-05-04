from stedent import Student
from course import Course
import os
import sys

use = ''
password = ''

endc = '\033[0m'
green = '\033[1;32;40m'
red = '\033[31m'
orange = "\033[33m"

bMain = False

def admin_li():
    while 1:
        os.system('cls')
        print(green, "Logged as in 'admin' ")
        print(endc)
        print("--Main Menu")
        print("  |- 1) Student Management ")
        print("  |- 2) Course Management ")
        print("  |- 3) Change Username/password ")
        print("  |- 4) Log-out ")
        print("  |- 5) Exit ")
        choose = input("\nchoose(1_5):")

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
                courses = Course()
                student_number = input("Enter student number: ")
                print(students.show_a_student(student_number))

                with open("student_courses.txt") as file:
                    sac = file.readlines()

                for item in sac:
                    i = item.split(",")
                    if i[0] == student_number:
                        showc = (courses.show_a_course(i[1].strip())).strip()
                        print("\t" + showc[2:])

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
                if not add_std.browse(student_number):
                    fname = input("Enter student first name: ")
                    lname = input("Enter student last name: ")
                    avg = input("Enter student average: ")
                    add_std.add(student_number, fname, lname, avg)
                    print(green + "you added a student successfully." + endc)
                else:
                    print(red + "this student number is already exists!!" + endc)
                input("\npress any key to back:")
                continue

            elif ch == '5':
                os.system('cls')
                check_edit = Student()
                student_number = input("Enter student number to edit: ")
                print(check_edit.show_a_student(student_number))
                if check_edit.check_edit(student_number):
                    print(orange + "press enter to skip" + endc + "\n")
                    new_student_number = input("Enter new student number: ")
                    new_fname = input("Enter student first name: ")
                    new_lname = input("Enter student last name: ")
                    new_avg = input("Enter student average: ")
                    edit = Student()
                    edit.edit(student_number, new_student_number, new_fname, new_lname, new_avg)
                    print(green + "you edited student successfully." + endc)
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

                # add_std = Student()
                # student_number = input("Enter student number: ")
                # fname = input("Enter student first name: ")
                # lname = input("Enter student last name: ")
                # avg = input("Enter student average: ")
                #
                # if add_std.add(student_number, fname, lname, avg):
                #     print( green + "you added a student successfully." + endc)
                #
                # else:
                #     print(red + "this student number is already exists!!" + endc)
                # input("\npress any key to back:")
                # continue

            elif ch == '7':
                os.system('cls')
                continue

            else:
                os.system('cls')
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
            print("  |- 7) Unit selection for students ")
            print("  |- 8) Back ")

            ch = input("\nchoose(1_8):")

            if ch == '1':
                os.system('cls')
                students = Course()
                # print("student number, fname, lname, avg\n")
                print(students.show_all_courses())
                input("\npress any key to back:")
                continue

            elif ch == '2':
                os.system('cls')
                students = Course()
                student_number = input("Enter course number: ")
                print(students.show_a_course(student_number))
                input("\npress any key to back:")
                continue

            elif ch == '3':
                os.system('cls')
                students = Course()
                cnumber = input("Enter course number: ")
                print(students.show_search(cnumber))
                input("\npress any key to back:")
                continue

            elif ch == '4':
                os.system('cls')
                add_std = Course()
                course_number = input("Enter course number: ")
                if not add_std.cbrowse(course_number):
                    cname = input("Enter course name: ")
                    tname = input("Enter teacher name: ")
                    add_std.add(course_number, cname, tname)
                    print(green + "you added a course successfully." + endc)
                else:
                    print(red + "this course number is already exists!!" + endc)
                input("\npress any key to back:")
                continue

            elif ch == '5':
                os.system('cls')
                check_edit = Course()
                course_number = input("Enter course number to edit: ")
                print(check_edit.show_a_course(course_number))
                if check_edit.check_edit(course_number):
                    print(orange + "press enter to skip" + endc + "\n")
                    new_course_number = input("Enter new course number: ")
                    new_cname = input("Enter course name: ")
                    new_tname = input("Enter teacher name: ")
                    edit = Course()
                    edit.edit(course_number, new_course_number, new_cname, new_tname)
                    print(green + "you edited course successfully." + endc)
                input("\npress any key to back:")

            elif ch == '6':
                os.system('cls')
                remove_std = Course()
                course_number = input("Enter course number to remove: ")
                print(remove_std.show_a_course(course_number))
                x = input(red + "are you sure you want to delete(y|n)? " + endc)
                if x == 'y':
                    remove = Course()
                    remove.remove(course_number)
                    print("Course deleted!")
                    input("\npress any key to back:")
                elif x == 'n':
                    continue

            elif ch == '7':
                os.system('cls')
                students = Student()
                courses = Course()
                student_number = input("Enter student number: ")

                print("Student:")
                # print(students.show_a_student(student_number))

                with open("student_courses.txt") as file:
                    sac = file.readlines()

                for item in sac:
                    i = item.split(",")
                    if (i[0] == student_number):
                        showc = (courses.show_a_course(i[1].strip())).strip()
                        print("\t" + showc[2:])

                print(courses.show_all_courses())

                caid = input("Please enter the course number you want to add/remove (example : add 1234 or remove 1234):")
                clist = caid.split(" ")

                if(clist[0] == "add"):
                    clist[0] = 0
                elif(clist[0] == "remove"):
                    clist[0] = 1
                else:
                    continue

                a = courses.UnitSelection(student_number, clist[1].strip(), clist[0])

                if(a) and (clist[0] == 1):
                    print("Course removed successfully")
                elif(a) and (clist[0] == 0):
                    print("Course added successfully")
                else:
                    print(str(a))
                    print("Error!!!")

                input("\npress any key to back:")
                continue

            elif ch == '8':
                os.system('cls')
                continue

            else:
                os.system('cls')
                print("You entered a wrong number. Please try again.")
                continue
        elif choose == '3':
            users = []
            global use
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
                        print(green + "you changed your username/password successfully" + endc)
                    print(red + "wrong input, try again" + endc)
                    input("\npress any key to back:")


                else:
                    continue

        elif choose == '4':
            os.system('cls')
            main()
            return
        elif choose == '5':
           a = input(red + "are you sure(y/n)?" + endc)
           if a == 'y':
             os.system('cls')
             sys.exit(0)
           if a == 'n':
              continue
        else:
            print(red + "Error please try again!!" + endc)
            input("\npress any key to back:")
            continue

def manager_li():
    pass

def teacher_li():
    pass

def student_li():
    while 1:
        os.system('cls')
        print(green, "Logged as in 'student' ")
        print(endc)
        print("--Main Menu")
        print("  |- 1) List all Course ")
        print("  |- 2) Browse a Course ")
        print("  |- 3) Search Course")
        print("  |- 4) Unit selection ")
        print("  |- 5) Change password ")
        print("  |- 6) Log-out ")
        print("  |- 7) Exit ")
        ch = input("\nchoose(1_7):")
        if ch == '1':
            os.system('cls')
            students = Course()
            print(students.show_all_courses())
            input("\npress any key to back:")
            continue

        elif ch == '2':
            os.system('cls')
            students = Course()
            student_number = input("Enter course number: ")
            print(students.show_a_course(student_number))
            input("\npress any key to back:")
            continue

        elif ch == '3':
            os.system('cls')
            students = Course()
            cnumber = input("Enter course number: ")
            print(students.show_search(cnumber))
            input("\npress any key to back:")
            continue

        elif ch == '4':
            pass
        elif ch == '5':
            users = []
            global use
            with open("users.txt") as File:
                users = File.readlines()
            for inum, item in enumerate(users):
                i = (item.split(","))
                if use == i[0].strip():
                    pass4ch = input("Please Enter your password :")
                    if i[1].strip() == pass4ch:
                        newPassword = input("Please enter your new Password:")
                        users[inum] = "{}, {}, {}".format(i[0].strip(), newPassword, i[2].strip())
                        with open("users.txt", "w") as File:
                            for item in users:
                                File.write(item + "\n")
                    print(green + "you changed your password successfully" + endc)
                    input("\npress any key to back:")

        elif ch == '6':
            os.system('cls')
            main()
            return
        elif ch == '7':
            a = input(red + "are you sure(y/n)?" + endc)
            if a == 'y':
                os.system('cls')
                sys.exit(0)
            if a == 'n':
                continue
        else:
            print(red + "Error please try again!!" + endc)
            input("\npress any key to back:")

            continue


def main():
    os.system('cls')
    print("================== Welcome ==================\n")
    print("---Login\n")

    while 1:
        global use
        global password
        use = input("\tEnter your username:")
        password = input("\tEnter your password:")
        # use = 'admin'
        # password = '1234'
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
            student_li()
            break
        elif flag == 4:
            os.system('cls')
            print(green, "Logged as in 'teacher' ")
            print(endc)
            teacher_li()
            break
        else:
            print("Error! Flag is not correct.")
            continue


if bMain == False:
    bMain = True
    main()
