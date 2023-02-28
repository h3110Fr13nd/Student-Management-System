import os
import pandas as pd
class Student:
    '''Student class for student management system'''
    students = pd.read_excel('./data/student_data.xlsx')
    def __init__(self, enrollment, name, branch, **kwargs):
        self.enrollment = enrollment
        self.name = name
        self.branch = branch
        self.semester = kwargs.get('semester', 1)
        self.roll_no = kwargs.get('roll_no', 1)
        self.email = kwargs.get('email', '')
        self.phone = kwargs.get('phone', '')
        self.temp_address = kwargs.get('temp_address', '')
        self.perm_address = kwargs.get('perm_address', '')
        self.dob = kwargs.get('dob', '')
        self.division = kwargs.get('division', 'A1')
        self.mentor = kwargs.get('mentor', '')
        self.father_name = kwargs.get('father_name', '')
        self.mother_name = kwargs.get('mother_name', '')
        self.father_phone = kwargs.get('father_phone', '')
        self.mother_phone = kwargs.get('mother_phone', '')
        self.father_email = kwargs.get('father_email', '')
        self.mother_email = kwargs.get('mother_email', '')
        self.father_occupation = kwargs.get('father_occupation', '')
        self.mother_occupation = kwargs.get('mother_occupation', '')
        self.father_income = kwargs.get('father_income', '')
        self.mother_income = kwargs.get('mother_income', '')
        # self.father_qualification = kwargs.get('father_qualification', '')
        # self.mother_qualification = kwargs.get('mother_qualification', '')
        # self.father_address = kwargs.get('father_address', '')
        # self.mother_address = kwargs.get('mother_address', '')
        self.photo = kwargs.get('photo', '')
        self.fee = kwargs.get('fee', 0)
        # self.fee_paid = kwargs.get('fee_paid', 0)
        # self.fee_due = kwargs.get('fee_due', 0)
        # self.fee_status = kwargs.get('fee_status', 'Not Paid')
        self.status = kwargs.get('status', 'Active')
        self.remarks = kwargs.get('remarks', '')
        self.admission_date = kwargs.get('admission_date', '')
        # self.admission_time = kwargs.get('admission_time', '')
        self.last_updated = kwargs.get('last_updated', '')
        # self.last_updated_time = kwargs.get('last_updated_time', '')
        # self.created_by = kwargs.get('created_by', '')
        # self.updated_by = kwargs.get('updated_by', '')

    def add_student(self,**kwargs):
        '''add student to the database'''
        Student.students = Student.students.append(self.__dict__, ignore_index=True)
        Student.students.to_excel('./data/student_data.xlsx', index=False, sheet_name='')
        return True

    def update_student(self, enrollment):
        '''update student data'''
        Student.students.loc[Student.students['enrollment'] == enrollment, :] = self.__dict__
        Student.students.to_excel('./data/student_data.xlsx', index=False)
        return True

    def delete_student(self, enrollment):
        '''delete student from database'''
        Student.students = Student.students[Student.students['enrollment'] != enrollment]
        Student.students.to_excel('./data/student_data.xlsx', index=False)
        return True
    
    def get_student(self, enrollment):
        '''get student data'''
        student = Student.students[Student.students['enrollment'] == enrollment]
        return student
    
    def get_all_students(self):
        '''get all students data'''
        return Student.students
    
    def get_student_by_branch(self, branch):
        '''get student data by branch'''
        student = Student.students[Student.students['branch'] == branch]
        return student
    
    def get_student_by_semester(self, semester):
        '''get student data by semester'''
        student = Student.students[Student.students['semester'] == semester]
        return student
    
    def get_student_by_division(self, division):
        '''get student data by division'''
        student = Student.students[Student.students['division'] == division]
        return student
    
    def get_student_by_mentor(self, mentor):
        '''get student data by mentor'''
        student = Student.students[Student.students['mentor'] == mentor]
        return student
    
    def get_student_by_name(self, name):
        '''get student data by name'''
        student = Student.students[Student.students['name'] == name]
        return student
    
    def get_student_by_roll_no(self, roll_no):
        '''get student data by roll no'''
        student = Student.students[Student.students['roll_no'] == roll_no]
        return student
    
    def get_student_by_email(self, email):
        '''get student data by email'''
        student = Student.students[Student.students['email'] == email]
        return student
    
    def get_student_by_phone(self, phone):
        '''get student data by phone'''
        student = Student.students[Student.students['phone'] == phone]
        return student
    
    
    



df = pd.read_csv('student_data.csv')
df.to_excel('student_data.xlsx', index=False)