import os
from datetime import datetime
from flask import Flask, render_template, request, redirect, url_for, flash
from flask_sqlalchemy import SQLAlchemy
from flask_wtf.csrf import CSRFProtect # For CSRF protection

# Import email service
from guldokoni.services.email_service import send_order_email

app = Flask(__name__)

# Configuration (using environment variables as per review)
app.config['SECRET_KEY'] = os.getenv('FLASK_SECRET_KEY', 'a_very_secret_key_for_dev_only') # CHANGE THIS IN PRODUCTION
app.config['SQLALCHEMY_DATABASE_URI'] = os.getenv('DATABASE_URL', 'sqlite:///guldokoni.db')
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

# Email configuration (for the shop owner)
app.config['RECIPIENT_EMAIL'] = os.getenv('RECIPIENT_EMAIL', 'shop_owner@example.com')

db = SQLAlchemy(app)
csrf = CSRFProtect(app) # Initialize CSRF protection

# Order Model
class Order(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    customer_name = db.Column(db.String(100), nullable=False)
    customer_phone = db.Column(db.String(20), nullable=False)
    delivery_address = db.Column(db.String(200), nullable=False)
    order_details = db.Column(db.Text, nullable=False)
    timestamp = db.Column(db.DateTime, default=datetime.utcnow)

    def __repr__(self):
        return f'<Order {self.id} - {self.customer_name}>'

# Create database tables if they don't exist
with app.app_context():
    db.create_all()

@app.route('/')
def index():
    # TODO: Render index.html with CSRF token
    return render_template('index.html')

@app.route('/order', methods=['POST'])
def place_order():
    if not request.form:
        flash('Form data is missing.', 'error')
        return redirect(url_for('index'))

    customer_name = request.form.get('customer_name')
    customer_phone = request.form.get('customer_phone')
    delivery_address = request.form.get('delivery_address')
    order_details = request.form.get('order_details')

    # Basic server-side validation
    if not all([customer_name, customer_phone, delivery_address, order_details]):
        flash('Iltimos, barcha maydonlarni to\'ldiring.', 'error')
        return redirect(url_for('index'))

    # TODO: Add more robust validation (e.g., phone number format)
    # TODO: Add XSS sanitization for user-provided input, especially order_details
    # Example for XSS protection:
    # from markupsafe import escape
    # order_details = str(escape(order_details))

    try:
        new_order = Order(
            customer_name=customer_name,
            customer_phone=customer_phone,
            delivery_address=delivery_address,
            order_details=order_details
        )
        db.session.add(new_order)
        db.session.commit()

        # Send email to shop owner
        subject = f"Yangi buyurtma: {customer_name}"
        body = (
            f"Mijoz ismi: {customer_name}\n"
            f"Telefon: {customer_phone}\n"
            f"Manzil: {delivery_address}\n"
            f"Buyurtma tafsilotlari:\n{order_details}\n"
            f"Buyurtma vaqti: {new_order.timestamp}"
        )
        
        email_sent = send_order_email(app.config['RECIPIENT_EMAIL'], subject, body)
        
        if not email_sent:
            # Log this error, but still show success to user if DB save was successful
            print(f"ERROR: Email could not be sent to {app.config['RECIPIENT_EMAIL']}")
            flash('Buyurtma qabul qilindi, ammo elektron pochta yuborishda xatolik yuz berdi.', 'warning')
        else:
            flash('Buyurtmangiz muvaffaqiyatli qabul qilindi!', 'success')

        # TODO: Add functionality to send confirmation email to customer (as per review)
        # if customer_email:
        #     send_order_email(customer_email, "Buyurtmangiz tasdiqlandi", "Tafsilotlar...")

        return redirect(url_for('success'))

    except Exception as e:
        db.session.rollback()
        print(f"Error placing order: {e}")
        flash('Buyurtma berishda xatolik yuz berdi. Iltimos, qayta urinib ko\'ring.', 'error')
        return redirect(url_for('index'))

@app.route('/success')
def success():
    return render_template('success.html')

if __name__ == '__main__':
    # For development, set environment variables like:
    # export FLASK_SECRET_KEY='your_dev_secret_key'
    # export DATABASE_URL='sqlite:///guldokoni.db'
    # export RECIPIENT_EMAIL='your_shop_email@example.com'
    # export SMTP_SERVER='smtp.example.com'
    # export SMTP_PORT='587'
    # export SMTP_USERNAME='your_smtp_username'
    # export SMTP_PASSWORD='your_smtp_password'
    # export SENDER_EMAIL='your_sender_email@example.com'
    app.run(debug=True)
