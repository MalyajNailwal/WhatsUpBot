# WhatsUpBot

WhatsUpBot is a Python-based WhatsApp bot designed to automate messaging and perform various tasks, such as fetching news, providing Wikipedia summaries, and responding to user queries. The bot leverages libraries like `pyautogui` for virtual keyboard/mouse control, `webbrowser` for opening WhatsApp Web, and `BeautifulSoup` for web scraping.

## Features

- **Automated Messaging**: Responds to user queries in real-time.
- **Wikipedia Integration**: Provides concise information on topics using Wikipedia.
- **News Updates**: Fetches the latest news headlines.
- **Text-to-Speech**: Optional feature to speak responses out loud.
- **Customizable Responses**: Easily tweak reply messages to suit your needs.

## Requirements

Ensure the following dependencies are installed:

- Python 3.x
- Libraries:
  - `pyautogui`
  - `webbrowser`
  - `requests`
  - `bs4` (BeautifulSoup)
  - `pyttsx3`
  - `wikipedia`
  - `tkinter`

To install the required libraries, run:

```bash
pip install pyautogui requests beautifulsoup4 pyttsx3 wikipedia
```

## Setup Instructions

1. Clone the repository:

    ```bash
    git clone https://github.com/MalyajNailwal/WhatsUpBot.git
    ```

2. Navigate to the project directory:

    ```bash
    cd WhatsUpBot
    ```

3. Run the script:

    ```bash
    python bot.py
    ```

4. Open WhatsApp Web:

    The bot will automatically open WhatsApp Web. Ensure your account is logged in.

## Usage

1. **Start WhatsApp Web**:
    - The script opens WhatsApp Web and waits for user interaction.

2. **Interaction**:
    - **Greet the bot**: Say "Hello" or "Hi" to get a greeting.
    - **Ask for news**: Use "news" to receive the latest 3 news headlines.
    - **Wikipedia queries**: Use "Tell me about [topic]" to get a brief summary of the topic.
    - **Text-to-Speech**: Use "you speak" to hear the bot speak a predefined message.

3. **Automated Responses**:
    - "How are you" gets a dynamic reply.
    - "Your name" provides the bot's name.
    - "Sorry" receives a customized response.
    - "Take over human" triggers humorous replies.

## Code Structure

- `bot.py`: Main script containing all bot functionalities.

## Key Functions

- `send_message(msg)`: Sends a message to WhatsApp.
- `get_clipboard_text()`: Retrieves text from the clipboard.
- `greet_user()`: Greets the user based on the time of day.
- `handle_common_queries(cb)`: Handles common user queries.
- `fetch_news()`: Fetches top 3 news headlines.
- `fetch_wikipedia_summary(topic)`: Fetches a brief summary of a given topic from Wikipedia.
- `speak_message(message)`: Converts text to speech using `pyttsx3`.
- `process_messages()`: Monitors and processes incoming messages.

## Notes

- Ensure WhatsApp Web is active and connected.
- Adjust the script delays (`time.sleep`) if experiencing issues with performance.
- Modify the predefined responses and message handling logic to suit your preferences.

## Contributing

We welcome contributions to enhance WhatsUpBot. Submit issues or pull requests on the [GitHub repository](https://github.com/MalyajNailwal/WhatsUpBot).

## License

This project is licensed under the MIT License. See the LICENSE file for details.

---

For any queries, feel free to contact [Malyaj Nailwal](mailto:malyajnailwal@example.com).
