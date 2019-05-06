class Student(object):
    def login(self, username, password):
        users_list = []
        with open("users.txt", "r") as usersfile:
            users_file = usersfile.readlines()
            for users in users_file:
                if users != '\n':
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

    def search(self, student_number):
        findstd = []
        student_list = Student.list_std(self)

        with open("students.txt", "r") as studentsfile:
            student_file = studentsfile.readlines()

        b = False

        for i, item in enumerate(student_file):
            if item.__contains__(student_number):
                findstd.append(student_list[i])
                b = True
        if b:
            return findstd
        else:
            return '\033[31m' + "Not found!!" + '\033[0m'

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
            return '\033[31m' + "Not found!!" + '\033[0m'
        else:
            return "\n{}) {}: {} {}, {}\n\t".format(cnt+1, las['studentID'],las['fname'], las['lname'], las['avarage'])

    def show_search(self, student_number):
        las = Student.search(self, student_number)
        if type(las) == list:
            cnt = 0
            result = '\033[1;32;40m' + "---Found ({}) result \n\n\t".format(len(las)) + '\033[0m'
            for i, item in enumerate(las):
                result += "{}) {}: {} {}, {}\n\t".format(cnt+1, item['studentID'],
                                                  item['fname'], item['lname'], item['avarage'])
                cnt += 1
            return result
        else:
            return las

    def add(self, student_numer, fname, lname, avg):
        if not Student.browse(self, student_numer):
            with open("students.txt", "a") as studentsfile:
                studentsfile.write("{}, {}, {}, {}\n".format(student_numer, fname, lname, avg))
            return True
        else:
            return False

    def check_edit(self, student_number):
        las = Student.list_std(self)
        for i, x in enumerate(las):
            if las[i]['studentID'] == student_number:
                return True
        return False

    def edit(self, student_number, new_student_num, new_fname, new_lname, new_avg):
        las = Student.list_std(self)
        for i, x in enumerate(las):
            if las[i]['studentID'] == student_number:
                if new_student_num != "":
                    las[i]['studentID'] = new_student_num
                if new_fname != "":
                    las[i]['fname'] = new_fname
                if new_lname != "":
                    las[i]['lname'] = new_lname
                if new_avg != "":
                    las[i]['avarage'] = new_avg
        with open("students.txt", 'w') as f:
            with open("students.txt", 'a') as f:
                for i, item in enumerate(las):
                    f.write(las[i]['studentID']+", "+las[i]['fname']+", "+las[i]['lname']+", "+las[i]['avarage']+"\n")

    def remove(self, student_number):
        las = Student.list_std(self)
        for i, x in enumerate(las):
            if las[i]['studentID'] == student_number:
                las.pop(i)
        with open("students.txt", 'w') as f:
            with open("students.txt", 'a') as f:
                for i, item in enumerate(las):
                    f.write(las[i]['studentID']+", "+las[i]['fname']+", "+las[i]['lname']+", "+las[i]['avarage']+"\n")
