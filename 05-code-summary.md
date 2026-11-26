## Yaratilgan fayllar
Ushbu loyiha skeleti quyidagi uchta asosiy fayldan iborat bo'lib, ular `guldokoni` loyiha papkasi ichida joylashgan:

1.  `workspace/guldokoni/app.py`: Flask ilovasining asosiy fayli. U konfiguratsiya, ma'lumotlar bazasi modeli (Order), marshrutlar (`/`, `/order`, `/success`), forma ma'lumotlarini qayta ishlash, ma'lumotlar bazasiga saqlash va elektron pochta xizmati bilan integratsiyani o'z ichiga oladi. Shuningdek, xavfsizlik bo'yicha tavsiyalar (muhit o'zgaruvchilari, CSRF himoyasi) hisobga olingan.
2.  `workspace/guldokoni/services/email_service.py`: Elektron pochta yuborish uchun alohida modul. U `send_order_email` funksiyasini taqdim etadi va SMTP sozlamalarini muhit o'zgaruvchilaridan oladi.
3.  `workspace/guldokoni/tests/test_app.py`: Ilova va elektron pochta xizmati uchun unit va integratsion testlarni o'z ichiga olgan test fayli. Flask test klienti va `unittest.mock` yordamida funksionallik tekshiriladi.

## Modul tavsifi

### `app.py`
*   **Maqsad:** Guldokoni uchun buyurtma qabul qilish veb-ilovasining asosiy logikasini boshqarish.
*   **Funksionallik:**
    *   Flask ilovasini initsializatsiya qilish va konfiguratsiya sozlamalarini (SECRET_KEY, DATABASE_URL, RECIPIENT_EMAIL) muhit o'zgaruvchilaridan yuklash.
    *   `Flask-SQLAlchemy` yordamida SQLite ma'lumotlar bazasini sozlash va `Order` modelini aniqlash. `Order` modeli `customer_name`, `customer_phone`, `delivery_address`, `order_details`, `timestamp` maydonlariga ega.
    *   `Flask-WTF` orqali CSRF himoyasini integratsiya qilish.
    *   `GET /` marshruti: Buyurtma formasini ko'rsatuvchi `index.html` shablonini render qiladi.
    *   `POST /order` marshruti: Mijoz tomonidan yuborilgan forma ma'lumotlarini qabul qiladi, server tomonida validatsiya qiladi (bo'sh maydonlar), yangi `Order` obyektini yaratib ma'lumotlar bazasiga saqlaydi. `email_service.send_order_email` funksiyasini chaqirib, guldokoni egasiga buyurtma tafsilotlarini yuboradi. Muvaffaqiyatli bo'lsa `success.html` ga yo'naltiradi, aks holda xato xabarini ko'rsatadi.
    *   `GET /success` marshruti: Buyurtma muvaffaqiyatli qabul qilinganini tasdiqlovchi `success.html` shablonini render qiladi.
*   **Integratsiya:** `email_service.py` moduli bilan, shuningdek, `templates/index.html` va `templates/success.html` shablonlari bilan ishlaydi.

### `services/email_service.py`
*   **Maqsad:** Elektron pochta xabarlarini yuborish uchun yordamchi funksiyani taqdim etish.
*   **Funksionallik:**
    *   `send_order_email(recipient, subject, body)` funksiyasi: Berilgan qabul qiluvchiga (guldokoni egasi), mavzu va tana bilan elektron pochta yuboradi. SMTP server ma'lumotlari (`SMTP_SERVER`, `SMTP_PORT`, `SMTP_USERNAME`, `SMTP_PASSWORD`, `SENDER_EMAIL`) muhit o'zgaruvchilaridan olinadi. `smtplib` modulidan foydalanadi va TLS orqali xavfsiz ulanishni ta'minlaydi. Elektron pochta yuborishdagi xatolarni (autentifikatsiya, ulanish) qayta ishlaydi.
*   **Integratsiya:** `app.py` tomonidan buyurtma qabul qilinganda chaqiriladi.

## Ishga tushirish

1.  **Loyiha papkasini yaratish:**
    `mkdir -p workspace/guldokoni/services`
    `mkdir -p workspace/guldokoni/tests`
    `mkdir -p workspace/guldokoni/templates` (HTML shablonlari uchun)
    `mkdir -p workspace/guldokoni/static/css` (CSS fayllari uchun)
    `mkdir -p workspace/guldokoni/static/js` (JavaScript fayllari uchun)

2.  **Fayllarni joylashtirish:** Yuqoridagi kodni mos fayllarga saqlang (`app.py`, `email_service.py`, `test_app.py`).

3.  **Kerakli kutubxonalarni o'rnatish:**
    `pip install Flask Flask-SQLAlchemy Flask-WTF`

