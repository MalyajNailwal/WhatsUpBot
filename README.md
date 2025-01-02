# WhatsUpBot

WhatsUpBot is a powerful and easy-to-use WhatsApp bot designed to streamline booking rides for transport businesses. With a simple setup, it enables users to communicate efficiently and book rides directly through WhatsApp.

## Features

- **Seamless Ride Booking**: Users can book rides effortlessly by interacting with the bot.
- **Automated Responses**: The bot handles queries and automates the booking process.
- **Customizable Settings**: Easily adapt the bot to suit your business needs.
- **User-Friendly Interface**: Intuitive and straightforward interactions for customers.

## Getting Started

### Prerequisites

Ensure you have the following installed on your system:

- [Node.js](https://nodejs.org/) (v14 or higher)
- [npm](https://www.npmjs.com/)
- [WhatsApp Business API](https://business.whatsapp.com/)

### Installation

Follow these steps to install and set up WhatsUpBot:

1. Clone the repository:

    ```bash
    git clone https://github.com/MalyajNailwal/WhatsUpBot.git
    ```

2. Navigate to the project directory:

    ```bash
    cd WhatsUpBot
    ```

3. Install dependencies:

    ```bash
    npm install
    ```

4. Configure environment variables:

    Create a `.env` file in the root directory and add the following details:

    ```env
    WHATSAPP_API_KEY=<your_whatsapp_api_key>
    BUSINESS_NAME=<your_business_name>
    TRANSPORT_CONTACT=<contact_number>
    ```

5. Start the bot:

    ```bash
    npm start
    ```

## How to Use

1. **Start a Conversation**:
    - Save the bot's WhatsApp number on your phone.
    - Send a message like "Hi" or "Book a ride" to initiate a conversation.

2. **Book a Ride**:
    - Follow the prompts provided by the bot to specify the pickup and drop-off locations, date, time, and other details.

3. **Confirmation**:
    - The bot will confirm your booking details and provide a reference number for tracking.

4. **Modify/Cancel Booking**:
    - Send commands like "Modify Booking" or "Cancel Booking" followed by your reference number.

## Project Structure

```
WhatsUpBot/
├── src/
│   ├── bot.js           # Core bot logic
│   ├── config.js        # Configuration settings
│   └── utils.js         # Utility functions
├── .env                 # Environment variables
├── package.json         # Project metadata and dependencies
└── README.md            # Project documentation
```

## Contributing

We welcome contributions to enhance the functionality and features of WhatsUpBot. Feel free to submit a pull request or open an issue.

### Steps to Contribute

1. Fork the repository.
2. Create a new branch for your feature:

    ```bash
    git checkout -b feature-name
    ```

3. Make your changes and commit them:

    ```bash
    git commit -m "Add new feature"
    ```

4. Push your changes:

    ```bash
    git push origin feature-name
    ```

5. Open a pull request on the main repository.

## License

This project is licensed under the [MIT License](LICENSE).

## Acknowledgments

- [Node.js](https://nodejs.org/)
- [WhatsApp Business API](https://business.whatsapp.com/)

---

For any queries or support, please contact [Malyaj Nailwal](mailto:malyajnailwal@example.com).
