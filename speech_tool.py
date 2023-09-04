
import speech_recognition as sr

class microphone:
    
    def run():
        r = sr.Recognizer()
        mic = sr.Microphone()
    
        with mic as source:
            r.adjust_for_ambient_noise(source)
            print("Say something!")
            audio = r.listen(source)
    
            try:
                words = r.recognize_google(audio)
                print("You said: " + " ".join(words))
            except sr.UnknownValueError:
                print("Could not understand you.")
    
            text = " ".join(words)

            return text