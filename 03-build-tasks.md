## Loyiha skeleti
*   `guldokoni/` asosiy loyiha papkasini yaratish.
*   `app.py`, `config.py`, `models.py` asosiy Python fayllarini yaratish.
*   `services/`, `static/`, `templates/`, `tests/` papkalarini yaratish.
*   `services/` ichida `email_service.py` faylini yaratish.
*   `static/css/style.css` va `static/js/script.js` fayllarini yaratish.
*   `templates/index.html` va `templates/success.html` fayllarini yaratish.
*   `tests/test_app.py` va `tests/test_email_service.py` fayllarini yaratish.

## Modullar bo'yicha vazifalar
*   **`config.py`:**
    *   **Vazifa:** Flask ilovasi uchun `SECRET_KEY`, SMTP server ma'lumotlari (`SMTP_SERVER`, `SMTP_PORT`, `SMTP_USERNAME`, `SMTP_PASSWORD`) va buyurtmalar qabul qiluvchi elektron pochta manzilini (`RECIPIENT_EMAIL`) aniqlash.
    *   **Kirish:** Hech qanday.
    *   **Chiqish:** Ilova tomonidan foydalaniladigan konfiguratsiya o'zgaruvchilari.
    *   **Test:** Konfiguratsiya o'zgaruvchilari to'g'ri yuklanganligini va mavjudligini tekshirish.
*   **`models.py`:**
    *   **Vazifa:** SQLite ma'lumotlar bazasi uchun `Order` modelini (SQLAlchemy yordamida) yaratish. Model `id`, `customer_name`, `customer_phone`, `delivery_address`, `order_details`, `timestamp` maydonlariga ega bo'lishi kerak.
    *   **Kirish:** Hech qanday.
    *   **Chiqish:** Ma'lumotlar bazasi bilan o'zaro aloqa qilish uchun `Order` klassi.
    *   **Test:** `Order` obyektini yaratish, saqlash va ma'lumotlar bazasidan o'qish funksionalligini tekshirish.
*   **`services/email_service.py`:**
    *   **Vazifa:** `send_order_email(recipient, subject, body)` funksiyasini amalga oshirish. Bu funksiya `config.py` dagi SMTP ma'lumotlari yordamida elektron pochta xabarini yuborishi kerak.
    *   **Kirish:** `recipient` (String), `subject` (String), `body` (String).
    *   **Chiqish:** Elektron pochta muvaffaqiyatli yuborilgan bo'lsa `True`, aks holda `False` (yoki xato obyektini qaytarish).
    *   **Test:** Mock SMTP server yordamida elektron pochta yuborish jarayonini va xato holatlarini testlash.
*   **`static/css/style.css`:**
    *   **Vazifa:** `index.html` va `success.html` sahifalari uchun asosiy stil qoidalarini (masalan, forma elementlari, tugmalar, sahifa joylashuvi) yozish.
    *   **Kirish:** Hech qanday.
    *   **Chiqish:** Veb-sahifalarning vizual ko'rinishini belgilovchi CSS qoidalari.
    *   **Test:** Sahifalarning brauzerda to'g'ri ko'rsatilishini vizual tekshirish.
