offered_courses = {"math","physics","computer science","biology","chemistry","statistics","english","economics","history","philosophy","sociology","political science","geography","psychology","art","music","engineering","law","medicine","business"}

main_students_data = {}
courses = set()


def display_main_menu():
	main_menu = """

	Welcome to The University

	Enter as a :

	1. Student
	2. HOD
	3. Exit
	
	"""
	print(main_menu)

def number_of_available_courses(input):
	count_items = 0
	for item in input:
		count_items+=1
	return count_items


def view_available_course():
	print("Avaible Courses: ")
	for course in offered_courses:
		print(course, end = " | ")
	print()

#======= Students functions ============

def student_menu_level_one():
	menu = """
	Which of these best describe you?
	
	1. New student
	2. Returning student

	0. Back

	"""	
	print(menu)

def returning_student_level_one(input):
	menu = f"""
	
	Welcome back {main_students_data[input]["name"]}!
	
	1. View profile
	2. View offered courses
	3. View my address Zip code
	4. View my address city
	5. Edit profile
	6. Edit courses (add, remove, update)

	0. Back

	"""
	print(menu)


def returning_student_edit_profile():
	menu = f"""
	
	You can make changes to: 
	
	1. Change name
	2. Change age
	3. Change Address

	0. Back

	"""
	print(menu)


def returning_student_edit_course():
	menu = f"""
	
	Make changes to your courses: 
	
	1. Add a new course
	2. Remove a course

	0. Back

	"""
	print(menu)

def view_specific_student_profile(input):
	student_profile = main_students_data[input]
	for item, item_value in student_profile.items():
		print(item, item_value)

def view_offered_courses_by_student(input):
	count_course = 0
	student_courses = main_students_data[input]["courses"]
	print("Your courses: ")
	for course in student_courses:
		count_course+=1
		print(f"{count_course}. {course}")

def get_address_by_zip_code(main_students_data, input):
	zip = main_students_data[input]["address"]["zip_code"]
	return zip

def get_address_by_city(main_students_data, input):
	city = main_students_data[input]["address"]["city"]
	return city

def set_address_by_zip_code(main_students_data, userid, new_zip_code):
	main_students_data[userid]["address"]["zip_code"] = new_zip_code
	return new_zip_code

def set_address_by_city(main_students_data, userid, new_city):
	main_students_data[userid]["address"]["city"] = new_city
	return new_city


def get_student_name(main_students_data, userid):
	student_name = main_students_data[userid]["name"]
	return student_name
	
def set_student_name(main_students_data, userid, new_name):
	main_students_data[userid]["name"] = new_name
	return new_name

def get_student_age(main_students_data, userid):
	age = main_students_data[userid]["age"]
	return age

def set_student_age(main_students_data, userid, new_age):
	main_students_data[userid]["age"] = new_age
	return new_age

def add_course(main_students_data, userid, new_course):
	main_students_data[userid]["courses"].add(new_course)
	return f"{new_course} added successfully!"


def remove_course(main_students_data, userid, course_name):
	main_students_data[userid]["courses"].remove(course_name)
	return f"{course_name} removed successfully!"

# ======= HOD/ university function ========

def hod_menu_level_one():
	menu = """

	Welcome back Mr. HOD

	1. View all students profile
	2. View number of registered students

	0. Back

	"""
	print(menu)

def view_all_student_profile():
	for key, value in main_students_data.items():
		print("============================")
		print("Student's ID: " + key)
		print("----------------------------")
		for key1, value1 in value.items():
			print(key1, value1)

def view_number_of_registered_students(input):
	count_student = 0
	for key in input:
		count_student+=1
	return count_student


