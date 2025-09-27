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
mainMenu = int(input())
match mainMenu:
	case 1: print("Phone book")
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