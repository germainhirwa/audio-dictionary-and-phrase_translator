from datetime import datetime
from gtts import gTTS
import os
from PyDictionary import PyDictionary


class Speaking:
    def speak(self, audio):
        tts = gTTS(text=audio, lang='en')
        tts.save("output.mp3")
        os.system("mpg321 output.mp3")

class GFG:
    def Dictionary(self):
        speak = Speaking()
        dictionary = PyDictionary()
        name = input("What is your name?: ")

        # Get the current time
        current_time = datetime.now().time()

        if current_time.hour < 12:
            greet = "Good morning"
        elif 12 <= current_time.hour < 18:
            greet = "Good afternoon"
        else:
            greet = "Good evening"

        day_of_week = datetime.now().strftime("%A")
        if day_of_week in ["Monday", "Tuesday", "Wednesday", "Thursday"]:
            day_greet = "Have a great week"
        else:
            day_greet = "Have a great weekend"

        speak.speak(
            f"{greet} Mr {name}.I want to help you to know the meanings of English words. Please type the word that you want to find the meaning for below.")
        query = input("Enter a word: ")

        # Find the meaning of the word
        meaning = dictionary.meaning(query)

        if meaning:
            # Check if there is a 'Noun' and 'Verb' definition
            if 'Noun' in meaning:
                speak.speak(f"{query} as a noun means {meaning['Noun'][0]}.")
            if 'Verb' in meaning:
                speak.speak(f"{query} as a verb means {meaning['Verb'][0]}.")

            # Ask if the user is satisfied with the definition
            speak.speak("Are you satisfied with the definition?")
            user_satisfied = input("Are you satisfied with the definition? (yes/no): ").lower()
            if user_satisfied == 'yes':
                speak.speak(f"Great! {day_greet} and a wonderful day, {name}.")
            else:
                # Convert the meaning dictionary to a string and speak it
                meaning_str = "\n".join([f"{part}: {', '.join(definitions)}" for part, definitions in meaning.items()])
                print(meaning_str)
                speak.speak(meaning_str)
                speak.speak(f"I'm sorry if I didn't give you your desired definition for {query}. {day_greet} and a wonderful day, {name}.")
        else:
            print("Meaning not found for the word.")
            speak.speak(f"I'm sorry I couldn't find the meaning of {query}. {day_greet} and a a wonderful day, {name}.")


if __name__ == '__main__':
    GFG().Dictionary()