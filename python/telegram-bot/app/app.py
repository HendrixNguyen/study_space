from telegram.ext import (
    Application,
    CommandHandler,
    ContextTypes,
    MessageHandler,
    filters,
)

from . import logger
from dotenv import load_dotenv


class App:
    def main() -> None:
        load_dotenv()

        _botToken = os.getenv("BOT_TOKEN")

        """Start the bot."""
        # Create the Application and pass it your bot's token.
        application = Application.builder().token(_botToken).build()
        # on different commands - answer in Telegram
        application.add_handler(CommandHandler("start", start))
        application.add_handler(CommandHandler("help", help_command))
        application.add_handler(CommandHandler("get_new_ip", get_public_ip))

        # on non command i.e message - echo the message on Telegram
        application.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, echo))

        # Run the bot until the user presses Ctrl-C
        application.run_polling()
