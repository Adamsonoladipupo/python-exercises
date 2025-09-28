nokia3310 = """
	Welcome! Select an option to get started
			
	1-> Phone book
	2-> Messages
	3-> Chat
	4-> Call register
	5-> Tones
	6-> Settings
	7-> Call divert
	8-> Games
	9-> Calculator
	10-> Reminders
	11-> Clock
	12-> Alarm
	13-> SIM services

"""
print(nokia3310)
main_menu = int(input())
match main_menu:
	case 1: 
		doc_phone_book = """
			Phone book selected...
			Make a selection to proceed

			1-> Search
			2-> Service number
			3-> Add name
			4-> Erase
			5-> Edit
			6-> Assign tone
			7-> Send b'card
			8-> Options
			9-> Speed dails
			10-> Voice tags
		"""
		print(doc_phone_book)
		phone_book = int(input())
		match phone_book:
			case 1: print("Search")
			case 2: print("Service number")
			case 3: print("Add name")
			case 4: print("Erase")
			case 5: print("Edit")
			case 6: print("Assign tone")
			case 7: print("Send b'card")
			case 8: 
				doc_option = """
					Option selected...
					Make a selection to proceed

					1-> Type of view
					2-> Memory status
				"""
				print(doc_option)
				option = int(input())
				match option:
					case 1: print("Type of view")
					case 2: print("Memory status")
			case 9: print("Speed dails")
			case 10: print("Voice tags")
	case 2: print("Messages")
	case 3: print("chat")
	case 4: print("Call register")
	case 5: print("Tones")
	case 6: print("Settings")
	case 7: print("Call diveet")
	case 8: print("Games")
	case 9: print("Calculator")
	case 10: print("Reminders")
	case 11: print("Clock")
	case 12: print("Alarm")
	case 13: print("SIM servives")
