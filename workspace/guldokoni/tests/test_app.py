import unittest
import os
import sys
import io
from unittest.mock import patch, MagicMock
from datetime import datetime

# Set environment variables for testing
os.environ['FLASK_SECRET_KEY'] = 'test_secret_key'
os.environ['DATABASE_URL'] = 'sqlite:///:memory:' # Use in-memory SQLite for tests
os.environ['RECIPIENT_EMAIL'] = 'test_shop_owner@example.com'
os.environ['SMTP_SERVER'] = 'smtp.test.com'
os.environ['SMTP_PORT'] = '587'
os.environ['SMTP_USERNAME'] = 'test_user'
os.environ['SMTP_PASSWORD'] = 'test_password'
os.environ['SENDER_EMAIL'] = 'test_sender@example.com'

# Import app and email_service after setting environment variables
from guldokoni.app import app, db, Order
from guldokoni.services.email_service import send_order_email

class GuldokoniAppTests(unittest.TestCase):

    def setUp(self):
        app.config['TESTING'] = True
        app.config['WTF_CSRF_ENABLED'] = False # Disable CSRF for easier testing
        self.app = app.test_client()
        with app.app_context():
            db.create_all()

    def tearDown(self):
        with app.app_context():
            db.session.remove()
            db.drop_all()

    def test_index_page(self):
        response = self.app.get('/')
        self.assertEqual(response.status_code, 200)
        self.assertIn(b'Guldokoni Buyurtma Formasi', response.data) # Check for a title or heading

    @patch('guldokoni.services.email_service.send_order_email')
    def test_place_order_success(self, mock_send_email):
        mock_send_email.return_value = True # Mock email sending to succeed

        data = {
            'customer_name': 'Ali Valiev',
            'customer_phone': '998901234567',
            'delivery_address': 'Toshkent, Mirzo Ulugbek tumani, Mustaqillik ko\'chasi 15',
            'order_details': '10 ta qizil atirgul, 5 ta oq liliya. Soat 14:00 da yetkazib berilsin.',
            'csrf_token': 'dummy' # CSRF disabled for testing, but form might expect it
        }
        response = self.app.post('/order', data=data, follow_redirects=True)
        self.assertEqual(response.status_code, 200) # Should redirect to success page
        self.assertIn(b'Buyurtmangiz muvaffaqiyatli qabul qilindi!', response.data)
        mock_send_email.assert_called_once()

        with app.app_context():
            order = Order.query.first()
            self.assertIsNotNone(order)
            self.assertEqual(order.customer_name, 'Ali Valiev')
            self.assertEqual(order.customer_phone, '998901234567')
            self.assertEqual(order.delivery_address, 'Toshkent, Mirzo Ulugbek tumani, Mustaqillik ko\'chasi 15')
            self.assertEqual(order.order_details, '10 ta qizil atirgul, 5 ta oq liliya. Soat 14:00 da yetkazib berilsin.')

    @patch('guldokoni.services.email_service.send_order_email')
    def test_place_order_missing_data(self, mock_send_email):
        data = {
            'customer_name': 'Ali Valiev',
            'customer_phone': '', # Missing phone
            'delivery_address': 'Toshkent, Mirzo Ulugbek tumani, Mustaqillik ko\'chasi 15',
            'order_details': '10 ta qizil atirgul',
            'csrf_token': 'dummy'
        }
        response = self.app.post('/order', data=data, follow_redirects=True)
        self.assertEqual(response.status_code, 200) # Should redirect back to index
        self.assertIn(b'Iltimos, barcha maydonlarni to\'ldiring.', response.data)
        mock_send_email.assert_not_called()

        with app.app_context():
            self.assertEqual(Order.query.count(), 0) # No order should be saved

    @patch('guldokoni.services.email_service.send_order_email')
    def test_place_order_email_failure(self, mock_send_email):
        mock_send_email.return_value = False # Mock email sending to fail

        data = {
            'customer_name': 'Vali Aliev',
            'customer_phone': '998912345678',
            'delivery_address': 'Samarqand, Registon ko\'chasi 1',
            'order_details': '5 ta sariq atirgul',
            'csrf_token': 'dummy'
        }
        response = self.app.post('/order', data=data, follow_redirects=True)
        self.assertEqual(response.status_code, 200)
        self.assertIn(b'Buyurtma qabul qilindi, ammo elektron pochta yuborishda xatolik yuz berdi.', response.data)
        mock_send_email.assert_called_once()

        with app.app_context():
            self.assertEqual(Order.query.count(), 1) # Order should still be saved

    def test_success_page(self):
        response = self.app.get('/success')
        self.assertEqual(response.status_code, 200)
        self.assertIn(b'Buyurtmangiz muvaffaqiyatli qabul qilindi!', response.data)

class EmailServiceTests(unittest.TestCase):

    @patch('smtplib.SMTP')
    def test_send_order_email_success(self, mock_smtp):
        # Configure mock SMTP server
        mock_instance = mock_smtp.return_value.__enter__.return_value
        mock_instance.starttls.return_value = None
        mock_instance.login.return_value = None
        mock_instance.send_message.return_value = {}

        recipient = 'test@example.com'
        subject = 'Test Subject'
        body = 'Test Body'

        result = send_order_email(recipient, subject, body)
        self.assertTrue(result)
        mock_smtp.assert_called_once_with('smtp.test.com', 587)
        mock_instance.starttls.assert_called_once()
        mock_instance.login.assert_called_once_with('test_user', 'test_password')
        mock_instance.send_message.assert_called_once()

    @patch('smtplib.SMTP')
    def test_send_order_email_auth_failure(self, mock_smtp):
        mock_instance = mock_smtp.return_value.__enter__.return_value
        mock_instance.starttls.return_value = None
        mock_instance.login.side_effect = smtplib.SMTPAuthenticationError(535, 'Authentication failed')

        result = send_order_email('test@example.com', 'Test Subject', 'Test Body')
        self.assertFalse(result)
        self.assertIn("SMTP autentifikatsiya xatosi", self.captured_output.getvalue())

    @patch('smtplib.SMTP')
    def test_send_order_email_connection_failure(self, mock_smtp):
        mock_smtp.side_effect = smtplib.SMTPConnectError(10061, 'Connection refused')

        result = send_order_email('test@example.com', 'Test Subject', 'Test Body')
        self.assertFalse(result)
        self.assertIn("SMTP serverga ulanishda xatolik", self.captured_output.getvalue())

    def setUp(self):
        # Capture print output for error messages
        self.held, self.captured_output = sys.stdout, io.StringIO()
        sys.stdout = self.captured_output

    def tearDown(self):
        sys.stdout = self.held # Restore stdout

if __name__ == '__main__':
    unittest.main()
