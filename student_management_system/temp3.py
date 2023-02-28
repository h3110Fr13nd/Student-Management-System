import pandas as pd
import datetime
from utils import print_df_from_dict

class Students:
    '''student class'''
    students_df = pd.read_excel('./data/student_data.xlsx')
    students = students_df.set_index('enrollment')
    students = students.to_dict('index')

    @classmethod
    def update_students(cls):
        '''update students'''
        # print(cls.students)
        cls.students_df = pd.DataFrame(cls.students).T
        cls.students_df.index.name = 'enrollment'
        cls.students_df.to_excel('./data/student_data.xlsx', index=True)
    @classmethod
    def add_student(cls, enrollment, branch, semester, division, roll_no, name, gender, dob, guardian_name, phone, email, mentor):
        '''add student to database'''
        if enrollment not in cls.students:
            cls.students[enrollment] = {
                'branch': branch,
                'semester': semester,
                'division': division,
                'roll_no': roll_no,
                'name': name,
                'gender': gender,
                'dob': dob,
                'guardian_name': guardian_name,
                'phone': phone,
                'email': email,
                'mentor': mentor,
                'admission_date': datetime.datetime.now().strftime("%d-%m-%Y")
            }
            cls.update_students()
            return True
        else:
            return False
    
    @classmethod
    def update_student(cls, enrollment, **kwargs):
        '''update student'''
        if enrollment in cls.students:
            cls.students[enrollment].update(kwargs)
            cls.update_students()
            return True
        else:
            return False
    @classmethod
    def delete_student(cls, enrollment):
        '''delete student from database'''
        if enrollment in cls.students:
            del cls.students[enrollment]
            cls.update_students()
            return True
        else:
            return False
    
    @classmethod
    def get_student(cls, enrollment):
        '''get student'''
        if enrollment in cls.students:
            return {enrollment: cls.students[enrollment]}
        else:
            return False
        
    @classmethod
    def get_all_students(cls):
        '''get all students'''
        return cls.students
    
    @classmethod
    def get_students_by_branch(cls, branch):
        '''get students by branch'''
        return {k:v for k,v in cls.students.items() if v['branch'] == branch}

    @classmethod
    def get_students_by_semester(cls, semester):
        '''get students by semester'''
        return {k:v for k,v in cls.students.items() if v['semester'] == semester}

    @classmethod
    def get_students_by_division(cls, division):
        '''get students by division'''
        return {k:v for k,v in cls.students.items() if v['division'] == division}
    
    @classmethod
    def get_students_by_roll_no(cls, roll_no):
        '''get students by roll no'''
        return {k:v for k,v in cls.students.items() if v['roll_no'] == roll_no}

    @classmethod
    def get_students_by_name(cls, name):
        '''get students by name'''
        return {k:v for k,v in cls.students.items() if v['name'] == name}
    
    @classmethod
    def get_students_by_mentor(cls, mentor):
        '''get students by mentor'''
        return {k:v for k,v in cls.students.items() if v['mentor'] == mentor}
    
    @classmethod
    def get_students_by_branch_semester(cls, branch, semester):
        '''get students by branch and semester'''
        return cls.students[(cls.students['branch'] == branch) & (cls.students['semester'] == semester)]
    
    @classmethod
    def get_students_by_branch_semester_division(cls, branch, semester, division):
        '''get students by branch, semester and division'''
        return cls.students[(cls.students['branch'] == branch) & (cls.students['semester'] == semester) & (cls.students['division'] == division)]
    

    def __init__(self, enrollment, branch, semester, division, 
                 roll_no, name, gender, dob, guardian_name, 
                 phone, email, mentor):
        self.enrollment = enrollment
        self.branch = branch
        self.semester = semester
        self.division = division
        self.roll_no = roll_no
        self.name = name
        self.gender = gender
        self.dob = dob
        self.guardian_name = guardian_name
        self.phone = phone
        self.email = email
        self.mentor = mentor
        #self.photo = None
        self.admission_date = datetime.datetime.now().strftime("%d-%m-%Y")
        self.attendance = Attendance(self.enrollment)
        self.marks = Marks(self.enrollment)

