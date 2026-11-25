## Yaratilgan fayllar
Ushbu kod skeleti `dokon` loyihasining `sms_notifications` moduli uchun asosiy tuzilmani taqdim etadi. Jami 3 ta fayl yaratildi:

1.  `workspace/dokon_backend/dokon_backend/settings.py`: Django loyihasining asosiy sozlamalar fayli. `sms_notifications` ilovasi `INSTALLED_APPS` ro'yxatiga qo'shilgan.
2.  `workspace/dokon_backend/sms_notifications/services.py`: SMS yuborish logikasini o'z ichiga olgan asosiy modul fayli. Hozircha SMS yuborish jarayonini simulyatsiya qiladi va loglarga yozadi.
3.  `workspace/dokon_backend/sms_notifications/tests.py`: `sms_notifications/services.py` faylidagi `send_sms` funksiyasi uchun unit testlarni o'z ichiga oladi.

## Modul tavsifi
`sms_notifications` moduli foydalanuvchilarga SMS xabarnomalar yuborish uchun mo'ljallangan.
*   **`services.py`**: Bu fayl SMS provayder (masalan, Twilio, Vonage) bilan aloqa qilish uchun asosiy funksiyalarni o'z ichiga oladi. `send_sms` funksiyasi telefon raqami va xabar matnini qabul qilib, SMS yuborish jarayonini boshlaydi. Hozirda u faqat logga yozish orqali simulyatsiya qilinadi.
*   **`tests.py`**: `services.py` dagi `send_sms` funksiyasining turli holatlarda (muvaffaqiyatli yuborish, bo'sh raqam/xabar) to'g'ri ishlashini tekshiruvchi testlarni o'z ichiga oladi.

## Ishga tushirish
Ushbu skeletni ishga tushirish uchun quyidagi qadamlarni bajarishingiz kerak:

1.  **Django loyihasini sozlash:**
    *   `workspace/dokon_backend/` papkasiga o'ting.
    *   Virtual muhit yarating va faollashtiring:
        ```bash
        python -m venv venv
        source venv/bin/activate # Linux/macOS
        # venv\Scripts\activate # Windows
        ```
    *   Kerakli kutubxonalarni o'rnating (Django):
        ```bash
        pip install Django
        ```
    *   Ma'lumotlar bazasi migratsiyalarini bajaring:
        ```bash
        python manage.py migrate
        ```
    *   Django rivojlanish serverini ishga tushiring:
        ```bash
        python manage.py runserver
        ```
    *   Brauzeringizda `http://127.0.0.1:8000/` manziliga kirib, Django loyihasining muvaffaqiyatli ishga tushganligini tekshiring.

## Test qilish
Yaratilgan unit testlarni bajarish uchun:

1.  `workspace/dokon_backend/` papkasida ekanligingizga ishonch hosil qiling.
2.  Quyidagi buyruqni bajaring:
    ```bash
    python manage.py test sms_notifications
    ```
    Barcha testlar muvaffaqiyatli o'tishi kerak.

## Keyingi qadamlar
1.  **Haqiqiy SMS provayder integratsiyasi:** `sms_notifications/services.py` faylidagi `send_sms` funksiyasini Twilio, Vonage yoki boshqa tanlangan SMS provayderining API chaqiruvlari bilan almashtiring. Provayder API kalitlarini `dokon_backend/settings.py` faylida yoki muhit o'zgaruvchilari orqali xavfsiz tarzda saqlashni unutmang.
2.  **Celery integratsiyasi:** Asinxron SMS yuborish uchun Celery va Redisni sozlang. `dokon_backend/settings.py` faylidagi Celery konfiguratsiyasini faollashtiring va `sms_notifications/tasks.py` faylini yaratib, `send_sms` funksiyasini Celery vazifasi sifatida belgilang.
3.  **Boshqa modullarni yaratish:** `users`, `products`, `orders` kabi boshqa Django ilovalarini yaratish va ularning modellarini, serializerlarini, viewlarini va URL konfiguratsiyalarini implementatsiya qilishni davom ettiring.
4.  **API endpointlarini yaratish:** `users`, `products`, `orders` ilovalari uchun RESTful API endpointlarini Django REST Framework yordamida yarating.
5.  **Frontend loyihasini boshlash:** `dokon-frontend` React loyihasini `create-react-app` yordamida yaratib, backend API bilan aloqa qilish uchun UI komponentlari va sahifalarini ishlab chiqing.