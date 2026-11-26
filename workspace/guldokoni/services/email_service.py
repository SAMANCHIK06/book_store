import smtplib
from email.mime.text import MIMEText
import os

def send_order_email(recipient, subject, body):
    """
    Guldokoni egasiga buyurtma tafsilotlari bilan elektron pochta yuboradi.
    Konfiguratsiya ma'lumotlari muhit o'zgaruvchilaridan olinadi.
    """
    smtp_server = os.getenv('SMTP_SERVER')
    smtp_port = int(os.getenv('SMTP_PORT', 587)) # Default to 587 if not set
    smtp_username = os.getenv('SMTP_USERNAME')
    smtp_password = os.getenv('SMTP_PASSWORD')
    sender_email = os.getenv('SENDER_EMAIL', smtp_username) # Use username as sender if not specified

    if not all([smtp_server, smtp_username, smtp_password, sender_email]):
        print("ERROR: SMTP konfiguratsiya ma'lumotlari to'liq emas. Elektron pochta yuborilmadi.")
        return False

    msg = MIMEText(body, 'plain', 'utf-8')
    msg['Subject'] = subject
    msg['From'] = sender_email
    msg['To'] = recipient

    try:
        with smtplib.SMTP(smtp_server, smtp_port) as server:
            server.starttls()  # Secure the connection
            server.login(smtp_username, smtp_password)
            server.send_message(msg)
        return True
    except smtplib.SMTPAuthenticationError:
        print("ERROR: SMTP autentifikatsiya xatosi. Foydalanuvchi nomi yoki parol noto'g'ri.")
        return False
    except smtplib.SMTPConnectError:
        print(f"ERROR: SMTP serverga ulanishda xatolik: {smtp_server}:{smtp_port}")
        return False
    except Exception as e:
        print(f"ERROR: Elektron pochta yuborishda kutilmagan xatolik: {e}")
        return False
