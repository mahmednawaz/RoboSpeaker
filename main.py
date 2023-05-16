# Start by importing the win32com package
import win32com.client as wincom
if __name__ == "__main__":
    
    while True: 
        speak = wincom.Dispatch("SAPI.SpVoice")
        print("Welcome to robo speaker...!")
        text = input("what you want to me to speak... ")
        if text == "exit":
            break
        speak.Speak(text)
    