from django.test import TestCase
from unittest.mock import patch
from .services import send_sms

class SMSServiceTests(TestCase):
    def test_send_sms_success(self):
        """
        SMS yuborish funksiyasining muvaffaqiyatli ishlashini tekshirish.
        """
        phone_number = "+998901234567"
        message = "Salom, bu test xabari!"
        
        # Log yozishni mock qilish, haqiqiy SMS yuborish yo'qligi sababli
        with patch('sms_notifications.services.logger.info') as mock_logger_info:
            result = send_sms(phone_number, message)
            self.assertTrue(result)
            mock_logger_info.assert_called_with(f"SMS yuborish simulyatsiyasi: '{message}' raqamiga {phone_number}")

    def test_send_sms_empty_phone_number(self):
        """
        Bo'sh telefon raqami bilan SMS yuborishda xatolikni tekshirish.
        """
        phone_number = ""
        message = "Salom, bu test xabari!"
        
        with patch('sms_notifications.services.logger.error') as mock_logger_error:
            result = send_sms(phone_number, message)
            self.assertFalse(result)
            mock_logger_error.assert_called_with("Telefon raqami yoki xabar bo'sh bo'lishi mumkin emas.")

    def test_send_sms_empty_message(self):
        """
        Bo'sh xabar bilan SMS yuborishda xatolikni tekshirish.
        """
        phone_number = "+998901234567"
        message = ""
        
        with patch('sms_notifications.services.logger.error') as mock_logger_error:
            result = send_sms(phone_number, message)
            self.assertFalse(result)
            mock_logger_error.assert_called_with("Telefon raqami yoki xabar bo'sh bo'lishi mumkin emas.")

    def test_send_sms_none_inputs(self):
        """
        None qiymatlari bilan SMS yuborishda xatolikni tekshirish.
        """
        with patch('sms_notifications.services.logger.error') as mock_logger_error:
            result_phone = send_sms(None, "Test")
            self.assertFalse(result_phone)
            mock_logger_error.assert_called_with("Telefon raqami yoki xabar bo'sh bo'lishi mumkin emas.")
            
            mock_logger_error.reset_mock() # Reset mock for the next call
            result_message = send_sms("+998901234567", None)
            self.assertFalse(result_message)
            mock_logger_error.assert_called_with("Telefon raqami yoki xabar bo'sh bo'lishi mumkin emas.")
