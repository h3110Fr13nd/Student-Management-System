import csv
import os
import pandas as pd


class Student:
    '''Student class for student management system'''
    def __init__(self, enrollment, name, degree, branch, **kwargs):
        self.enrollment = enrollment
        self.name = name
        self.degree = degree
        self.branch = branch
        self.__dict__.update(kwargs)
