class Course():

    def list_cs(self):
        course_list = []
        with open("courses.txt", "r") as file:
            cfile = file.readlines()
            for c in cfile:
                c = c.split(",")
                course_information = {
                    "courseID": c[0].strip(),
                    "cname": c[1].strip(),
                    "tname": c[2].strip()
                 }
                course_list.append(course_information)
        return course_list

    def cbrowse(self, cnumber):
        clist = Course.list_cs(self)
        for i, item in enumerate(clist):
            if item['courseID'] == cnumber:
                return clist[i]

        return False
    #         student curses

    # def search(self, student_number):
    #     student_list = Student.list_std(self)
    #     for i, item in enumerate(student_list):
    #         if item['studentID'].__contains__(student_number):
    #             student_list = student_list[i]
    #     return student_list

    def show_all_courses(self):
        las = Course.list_cs(self)
        cnt = 0
        result = "All Courses :\n\n\t"
        for i, item in enumerate(las):
            result += "{}) {}: {} - {}\n\t".format(cnt+1, item['courseID'],
                                              item['cname'], item['tname'])
            cnt += 1
        return result

    def show_a_course(self, cnumber):
        las = Course.cbrowse(self, cnumber)
        cnt = 0
        if las == False:
            return ('\033[31m' + "Not found!!" + '\033[0m')
        else:
            return ("{}) {}: {} - {}\n\t".format(cnt+1, las['courseID'],
                                              las['cname'], las['tname']))


    def add(self, cnumer, cname, tname):
         pass
