import logging

logger = logging.getLogger(__name__)

def send_sms(phone_number: str, message: str) -> bool:
    """
    SMS xizmati provayderi orqali SMS yuborish uchun placeholder funksiya.
    Hozircha faqat logga yozadi.
    Kelajakda Twilio, Vonage yoki boshqa provayder API integratsiyasi shu yerda amalga oshiriladi.
    """
    if not phone_number or not message:
        logger.error("Telefon raqami yoki xabar bo'sh bo'lishi mumkin emas.")
        return False

    # Haqiqiy SMS yuborish logikasi shu yerda bo'ladi
    # Masalan:
    # from twilio.rest import Client
    # client = Client(settings.TWILIO_ACCOUNT_SID, settings.TWILIO_AUTH_TOKEN)
    # message = client.messages.create(
    #     to=phone_number,
    #     from_=settings.TWILIO_PHONE_NUMBER,
    #     body=message
    # )
    # logger.info(f"SMS yuborildi: {message.sid}")

    logger.info(f"SMS yuborish simulyatsiyasi: '{message}' raqamiga {phone_number}")
    return True

# Celery vazifasi uchun placeholder (agar kerak bo'lsa, alohida tasks.py da bo'lishi mumkin)
# from celery import shared_task
# @shared_task
# def send_sms_async(phone_number: str, message: str):
#     send_sms(phone_number, message)
