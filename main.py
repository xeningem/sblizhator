from telegram import Update
from telegram.ext import ApplicationBuilder, Updater, CommandHandler, MessageHandler, CallbackContext
from questions import questions
import random
import os
from dotenv import load_dotenv

load_dotenv(".env")
processed_questions = [f"{i+1}: {question}" for i, question in enumerate(questions)]

# Start command
async def start(update: Update, context: CallbackContext) -> None:
    await update.message.reply_text("Привет! Я помогу вам сближаться с помощью вопросов. Напишите /question, чтобы начать. Вопросы взяты у @VintovkinaEd_bot")


# Send a random question
async def question(update: Update, context: CallbackContext) -> None:
    # Choose a random question from the list
    random_question = random.choice(processed_questions)
    user = update.effective_user
    user_info = f"{user.id} {user.name}"
    print(user_info, random_question)
    await update.message.reply_text(random_question)


# Error handling
async def error(update: Update, context: CallbackContext) -> None:
    print(f"Update {update} caused error {context.error}")


def main():
    # Bot Token
    bot_token = os.getenv("BOT_TOKEN")

    app = ApplicationBuilder().token(bot_token).build()

    # Handlers for commands
    app.add_handler(CommandHandler("start", start))
    app.add_handler(CommandHandler("question", question))

    # Error handling
    app.add_error_handler(error)

    app.run_polling()


if __name__ == '__main__':
    main()