class Attendance:
    '''attendance class'''
    def __init__(self, enrollment):
        self.enrollment = enrollment
        self.attendance = pd.read_excel('./data/attendance_data.xlsx')
        self.attendance = self.attendance[self.attendance['enrollment'] == self.enrollment]
        self.attendance = self.attendance.set_index('date')
        self.attendance.index = pd.to_datetime(self.attendance.index)
        self.attendance = self.attendance.sort_index()
        self.attendance = self.attendance.drop(['enrollment'], axis=1)
        self.attendance = self.attendance.drop_duplicates()
    
    def add_attendance(self, date, status):
        '''add attendance'''
        if date in self.attendance.index:
            return False
        else:
            self.attendance.loc[date] = status
            self.attendance.to_excel('./data/attendance_data.xlsx', index=True)
            return True
    
    def update_attendance(self, date, status):
        '''update attendance'''
        if date in self.attendance.index:
            self.attendance.loc[date] = status
            self.attendance.to_excel('./data/attendance_data.xlsx', index=True)
            return True
        else:
            return False
    
    def delete_attendance(self, date):
        '''delete attendance'''
        if date in self.attendance.index:
            self.attendance = self.attendance.drop(date)
            self.attendance.to_excel('./data/attendance_data.xlsx', index=True)
            return True
        else:
            return False
    
    def get_attendance(self, date):
        '''get attendance'''
        if date in self.attendance.index:
            return self.attendance.loc[date]
        else:
            return False
    
    def get_all_attendance(self):
        '''get all attendance'''
        return self.attendance
    
    def get_attendance_by_month(self, month):
        '''get attendance by month'''
        return self.attendance[self.attendance.index.month == month]
    
    def get_attendance_by_year(self, year):
        '''get attendance by year'''
        return self.attendance[self.attendance.index.year == year]
    
    def get_attendance_by_date_range(self, start_date, end_date):
        '''get attendance by date range'''
        return self.attendance[start_date:end_date]
    
    def get_attendance_by_month_year(self, month, year):
        '''get attendance by month and year'''
        return self.attendance[(self.attendance.index.month == month) & (self.attendance.index.year == year)]
    
    def get_attendance_by_date_range_year(self, start_date, end_date, year):
        '''get attendance by date range and year'''
        return self.attendance[(self.attendance.index >= start_date) & (self.attendance.index <= end_date) & (self.attendance.index.year == year)]
    
    def get_attendance_by_date_range_month(self, start_date, end_date, month):
        '''get attendance by date range and month'''
        return self.attendance[(self.attendance.index >= start_date) & (self.attendance.index <= end_date) & (self.attendance.index.month == month)]
    
    def get_attendance_by_date_range_month_year(self, start_date, end_date, month, year):
        '''get attendance by date range, month and year'''
        return self.attendance[(self.attendance.index >= start_date) & (self.attendance.index <= end_date) & (self.attendance.index.month == month) & (self.attendance.index.year == year)]
    
    def get_attendance_by_month_year_range(self, start_month, end_month, start_year, end_year):
        '''get attendance by month, year range'''
        return self.attendance[(self.attendance.index.month >= start_month) & (self.attendance.index.month <= end_month) & (self.attendance.index.year >= start_year) & (self.attendance.index.year <= end_year)]
    
    def get_attendance_by_date_range_month_year_range(self, start_date, end_date, start_month, end_month, start_year, end_year):
        '''get attendance by date range, month, year range'''
        return self.attendance[(self.attendance.index >= start_date) & (self.attendance.index <= end_date) & (self.attendance.index.month >= start_month) & (self.attendance.index.month <= end_month) & (self.attendance.index.year >= start_year) & (self.attendance.index.year <= end_year)]
    
