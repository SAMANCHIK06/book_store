## Texnologiya tanlovi

*   **Backend:** Python tilida yozilgan Django veb-freymvorki, Django REST Framework (DRF) bilan birgalikda RESTful API yaratish uchun tanlanadi. Bu tez rivojlanish, keng funksionallik va katta hamjamiyat yordamini ta'minlaydi.
*   **Frontend:** React.js kutubxonasi foydalanuvchi interfeysini yaratish uchun tanlanadi. Bu komponentga asoslangan yondashuv, yuqori unumdorlik va keng ekotizimga ega bo'lib, mijoz tomonida dinamik tajribani ta'minlaydi.
*   **Ma'lumotlar bazasi:** PostgreSQL relyatsion ma'lumotlar bazasi tanlanadi. U ochiq kodli, ishonchli, kengaytiriladigan va murakkab ma'lumotlar tuzilmalari bilan ishlash uchun juda mos keladi, bu e-commerce loyihalari uchun muhimdir.
*   **SMS xizmati:** SMS yuborish uchun Twilio, Vonage (Nexmo) yoki mahalliy SMS gateway provayderlaridan biri integratsiya qilinadi. "Byudjet yo'q" cheklovi tufayli, tejamkor tariflar yoki bepul sinov imkoniyatlari mavjud provayderlar afzal ko'riladi.
*   **Asinxron vazifalar:** Celery ish navbati Redis brokeri bilan birgalikda SMS yuborish kabi fon vazifalarini asinxron tarzda bajarish uchun ishlatiladi. Bu asosiy veb-server jarayonini blokirovka qilmasdan, foydalanuvchi tajribasini yaxshilaydi.

## Papkalar va modullar tuzilmasi

*   **Monorepo/Polyrepo:** Loyiha ikkita alohida repozitoriyaga bo'linadi: `dokon-backend` (Django) va `dokon-frontend` (React). Bu har bir qismning mustaqil rivojlanishi, joylashtirilishi va masshtablanishini ta'minlaydi.
*   **`dokon-backend` (Django):**
    *   `core/`: Loyihaning umumiy sozlamalari va asosiy konfiguratsiyasi.
    *   `users/`: Foydalanuvchi autentifikatsiyasi, ro'yxatdan o'tish va profil boshqaruvi uchun ilova.
    *   `products/`: Mahsulotlar, kategoriyalar va inventar boshqaruvi uchun ilova.
    *   `orders/`: Buyurtmalar, savat va to'lov jarayonlari uchun ilova.
    *   `sms_notifications/`: SMS xizmati bilan integratsiya va xabarnomalar yuborish logikasi uchun ilova.
    *   `api/`: DRF serializerlari, viewsetlari va URL konfiguratsiyasi.
*   **`dokon-frontend` (React):**
    *   `src/components/`: Qayta ishlatiladigan UI komponentlari (tugmalar, kartochkalar, formalar).
    *   `src/pages/`: Loyihaning asosiy sahifalari (Bosh sahifa, Mahsulotlar, Savat, Buyurtmalarim, Kirish/Ro'yxatdan o'tish).
    *   `src/services/`: Backend API bilan aloqa qilish uchun funksiyalar (API chaqiruvlari).
    *   `src/context/`: Global holatni boshqarish uchun React Context API yoki Redux/Zustand kabi holat boshqaruv kutubxonalari.
    *   `src/utils/`: Umumiy yordamchi funksiyalar va konstantalar.

## API endpointlar

*   **Autentifikatsiya va foydalanuvchi boshqaruvi:**
    *   `POST /api/auth/register/`: Yangi foydalanuvchini ro'yxatdan o'tkazish.
    *   `POST /api/auth/login/`: Foydalanuvchi tizimga kirishi va JWT tokenlarini olish.
    *   `POST /api/auth/token/refresh/`: Yangi kirish tokenini olish uchun yangilash tokenidan foydalanish.
    *   `GET /api/users/me/`: Joriy foydalanuvchi profil ma'lumotlarini olish.
*   **Mahsulotlar:**
    *   `GET /api/products/`: Barcha mahsulotlar ro'yxatini olish.
    *   `GET /api/products/{id}/`: Muayyan mahsulot ma'lumotlarini olish.
    *   `GET /api/categories/`: Mahsulot kategoriyalari ro'yxatini olish.
*   **Savat va buyurtmalar:**
    *   `GET /api/cart/`: Joriy foydalanuvchi savatining tarkibini olish.
    *   `POST /api/cart/items/`: Savatga mahsulot qo'shish.
    *   `PUT /api/cart/items/{id}/`: Savatdagi mahsulot miqdorini yangilash.
    *   `DELETE /api/cart/items/{id}/`: Savatdan mahsulotni olib tashlash.
    *   `POST /api/orders/`: Yangi buyurtma yaratish (savat asosida).
    *   `GET /api/orders/`: Joriy foydalanuvchining barcha buyurtmalari ro'yxatini olish.
    *   `GET /api/orders/{id}/`: Muayyan buyurtma ma'lumotlarini olish.
