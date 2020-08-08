import time

def questionnaire():
	user_reply1 = input("Do you live in the same house as that of the case?")
	user_reply2 = input("Are you their intimate partner?")
	user_reply3 = input("Have you provided any care to the patient while he or she was sick?")
	if user_reply1 == "no" and user_reply2 == "no" and user_reply3 == "no":
		user_reply4 = input("Were you in the same indoor environment like a classroom with the patient for 15 minutes or more during his or her infectious period? ")
		if user_reply4 == "no":
			print("NO IDENTIFIABLE RISK")	
		elif user_reply4 == "yes":
			user_reply7 = input("Were you within 6 feet of the patient for 15 minutes or more?")
			user_reply8 = input("Has the patient coughed or sneezed on you since 48 hours before they fell ill?")
			if user_reply7 == "no" and user_reply8 == "no":
				print("NO IDENTIFIABLE RISK")
			elif user_reply7 == "yes" or user_reply8 == "yes":
				print("MEDIUM RISK")
				user_reply9 = input("Do you have fever coughness or shortness of breath?")
				if user_reply9 == "yes":
					print("Isolate yourself until at least seven days have passed since sympton onset and 72 hours since fever resolved and respiratory symptoms improved .Seek testing if possible.")
				elif  user_reply9 == "no":
					print("Quarantine for 14 days since your last exposure to the patient. Stay home as much as possible and six feet from others when you must go out. Watch for any symptoms")
				else:
					print("Please type your answer that is- yes or no(in lowercase).")
					print("----RESTART----")
					time.sleep(1)
					questionnaire()
			else:
				print("Please type your answer that is- yes or no(in lowercase).")
				print("----RESTART----")
				time.sleep(1)
				questionnaire()
		else:
			print("Please type your answer that is- yes or no(in lowercase).")
			print("----RESTART----")
			time.sleep(1)
			questionnaire()
	elif user_reply1 == "yes" or user_reply2 == "yes" or user_reply3 == "yes":
		user_reply5 = input("While the patient has been ill, has he or she been spending most of the time in a different room from you?")
		user_reply6 = input("When you are in the same room, and in all your interactions, are you using aface mask or gloves?")
		if user_reply5 == "yes" and user_reply6 == "yes":
			print("MEDIUM RISK")
			user_reply9 = input("Do you have fever coughness or shortness of breath?")
			if user_reply9 == "yes":
				print("Isolate yourself until at least seven days have passed since sympton onset and 72 hours since fever resolved and respiratory symptoms improved .Seek testing if possible.")
			elif  user_reply9 == "no":
				print("Quarantine for 14 days since your last exposure to the patient. Stay home as much as possible and six feet from others when you must go out. Watch for any symptoms")
			else:
				print("Please type your answer that is- yes or no(in lowercase).")
				print("----RESTART----")
				time.sleep(1)
				questionnaire()
		elif user_reply5 == "no" or user_reply6 == "no":
			print("HIGH RISK")
			user_reply9 = input("Do you have fever coughness or shortness of breath?")
			if user_reply9 == "yes":
				print("Isolate yourself until at least seven days have passed since sympton onset and 72 hours since fever resolved and respiratory symptoms improved. Seek testing if possible.")
			elif  user_reply9 == "no":
				print("Quarantine for 14 days since your last exposure to the patient. Stay home as much as possible and six feet from others when you must go out. Watch for any symptoms")
			else:
				print("Please type your answer that is- yes or no(in lowercase).")
				print("----RESTART----")
				time.sleep(1)
				questionnaire()
		else:
			print("Please type your answer that is- yes or no(in lowercase).")
			print("----RESTART----")
			time.sleep(1)
			questionnaire()
	else:
		print("Please type your answer that is- yes or no(in lowercase).")
		print("----RESTART----")
		time.sleep(1)
		questionnaire()

questionnaire()

