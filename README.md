# Telegram GPT-4 Vision Bot

![shreyas-06-03-2024 at 05 33 29@2x](https://github.com/shreyas-makes/telegram-mealchat/assets/7238886/7c98ccc7-00ad-41c4-8f0a-888df1665bb0)
![shreyas-06-03-2024 at 05 34 03@2x](https://github.com/shreyas-makes/telegram-mealchat/assets/7238886/8fa1ee2c-6332-4333-9248-a9faf9573afd)
![shreyas-06-03-2024 at 05 34 17@2x](https://github.com/shreyas-makes/telegram-mealchat/assets/7238886/4eeab5eb-c383-42c8-a6de-b6055597253e)

## Description
This is a Telegram bot that receives an image and replies with a description of the image using OpenAI's GPT-4 Vision model.

## Features
- Receives images from users via Telegram.
- Uses the GPT-4 Vision model to generate a textual description of the images.
- Responds to users with the description of the images.

## Prerequisites
- Python 3.9 or higher
- Install required Python packages:
`pip install python-telegram-bot httpx python-dotenv`

## Usage
1. Clone the repository:
`git clone <repository-url>`

2. Navigate to the project directory:
`cd telegram-gpt4-vision-bot`

3. Install dependencies:
`pip install -r requirements.txt`


## Configuration
1. Create a Telegram Bot:
- Create a new bot on Telegram by following the instructions [here](https://core.telegram.org/bots#3-how-do-i-create-a-bot).
- Note down the API token provided by BotFather.

2. Create a `.env` file in the project directory:
Add your Telegram API token to the `.env` file:
  ```
  TELEGRAM_API_KEY=<your-telegram-api-token>
  ```

## Usage

Run the bot script:
`python3.9 vision-gpt-telegram.py`


3. Start a conversation with your bot on Telegram and send an image to receive a description.

## Deployment
You can deploy this bot on cloud platforms like Heroku, AWS, or Google Cloud Platform for continuous operation.

## Contributing
Contributions are welcome! Feel free to submit issues or pull requests.

Make sure to replace <repository-url> with the actual URL of your repository and <your-telegram-api-token> with your Telegram API token. Feel free to modify it according to your project's requirements.