*   **SMS xabarnomalari (ichki API):**
    *   `POST /api/sms/send-otp/`: Foydalanuvchi raqamiga OTP yuborish (agar autentifikatsiyada ishlatilsa).
    *   `POST /api/orders/{id}/send-confirmation-sms/`: Buyurtma tasdiqlash SMSini yuborish (bu endpoint odatda ichki tizim tomonidan chaqiriladi, to'g'ridan-to'g'ri frontenddan emas).

## Autentifikatsiya

*   **Mexanizm:** Token-ga asoslangan autentifikatsiya (JSON Web Tokens - JWT) ishlatiladi. Foydalanuvchi tizimga kirganda, server kirish (access) va yangilash (refresh) tokenlarini qaytaradi.
*   **Oqim:**
    1.  Foydalanuvchi login ma'lumotlarini (elektron pochta/telefon raqami va parol) frontend orqali backendga yuboradi.
    2.  Backend ma'lumotlarni tekshiradi va agar to'g'ri bo'lsa, imzolangan kirish va yangilash tokenlarini qaytaradi.
    3.  Frontend kirish tokenini (odatda `localStorage` yoki `sessionStorage`da) va yangilash tokenini (xavfsiz `HttpOnly` cookie-da) saqlaydi.
    4.  Keyingi himoyalangan API so'rovlari `Authorization` sarlavhasida kirish tokenini (`Bearer <token>`) o'z ichiga oladi.
    5.  Kirish tokenining muddati tugaganda, frontend yangilash tokenidan foydalanib yangi kirish tokenini so'raydi.
*   **Backend implementatsiyasi:** Django REST Framework Simple JWT kutubxonasi tokenlarni yaratish, tekshirish va yangilash uchun ishlatiladi.
*   **Xavfsizlik:** Kirish tokenlari qisqa muddatli bo'ladi. Yangilash tokenlari uzoqroq muddatli bo'lib, `HttpOnly` va `Secure` flaglari bilan cookie-larda saqlanadi, bu XSS hujumlaridan himoya qilishga yordam beradi.

## Ma'lumotlar oqimi

*   **Foydalanuvchi ro'yxatdan o'tishi/kirishi:**
    1.  Frontend foydalanuvchi ma'lumotlarini (e-pochta, parol) `POST /api/auth/register/` yoki `POST /api/auth/login/` endpointiga yuboradi.
    2.  Backend ma'lumotlarni tekshiradi, foydalanuvchini yaratadi/autentifikatsiya qiladi va JWT tokenlarini qaytaradi.
    3.  Frontend tokenlarni saqlaydi va foydalanuvchini shaxsiy sahifasiga yo'naltiradi.
*   **Mahsulotlarni ko'rish va savatga qo'shish:**
    1.  Frontend `GET /api/products/` endpointiga so'rov yuborib, mahsulotlar ro'yxatini oladi va ularni ko'rsatadi.
    2.  Foydalanuvchi mahsulotni savatga qo'shganda, frontend `POST /api/cart/items/` endpointiga mahsulot IDsi va miqdori bilan so'rov yuboradi.
    3.  Backend savatni yangilaydi va tasdiqlash javobini qaytaradi.
*   **Buyurtma berish va SMS yuborish:**
    1.  Foydalanuvchi savatni tasdiqlab, buyurtma berish tugmasini bosganda, frontend `POST /api/orders/` endpointiga so'rov yuboradi.
    2.  Backend buyurtmani yaratadi, savatni bo'shatadi va buyurtma holatini ma'lumotlar bazasiga yozadi.
    3.  Buyurtma muvaffaqiyatli yaratilgandan so'ng, backend `sms_notifications` ilovasi orqali Celery ish navbatiga SMS yuborish vazifasini qo'shadi.
    4.  Celery ishchisi vazifani oladi, SMS xizmati API (masalan, Twilio) orqali foydalanuvchining telefon raqamiga buyurtma tasdiqlash SMSini yuboradi.
    5.  Backend frontendga buyurtma tasdiqlash javobini qaytaradi.

## Xavfsizlik qoidalari

