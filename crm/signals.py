from django.db.models.signals import post_save
from django.dispatch import receiver
from django.conf import settings
from telegram import Bot, InlineKeyboardButton, InlineKeyboardMarkup
from .models import Client


@receiver(post_save, sender=Client)
def notify_new_client(sender, instance, created, **kwargs):
    if created:
        bot = Bot(token=settings.TELEGRAM_BOT_TOKEN)
        keyboard = [
            [InlineKeyboardButton("✅ Принять:", callback_data=f"accept_{instance.id}")]
        ]
        message = (
            f"📌 Новая заявка!:\n"
            f"Фио: {instance.full_name}\n"
            f"Номер: {instance.phone}\n"
            f"Пакет: {instance.package}\n"
            f"Место: {instance.country}, {instance.city}"
        )
        bot.send_message(
            chat_id=settings.TELEGRAM_GROUP_CHAT_ID,
            text=message,
            reply_markup=InlineKeyboardMarkup(keyboard)
        )