4.  **Muhit o'zgaruvchilarini sozlash:** Ilovani ishga tushirishdan oldin quyidagi muhit o'zgaruvchilarini o'rnating. Bu xavfsizlik nuqtai nazaridan muhimdir.
    ```bash
    export FLASK_SECRET_KEY='sizning_maxfiy_kalitingiz_bu_juda_muhim'
    export DATABASE_URL='sqlite:///guldokoni.db'
    export RECIPIENT_EMAIL='guldokoni_egasi@example.com'
    export SMTP_SERVER='smtp.sizning_provayderingiz.com'
    export SMTP_PORT='587' # Yoki 465 SSL uchun
    export SMTP_USERNAME='sizning_smtp_foydalanuvchi_nomingiz'
    export SMTP_PASSWORD='sizning_smtp_parolingiz'
    export SENDER_EMAIL='sizning_yuboruvchi_emailingiz@example.com' # Agar SMTP_USERNAME dan farqli bo'lsa
    ```
    *Eslatma:* `FLASK_SECRET_KEY` ni ishlab chiqarishda kuchli va noyob qiymatga o'zgartiring.

5.  **Ilovani ishga tushirish:**
    `cd workspace/guldokoni`
    `python app.py`

6.  **Frontend fayllarini yaratish (qo'lda):** `templates/index.html`, `templates/success.html`, `static/css/style.css`, `static/js/script.js` fayllarini build vazifalarida ko'rsatilgan mazmun bilan yaratishingiz kerak bo'ladi. Ushbu skeletda ularning mazmuni berilmagan, faqat ularga murojaat qilingan.

## Test qilish

1.  **Test muhitini sozlash:** Testlar uchun muhit o'zgaruvchilari `test_app.py` faylida o'rnatilgan, shuning uchun ularni qo'lda sozlash shart emas.

2.  **Testlarni ishga tushirish:**
    `cd workspace/guldokoni`
    `python -m unittest tests/test_app.py`

    Bu buyruq `test_app.py` faylidagi barcha unit va integratsion testlarni ishga tushiradi. Testlar quyidagilarni tekshiradi:
    *   Asosiy sahifaning yuklanishi.
    *   Buyurtma berishning muvaffaqiyatli holati (DBga saqlash va email yuborish).
    *   Buyurtma berishda ma'lumotlar yetishmagan holat.
    *   Buyurtma berishda email yuborishdagi xatolik (DBga saqlash davom etishi).
    *   Muvaffaqiyat sahifasining yuklanishi.
    *   `email_service.py` dagi `send_order_email` funksiyasining turli holatlarda (muvaffaqiyat, autentifikatsiya xatosi, ulanish xatosi) ishlashi.

## Keyingi qadamlar

1.  **Frontendni yakunlash:** `templates/index.html`, `templates/success.html`, `static/css/style.css`, `static/js/script.js` fayllarini build vazifalarida ko'rsatilgan talablarga muvofiq to'ldirish.
2.  **Mijozga tasdiqlash xabari:** Buyurtma qabul qilingandan so'ng mijozga elektron pochta orqali tasdiqlash xabarini yuborish funksionalligini qo'shish.
3.  **Kengaytirilgan validatsiya va XSS himoyasi:** `app.py` dagi forma ma'lumotlari uchun yanada kuchliroq validatsiya qoidalarini (masalan, telefon raqami formati, `order_details` maydoni uchun XSS sanitizatsiyasi) qo'shish.
4.  **Xato boshqaruvi:** Foydalanuvchiga qulayroq xato xabarlarini ko'rsatish va ichki tizim ma'lumotlarining oshkor bo'lishini oldini olish uchun xato boshqaruvini yaxshilash.
5.  **Admin paneli:** Guldokoni egalari uchun buyurtmalarni ko'rish, filtrlash va boshqarish imkoniyatini beruvchi oddiy admin panelini yaratish.
6.  **Avtomatlashtirilgan frontend testlari:** Selenium yoki Cypress kabi vositalar yordamida frontend validatsiyasi va sahifa interfeysini avtomatlashtirilgan testlar bilan qoplash.
7.  **Ishlash (Performance) testlari:** Saytning yuklanish vaqti va elektron pochta yetkazib berish vaqti kabi qabul mezonlarini tekshirish uchun ishlash testlarini qo'shish.
8.  **Haqiqiy SMTP testlari:** Test muhitida haqiqiy SMTP serveriga ulanib, elektron pochta yuborishning integratsion testlarini o'tkazish.
9.  **Hosting va resurslar:** Loyihani joylashtirish (hosting), domen va SSL sertifikati kabi resurslarni ta'minlash va sozlash.
