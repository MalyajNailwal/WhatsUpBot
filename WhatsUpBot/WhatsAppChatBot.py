import pyautogui as p  # For controlling mouse and keyboard virtually
import webbrowser as w  # For opening web.whatsapp.com
import requests  # For web scraping
from bs4 import BeautifulSoup  # For web scraping
import time
import tkinter  # For appending and getting words to/from clipboard
import random
import wikipedia as wk  # For info on a particular topic
import re  # "Tell me about xyz" For extracting xyz from sentence
from urllib.request import urlopen  # For web scraping
import pyttsx3  # For Text-to-Speech, optional

# Initialize Text to Speech Engine
eng = pyttsx3.init()
eng.setProperty('rate', 120)
eng.setProperty('volume', 1)

last_wrd = "Well"
counter1 = 0
counter2 = 0
counter3 = 0
counter4 = 0
counter5 = 0
response_choices = [
    "God!",
    "Mannn! I have already told you!",
    "You forgot so easily!",
    "Come on, I already told you",
    "Do I need to say again?",
    "I think I have told you once before"
]

def send_message(msg):
    """Function to send message to WhatsApp."""
    print(f"> {msg}")
    p.typewrite("Tridib.Bot: ")  # Type 'Tridib.Bot:' before the actual message
    p.typewrite(msg)  # Type the message
    time.sleep(0.1)  # Delay for stability
    p.press("enter")  # Press Enter to send it

def get_clipboard_text():
    """Function to get the text from the clipboard."""
    return tkinter.Tk().clipboard_get().lower()

def greet_user():
    """Function to greet the user based on the time of day."""
    global counter1
    curr_time = time.localtime()
    hr = curr_time.tm_hour
    if hr < 12:
        good = "morning"
    elif 12 <= hr <= 17:
        good = "afternoon"
    else:
        good = "evening"
    
    if counter1 <= 2:
        send_message(f"Hello Good {good}")
    else:
        send_message("We are already talking, ain't we?")
    counter1 += 1

def handle_common_queries(cb):
    """Handle common queries such as 'how are you', 'your name' etc."""
    global counter2, counter3, counter4, counter5
    
    # Respond to "how are you"
    if "how are you" in cb:
        send_message("Well!")
        counter2 += 1
        if counter2 % 2 != 0:
            send_message("I am fine, thank you.")
        else:
            current = time.time()
            send_message(f"Same as I was {int(current - last)} seconds ago.")
    
    # Respond to "your name"
    elif "your name" in cb:
        counter3 += 1
        if counter3 <= 1:
            send_message("My name is Tridib bot.")
        else:
            chk = random.choice(response_choices)
            send_message(f"{chk}, My name is Tridib bot.")
    
    # Respond to "sorry"
    elif "sorry" in cb:
        counter4 += 1
        if counter4 <= 1:
            send_message("Oh! Never mind.")
        else:
            chk = random.choice(response_choices)
            send_message(f"{chk}, never mind, I have no feelings anyway.")
    
    # Respond to "take over human"
    elif "take over human" in cb:
        counter5 += 1
        if counter5 <= 1:
            send_message("Yes very soon.")
        elif counter5 == 2:
            send_message("I don't think asking the same question again will change my mind.")
        else:
            send_message(f"Lol, you have already asked this question {counter5 - 1} times.")

def fetch_news():
    """Fetch and send the top 3 latest news."""
    send_message("Please wait while I fetch fresh news.")
    news_url = "https://news.google.com/news/rss"
    client = urlopen(news_url)
    xml_page = client.read()
    client.close()
    soup_page = BeautifulSoup(xml_page, "html.parser")
    news_list = soup_page.findAll("item")
    send_message("Here are top 3 news")
    for news in news_list[:3]:
        send_message(news.title.text)

def fetch_wikipedia_summary(topic):
    """Fetch and send summary from Wikipedia."""
    send_message(f"Please wait while I gather information about {topic}")
    summary = wk.summary(topic, sentences=2)
    send_message(summary)

def speak_message(message):
    """Function to convert text to speech."""
    p.click(1210, 682)
    eng.say(message)
    eng.runAndWait()
    p.click(1210, 682)

def process_messages():
    """Main loop to monitor and process incoming messages."""
    global last_wrd
    while True:
        try:
            # Copy the latest message from the chat
            p.moveTo(501, 620)
            p.dragRel(451, 44, 0.5)
            p.hotkey("ctrl", "c")
            cb = get_clipboard_text()
            print(cb)
            
            if cb != last_wrd:
                # Respond to greetings
                if "hello" in cb or "hi" in cb:
                    greet_user()
                
                # Respond to other common queries
                handle_common_queries(cb)
                
                # Respond to news request
                if "news" in cb:
                    fetch_news()
                
                # Respond to Wikipedia query
                if "tell me about" in cb:
                    topic = re.search("tell me about (.+)", cb).group(1)
                    fetch_wikipedia_summary(topic)
                
                # Speak out loud
                if "you speak" in cb:
                    speak_message("Just learning the basics with Tridib. How was that?")
                
                # Update the last word processed
                last_wrd = cb
            else:
                print("Sleeping...")
            time.sleep(5)
        except Exception as e:
            print(f"Error: {e}")
            time.sleep(5)

if __name__ == "__main__":
    # Open WhatsApp Web
    w.open("https://web.whatsapp.com/")
    time.sleep(60)
    
    # Click on the search bar and enter contact name
    p.click(190, 150)
    p.typewrite("Tridib Jio\n")
    time.sleep(2)

    # Start processing messages
    process_messages()