*   **`static/js/script.js`:**
    *   **Vazifa:** Buyurtma formasini yuborishdan oldin frontend validatsiyasini amalga oshirish (masalan, barcha majburiy maydonlar to'ldirilganligini tekshirish).
    *   **Kirish:** Forma yuborish hodisasi.
    *   **Chiqish:** Agar validatsiya muvaffaqiyatli bo'lsa, formani yuborishga ruxsat berish; aks holda foydalanuvchiga xato xabarini ko'rsatish.
    *   **Test:** Forma maydonlarini bo'sh qoldirib yoki noto'g'ri ma'lumot kiritib, validatsiyaning ishlashini brauzerda tekshirish.
*   **`templates/index.html`:**
    *   **Vazifa:** Mijozlar uchun buyurtma formasini o'z ichiga olgan asosiy HTML sahifasini yaratish. Forma `customer_name`, `customer_phone`, `delivery_address` (input) va `order_details` (textarea) maydonlariga ega bo'lishi kerak.
    *   **Kirish:** Hech qanday.
    *   **Chiqish:** Mijozga ko'rsatiladigan HTML sahifa.
    *   **Test:** Barcha kerakli forma maydonlari va "Yuborish" tugmasi mavjudligini va to'g'ri joylashganligini tekshirish.
*   **`templates/success.html`:**
    *   **Vazifa:** Buyurtma muvaffaqiyatli yuborilganidan keyin foydalanuvchiga ko'rsatiladigan tasdiqlash sahifasini yaratish.
    *   **Kirish:** Hech qanday.
    *   **Chiqish:** Tasdiqlovchi xabar bilan HTML sahifa.
    *   **Test:** Sahifaning to'g'ri yuklanishini va tasdiqlovchi xabarni ko'rsatishini tekshirish.
*   **`app.py`:**
    *   **Vazifa:** Flask ilovasini initsializatsiya qilish, marshrutlarni (`/` va `/order`) aniqlash, forma ma'lumotlarini qayta ishlash, ma'lumotlar bazasi va elektron pochta xizmati bilan integratsiya qilish.
    *   **Kirish:** HTTP so'rovlari.
    *   **Chiqish:** HTTP javoblari (HTML sahifalar, yo'naltirishlar).
    *   **Test:** `/` va `/order` marshrutlarining to'g'ri ishlashini, forma ma'lumotlarini qayta ishlashni va javoblarni tekshirish.

## Ma'lumotlar bazasi modeli
*   `models.py` faylida `SQLAlchemy` kutubxonasidan foydalanib, `Order` nomli ma'lumotlar bazasi modelini aniqlash.
*   `Order` modeliga quyidagi ustunlarni qo'shish: `id` (Integer, Primary Key), `customer_name` (String, Not Null), `customer_phone` (String, Not Null), `delivery_address` (String, Not Null), `order_details` (Text, Not Null), `timestamp` (DateTime, default=datetime.utcnow).
*   `app.py` faylida `SQLAlchemy` obyektini initsializatsiya qilish va ilova kontekstida ma'lumotlar bazasi jadvallarini yaratish funksiyasini (masalan, `db.create_all()`) qo'shish.

## API yaratish
*   `app.py` faylida `POST` metodi uchun `/order` marshrutini yaratish.
*   Marshrut ichida `request.form` orqali mijoz tomonidan yuborilgan `customer_name`, `customer_phone`, `delivery_address`, `order_details` ma'lumotlarini qabul qilish.
*   Qabul qilingan ma'lumotlarni backendda validatsiya qilish (masalan, barcha maydonlar to'ldirilganligini va telefon raqami formatini tekshirish). Agar validatsiya muvaffaqiyatsiz bo'lsa, 400 Bad Request javobini qaytarish.
*   Validatsiyadan o'tgan ma'lumotlar asosida `Order` modelining yangi obyektini yaratish va uni SQLite ma'lumotlar bazasiga saqlash.
*   `services/email_service.py` modulidagi `send_order_email` funksiyasini chaqirib, guldokoni egasiga buyurtma tafsilotlarini elektron pochta orqali yuborish.
*   Buyurtma muvaffaqiyatli qabul qilinganidan va elektron pochta yuborilganidan so'ng, `success.html` shablonini render qilish yoki unga yo'naltirish.

## Interfeys yaratish
*   `templates/index.html` faylida `form` tegini yaratish, `action="/order"` va `method="POST"` atributlarini belgilash.
*   Forma ichida `label` va `input` teglaridan foydalanib, `customer_name`, `customer_phone`, `delivery_address` uchun matn kiritish maydonlarini, `order_details` uchun esa `textarea` maydonini yaratish.
*   Formaga "Buyurtma berish" tugmasini qo'shish.
*   `static/css/style.css` faylida forma elementlari, tugmalar va sahifaning umumiy joylashuvi uchun stil qoidalarini yozish (masalan, ranglar, shriftlar, padding, margin).
*   `static/js/script.js` faylida forma yuborilishini ushlab turuvchi va maydonlarning bo'sh emasligini tekshiruvchi JavaScript kodini yozish. Agar maydonlar bo'sh bo'lsa, foydalanuvchiga ogohlantirish ko'rsatish.
*   `templates/success.html` faylida "Buyurtmangiz muvaffaqiyatli qabul qilindi!" kabi tasdiqlovchi xabar va bosh sahifaga qaytish tugmasini joylashtirish.

## Testlar
*   **Unit testlar (`tests/test_email_service.py`):**
    *   `send_order_email` funksiyasini mock SMTP server yordamida testlash. Funksiya to'g'ri chaqirilganligini, mavzu va tana ma'lumotlari to'g'ri uzatilganligini tekshirish.
    *   SMTP serveriga ulanishdagi xatolar yoki autentifikatsiya muammolari kabi salbiy holatlarni testlash.
*   **Unit testlar (`tests/test_models.py` yoki `test_app.py` ichida):**
    *   `Order` modelining obyektini yaratish va uning maydonlariga qiymatlarni to'g'ri tayinlashni tekshirish.
    *   Test ma'lumotlar bazasiga `Order` obyektini saqlash va uni qayta o'qish orqali ma'lumotlar bazasi operatsiyalarini tekshirish.
*   **Integratsion testlar (`tests/test_app.py`):**
    *   Flask test klienti yordamida `GET /` marshrutiga so'rov yuborish va `index.html` shablonining muvaffaqiyatli render qilinganligini tekshirish.
    *   `POST /order` endpointiga to'g'ri forma ma'lumotlari bilan so'rov yuborish va 302 (yo'naltirish) yoki 200 OK (success.html) javobini kutish.
    *   `POST /order` endpointiga noto'g'ri (masalan, bo'sh maydonlar) forma ma'lumotlari bilan so'rov yuborish va 400 Bad Request javobini kutish.
    *   `POST /order` so'rovi bajarilganda `email_service.send_order_email` funksiyasi chaqirilganligini va `Order` obyektining ma'lumotlar bazasiga saqlanganligini mocklar yordamida tekshirish.

## Integratsiya ishlari
*   `app.py` faylida `config.py` dan konfiguratsiya ma'lumotlarini import qilish va Flask ilovasiga yuklash.
*   `app.py` faylida `models.py` dagi `Order` modelini va `services/email_service.py` dagi `send_order_email` funksiyasini import qilish.
*   `app.py` dagi `POST /order` marshrutida `Order` modelini ma'lumotlar bazasiga yozish va `send_order_email` funksiyasini chaqirish.
*   `templates/index.html` faylida `static/css/style.css` va `static/js/script.js` fayllarini to'g'ri ulash.
*   Flask ilovasini ishga tushirish uchun `app.py` faylida `if __name__ == '__main__': app.run()` blokini qo'shish.

## Bajarish ketma-ketligi
1.  **Loyiha skeletini yaratish:** Barcha papkalar va asosiy fayllarni tuzish.
2.  **Konfiguratsiya faylini yaratish:** `config.py` faylida barcha kerakli sozlamalarni aniqlash.
3.  **Ma'lumotlar bazasi modelini yaratish:** `models.py` da `Order` modelini aniqlash va `app.py` da DB initsializatsiyasini sozlash.
4.  **Elektron pochta xizmatini yaratish:** `services/email_service.py` da `send_order_email` funksiyasini yozish.
5.  **Asosiy Flask ilovasini sozlash:** `app.py` da Flask ilovasini initsializatsiya qilish va `/` marshrutini yaratish.
6.  **Frontend sahifalarini yaratish:** `templates/index.html` va `templates/success.html` ni yaratish.
7.  **Frontend stil va skriptlarini yaratish:** `static/css/style.css` va `static/js/script.js` ni yozish.
8.  **API endpointini yaratish:** `app.py` da `POST /order` marshrutini amalga oshirish (validatsiya, DBga saqlash, email yuborish).
9.  **Unit testlarni yozish:** `test_email_service.py` va `test_app.py` (model testlari bilan) uchun testlarni yozish.
10. **Integratsion testlarni yozish:** `test_app.py` da API endpointi uchun testlarni yozish.
11. **Ilovani lokal ishga tushirish va qo'lda testlash:** Barcha funksionallikni brauzer orqali tekshirish.