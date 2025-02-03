import logging
from django.core.management.base import BaseCommand
from telegram.ext import Updater, CommandHandler, CallbackQueryHandler
from django.conf import settings
from ...models import Client, Manager

TELEGRAM_BOT_TOKEN = '7110448157:AAHlcqtKD1bLeNX1p2QtZgxs7u3hTMGD9VE'
GROUP_CHAT_ID = '-4772065501'

logger = logging.getLogger(__name__)


def handle_accept(update, context):
    query = update.callback_query
    query.answer()

    # Extract client ID from callback data
    client_id = query.data.split('_')[1]

    try:
        client = Client.objects.get(id=client_id)
        manager = Manager.objects.get(telegram_id=str(query.from_user.id))
    except (Client.DoesNotExist, Manager.DoesNotExist):
        query.edit_message_text("❗ Error processing request")
        return

    # Check if client already has a manager
    if client.status != 'new':
        query.edit_message_text("⚠️ This request was already accepted!")
        return

    # Update client status and manager
    client.status = 'processing'
    client.manager = manager
    client.save()

    # Edit original message to remove button
    new_text = f"✅ Принятый: {manager.user.username}\n" + query.message.text
    query.edit_message_text(text=new_text)


class Command(BaseCommand):
    help = 'Run Telegram bot'

    def handle(self, *args, **options):
        # Use settings instead of hardcoded values
        updater = Updater(settings.TELEGRAM_BOT_TOKEN)
        dp = updater.dispatcher

        dp.add_handler(CallbackQueryHandler(handle_accept, pattern='^accept_'))

        self.stdout.write("Bot started")
        updater.start_polling()
        updater.idle()