class Subject:
    def __init__(self, subject_code, subject_name, subject_credit_theory,subject_credit_practical, taught_in_sem):
        self.subject_code = subject_code
        self.subject_name = subject_name
        self.subject_credit_theory = subject_credit_theory
        self.subject_credit_practical = subject_credit_practical
        self.taught_in_sem = taught_in_sem

class Subjects:
    # Fetching data from excel file
    subjects = pd.read_excel('./data/subjects_data.xlsx')
    subjects = subjects.set_index('subject_code')
    subjects = subjects.to_dict('index')
    
    @classmethod
    def update_excel(cls):
        df = pd.DataFrame(cls.subjects)
        df = df.T
        df.to_excel('./data/subjects_data.xlsx', index=True)
    
    @classmethod
    def add_subject(cls, subject_code, subject_name, subject_credit_theory, 
                    subject_credit_practical, taught_in_sem):
        if subject_code not in cls.subjects:
            cls.subjects[subject_code] = Subject(subject_code, subject_name, subject_credit_theory, subject_credit_practical, taught_in_sem)
            cls.update_excel()
            return True
        else:
            return False
    @classmethod
    def update_subject(cls, subject_code, subject_name, subject_credit_theory, subject_credit_practical, taught_in_sem):
        if subject_code in cls.subjects:
            cls.subjects[subject_code].subject_name = subject_name
            cls.subjects[subject_code].subject_credit_theory = subject_credit_theory
            cls.subjects[subject_code].subject_credit_practical = subject_credit_practical
            cls.subjects[subject_code].taught_in_sem = taught_in_sem
            cls.update_excel()
            return True
        else:
            return False
    
    @classmethod
    def delete_subject(cls, subject_code):
        if subject_code in cls.subjects:
            del cls.subjects[subject_code]
            cls.update_excel()
            return True
        else:
            return False
    
    @classmethod
    def get_subject(cls, subject_code):
        if subject_code in cls.subjects:
            return cls.subjects[subject_code]
        else:
            return False
    @classmethod
    def get_subjects_by_name(cls, subject_name):
        return {k:v for k,v in cls.subjects.items() if v.subject_name == subject_name}

    @classmethod
    def get_all_subjects(cls):
        return cls.subjects
    
    @classmethod
    def get_subjects_by_sem(cls, taught_in_sem):
        return {k:v for k,v in cls.subjects.items() if v.taught_in_sem == taught_in_sem}
    
    @classmethod
    def get_subjects_by_sem_range(cls, start_sem, end_sem):
        return {k:v for k,v in cls.subjects.items() if v.taught_in_sem >= start_sem and v.taught_in_sem <= end_sem}

