from university_record_system_function import *


while True:
	display_main_menu()
	user_input = input("Select an option to proceed:")
	match user_input:
		case "1":
			while True: 
				student_menu_level_one()
				user_input = input("Select an option to proceed: ")
				match user_input:
					case "1":
						print("Thank you for choosing us! \nLet get to know.")
				
						userid = input("pick a username (key): ")
						name = input("What is your name: ")
						age = input("how old are you: ")
						city = input("what city are you from: ")
						zip_code = int(input("enter zip code: "))

						view_available_course()
						countCourse = 1;
						course_input = "";
						courses = set()
						while True:
							course_input = input(f"Enter your prefered course {countCourse} (*STOP* to stop entering course): ").lower()
							if course_input in offered_courses:
								courses.add(course_input)
								countCourse +=1
							else:
								print("Please, choose from the course available")
							if course_input == "stop":
								break

						#courses.remove("stop")
	
						student_data = {
							"name" : name,
							"age" : age,
							"address" : {"zip_code": zip_code, "city": city},
							"courses" : courses
						}
						main_students_data[userid] = student_data
						
						
						
						print("Information saved successfully . . .")

					case "2":
						userid = input("Enter your userID/ username: ")
						if userid in main_students_data:
							specific_student = main_students_data[userid]
							while True:
								returning_student_level_one(userid)
								user_input = input("select an option to proceed: ")
								match user_input:
									case "1":
										view_specific_student_profile(userid)
									case "2":
										view_offered_courses_by_student(userid)
									case "3":
										print("Zip code: ", get_address_by_zip_code(main_students_data, userid))
									case "4":
										print("City: ", get_address_by_city(main_students_data, userid))
									case "5":
										returning_student_edit_profile()
										while True:
											user_input = input("Select an option to proceed: ")
											match user_input:
												case "1":
													print("Your previous name: ", get_student_name(main_students_data, userid))
													new_name = input("Enter a new name: ")
													set_student_name(main_students_data, userid, new_name)
													print(f"name changed to '{new_name}' successfully: ")
													
												case "2":
													print("Your previous age: ", get_student_age(main_students_data, userid))
													new_age = input("Enter a new age: ")
													set_student_age(main_students_data, userid, new_age)
													print(f"name changed to '{new_age }' successfully: ")

												case "3":
													new_zip_code = input("Enter your new zip code: ")
													set_address_by_zip_code(main_students_data, userid, new_zip_code)
													new_city = input("Enter your new city: ")
													set_address_by_city(main_students_data, userid, new_city)
													print("Address chnaged successfully . . .")

												case "0":
													break
												case _:
													print("Please, enter a valid option")
									case "6":
										returning_student_edit_course()
										while True:
											user_input = input("Select an option to proceed: ")
											match user_input:
												case "1":
													new_course = input("Enter course name: ")
													adding_course = add_course(main_students_data, userid, new_course)
													print(adding_course)
												case "2":
													course_name = input("Enter course name: ").lower()
													if course_name in main_students_data[userid]["courses"]:
														removing_course = remove_course(main_students_data, userid, course_name)
														print(removing_course)
													else:
														print(f"{course_name} is not among your offered course")
												case "0":
													break
												case _:
													print("Please, enter a valid option")
									case "0":
										break
									case _: 
										print("Please, enter a valid option")
						else : 
							print("user does not exist")
							
					case "0":
						break
					case _:
						print("Please, enter a valid input")
			
		case "2": 
			user_input = input("Enter your admin PIN: ")
			if user_input == "4321":
				hod_menu_level_one()
				while True:
					user_input = input("Select an option to proceed: ")
					match user_input:
						case "1":
							view_all_student_profile()
							
						case "2":
							number_of_students = view_number_of_registered_students(main_students_data)
							print(f"Number of registered students: {number_of_students}")
						case "0":
							break
						case _: print("Please, enter a valid input1")
			else :
				trial_count = 3
				while trial_count > 1:
					trial_count -=1
					user_input = input(f"wrong PIN, you have {trial_count} more trial: ")
					
			
		case "3": 
			print("Thank you for schooling with us!")
			break
		case _:
			print("Please, enter a valid input")

