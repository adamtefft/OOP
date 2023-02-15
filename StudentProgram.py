import StudentClass as sc

studentID = 1001
name = 'John'
dob = '10/11/2001'
classification = 'junior'


student1 = sc.Student(studentID, name, dob, classification)

student1.age()
student1.calc_registration

print(f"Student Age is: {student1.get_age()}")
print(f"Student can register between: {student1.get_register()}")