class Marks:
    # Fetching data from excel file with subject_code and enrollment as index and there are 4 tests for theory and 1 practical
    marks = pd.read_excel('./data/marks_data.xlsx')
    marks = marks.set_index(['subject_code', 'enrollment'])
    marks = marks.to_dict('index')

    @classmethod
    def update_excel(cls):
        df = pd.DataFrame(cls.marks)
        df = df.T
        df.to_excel('./data/marks_data.xlsx', index=True)

    @classmethod
    def add_marks(cls, subject_code, enrollment, test1_theory, test2_theory, test3_theory, test4_theory, practical_project):
        if (subject_code, enrollment) not in cls.marks:
            cls.marks[(subject_code, enrollment)] = {'test1_theory': test1_theory, 'test2_theory': test2_theory, 'test3_theory': test3_theory, 'test4_theory': test4_theory, 'practical_project': practical_project}
            cls.update_excel()
            return True
        else:
            return False
    
    @classmethod
    def update_marks(cls, subject_code, enrollment, test1_theory, test2_theory, test3_theory, test4_theory, practical_project):
        if (subject_code, enrollment) in cls.marks:
            cls.marks[(subject_code, enrollment)]['test1_theory'] = test1_theory
            cls.marks[(subject_code, enrollment)]['test2_theory'] = test2_theory
            cls.marks[(subject_code, enrollment)]['test3_theory'] = test3_theory
            cls.marks[(subject_code, enrollment)]['test4_theory'] = test4_theory
            cls.marks[(subject_code, enrollment)]['practical_project'] = practical_project
            cls.update_excel()
            return True
        else:
            return False
    
    @classmethod
    def update_marks_by_test(cls, subject_code, enrollment, test, marks):
        if (subject_code, enrollment) in cls.marks:
            cls.marks[(subject_code, enrollment)][test] = marks
            cls.update_excel()
            return True
        else:
            return False
    
    @classmethod
    def delete_marks(cls, subject_code, enrollment):
        if (subject_code, enrollment) in cls.marks:
            del cls.marks[(subject_code, enrollment)]
            cls.update_excel()
            return True
        else:
            return False
    
    @classmethod
    def get_marks(cls, subject_code, enrollment):
        if (subject_code, enrollment) in cls.marks:
            return cls.marks[(subject_code, enrollment)]
        else:
            return False
    
    @classmethod
    def get_all_marks(cls):
        return cls.marks
    
    @classmethod
    def get_total_marks(cls, subject_code, enrollment):
        if (subject_code, enrollment) in cls.marks:
            return sum(cls.marks[(subject_code, enrollment)].values())
        else:
            return False
    @classmethod
    def get_total_marks_by_subject(cls, subject_code):
        return {k:sum(v.values()) for k,v in cls.marks.items() if k[0] == subject_code}
    
    @classmethod
    def get_total_marks_by_enrollment(cls, enrollment):
        return {k:sum(v.values()) for k,v in cls.marks.items() if k[1] == enrollment}
    
    @classmethod
    def get_total_marks_by_subject_and_enrollment(cls, subject_code, enrollment):
        return {k:sum(v.values()) for k,v in cls.marks.items() if k[0] == subject_code and k[1] == enrollment}
    
    @classmethod
    def get_total_marks_by_sem(cls, taught_in_sem):
        return {k:sum(v.values()) for k,v in cls.marks.items() if Subjects.get_subject(k[0]).taught_in_sem == taught_in_sem}
    
    @classmethod
    def get_total_marks_by_sem_range(cls, start_sem, end_sem):
        return {k:sum(v.values()) for k,v in cls.marks.items() if Subjects.get_subject(k[0]).taught_in_sem >= start_sem and Subjects.get_subject(k[0]).taught_in_sem <= end_sem}
    
    @classmethod
    def get_total_marks_by_subject_and_sem(cls, subject_code, taught_in_sem):
        return {k:sum(v.values()) for k,v in cls.marks.items() if k[0] == subject_code and Subjects.get_subject(k[0]).taught_in_sem == taught_in_sem}

    @classmethod
    def get_marks_by_subject(cls, subject_code):
        return {k:v for k,v in cls.marks.items() if k[0] == subject_code}
    
    @classmethod
    def get_marks_by_enrollment(cls, enrollment):
        return {k:v for k,v in cls.marks.items() if k[1] == enrollment}
    
    @classmethod
    def get_marks_by_subject_and_enrollment(cls, subject_code, enrollment):
        return {k:v for k,v in cls.marks.items() if k[0] == subject_code and k[1] == enrollment}
    
    @classmethod
    def get_marks_by_sem(cls, taught_in_sem):
        return {k:v for k,v in cls.marks.items() if Subjects.get_subject(k[0]).taught_in_sem == taught_in_sem}
    
    @classmethod
    def get_marks_by_sem_range(cls, start_sem, end_sem):
        return {k:v for k,v in cls.marks.items() if Subjects.get_subject(k[0]).taught_in_sem >= start_sem and Subjects.get_subject(k[0]).taught_in_sem <= end_sem}
    
    @classmethod
    def get_marks_by_subject_and_sem(cls, subject_code, taught_in_sem):
        return {k:v for k,v in cls.marks.items() if k[0] == subject_code and Subjects.get_subject(k[0]).taught_in_sem == taught_in_sem}
    
    @classmethod
    def get_marks_by_subject_and_sem_range(cls, subject_code, start_sem, end_sem):
        return {k:v for k,v in cls.marks.items() if k[0] == subject_code and Subjects.get_subject(k[0]).taught_in_sem >= start_sem and Subjects.get_subject(k[0]).taught_in_sem <= end_sem}
    
    @classmethod
    def get_marks_by_enrollment_and_sem(cls, enrollment, taught_in_sem):
        return {k:v for k,v in cls.marks.items() if k[1] == enrollment and Subjects.get_subject(k[0]).taught_in_sem == taught_in_sem}
    
    @classmethod
    def get_marks_by_enrollment_and_sem_range(cls, enrollment, start_sem, end_sem):
        return {k:v for k,v in cls.marks.items() if k[1] == enrollment and Subjects.get_subject(k[0]).taught_in_sem >= start_sem and Subjects.get_subject(k[0]).taught_in_sem <= end_sem}
    
    @classmethod
    def get_marks_by_subject_and_enrollment_and_sem(cls, subject_code, enrollment, taught_in_sem):
        return {k:v for k,v in cls.marks.items() if k[0] == subject_code and k[1] == enrollment and Subjects.get_subject(k[0]).taught_in_sem == taught_in_sem}
    
    @classmethod
    def get_marks_by_subject_and_enrollment_and_sem_range(cls, subject_code, enrollment, start_sem, end_sem):
        return {k:v for k,v in cls.marks.items() if k[0] == subject_code and k[1] == enrollment and Subjects.get_subject(k[0]).taught_in_sem >= start_sem and Subjects.get_subject(k[0]).taught_in_sem <= end_sem}
    