*   **API xavfsizligi:**
    *   **HTTPS:** Barcha aloqa SSL/TLS orqali shifrlanadi, bu ma'lumotlarning tinglanishini oldini oladi.
    *   **JWT:** Tokenlar imzolangan bo'lib, ularning butunligini ta'minlaydi va ruxsatsiz kirishni cheklaydi.
    *   **Kirishni cheklash (Rate Limiting):** Brute-force hujumlarini oldini olish uchun login va ro'yxatdan o'tish endpointlariga so'rovlar soni cheklanadi.
    *   **Kiritishni tekshirish (Input Validation):** Barcha foydalanuvchi kiritishlari (formalar, API so'rovlari) server tomonida tekshiriladi, bu SQL injection, XSS va boshqa hujumlarni oldini oladi.
    *   **CORS (Cross-Origin Resource Sharing):** Faqat ruxsat etilgan frontend domenlaridan APIga kirishga ruxsat beriladi.
*   **Ma'lumotlar bazasi xavfsizligi:**
    *   **Eng kam imtiyoz prinsipi:** Ma'lumotlar bazasi foydalanuvchilari faqat o'z vazifalarini bajarish uchun zarur bo'lgan minimal imtiyozlarga ega bo'ladi.
    *   **Parollarni xeshlash:** Foydalanuvchi parollari ma'lumotlar bazasida xeshlangan va tuzlangan (salted) holda saqlanadi (Django buni avtomatik bajaradi).
    *   **Zaxira nusxalash:** Ma'lumotlar bazasining muntazam zaxira nusxalari olinadi va xavfsiz joyda saqlanadi.
*   **SMS xavfsizligi:**
    *   **API kalitlarini himoyalash:** SMS xizmatining API kalitlari muhit o'zgaruvchilari (environment variables) orqali saqlanadi va kodga qattiq kodlanmaydi.
    *   **Server tomonida yuborish:** SMS yuborish faqat backend tomonidan amalga oshiriladi, frontenddan to'g'ridan-to'g'ri SMS xizmatiga kirishga ruxsat berilmaydi.
    *   **Raqamlarni tekshirish:** SMS yuborishdan oldin telefon raqamlari formatini tekshirish va spamni oldini olish uchun cheklovlar qo'llash.

## Test strategiyasi

*   **Unit testlar:**
    *   Har bir alohida funksiya, metod, model va serializer uchun testlar yoziladi.
    *   Frontendda React komponentlari, utilitlar va xizmatlar uchun testlar yoziladi (masalan, Jest va React Testing Library yordamida).
    *   Backendda Django modellarining xulq-atvori, yordamchi funksiyalar va kichik logikalar uchun testlar yoziladi.
*   **Integratsiya testlari:**
    *   Turli modullar o'rtasidagi o'zaro aloqalarni tekshirish uchun testlar yoziladi.
    *   Backendda API endpointlarining ma'lumotlar bazasi bilan to'g'ri ishlashini, bir nechta ilovalar o'rtasidagi aloqalarni tekshirish.
    *   Frontendda komponentlarning API bilan to'g'ri aloqa qilishini tekshirish.
*   **End-to-End (E2E) testlar:**
    *   Foydalanuvchi stsenariylarini (masalan, ro'yxatdan o'tish, tizimga kirish, mahsulotni savatga qo'shish, buyurtma berish) simulyatsiya qilish uchun testlar yoziladi.
    *   Cypress yoki Playwright kabi vositalar yordamida butun tizimning to'g'ri ishlashi tekshiriladi.
*   **Xavfsizlik testlari:**
    *   Vulnerabilitetlarni skanerlash (SAST/DAST) va penetratsion testlar o'tkaziladi.
    *   Autentifikatsiya, avtorizatsiya va ma'lumotlar kiritish joylarida xavfsizlik zaifliklari tekshiriladi.

## Deploy uchun talablar

*   **Muhitlar:** Loyiha kamida uchta muhitda joylashtiriladi:
    *   **Development:** Rivojlanish uchun mahalliy muhit.
    *   **Staging:** Ishlab chiqarish muhitiga o'xshash test muhiti, yakuniy sinovlar va mijozga namoyish qilish uchun.
    *   **Production:** Jonli foydalanuvchilar uchun ishlaydigan muhit.
*   **Konteynerizatsiya:** Loyihaning har bir qismi (backend, frontend, PostgreSQL, Redis, Celery) Docker konteynerlariga qadoqlanadi. Docker Compose mahalliy rivojlanish va kichik miqyosdagi joylashtirish uchun ishlatiladi.
*   **CI/CD (Uzluksiz integratsiya/Uzluksiz joylashtirish):** GitHub Actions yoki GitLab CI/CD kabi vositalar yordamida avtomatlashtirilgan testlash, kod sifatini tekshirish va ishlab chiqarish muhitiga joylashtirish jarayonlari o'rnatiladi.
*   **Server konfiguratsiyasi:**
    *   **Backend:** Gunicorn yoki uWSGI kabi WSGI serveri Django ilovasini boshqaradi. Nginx veb-serveri statik fayllarni taqdim etadi va Gunicorn/uWSGI uchun proksi vazifasini bajaradi.
    *   **Frontend:** Nginx yoki boshqa veb-server React ilovasining statik fayllarini taqdim etadi.
    *   **Ma'lumotlar bazasi:** PostgreSQL serveri alohida yoki konteynerda ishlaydi.
    *   **Kesh/Navbat:** Redis serveri Celery uchun broker va kesh xizmati sifatida ishlatiladi.
*   **Monitoring va loglash:** Tizimning ishlashini kuzatish (CPU, RAM, disk, tarmoq) va xatolarni qayd etish uchun Prometheus/Grafana yoki ELK stack (Elasticsearch, Logstash, Kibana) kabi vositalar integratsiya qilinadi.