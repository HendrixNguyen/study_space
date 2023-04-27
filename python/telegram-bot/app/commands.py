import requests
from telegram import ForceReply, Update


class Commander:
    def __init__():
        pass

    # Define a few command handlers. These usually take the two arguments update and
    # context.
    async def start(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
        """Send a message when the command /start is issued."""
        user = update.effective_user
        await update.message.reply_html(
            rf"Hi {user.mention_html()}!",
            reply_markup=ForceReply(selective=True),
        )

    async def help_command(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
        """Send a message when the command /help is issued."""
        await update.message.reply_text("Help!")

    async def echo(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
        """Echo the user message."""
        await update.message.reply_text(update.message.text)

    async def get_public_ip(update: Update, context: ContextTypes.DEFAULT_TYPE) -> str:
        """Get the public Ip."""
        ip_public = requests.get("https://ifconfig.me")
        await update.message.reply_text(ip_public.text)
        return ip_public.text
