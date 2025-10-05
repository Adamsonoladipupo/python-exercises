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
while main_menu < 0 or main_menu > 13:
	print("Invalid input, select from the Menu")
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

		while phone_book < 0 or phone_book > 10:
			print("Invalid input, select from the Menu")
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

				while option < 0 or option > 10:
					print("Invalid input, select from the Menu")
					option = int(input())
				match option:
					case 1: print("Type of view")
					case 2: print("Memory status")
			case 9: print("Speed dails")
			case 10: print("Voice tags")

	case 2: 
		doc_message = """
			Messages selected...
			Make a selection to proceed

			1-> Write message
			2-> Inbox
			3-> Outbox
			4-> Picture image
			5-> Templates
			6-> Smileys
			7-> Message settings
			8-> Info service
			9->  Voice mailbox number
			10-> Service command editor
		"""
		print(doc_message)
		message = int(input())

		while message < 0 or message > 10:
			print("Invalid input, select from the Menu")
			message = int(input())
		match message:
			case 1: print("Write message")
			case 2: print("Inbox")
			case 3: print("Outbox")
			case 4: print("Picture image")
			case 5: print("Templatese")
			case 6: print("Smileys")
			case 7: 
				doc_message_setting = """
					Message settings selected
					Make a selection to proceed

					1-> Set 1
					2-> Common
				"""
				print(doc_message_setting)
				message_setting = int(input())

				while message_setting < 0 or message_setting > 2:
					print("Invalid input, select from the Menu")
					message_setting = int(input())
				match message_setting:
					case 1: 
						doc_set1 = """
							Set 1 selected
							Make a selection to proceed

							1-> Message centre number
							2-> Message sent as
							3-> Message validity
						"""
						print(doc_set1)
						set1 = int(input())

						while set1 < 0 or set1 > 3:
							print("Invalid input, select from the Menu")
							set1 = int(input())
						match set1:
							case 1: print("Message centre number")
							case 2: print("Message sent as")
							case 3: print("Message validity")
					case 2:
						doc_common = """
							Common selected
							Make a selection to proceed

							1-> Delivery report
							2-> Reply via same centre
							3-> Character report
						"""
						print(doc_common)
						common = int(input())

						while common < 0 or common > 3:
							print("Invalid input, select from the Menu")
							common = int(input())
						match common:
							case 1: print("Delivery report")
							case 2: print("Reply via same centre")
							case 3: print("Character report")
				
			case 8: print("info services")
			case 9: print("Voice mailbox number")
			case 10: print("Service command editor")

	case 3: print("chat")
	case 4: 
		doc_call_register = """
			Call Register selected ...
			Make a selection to proceed

			1-> Missed calls
			2-> Received calls
			3-> Dailled calls
			4-> Erase recent call list
			5-> Show call duration
			6-> Show call cost
			7-> Call cost settings
			8-> Prepaid credit
		"""
		print(doc_call_register)
		call_register = int(input())

		while call_register < 0 or call_register > 8:
			print("Invalid input, select from the Menu")
			call_register = int(input())
		match call_register:
			case 1: print("Missed calls")
			case 2: print("Received calls")
			case 3: print("Dailled calls")
			case 4: print("Erase recent call list")
			case 5: 
				doc_call_duration = """
					Show Call duration selected ...
					Make a selection to proceed

					1-> Last call duration
					2-> All calls' duration
					3-> Received calls' duration
					4-> Dialled calls' duration
					5-> Clear timers
				"""
				print (doc_call_duration)
				call_duration = int(input())

				while call_duration < 0 or call_duration > 5:
					print("Invalid input, select from the Menu")
					call_duration = int(input())
				match call_duration:
					case 1: print("Last call duration")
					case 2: print("All calls' duration")
					case 3: print("Received calls' duration")
					case 4: print("Dialled calls' duration")
					case 5: print("Clear timers")
			case 6: 
				doc_call_cost = """
					Show Call costs selected ...
					Make a selection to proceed

					1-> Last call cost
					2-> All calls' cost
					3-> Clear counters
				"""
				print (doc_call_cost)
				call_cost = int(input())

				while call_cost < 0 or call_cost > 3:
					print("Invalid input, select from the Menu")
					call_cost = int(input())
				match call_cost:
					case 1: print("Last call cost")
					case 2: print("All calls' cost")
					case 3: print("Clear counters")
			case 7: 
				doc_call_cost_setting = """
					Call costs settings selected ...
					Make a selection to proceed

					1-> Call cost limit
					2-> Show costs limit
				"""
				print (doc_call_cost_setting)
				call_cost_setting = int(input())

				while call_cost_setting < 0 or call_cost_setting > 2:
					print("Invalid input, select from the Menu")
					call_cost_setting = int(input())
				match call_cost_setting:
					case 1: print("Call cost limit")
					case 2: print("Show costs limit")
			case 8: print("Prepaid credit")
	case 5:
		doc_tone = """
			Tones selected ...
			Make a selection to proceed

			1-> Ringing tone
			2-> Ringing volume
			3-> Incoming call alert
			4-> Composer
			5-> Message alert tone
			6-> Keypad tones
			7-> Warning and game tones
			8-> Vibrating alert
			9-> Screen saver
		"""
		print(doc_tone)
		tones = int(input())

		while tones < 0 or tones > 9:
			print("Invalid input, select from the Menu")
			tones = int(input())
		match tones:
			case 1: print("Ringing tone")
			case 2: print("Ringing volume")
			case 3: print("Incoming call alert")
			case 4: print("Composer")
			case 5: print("Message alert tone")
			case 6: print("Keypad tones")
			case 7: print("Warning and game tones")
			case 8: print("Vibrating alert")
			case 9: print("Screen saver")
	case 6:
		doc_setting = """
			Settings selected ...
			Make a selection to proceed

			1-> Call settings
			2-> Phone settings
			3-> Security settings
			4-> Restore factory settings
		"""
		print(doc_setting)
		settings = int(input())

		while settings < 0 or settings > 4:
			print("Invalid input, select from the Menu")
			settings = int(input())
		match settings:
			case 1: 
				doc_call_setting = """
					Call settings selected ...
					Make a selection to proceed

					1-> Automatic redial
					2-> Speed dialling
					3-> Call waiting options
					4-> Own number sending
					5-> Phone line in use
					6-> Automatic answer
				"""
				print (doc_call_setting)
				call_setting = int(input())

				while call_setting < 0 or call_setting > 6:
					print("Invalid input, select from the Menu")
					call_setting = int(input())
				match call_setting:
					case 1: print("Automatic redial")
					case 2: print("Speed dialling")
					case 3: print("Call waiting options")
					case 4: print("Own number sending")
					case 5: print("Phone line in use")
					case 6: print("Automatic answer")
			case 2:
				doc_phone_setting = """
					Phone settings selected ...
					Make a selection to proceed

					1-> Language
					2-> Cell info display
					3-> Welcome note
					4-> Network selection
					5-> Lights
					6-> Confirm SIM service actions
				"""
				print (doc_phone_setting)
				phone_setting = int(input())

				while phone_setting < 0 or phone_setting > 6:
					print("Invalid input, select from the Menu")
					phone_setting = int(input())
				match phone_setting:
					case 1: print("Language")
					case 2: print("Cell info display")
					case 3: print("Welcome note")
					case 4: print("Network selection")
					case 5: print("Lights")
					case 6: print("Confirm SIM service actions")
			case 3:
				doc_security_setting = """
					Security settings selected ...
					Make a selection to proceed

					1-> PIN code request
					2-> Call barring request
					3-> Fixed dialling
					4-> Closed user group
					5-> Phone security
					6-> Change access codes
				"""
				print (doc_security_setting)
				security_setting = int(input())

				while security_setting < 0 or security_setting > 6:
					print("Invalid input, select from the Menu")
					security_setting = int(input())
				match security_setting:
					case 1: print("PIN code request")
					case 2: print("Call barring request")
					case 3: print("Fixed dialling")
					case 4: print("Closed user group")
					case 5: print("Phone security")
					case 6: print("Change access codes")
			case 4: print("Restore factory settings")
	case 7: print("Call diveet")
	case 8: print("Games")
	case 9: print("Calculator")
	case 10: print("Reminders")
	case 11:
		doc_clock = """
			Clock selected ...
			Make a selection to proceed

			1-> Alarm clock
			2-> Clock settings
			3-> Date settings
			4-> Stopwatch
			5-> Countdown timer
			6-> Auto update of date and time
		"""
		print(doc_clock)
		clock = int(input())

		while clock < 0 or clock > 6:
			print("Invalid input, select from the Menu")
			clock = int(input())
		match clock:
			case 1: print("Alarm clock")
			case 2: print("Clock settings")
			case 3: print("Date settings")
			case 4: print("Stopwatch")
			case 5: print("Countdown timer")
			case 6: print("Auto update of date and time")
	case 12: print("Alarm")
	case 13: print("SIM servives")

