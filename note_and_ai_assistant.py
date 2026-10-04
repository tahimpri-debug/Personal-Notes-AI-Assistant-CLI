import json
import requests
import os
from datetime import datetime
from dotenv import load_dotenv


load_dotenv()
api_key = os.environ.get("OPENROUTER_AI_API_KEY")

def loat_notes(filename = "notes.json"):
    try:
        with open(filename, "r") as f:
            return json.load(f)
    except FileNotFoundError:
        return []

def save_notes(notes, filename= "notes.json"):
    with open(filename, "w")as f:
        json.dump(notes, f, indent=2)

def add_note(notes, text):
    note = {
        "text": text,
        "date": datetime.now().strftime("%Y-%m-%d"),
        "ai_response": None
    }
    notes.append(note)
    save_notes(notes)

def view_all_notes(notes):
    if not notes:
        print("\nNo note add yet...")
        return
    print("\n===== Your Notes =====\n")
    for i,note in enumerate(notes, start=1):
        print(f"{i}. {note['text']} ({note['date']})")
        if note["ai_response"]:
            print(f"    Ai said: {note['ai_response']}")
    print()

def get_random_fact():
    url = "https://uselessfacts.jsph.pl/api/v2/facts/random"
    try:
        response = requests.get(url)
        if response.status_code == 200:
            data = response.json()
            fact = data['text']
            print(f"\nRandome fact : {fact}\n")
            return fact
        else: 
            print("Something went wrong. status code :", response.status_code)
    except requests.exceptions.RequestException:
        print("Could not connect to the API. Check your internet.")
        return None

def ask_ai_about_note (note_text):
    if not api_key:
        print("Pleace check your .env first ")
        return None

    url = "https://openrouter.ai/api/v1/chat/completions"

    headers = {
        "Authorization": "Bearer {api_key}",
        "Content-Type": "application/json"
    }
    body = {
        "model": 'openai/gpt-4o',
        "massages": [
            {"role": "user", "content": f"Briefly explain or reflect on this note: {note_text}"}
        ]
    }

    try:
        responst = requests.post(url, headers=headers, json=body)
        if responst.status_code == 200:
            data = responst.json()
            reply = data["choices"][0]["massage"]["content"]
            return reply.strip()
        else:
            print("something wrong. status code : ", responst.status_code)
            print(responst.text)
            return None
    except requests.exceptions.RequestException:
        print("could not connect to the API. Chech your internet.")
        return None



if __name__ == "__main__":

    notes =  loat_notes()
    while True:
        print("="*40)
        print("\n1. Add a note")
        print("2. View all notes")
        print("3. Get a random fact from the internet")
        print("4. Fetch a fact and save it as a note")
        print("5. Ask AI about a save note")
        print("6. Exit...\n")
        print("="*40)

        choice_option = input("Enter what you want to do : ").strip()

        if choice_option == "1":
            text = input("Enter your text : ").strip()
            if text :
                add_note(notes, text)
                print("Note is added \n")
            else:
                print("NOte cannot be emply")

        elif choice_option == "2":
            view_all_notes(notes)

        elif choice_option == "3":
            get_random_fact()

        elif choice_option == "4":
            fact = get_random_fact()
            if fact:
                add_note(notes, fact)
                print("Fact saved as a note. \n")

        elif choice_option == "5":
            view_all_notes(notes)
            if notes :
                try :
                    index = int(input("Which note number ? ")) - 1
                    if 0 <= index <len(notes):
                        reply = ask_ai_about_note(notes[index]['text'])
                        if reply:
                            print(f"\nAI: {reply}")
                            notes[index]["ai_response"] = reply
                            save_notes(notes)
                    else:
                        print("Invalid note number. \n")
                except ValueError:
                    print("Pleace enter a valid number. \n")

        elif choice_option == "6":
            print("Quinting ...")
            break

        else:
            print("Choice invaled number. try again \n")