# C09_EX01: Avand fisierul numbers.json, scrieti un program care calculeaza media numerelor 
# din "integer_numbers", media numerelor din "float_numbers", cat si media tuturor numerelor.

import json

with open("numbers.json","r") as f:
    from_file=json.load(f)

lst1=from_file['integer_numbers']
lst2=from_file['float_numbers']
sum1=0

for x in lst1:
    sum1=sum1+x

media1=sum1/len(lst1)
print(media1)

#v2
print(sum(lst1)/len(lst1))
print(sum(lst2)/len(lst2))
#v3
import statistics
print(statistics.mean(lst1+lst2))

sum2=0

for x in lst2:
    sum2=sum2+x
media2=sum2/len(lst2)

print(media2)

media_totala=(sum1+sum2)/(len(lst1)+len(lst2))
print(media_totala)

# 1.Given the multi-line string student_grades:
#  a). Using the below data, create your student_grades.csv from student_grades string.
#  b). List the contents of the file as a list of dicts, a row being a dict of form:
#  {"student_name": <name_of_student>, "subject": <name_of_subject>, "grade": <grade>}
#  c). List the student that has the most grades and how many it has   # => Celine, 3  poate fi si un dict {"student": "Celine", "no_of_grades": 3} sau {"Celine": 3} sau ("Celine", 3), "Student with most grades ... "

student_grades = '''
Eveline,math,9
Andrew,physics,6
Celine,music,10
Matthew,math,7
Celine,english,10
Matthew,english,10
Celine,chemistry,6
'''
# a)
import csv
rows_as_strings = student_grades.strip("\n").split("\n")
rows = []

for row in rows_as_strings:
    rows.append(row.split(","))

print(rows)

with open("student_grades.csv", "w", newline="") as f:
    writer = csv.writer(f)
    writer.writerows(rows)

# b)
# List the contents of the file as a list of dicts, a row being a dict of form:

list_of_students = []
with open("student_grades.csv", "r", newline="") as f:
    reader = csv.DictReader(f, fieldnames = ["student_name", "subject", "grade"])

    for row in reader:
        list_of_students.append(row)
print(list_of_students)

# c)

no_of_grades = {}
for student in list_of_students:
    key = student['student_name']
    if key in no_of_grades:
        no_of_grades[student['student_name']] += 1
    else:
        no_of_grades[student['student_name']] = 1

most_grades = max(no_of_grades.values())
for student in no_of_grades:
    if no_of_grades[student] == most_grades:
        student_no_of_grades = {
            "student": student,
            "no_of_grades": most_grades
        }
print(student_no_of_grades)




