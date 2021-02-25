#!/usr/bin/env python

students_count = int(input())
students_marks = {}
for n in range(students_count):
    student_list = input().split()
    average = sum([float(i) for i in student_list[1:]]) / 3.0
    students_marks[student_list[0]] = average

print("{:.2f}".format(students_marks[input()]))
