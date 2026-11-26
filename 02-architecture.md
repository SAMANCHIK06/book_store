## Texnologiya tanlovi
*   **Backend:** Python 3.x va Flask veb-freymvorki. Bu yechim "byudjet mavjud emas" chekloviga mos keladi, chunki Flask yengil, tez o'rganiladigan va kichik loyihalar uchun ideal.
*   **Frontend:** HTML5, CSS3 va minimal JavaScript. Interaktivlik va formani validatsiya qilish uchun zarur bo'lgan JavaScript kodlari yoziladi.
*   **Ma'lumotlar bazasi:** SQLite. Bu faylga asoslangan ma'lumotlar bazasi bo'lib, o'rnatish va boshqarish uchun hech qanday qo'shimcha server talab qilmaydi, bu esa "byudjet mavjud emas" talabiga to'liq javob beradi.
*   **Elektron pochta xizmati:** Pythonning `smtplib` moduli. Bu modul SMTP protokoli orqali elektron pochta xabarlarini yuborish imkonini beradi va tashqi kutubxonalarga bog'liqlikni kamaytiradi.

## Papkalar va modullar tuzilmasi
*   **`guldokoni/` (Loyihaning asosiy papkasi):**
    *   `app.py`: Flask ilovasining asosiy fayli, marshrutlar (routes) va ilova konfiguratsiyasini o'z ichiga oladi.
    *   `config.py`: Ilova sozlamalari, masalan, SMTP server ma'lumotlari, elektron pochta manzillari va maxfiy kalitlar saqlanadi.
    *   `models.py`: Ma'lumotlar bazasi modellari (masalan, `Order` modeli) shu yerda aniqlanadi.
    *   `services/`: Tashqi xizmatlar bilan ishlash uchun modullar.
        *   `email_service.py`: Elektron pochta xabarlarini yuborish logikasi joylashgan modul.
    *   `static/`: Frontend resurslari (CSS, JavaScript, rasmlar).
        *   `css/style.css`: Saytning asosiy stil fayli.
        *   `js/script.js`: Frontend validatsiyasi va interaktivlik uchun JavaScript.
    *   `templates/`: HTML shablonlari.
        *   `index.html`: Asosiy buyurtma formasi joylashgan sahifa.
        *   `success.html`: Buyurtma muvaffaqiyatli yuborilganidan keyin ko'rsatiladigan sahifa.
    *   `tests/`: Test fayllari.
        *   `test_app.py`: Ilova marshrutlari va asosiy funksiyalar uchun testlar.
        *   `test_email_service.py`: Elektron pochta yuborish xizmati uchun testlar.

## API endpointlar
*   **`POST /order`:** Mijoz tomonidan to'ldirilgan buyurtma formasini qabul qilish uchun asosiy va yagona API endpoint.
    *   **Maqsad:** Mijozdan buyurtma ma'lumotlarini qabul qilish, ularni qayta ishlash va guldokoni egasiga elektron pochta orqali yuborish.
    *   **Kirish ma'lumotlari (Request Body):** `application/x-www-form-urlencoded` yoki `application/json` formatida quyidagi maydonlarni qabul qiladi: `customer_name`, `customer_phone`, `delivery_address`, `order_details`.
    *   **Chiqish ma'lumotlari (Response):** Muvaffaqiyatli yuborilgan taqdirda 200 OK statusi va tasdiqlovchi xabar (masalan, `{"message": "Buyurtmangiz qabul qilindi!"}`). Xatolik yuz berganda esa 400 Bad Request yoki 500 Internal Server Error statusi va xato xabari.

## Autentifikatsiya
*   **Mijozlar uchun:** 1-versiyada mijozlar uchun hech qanday autentifikatsiya talab qilinmaydi. Ular to'g'ridan-to'g'ri buyurtma formasini to'ldirib, yuborishlari mumkin.
*   **Guldokoni egalari uchun:** 1-versiyada guldokoni egalari uchun ham saytda maxsus admin paneli yoki autentifikatsiya mexanizmi mavjud emas. Buyurtmalar faqat elektron pochta orqali yuboriladi.
*   **Kelajakda (agar talab etilsa):** Agar kelajakda guldokoni egalari uchun buyurtmalarni saytda ko'rish yoki boshqarish paneli qo'shiladigan bo'lsa, u holda Flask-Login kabi kutubxonalar yordamida foydalanuvchi nomi/parolga asoslangan oddiy autentifikatsiya joriy etilishi mumkin.

