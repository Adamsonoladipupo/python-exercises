import unittest
from university_record_system_function import *

class TestForTheFunctionsInUniversityRecord(unittest.TestCase):
	def testing_if_caourse_are_available(self):
		expected = 4
		actual = number_of_available_courses(["Math", "Emglish", "Physics", "Art"])
		self.assertEqual(expected, actual)
	
	def testing_if_view_number_of_registered_students_return_number_of_studeents(self):
		expected = 1
		actual = view_number_of_registered_students({"ola123":[{"name":"oladipupo", "age":20}]})
		self.assertEqual(expected, actual)
	
	def testing_if_get_address_by_zip_code_return_zip_code(self):
		expected = 101252

		main_students_data = {}
		userid = "adam123"
		courses = {"Math", "English"}
		student_data = {
			"name" : "Adam",
			"age" : 22,
			"address" : {"zip_code": 101252, "city": "Abuja"},
			"courses" : courses
		}
		main_students_data[userid] = student_data
		actual = get_address_by_zip_code(main_students_data, userid)

		self.assertEqual(expected, actual)

	def testing_if_get_address_by_city_return_zip_code(self):
		expected = "Abuja"

		main_students_data = {}
		userid = "adam123"
		courses = {"Math", "English"}
		student_data = {
			"name" : "Adam",
			"age" : 22,
			"address" : {"zip_code": 101252, "city": "Abuja"},
			"courses" : courses
		}
		main_students_data[userid] = student_data
		actual = get_address_by_city(main_students_data, userid)

		self.assertEqual(expected, actual)


	def testing_if_set_address_by_city_set_new_zip_code(self):
		expected = "Abuja"

		new_city = "Abuja"

		main_students_data = {}
		userid = "adam123"
		courses = {"Math", "English"}
		student_data = {
			"name" : "Adam",
			"age" : 22,
			"address" : {"zip_code": 101252, "city": "Lagos"},
			"courses" : courses
		}
		main_students_data[userid] = student_data
		actual = set_address_by_city(main_students_data, userid, new_city)

		self.assertEqual(expected, actual)


	def testing_if_set_address_by_zip_code_set_new_zip_code(self):
		expected = 101205

		new_zip_code = 101205

		main_students_data = {}
		userid = "adam123"
		courses = {"Math", "English"}
		student_data = {
			"name" : "Adam",
			"age" : 22,
			"address" : {"zip_code": 000000, "city": "Lagos"},
			"courses" : courses
		}
		main_students_data[userid] = student_data
		actual = set_address_by_zip_code(main_students_data, userid, new_zip_code)

		self.assertEqual(expected, actual)



	def testing_if_get_student_name_return_student_name(self):
		expected = "Chief"

		main_students_data = {}
		userid = "adam123"
		courses = {"Math", "English"}
		student_data = {
			"name" : "Chief",
			"age" : 22,
			"address" : {"zip_code": 101252, "city": "Abuja"},
			"courses" : courses
		}
		main_students_data[userid] = student_data
		actual = get_student_name(main_students_data, userid)

		self.assertEqual(expected, actual)


	def testing_if_set_student_name_set_student_name(self):
		expected = "Ololade"

		new_name = "Ololade"

		main_students_data = {}
		userid = "adam123"
		courses = {"Math", "English"}
		student_data = {
			"name" : "Chief",
			"age" : 22,
			"address" : {"zip_code": 101252, "city": "Abuja"},
			"courses" : courses
		}
		main_students_data[userid] = student_data
		actual = set_student_name(main_students_data, userid, new_name)

		self.assertEqual(expected, actual)

	def testing_if_get_students_age_return_student_age(self):
		expected = 22

		main_students_data = {}
		userid = "adam123"
		courses = {"Math", "English"}
		student_data = {
			"name" : "Chief",
			"age" : 22,
			"address" : {"zip_code": 101252, "city": "Abuja"},
			"courses" : courses
		}
		main_students_data[userid] = student_data
		actual = get_student_age(main_students_data, userid)

		self.assertEqual(expected, actual)


	def testing_if_set_student_age_set_student_age(self):
		expected = 26

		new_age = 26

		main_students_data = {}
		userid = "adam123"
		courses = {"Math", "English"}
		student_data = {
			"name" : "Chief",
			"age" : 22,
			"address" : {"zip_code": 101252, "city": "Abuja"},
			"courses" : courses
		}
		main_students_data[userid] = student_data
		actual = set_student_age(main_students_data, userid, new_age)

		self.assertEqual(expected, actual)

	def testing_if_add_course_successfully_add_new_course(self):

		new_course = "Engineering"

		expected = f"{new_course} added successfully!"

		main_students_data = {}
		userid = "adam123"
		courses = {"Math", "English"}
		student_data = {
			"name" : "Chief",
			"age" : 22,
			"address" : {"zip_code": 101252, "city": "Abuja"},
			"courses" : courses
		}
		main_students_data[userid] = student_data
		actual = add_course(main_students_data, userid, new_course)

		self.assertEqual(expected, actual)

	def testing_if_remove_course_function_removes_course(self):

		course_name = "law"

		expected = f"{course_name} removed successfully!"

		courses = {"math", "law", "english"}

		main_students_data = {}
		userid = "ola123"
		student_data = {
			"name" : "name",
			"age" : 11,
			"address" : {"zip_code": 111111, "city": "city"},
			"courses" : courses
		}
		main_students_data[userid] = student_data
		actual = remove_course(main_students_data, userid, course_name)
		self.assertEqual(expected, actual)
		



