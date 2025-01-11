
# def rev_string(s):
#     s = s[::-1]
#     print(s)
#     return s
# rev_string("Muktesh")

# keys = ['Car1', 'Car2', 'Car3'] 
# values = ['Audi', 'BMW', 'Alto']

# dic = {}
# for i in range(len(keys)):
#     dic[keys[i]] = values[i] 

# for i in range(len(keys)):
#     print(f"key is : {keys[i]} and value is : {values[i]}")

# def is_key_presend(k):
#     for i in dic : 
#         if(i == k):
#             print("Yes the key is present")
#         else :
#             print("No the key is not present")

# squr_list = []
# squ_no = lambda a : a**2
# for i in range(11):
#     squr_list.append(squ_no(i))
# print(squr_list)

# import random
# rand_no = []
# for i in range (101):
#     rand_no.append(random.randint(1, 10))
# rand_no = tuple(rand_no)
# unique_no = set(rand_no)
# for i in unique_no : 
#     count = 0
#     for j in rand_no : 
#         if(i == j) :
#             count +=1
#     print(count)


students = []
class Student :
    def __init__(self, student_name, marks):
        self.stu_name = student_name
        self.marks = marks
        stu_data = {}
        stu_data["name"] = student_name
        stu_data["marks"] = marks
        students.append(stu_data)
   
    
stu1 = Student("Muktesh", 34)
stu2 = Student("Sunay", 33)
stu3 = Student("Money", 45)
stu4 = Student("Meena", 42)
stu5 = Student("Rahul", 23)


sorted_stu = sorted(students, key = lambda item : item["name"])
print(sorted_stu)


mean_marks = 0
for student in students:
    mean_marks += student["marks"]
mean_marks = mean_marks/len(students)
print(mean_marks)


topper = students[0] # let
for student in students:
    if student["marks"] > topper["marks"]:
        topper = student
print(f"Student {topper.get('name')} obtained maximum marks {topper.get('marks')}" )