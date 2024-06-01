import pyttsx3

if __name__ == "__main__":


    engine = pyttsx3.init()

    print("Welcome to RoboSpeaker")

    while True:
        x = input("What do you want me to pronounce : ")

        if x == "quit":
            engine.say("Bye Friend, Nice to talk with you")
            engine.runAndWait()
            break

        engine.say(x)
        engine.runAndWait()