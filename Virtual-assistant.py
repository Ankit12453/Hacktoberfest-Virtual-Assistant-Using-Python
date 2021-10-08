import pyttsx3
import speech_recognition as sr
import webbrowser
import datetime
import wikipedia
import pywhatkit



def takeCommand():

	r = sr.Recognizer()


	with sr.Microphone() as source:
		print('Listening')
		

		r.pause_threshold = 0.7
		audio = r.listen(source)
		

		try:
			print("Recognizing")
			

			Query = r.recognize_google(audio, language='en-in')
			print("the command is printed=", Query)
			
		except Exception as e:
			print(e)
			print("Say that again sir")
			return "None"
		
		return Query

def speak(audio):
	
	engine = pyttsx3.init()

	voices = engine.getProperty('voices')
	

	engine.setProperty('voice', voices[0].id)

	engine.say(audio)
	

	engine.runAndWait()

def tellDay():
	

	day = datetime.datetime.today().weekday() + 1
	

	Day_dict = {1: 'Monday', 2: 'Tuesday',
				3: 'Wednesday', 4: 'Thursday',
				5: 'Friday', 6: 'Saturday',
				7: 'Sunday'}
	
	if day in Day_dict.keys():
		day_of_the_week = Day_dict[day]
		print(day_of_the_week)
		speak("The day is " + day_of_the_week)


def tellTime():

	time = str(datetime.datetime.now())


	print(time)
	hour = time[11:13]
	min = time[14:16]
	speak(self, "The time is sir" + hour + "Hours and" + min + "Minutes")	

def Hello():

	speak("hello sir I am moxa, your desktop assistant.Tell me how may I help you")


def Take_query():


	Hello()

	while(True):

		query = takeCommand().lower()
		if "open geeksforgeeks" in query:
			speak("Opening GeeksforGeeks ")
			

			webbrowser.open("www.geeksforgeeks.com")
			continue
            
		elif "open google" in query:
			speak("Opening Google ")
			webbrowser.open("www.google.com")
			continue
			
		elif "which day it is" in query:
			tellDay()
			continue
			
		elif "open news" in query:
			speak("Opening news ")
			webbrowser.open("https://indianexpress.com/")
			continue
		
		elif "tell me the time" in query:
			tellTime()
			continue
			
		elif "take me to hacktoberfest" in query:
			speak("Opening Hacktoberfest ")
			webbrowser.open("https://hacktoberfest.digitalocean.com")
			continue
			
		elif "open hacktoberfest discussion thread in twitter" in query:
			speak("Opening Hacktoberfest Discussion thread in Twitter.")
			webbrowser.open("https://twitter.com/search?q=%23hacktoberfest")
			continue
			
		elif "First time Contributors can contribute to vinitshahdeo Github" in query:
			speak("First time Contributors in Hacktoberfest.")
			webbrowser.open("https://github.com/vinitshahdeo")
			continue
		
		
		elif "bye" in query:
			speak("Bye for now...stay safe , stay happy , stay healthy")
			exit()
		
		elif "from wikipedia" in query:
			

			speak("Checking the wikipedia ")
			query = query.replace("wikipedia", "")
			

			result = wikipedia.summary(query, sentences=4)
			speak("According to wikipedia")
			speak(result)
		
		elif "tell me your name" in query:
			speak("I am moxa. Your deskstop Assistant")

if __name__ == '__main__':

    Take_query()
