from telegram import Update
from telegram.ext import Application, MessageHandler, filters, CallbackContext

import httpx

async def photo_handler(update: Update, context: CallbackContext):
    print("Received a photo")
    photo_file = await update.message.photo[-1].get_file()
    file_url = photo_file.file_path
    print("File URL:", file_url)  # Print the file URL
    
    # Use httpx to asynchronously download the photo
    async with httpx.AsyncClient() as client:
        response = await client.get(file_url)
        if response.status_code == 200:
            with open('photo.jpg', 'wb') as f:
                f.write(response.content)
            print("Photo downloaded successfully.")

if __name__ == '__main__':
    application = Application.builder().token("6772726511:AAGGwktu6ELoy5ca14AD2r3RbEUo6AdbIVI").build()
    application.add_handler(MessageHandler(filters.PHOTO, photo_handler))
    application.run_polling()