## Ma'lumotlar oqimi
*   **1. Mijoz buyurtma formasini to'ldiradi:** Mijoz `index.html` sahifasidagi formaga ism, telefon, manzil va buyurtma tafsilotlarini kiritadi.
*   **2. Frontend ma'lumotlarni yuboradi:** Mijoz "Yuborish" tugmasini bosganda, JavaScript yordamida yoki to'g'ridan-to'g'ri HTML formasi orqali ma'lumotlar `POST /order` endpointiga yuboriladi.
*   **3. Backend ma'lumotlarni qabul qiladi va qayta ishlaydi:** Flask ilovasi `POST /order` so'rovini qabul qiladi. Kiritilgan ma'lumotlar validatsiya qilinadi (bo'sh maydonlar, telefon raqami formati).
*   **4. Backend elektron pochta yuboradi:** Validatsiyadan o'tgan ma'lumotlar `email_service.py` moduli orqali guldokoni egasining belgilangan elektron pochta manziliga yuboriladi.
*   **5. Backend ma'lumotlarni saqlaydi:** Buyurtma ma'lumotlari `models.py` orqali SQLite ma'lumotlar bazasiga saqlanadi. Bu kelajakda buyurtmalarni boshqarish uchun zamin yaratadi.
*   **6. Backend javob qaytaradi:** Elektron pochta muvaffaqiyatli yuborilganidan va ma'lumotlar saqlanganidan so'ng, backend frontendga muvaffaqiyatli javob (masalan, `success.html` sahifasiga yo'naltirish yoki JSON xabari) yuboradi.
*   **7. Frontend javobni ko'rsatadi:** Mijozga buyurtma muvaffaqiyatli qabul qilinganligi haqida xabar ko'rsatiladi.

## Xavfsizlik qoidalari
*   **Kiritilgan ma'lumotlarni validatsiya qilish:** Barcha kiruvchi ma'lumotlar (ism, telefon, manzil, buyurtma tafsilotlari) backendda to'g'ri formatda ekanligi va xavfli belgilar (masalan, XSS hujumlari uchun skriptlar) yo'qligi tekshiriladi.
*   **CSRF himoyasi:** Agar HTML formasi ishlatilsa, Flask-WTF kabi kutubxonalar yordamida CSRF (Cross-Site Request Forgery) tokenlari qo'llaniladi. Bu ruxsatsiz saytlardan keladigan so'rovlarning oldini oladi.
*   **Elektron pochta xavfsizligi:** SMTP serveriga ulanishda TLS/SSL shifrlashidan foydalaniladi. SMTP autentifikatsiya ma'lumotlari (foydalanuvchi nomi va parol) `config.py` faylida saqlanadi va versiya nazorati tizimiga (Git) to'g'ridan-to'g'ri joylashtirilmaydi (masalan, muhit o'zgaruvchilari orqali yuklanadi).
*   **Xato boshqaruvi:** Ilovada yuzaga kelishi mumkin bo'lgan xatolar (masalan, SMTP serveriga ulanishdagi muammolar, ma'lumotlar bazasiga yozishdagi xatolar) to'g'ri qayta ishlanadi va foydalanuvchiga umumiy xato xabarlari ko'rsatiladi, ichki tizim ma'lumotlari oshkor etilmaydi.

## Test strategiyasi
*   **Unit testlar:**
    *   `email_service.py` modulidagi elektron pochta yuborish funksiyasini izolyatsiya qilingan holda testlash. Mock obyektlar yordamida SMTP serveriga haqiqiy ulanishlarsiz testlar o'tkaziladi.
    *   `models.py` dagi ma'lumotlar bazasi modellari va ularning ishlashi testlanadi.
    *   Forma validatsiyasi logikasi alohida testlanadi.
*   **Integratsion testlar:**
    *   Flask ilovasining `POST /order` endpointiga so'rov yuborish va uning javobini tekshirish. Bu testda backendning barcha qismlari (validatsiya, elektron pochta yuborish, ma'lumotlar bazasiga yozish) birgalikda ishlayotganligi tekshiriladi.
    *   Elektron pochta xizmatining haqiqiy SMTP serveriga ulanib, test xabarini yuborish va uning yetib borishini tasdiqlash (faqat test muhitida).
*   **Frontend testlar:**
    *   HTML formasining to'g'ri ko'rsatilishini va maydonlarning mavjudligini vizual tekshirish.
    *   Minimal JavaScript validatsiyasining to'g'ri ishlashini brauzerda qo'lda tekshirish.

## Deploy uchun talablar
*   **Python muhiti:** Serverda Python 3.x o'rnatilgan bo'lishi va loyiha uchun virtual muhit yaratilishi kerak.
*   **Veb-server:** Flask ilovasini ishga tushirish uchun Gunicorn yoki uWSGI kabi WSGI serveri talab qilinadi. Bu server ilovani bir vaqtning o'zida bir nechta so'rovlarni qayta ishlashga imkon beradi.
*   **Proksi-server:** Nginx yoki Apache kabi proksi-server WSGI serveri oldida joylashadi. U statik fayllarni (CSS, JS) taqdim etadi, SSL/TLS shifrlashini boshqaradi va kiruvchi so'rovlarni Flask ilovasiga yo'naltiradi.
*   **SMTP serveriga kirish:** Elektron pochta xabarlarini yuborish uchun serverda tashqi SMTP serveriga (masalan, Gmail, SendGrid yoki boshqa pochta xizmati) kirish imkoniyati bo'lishi kerak. Kerakli portlar (masalan, 587 yoki 465) ochiq bo'lishi lozim.
*   **Ma'lumotlar bazasi fayli:** SQLite ma'lumotlar bazasi fayli (masalan, `instance/guldokoni.db`) ilova bilan birga joylashtiriladi va yozish uchun ruxsatlarga ega bo'lishi kerak.
*   **Muhit o'zgaruvchilari:** Maxfiy ma'lumotlar (masalan, SMTP parollari, Flask `SECRET_KEY`) `config.py` faylida to'g'ridan-to'g'ri saqlanmasdan, muhit o'zgaruvchilari orqali yuklanishi kerak.