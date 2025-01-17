class Course(object):
    def list_cs(self):
        course_list = []
        with open("courses.txt", "r") as file:
            cfile = file.readlines()
            for c in cfile:
                c = c.split(",")
                course_information = {
                    "courseID": c[0].strip(),
                    "cname": c[1].strip(),
                    "tname": c[2].strip(),
                    "tID": c[3].strip()
                 }
                course_list.append(course_information)
        return course_list

    def cbrowse(self, cnumber):
        clist = Course.list_cs(self)
        for i, item in enumerate(clist):
            if item['courseID'] == cnumber:
                return clist[i]

        return False

    def search(self, course_number):
        findstd = []
        course_list = Course.list_cs(self)

        with open("courses.txt", "r") as coursesfile:
            course_file = coursesfile.readlines()

        b = False

        for i, item in enumerate(course_file):
            if item.__contains__(course_number):
                findstd.append(course_list[i])
                b = True
        if b:
            return findstd
        else:
            return '\033[31m' + "Not found!!" + '\033[0m'

    def show_all_courses(self):
        las = Course.list_cs(self)
        cnt = 0
        result = "All Courses:\n\n\t"
        for i, item in enumerate(las):
            result += "{}) {}: {} - {} ({})\n\t".format(cnt+1, item['courseID'],
                                              item['cname'], item['tname'], item['tID'])
            cnt += 1
        return result

    def show_a_course(self, cnumber):
        las = Course.cbrowse(self, cnumber)
        cnt = 0
        if las == False:
            return '\033[31m' + "Not found!!" + '\033[0m'
        else:
            return ("{}) {}: {} - {} ({})\n\t".format(cnt+1, las['courseID'],
                                              las['cname'], las['tname'], las['tID']))

    def show_search(self, course_number):
        las = Course.search(self, course_number)
        if type(las) == list:
            cnt = 0
            result = '\033[1;32;40m' + "---Found ({}) result \n\n\t".format(len(las)) + '\033[0m'
            for i, item in enumerate(las):
                result += "{}) {}: {} - {}\n\t".format(cnt+1, item['courseID'], item['cname'], item['tname'])
                cnt += 1
            return result
        else:
            return las

    def add(self, course_number, cname, tname, tid):

        if Course.cbrowse(self, course_number) == False:
            with open("courses.txt", "a") as file:
                file.write("{}, {}, {}, {}\n".format(course_number, cname, tname, tid))
            return True
        else:
            return False

    def check_edit(self, course_number):
        las = Course.list_cs(self)
        for i, x in enumerate(las):
            if las[i]['courseID'] == course_number:
                return True
        return False

    def edit(self, course_number, new_course_num, new_name, new_teacher, new_tid):
        las = Course.list_cs(self)
        for i, x in enumerate(las):
            if las[i]['courseID'] == course_number:
                if new_course_num != "":
                    las[i]['courseID'] = new_course_num
                if new_name != "":
                    las[i]['cname'] = new_name
                if new_teacher != "":
                    las[i]['tname'] = new_teacher
                if new_tid != "":
                    las[i]['tID'] = new_tid
        with open("courses.txt", 'w') as f:
            with open("courses.txt", 'a') as f:
                for i, item in enumerate(las):
                    f.write(las[i]['courseID'] + ", " + las[i]['cname'] + ", " + las[i]['tname'] + ", " + las[i]['tid'] + "\n")

    def remove(self, course_number):
        las = Course.list_cs(self)
        for i, x in enumerate(las):
            if las[i]['courseID'] == course_number:
                las.pop(i)
        with open("courses.txt", 'w') as f:
            with open("courses.txt", 'a') as f:
                for i, item in enumerate(las):
                    f.write(las[i]['courseID'] + ", " + las[i]['cname'] + ", " + las[i]['tname'] + ", " + las[i]['tid'] + "\n")

    def UnitSelection(self, studentID, courseID, command): #TODO: FIX THIS !

        # 0 for add
        # 1 for remove

        sac = []

        with open("student_courses.txt") as file:
            sac = file.readlines()
            # print(sac)

        if command == 0:
            for item in sac:
                i = item.split(",")
                if (str(i[0]).strip() == str(studentID).strip()) and (str(i[1]).strip() == str(courseID).strip()):
                    return False
                if not Course.check_edit(self, courseID):
                    return False
            with open("student_courses.txt", "a") as file:
                file.write("{},{},-1\n".format(studentID, courseID))
            return True

        elif command == 1:
            for index, item in enumerate(sac):
                i = item.split(",")
                if (str(i[0]).strip() == str(studentID).strip()) and (str(i[1]).strip() == str(courseID).strip()):
                    sac.pop(index)

                    with open("student_courses.txt", 'w') as f:
                        with open("student_courses.txt", 'a') as f:
                            for ii in sac:
                                f.write(ii)
                    return True
            return False

    def Scoresys(self, studentID, courseID, score):
        #todo:mozmoz
        sac = []
        with open("student_courses.txt") as file:
            sac = file.readlines()

        for index, item in enumerate(sac):
            i = item.split(",")
            if (str(i[0]).strip() == str(studentID).strip()) and (str(i[1]).strip() == str(courseID).strip()):
                sac.pop(index)
                sac.append("{},{},{}".format(studentID, courseID, score))

                with open("student_courses.txt", 'w') as f:
                    with open("student_courses.txt", 'a') as f:
                        for ii in sac:
                            f.write(ii)
                return True
        return False

    def ShowMyStudents(self, id):
        with open("student_courses.txt") as file:
            sac = file.readlines()
        MyStudents = []
        b = True
        for raw_item in sac:
            item = raw_item.split(",")
            if item[1].strip() == id.strip():
                b = False
                MyStudents.append(item[0])
        if not b:
            return MyStudents
        else:
            return False

    def ShowMyCourses(self, id):

            courses = []
            course_id = []
            clist = Course.list_cs(self)
            for i, item in enumerate(clist):
                if item['tID'].strip() == id:
                    courses.append("\t{} : {} - {} ({})".format(clist[i]['courseID'], clist[i]['cname'],
                                                        clist[i]['tname'], clist[i]['tID']))
                    course_id.append(clist[i]['courseID'].strip())
            return [courses, course_id]
