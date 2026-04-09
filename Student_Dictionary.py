# # contains class students and their marks
# mydict = {"Neil" : 100, "Vijender" : 80, "Asha" : 20, "Ricky" : 40}

# # print marks of Neil
# marks = mydict["Neil"]
# print(f"marks of Neil is {marks}")


# # change marks to Neil to 50
# mydict["Neil"] = 50 
# print(mydict)

# # list of students in class

# students = mydict.keys()
# print(f"students in class : {students}")


# # list of marks in clas
# marks = mydict.values()
# print(f"marks of each students :{marks}")


# # Add a new Student in class, watson : 40
# mydict['Watson'] = 40
# print(mydict)


# # Remove a Student from Dict
# mydict.pop("Neil")
# print(mydict)


# # clear the whole dictionary
# mydict.clear()
# print(mydict)

# mydict["Neil"] = 50
# mydict["Vijender"] = 40
# print(mydict)




# r = input("Enter a Number : ")
# i = int(r)



# There is student , take the marks from user;
# marks = input("Enter all marks separated by comma: ")
# marks_list = marks.strip().split(",")

# i  = 0
# while i < len(marks_list):
# 	marks_list[i] = int(marks_list[i].strip())
# 	i = i + 1

# print(marks_list)


# We will create a class, where there will be some students, each student will have name, and each student will have 5 subjects and their marks have to be in list;

def main():
	print("##################### CLASS DASHBOARD ######################")
	dictionary = {}
	studentSubjects = ["Math", "English", "Science", "History", "Pyschology"]
			
	while (True):
		print("Enter 1 to add a Student.")
		print("Enter 2 to Display the Result.")
		print("Enter 3 to Exit the program.")
		choice = int(input("Enter your Choice:  "))		
		if (choice == 1):
			studentName = input("Enter Student Name: ")
			studentSubjectinString = ','.join(studentSubjects)
			studentMarks = input(f"Enter all marks separated by comma pertaining to {studentSubjectinString}: ")
			studentMarksList = studentMarks.strip().split(",")
			i = 0
			while (i < len(studentMarksList)):
				studentMarksList[i] = int(studentMarksList[i].strip())
				i = i + 1
			dictionary[studentName] = studentMarksList
			
			print(f"Student Added {studentName}, subjects => {studentSubjectinString}, marks => {studentMarksList}\n\n")
		elif (choice == 2):
			for key in dictionary.keys():
				studentMarksList = dictionary[key]
				totalMarks = 0.0
				print(f"Student Name : {key}")
				j = 0
				while (j < len(studentMarksList)):
					print(f"{studentSubjects[j]}: {studentMarksList[j]}")
					
				
					totalMarks += studentMarksList[j]
					j = j + 1

				percentage =  totalMarks /len(studentMarksList)

				
			print("\n\n")
		else:
			print("#################### GOOD BYE ######################")
			break

main()