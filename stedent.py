class Student():
    def login(self, username, password):
        users_list = []
        with open("users.txt", "r") as usersfile:
            users_file = usersfile.readlines()
            for users in users_file:
                users = users.split(",")
                users_information = {
                    "username": users[0].strip(),
                    "password": users[1].strip(),
                    "code": users[2].strip()}
                users_list.append(users_information)
            for item in users_list:
                if item['username'] == username and item['password'] == password:
                   return item['code']
        return 0

    def list_std(self):
        student_list = []
        with open("students.txt", "r") as studentsfile:
            student_file = studentsfile.readlines()
            for students in student_file:
                students = students.split(",")
                studentd_information = {
                    "studentID": students[0].strip(),
                    "fname": students[1].strip(),
                    "lname": students[2].strip(),
                    "avarage": students[3].strip()
                 }
                student_list.append(studentd_information)
        return student_list

    def browse(self, student_number):
        student_list = Student.list_std(self)
        for i, item in enumerate(student_list):
            if item['studentID'] == student_number:
                return student_list[i]

        return False
    #         student curses

    # def search(self, student_number):
    #     student_list = Student.list_std(self)
    #     for i, item in enumerate(student_list):
    #         if item['studentID'].__contains__(student_number):
    #             student_list = student_list[i]
    #     return student_list

    def show_all_students(self):
        las = Student.list_std(self)
        cnt = 0
        result = "All Students :\n\n\t"
        for i, item in enumerate(las):
            result += "{}) {}: {} {}, {}\n\t".format(cnt+1, item['studentID'],
                                              item['fname'], item['lname'], item['avarage'])
            cnt += 1
        return result

    def show_a_student(self, student_number):
        las = Student.browse(self, student_number)
        cnt = 0
        if las == False:
            return ('\033[31m' + "Not found!!" + '\033[0m')
        else:
            return ("{}) {}: {} {}, {}\n\t".format(cnt+1, las['studentID'],
                                     las['fname'], las['lname'], las['avarage']))


    def add(self, student_numer, fname, lname, avg):
         pass