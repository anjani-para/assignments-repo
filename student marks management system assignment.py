# Add the below given code in your code file to extract data from csv files
#  (student_marks.csv, subject_faculty.csv)

students_marks = []
with open('student_marks.csv') as f:
    for line in f:
        columns = line.split(',')
        columns[-1] = int(columns[-1].rstrip('\n'))
        students_marks.append(tuple(columns))

subject_faculty = []
with open('subject_faculty.csv') as f:
    for line in f:
        columns = line.split(',')
        columns[-1] = columns[-1].rstrip('\n')
        subject_faculty.append(tuple(columns))

print(students_marks)
print(subject_faculty)
# 1) Find the faculty with highest student count who got more than 90%.
def f(subj):
    count = 0
    for name, subject, marks in students_marks:
        if subject == subj:
            if marks > 90:
                count += 1
    return count

sub_count = {}
sub_count["Mathematics"] = f("Mathematics")
sub_count["Telugu"] = f("Telugu")
sub_count["English"] = f("English")
sub_count["Social"] = f("Social")
sub_count["Physics"] = f("Physics")
sub_count["Chemistry"] = f("Chemistry")
highest_student_count = max(sub_count.items(), key=lambda x:x[1])
d1 = dict(subject_faculty)
print("The faculty with highest student count who got more than 90% is ", d1[highest_student_count[0]])

# 2) Find the faculty with highest pass percentage (> 40%)
# 3) Find the faculty with least pass percentage (<= 40%)
def pass_percentage(subj):
    sum = 0
    for name, subject, marks in students_marks:
        if subject == subj:
            if marks < 33:
                pass
            else:
                sum += marks
    subject_per = sum / 100
    return subject_per

d = {}
d["Mathematics"] = pass_percentage("Mathematics")
d["Telugu"] = pass_percentage("Telugu")
d["English"] = pass_percentage("English")
d["Social"] = pass_percentage("Social")
d["Physics"] = pass_percentage("Physics")
d["Chemistry"] = pass_percentage("Chemistry")

HPP = max(d.items(), key=lambda x:x[1])
LPP = min(d.items(), key=lambda x:x[1])
print("highest pass percentage occured in: ", HPP[0])
print("Lowest pass percentage occured in: ", LPP[0])
print("Faculty with highest pass percentage is ", d1[HPP[0]])
print("Faculty with lowest pass percentage is ", d1[LPP[0]])

# 4) Who is the top student with maximum total?
# 7) Find the student with least numbers of marks as total.
student_totalmarks = {}
for student, subject, marks in students_marks:
    if student not in student_totalmarks:
        student_totalmarks[student] = [marks]
    else:
        student_totalmarks[student].append(marks)
max_total = max(student_totalmarks.items(), key=lambda x: sum(x[1]))
min_total = min(student_totalmarks.items(), key=lambda x: sum(x[1]))
print("Top student with maximum total is ", max_total[0])
print("Student with minimum total is ", min_total[0])

# 5) Who is the best student in Mathematics?
math_marks = {}
for student, subject, marks in students_marks:
    if subject == 'Mathematics':
        math_marks[student] = marks
max_math_score = max(math_marks.items(), key=lambda x:x[1])
print("The best student in Mathematics is ", max_math_score[0])

# 6) What is the average mark for each subject, (ignore failures)?
def marks(subj):
    sub_sum = 0
    for name, subject, marks in students_marks:
        if subject == subj:
                sub_sum += marks
    avg_mark = sub_sum / 100
    return avg_mark
print("avg mark for mathematics is ", marks('Mathematics'))
print("avg mark for telugu is ", marks('Telugu'))
print("avg mark for English is ", marks('English'))
print("avg mark for Social is ", marks('Social'))
print("avg mark for Physics is ", marks('Physics'))
print("avg mark for Chemistry is ", marks('Chemistry'))
