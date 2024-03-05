import wikipedia
import pyttsx3

def speak(text):
    engine = pyttsx3.init()
    engine.say(text)
    engine.runAndWait()

def search_and_speak(query):
    try:
        # Search Wikipedia for the query
        search_results = wikipedia.search(query)
        if not search_results:
            speak("Sorry, I couldn't find any information on that.")
            return
        page = wikipedia.page(search_results[0])

        # Fetch and speak the summary
        summary = wikipedia.summary(search_results[0], sentences=2)
        speak(summary)

    except wikipedia.exceptions.DisambiguationError as e:
        speak("Can you please be more specific?")
        print("DisambiguationError:", e)

    except wikipedia.exceptions.PageError as e:
        speak("Sorry, I couldn't find any information on that.")
        print("PageError:", e)

    except Exception as e:
        speak("Sorry, something went wrong.")
        print("Error:", e)

if __name__ == "__main__":
    query = input("What do you want to search on Wikipedia? ")
    search_and_speak(query)
