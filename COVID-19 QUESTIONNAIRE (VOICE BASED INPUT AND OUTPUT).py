import pyttsx3
import speech_recognition as sr 
import time


def questionnaire(): 
	r = sr.Recognizer() 
	engine = pyttsx3.init()                                                  
	user_reply1 = "Do you live in the same house as that of the case?"
	engine.say(user_reply1)
	engine.runAndWait()
	engine.stop()
	with sr.Microphone()as source:
		print("Please Reply in yes or no")
		audio = r.listen(source)
		user_reply10 = r.recognize_google(audio)
		user_reply1 = format(user_reply10)
	user_reply2 = "Are you their intimate partner?"
	engine.say(user_reply2)
	engine.runAndWait()
	engine.stop()
	with sr.Microphone()as source:
		print("Please Reply in yes or no")
		audio = r.listen(source)
		user_reply20 = r.recognize_google(audio)
		user_reply2 = format(user_reply20)
	user_reply3 = "Have you provided any care to the patient while he or she was sick?"
	engine.say(user_reply3)
	engine.runAndWait()
	engine.stop()
	with sr.Microphone()as source:
		print("Please Reply in yes or no")
		audio = r.listen(source)
		user_reply30 = r.recognize_google(audio)
		user_reply3 = format(user_reply30)
	if user_reply1 == "no" and user_reply2 == "no" and user_reply3 == "no":
		user_reply4 = "Were you in the same indoor environment like a classroom with the patient for 15 minutes or more during his or her infectious period? "
		engine.say(user_reply4)
		engine.runAndWait()
		engine.stop()
		with sr.Microphone()as source:
			print("Please Reply in yes or no")
			audio = r.listen(source)
			user_reply40 = r.recognize_google(audio)
			user_reply4 = format(user_reply40)
		if user_reply4 == "no":
			engine.say("NO IDENTIFIABLE RISK")	
			engine.runAndWait()
			engine.stop()
		elif user_reply4 == "yes":
			user_reply7 = "Were you within 6 feet of the patient for 15 minutes or more?"
			engine.say(user_reply7)
			engine.runAndWait()
			engine.stop()
			with sr.Microphone()as source:
				print("Please Reply in yes or no")
				audio = r.listen(source)
				user_reply70 = r.recognize_google(audio)
				user_reply7 = format(user_reply70)
			user_reply8 = "Has the patient coughed or sneezed on you since 48 hours before they fell ill?"
			engine.say(user_reply8)
			engine.runAndWait()
			engine.stop()
			with sr.Microphone()as source:
				print("Please Reply in yes or no")
				audio = r.listen(source)
				user_reply80 = r.recognize_google(audio)
				user_reply8 = format(user_reply80)
			if user_reply7 == "no" and user_reply8 == "no":
				engine.say("NO IDENTIFIABLE RISK")
				engine.runAndWait()
				engine.stop()
			elif user_reply7 == "yes" or user_reply8 == "yes":
				engine.say("MEDIUM RISK")
				engine.runAndWait()
				engine.stop()
				user_reply9 = "Do you have fever coughness or shortness of breath?"
				engine.say(user_reply9)
				engine.runAndWait()
				engine.stop()
				with sr.Microphone()as source:
					print("Please Reply in yes or no")
					audio = r.listen(source)
					user_reply90 = r.recognize_google(audio)
					user_reply9 = format(user_reply90)
				if user_reply9 == "yes":
					engine.say("Isolate yourself until at least seven days have passed since sympton onset and 72 hours since fever resolved and respiratory symptoms improved .Seek testing if possible.")
					engine.runAndWait()
					engine.stop()
				elif  user_reply9 == "no":
					engine.say("Quarantine for 14 days since your last exposure to the patient. Stay home as much as possible and six feet from others when you must go out. Watch for any symptoms")
					engine.runAndWait()
					engine.stop()
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
		user_reply5 = "While the patient has been ill, has he or she been spending most of the time in a different room from you?"
		engine.say(user_reply5)
		engine.runAndWait()
		engine.stop()
		with sr.Microphone()as source:
			print("Please Reply in yes or no")
			audio = r.listen(source)
			user_reply50 = r.recognize_google(audio)
			user_reply5 = format(user_reply50)
		user_reply6 = "When you are in the same room, and in all your interactions, are you using aface mask or gloves?"
		engine.say(user_reply6)
		engine.runAndWait()
		engine.stop()
		with sr.Microphone()as source:
			print("Please Reply in yes or no")
			audio = r.listen(source)
			user_reply60 = r.recognize_google(audio)
			user_reply6 = format(user_reply60)
		if user_reply5 == "yes" and user_reply6 == "yes":
			engine.say("MEDIUM RISK")
			engine.runAndWait()
			engine.stop()
			user_reply9 = "Do you have fever coughness or shortness of breath?"
			engine.say(user_reply9)
			engine.runAndWait()
			engine.stop()
			with sr.Microphone()as source:
				print("Please Reply in yes or no")
				audio = r.listen(source)
				user_reply90 = r.recognize_google(audio)
				user_reply9 = format(user_reply90)
			if user_reply9 == "yes":
				engine.say("Isolate yourself until at least seven days have passed since sympton onset and 72 hours since fever resolved and respiratory symptoms improved .Seek testing if possible.")
				engine.runAndWait()
				engine.stop()
			elif  user_reply9 == "no":
				engine.say("Quarantine for 14 days since your last exposure to the patient. Stay home as much as possible and six feet from others when you must go out. Watch for any symptoms")
				engine.runAndWait()
				engine.stop()
			else:
				print("Please type your answer that is- yes or no(in lowercase).")
				print("----RESTART----")
				time.sleep(1)
				questionnaire()
		elif user_reply5 == "no" or user_reply6 == "no":
			engine.say("HIGH RISK")
			engine.runAndWait()
			engine.stop()
			user_reply9 = input("Do you have fever coughness or shortness of breath?")
			if user_reply9 == "yes":
				engine.say("Isolate yourself until at least seven days have passed since sympton onset and 72 hours since fever resolved and respiratory symptoms improved. Seek testing if possible.")
				engine.runAndWait() 
				engine.stop()
			elif  user_reply9 == "no":
				engine.say("Quarantine for 14 days since your last exposure to the patient. Stay home as much as possible and six feet from others when you must go out. Watch for any symptoms")
				engine.runAndWait()
				engine.stop()
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

