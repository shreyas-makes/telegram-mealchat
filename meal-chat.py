from telegram import Update
from telegram.ext import Application, MessageHandler, filters, CallbackContext
from openai import OpenAI

import httpx

from dotenv import load_dotenv
import os

# Load environment variables from .env file
load_dotenv()

# Access environment variables
TELEGRAM_API_KEY = os.getenv("TELEGRAM_API_KEY")
OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")

# Initialize OpenAI client with your API key
client = OpenAI(api_key=OPENAI_API_KEY)

async def photo_handler(update: Update, context: CallbackContext):
    print("Received a photo")
    photo_file = await update.message.photo[-1].get_file()
    file_url = photo_file.file_path
    print("File URL:", file_url)  # Print the file URL

    # Use httpx to asynchronously download the photo
    async with httpx.AsyncClient() as client_http:
        response_image = await client_http.get(file_url)
        if response_image.status_code == 200:
            # Save the received image temporarily
            with open('photo.jpg', 'wb') as f:
                f.write(response_image.content)

            # Use GPT-4 Vision to describe the image
            response_gpt = client.chat.completions.create(
                model="gpt-4-vision-preview",
                messages=[
                    {
                        "role": "user",
                        "content": [
                            {"type": "text", "text": "Describe the dish in the image in two lines. Provide the breakdown in terms of calories as well as recommendation on how to make it more healthy"},
                            {"type": "image url",
                             "image_url": file_url}
                        ],
                    }
                ],
                max_tokens=300,
            )

            print("GPT-4 Vision response:", response_gpt)  # Print GPT-4 Vision response

            # Extract description text from GPT-4 Vision response
            description = response_gpt.choices[0].message.content

            # Reply to the user with the image description
            await update.message.reply_text(description)
        else:
            print("Failed to download image.")

async def text_handler(update: Update, context: CallbackContext):
    welcome_message = (
        "Welcome to our Healthy Diet ChatBot!\n\n"
        "A healthy diet is essential for overall well-being. "
        "It includes a balance of nutrients from various food groups such as fruits, vegetables, whole grains, lean proteins, and healthy fats.\n\n"
        "Remember, a colorful plate is often a healthy plate! Aim to include a variety of colorful fruits and vegetables in your meals, "
        "as they provide essential vitamins, minerals, and antioxidants.\n\n"
        "We encourage you to share a photo of the food you recently had. "
        "This will help us understand your dietary choices and provide personalized recommendations for healthier eating."
    )
    await update.message.reply_text(welcome_message)

if __name__ == '__main__':
    application = Application.builder().token(TELEGRAM_API_KEY).build()
    # Handler for photos
    application.add_handler(MessageHandler(filters.PHOTO, photo_handler))
    # Handler for text messages to send welcome message
    application.add_handler(MessageHandler(filters.TEXT, text_handler))
    application.run_polling()
