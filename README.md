# WhatsApp Bot

This is a Python-based WhatsApp bot that automates several tasks such as responding to queries, fetching news, providing Wikipedia summaries, and more.

## Features

- **Greeting User**: Greets the user based on the time of day.
- **Common Queries**: Responds to "How are you?", "Your name?", "Sorry", "Take over human?".
- **Fetch News**: Retrieves the top 3 latest news from Google News.
- **Wikipedia Summary**: Provides a brief summary of a topic from Wikipedia.
- **Text-to-Speech**: Reads messages out loud.

## Requirements

- `pyautogui`
- `requests`
- `beautifulsoup4`
- `pyttsx3`
- `wikipedia`

Install the dependencies:

```bash
pip install pyautogui requests beautifulsoup4 pyttsx3 wikipedia

How to Use
Open the script in your Python environment.
The script will open WhatsApp Web and wait for messages.
The bot will respond based on the following:
Greetings like "Hello", "Hi".
Common queries such as "How are you?", "Your name?".
Fetches news or provides Wikipedia summaries.
Reads messages out loud on request.

License
This project is open source and free to use.