class StudentMangement:

    def __init__(self):
        self.students = Students.get_all_students()
        self.subjects = Subjects.get_all_subjects()
        self.marks = Marks.get_all_marks()

        print("Welcome to Student Management System")
        print("1. Student Details (Add, Edit, Delete, View)")
        print("2. Subject Details (Add, Edit, Delete, View)")
        print("3. Marks Details (Add, Edit, Delete, View)")
        print("4. Attendance Details (Add, Edit, Delete, View)")
        print("5. Exit")

        choice = int(input("Enter your choice: "))
        
        if choice == 1:
            print("Student Details")
            print("     1. Add Student")
            print("     2. Edit Student")
            print("     3. Delete Student")
            print("     4. View Student")
            print("     5. Back")

            choice = int(input("Enter your choice: "))

            if choice == 1:
                print("     Add Student")
                name = input("          Enter name: ")
                enrollment = input("          Enter enrollment: ")
                semester = int(input("          Enter sem: "))
                division = input("          Enter div: ")
                roll_no = int(input("          Enter roll number: "))
                branch = input("          Enter branch: ")
                gender = input('          Enter Gender (M/F): ')
                dob = input('          Enter DOB in DD/MM/YYYY format: ')
                guardian_name = input('          Enter Guardian Name: ')
                phone = input('          Enter Phone Number: ')
                email = input('          Enter Email: ')
                # address = input('          Enter Address: ')
                mentor = input('          Enter Mentor: ')

                if Students.add_student(enrollment,branch,semester,division,roll_no,
                                     name, gender, dob, guardian_name, phone, email, mentor):
                    print("Student added successfully")
                else:
                    print("Student already exists")
            
            elif choice == 2:
                print("     Edit Student")
                enrollment = int(input("          Enter enrollment: "))
                
                if edit_student:=Students.get_student(enrollment):

                    pd.DataFrame(Students.students).T
                    print("          1. Edit Name")
                    print("          2. Edit Enrollment")
                    print("          3. Edit Semester")
                    print("          4. Edit Division")
                    print("          5. Edit Roll Number")
                    print("          6. Edit Branch")
                    print("          7. Edit DOB")
                    print("          8. Edit Guardian Name")
                    print("          9. Edit Phone Number")
                    print("          10. Edit Email")
                    print("          11. Edit Gender")
                    print("          12. Edit Mentor")
                    print("          13. Admission Date")
                    print("          13. Exit")

                    edit_choices = list(map(int,input("          Enter Choices in format <<choice1> <choice2> ...> \n          e.g. For sem and division and dob change type: 3 4 7\n          Enter your choices: ").split()))

                    for edit_choice in set(edit_choices):
                        if edit_choice==1:
                            name = input("              Enter name: ")
                            if Students.update_student(enrollment, name=name):
                                print("              Name changed successfully")
                            else:
                                print("              Student not found")
                        elif edit_choice==2:

                            new_enrollment = input("              Enter new enrollment: ")
                            if new_enrollment not in Students.students:
                                temp_student = Students.students[enrollment]
                                Students.students[new_enrollment] = temp_student
                                del Students.students[enrollment]
                                Students.update_students()
                                enrollment = new_enrollment
                                print("              Enrollment changed successfully")
                            else:
                                print("              Student already exists With this enrollment")
                        elif edit_choice==3:
                            semester = int(input("              Enter new sem: "))
                            if Students.update_student(enrollment, semester=semester):
                                print("              Semester changed successfully")
                            else:
                                print("              Student not found")
                        elif edit_choice==4:
                            division = input("              Enter new div: ")
                            if Students.update_student(enrollment, division=division):
                                print("              Division changed successfully")
                            else:
                                print("              Student not found")
                        elif edit_choice==5:
                            roll_no = int(input("              Enter new roll number: "))
                            if Students.update_student(enrollment, roll_no=roll_no):
                                print("              Roll Number changed successfully")
                            else:
                                print("              Student not found")
                        elif edit_choice==6:
                            branch = input("              Enter new branch: ")
                            if Students.update_student(enrollment, branch=branch):
                                print("              Branch changed successfully")
                            else:
                                print("              Student not found")
                        elif edit_choice==7:
                            dob = input("              Enter new DOB in DD/MM/YYYY format: ")
                            if Students.update_student(enrollment, dob=dob):
                                print("              DOB changed successfully")
                            else:
                                print("              Student not found")
                        elif edit_choice==8:
                            guardian_name = input("              Enter new Guardian Name: ")
                            if Students.update_student(enrollment, guardian_name=guardian_name):
                                print("              Guardian Name changed successfully")
                            else:
                                print("              Student not found")
                        elif edit_choice==9:
                            phone = input("              Enter new Phone Number: ")
                            if Students.update_student(enrollment, phone=phone):
                                print("              Phone Number changed successfully")
                            else:
                                print("              Student not found")
                        elif edit_choice==10:
                            email = input("              Enter new Email: ")
                            if Students.update_student(enrollment, email=email):
                                print("              Email changed successfully")
                            else:
                                print("              Student not found")
                        elif edit_choice==11:
                            gender = input("              Enter new Gender (M/F): ")
                            if Students.update_student(enrollment, gender=gender):
                                print("              Gender changed successfully")
                            else:
                                print("              Student not found")
                        elif edit_choice==12:
                            mentor = input("              Enter new Mentor: ")
                            if Students.update_student(enrollment, mentor=mentor):
                                print("              Mentor changed successfully")
                            else:
                                print("              Student not found")
                        elif edit_choice==13:
                            admission_date = input("              Enter new Admission Date in DD/MM/YYYY format: ")
                            if Students.update_student(enrollment, admission_date=admission_date):
                                print("              Admission Date changed successfully")
                            else:
                                print("              Student not found")
                        elif edit_choice==14:
                            break
                        else:
                            print("              Invalid Choice")
                            break
                else:
                    print("          Student not found")

            elif choice == 3:
                print("     Delete Student")
                enrollment = int(input("          Enter enrollment: "))
                if Students.delete_student(enrollment):
                    print("          Student deleted successfully")
                else:
                    print("          Student not found")

            elif choice == 4:

                print("     View Student(s)")
                print("          1. View All Students")
                print("          2. View Student by Enrollment")
                print("          3. View Student by Name")
                print("          4. View Student by Branch")
                print("          5. View Student by Semester")
                print("          6. View Student by Division")
                print("          7. View Student by Roll Number")
                print("          8. View Student by Mentor")
                print("          9. View Student By Branch and Semester")
                print("          10. View Student By Branch and Semester and Division")

                view_choice = int(input("          Enter your choice: "))
                if view_choice == 1:
                    students = Students.get_all_students()
                    if students:
                        print("             Students:")
                        print(Students.students_df)
                    else:
                        print("             No students found")
                elif view_choice == 2:
                    print("             View Student by Enrollment")
                    enrollment = int(input("             Enter enrollment: "))
                    student = Students.get_student(enrollment)
                    if student:
                        print("             Student:")
                        print(pd.DataFrame(student))
                    else:
                        print("             Student not found")
                elif view_choice == 3:
                    name = input("             Enter name: ")
                    students = Students.get_students_by_name(name)
                    if students:
                        print("             Students:")
                        print_df_from_dict(students)
                    else:
                        print("             Student not found")
                elif view_choice == 4:
                    branch = input("             Enter branch: ")
                    students = Students.get_students_by_branch(branch)
                    if students:
                        print("              Students:")
                        print_df_from_dict(students)
                    else:
                        print("             Student not found")
                elif view_choice == 5:
                    semester = int(input("             Enter semester: "))
                    students = Students.get_students_by_semester(semester)
                    if students:
                        print("             Students:")
                        print_df_from_dict(students)
                    else:
                        print("             Student not found")
                elif view_choice == 6:
                    division = input("             Enter division: ")
                    students = Students.get_students_by_division(division)
                    if students:
                        print("             Students:")
                        print_df_from_dict(students)
                    else:
                        print("             Student not found")
                elif view_choice == 7:
                    roll_no = int(input("             Enter roll number: "))
                    students = Students.get_students_by_roll_no(roll_no)
                    if students:
                        print("             Students:")
                        print_df_from_dict(students)
                    else:
                        print("             Student not found")
                elif view_choice == 8:
                    mentor = input("             Enter mentor: ")
                    students = Students.get_students_by_mentor(mentor)
                    if students:
                        print("             Students:")
                        print_df_from_dict(students)
                    else:
                        print("             Student not found")
                elif view_choice == 9:
                    branch = input("             Enter branch: ")
                    semester = int(input("             Enter semester: "))
                    students = Students.get_students_by_branch_semester(branch, semester)
                    if students:
                        print("             Students:")
                        print_df_from_dict(students)
                    else:
                        print("             Student not found")
                elif view_choice == 10:
                    branch = input("             Enter branch: ")
                    semester = int(input("             Enter semester: "))
                    division = input("             Enter division: ")
                    students = Students.get_students_by_branch_semester_division(branch, semester, division)
                    if students:
                        print("             Students:")
                        print_df_from_dict(students)
                    else:
                        print("             Student not found")
                else:
                    print("             Invalid Choice")

            elif choice == 5:
                print("         Back to Main Menu")

            else:
                print("         Invalid Choice")
                print("         Back to Main Menu")
        
        elif choice == 2:
            pass
            
if __name__ == '__main__':
    exit_choice = False
    while not exit_choice:
        StudentMangement()
        print("Do you want to continue? (Y/N)")
        choice = input("Enter your choice: ")
        if choice == 'N' or choice == 'n':
            exit_choice = True


