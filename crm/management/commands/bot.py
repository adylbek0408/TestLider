import logging
from django.core.management.base import BaseCommand
from telegram.ext import Updater, CallbackQueryHandler
from telegram.error import BadRequest
from django.conf import settings
from django.db import transaction
from ...models import Client, Manager

logger = logging.getLogger(__name__)


def handle_accept(update, context):
    query = update.callback_query
    try:
        # Answer the callback query immediately
        query.answer()
    except BadRequest as e:
        if "Query is too old" in str(e):
            logger.warning(f"Expired callback query: {e}")
            return
        raise

    client_id = query.data.split('_')[1]

    try:
        with transaction.atomic():
            client = Client.objects.select_for_update().get(id=client_id)

            if client.status != 'new':
                try:
                    query.edit_message_text("⚠️ This request has already been accepted!")
                except BadRequest as e:
                    logger.warning(f"Message edit failed: {e}")
                return

            manager = Manager.objects.get(telegram_id=str(query.from_user.id))

            client.status = 'processing'
            client.manager = manager
            client.save()

            new_text = f"✅ Accepted by: {manager.user.username}\nClient ID: {client.id}\n" + query.message.text
            try:
                query.edit_message_text(text=new_text)
            except BadRequest as e:
                logger.error(f"Failed to update message: {e}")

    except (Client.DoesNotExist, Manager.DoesNotExist):
        logger.error("Client or Manager not found")
        try:
            query.edit_message_text("❗ Error processing request")
        except BadRequest as e:
            logger.warning(f"Message edit failed: {e}")
    except Exception as e:
        logger.error(f"Unexpected error: {e}", exc_info=True)
        try:
            query.edit_message_text("❗ An error occurred, please try again.")
        except BadRequest as e:
            logger.warning(f"Message edit failed: {e}")


def error_handler(update, context):
    logger.error(msg="Telegram error encountered", exc_info=context.error)


class Command(BaseCommand):
    help = 'Run Telegram bot'

    def handle(self, *args, **options):
        updater = Updater(settings.TELEGRAM_BOT_TOKEN)
        dp = updater.dispatcher

        dp.add_handler(CallbackQueryHandler(handle_accept, pattern='^accept_'))
        dp.add_error_handler(error_handler)  # Add error handler

        self.stdout.write("Bot started")
        updater.start_polling()
        updater.idle()
