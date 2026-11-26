## Talablar qoplanishi
*   **Mijozga buyurtma tasdiqlash xabari yuborish talabi qoplanmagan:** Reja agentida "Buyurtma tasdiqlash (potensial)" sifatida ko'rsatilgan bo'lsa-da, arxitektura va build agentlarida mijozga elektron pochta orqali tasdiqlash xabari yuborish mexanizmi yoki vazifasi aniq belgilanmagan. Faqat `success.html` sahifasi mavjud.
*   **Guldokoni egalari uchun samarali boshqaruv qisman qoplangan:** Reja agentida "Guldokoni egalariga buyurtma ma'lumotlarini samarali boshqarish imkoniyatini yaratish" maqsad sifatida ko'rsatilgan. Ma'lumotlar bazasiga saqlash rejalashtirilgan, ammo bu ma'lumotlarni ko'rish, filtrlash yoki boshqarish uchun hech qanday interfeys (masalan, admin paneli) 1-versiyada mavjud emas. Bu "samarali boshqaruv" talabini to'liq qoplamaydi.
*   **Byudjet yo'qligi cheklovi texnologiya tanlovida hisobga olingan, ammo resurslar masalasi ochiq:** Arxitektura agenti Flask, SQLite kabi tekin texnologiyalarni tanlab, byudjet cheklovini hisobga olgan. Biroq, reja agentidagi "Loyiha amalga oshirish uchun resurslar (ishlab chiquvchi va hosting) qanday ta'minlanadi?" savoliga javob berilmagan. Bu loyihaning amalga oshirilishiga to'sqinlik qilishi mumkin.

## Reja va arxitektura mosligi
*   **SMTP autentifikatsiya ma'lumotlarini saqlashda ziddiyat:** Arxitektura agenti "SMTP autentifikatsiya ma'lumotlari... `config.py` faylida saqlanadi va versiya nazorati tizimiga (Git) to'g'ridan-to'g'ri joylashtirilmaydi (masalan, muhit o'zgaruvchilari orqali yuklanadi)" deb aytgan. Biroq, build agenti `config.py` da SMTP ma'lumotlarini aniqlashni vazifa qilib qo'ygan, bu esa ularni to'g'ridan-to'g'ri faylga yozishga olib kelishi mumkin. Bu reja va arxitektura o'rtasidagi ziddiyat.
*   **CSRF himoyasi bo'yicha aniq vazifa yo'qligi:** Arxitektura agenti "CSRF himoyasi: Flask-WTF kabi kutubxonalar yordamida CSRF tokenlari qo'llaniladi" deb ta'kidlagan. Ammo build agenti vazifalarida Flask-WTF ni integratsiya qilish yoki CSRF tokenlarini qo'llash haqida aniq vazifa belgilanmagan. Bu CSRF himoyasi e'tibordan chetda qolishi mumkinligini ko'rsatadi.
*   **Qabul mezonlari testlari reja va arxitekturada qoplanmagan:** Reja agentidagi "Saytning yuklanish vaqti 3 soniyadan oshmasligi kerak" va "Yuborilgan buyurtma ma'lumotlari guldokoni egasining belgilangan elektron pochta manziliga 1 daqiqa ichida yetib borishi kerak" kabi qabul mezonlari uchun arxitektura va build agentlarida aniq test strategiyalari yoki vazifalari belgilanmagan.

## Xavfsizlik muammolari
*   **Maxfiy ma'lumotlarni saqlashdagi xavf:** `config.py` faylida SMTP parollari va boshqa maxfiy ma'lumotlarni to'g'ridan-to'g'ri saqlash va ularni versiya nazorati tizimiga kiritish yuqori xavfsizlik muammosidir. Arxitektura agenti muhit o'zgaruvchilaridan foydalanishni tavsiya qilgan bo'lsa-da, build agenti vazifasi bunga ziddir.
    *   **Xavf darajasi:** Yuqori
*   **XSS hujumlaridan himoya qilishning yetishmasligi:** Arxitektura agenti "xavfli belgilar (masalan, XSS hujumlari uchun skriptlar) yo'qligi tekshiriladi" deb aytgan. Biroq, build agenti vazifalarida faqat "bo'sh maydonlar, telefon raqami formati" kabi oddiy validatsiyalar ko'rsatilgan. Kiruvchi ma'lumotlarni (ayniqsa `order_details` maydonini) XSS hujumlaridan himoya qilish uchun maxsus sanitizatsiya yoki HTML escape qilish haqida aniq ko'rsatma yo'q.
    *   **Xavf darajasi:** O'rta
*   **Xato boshqaruvining noaniqligi:** Arxitektura agenti "ichki tizim ma'lumotlari oshkor etilmaydi" deb ta'kidlagan. Ammo build agentida xato holatlarini qanday boshqarish, xato xabarlarini qanday ko'rsatish va ichki ma'lumotlarning oshkor bo'lishini oldini olish bo'yicha aniq vazifalar belgilanmagan. Bu xato yuz berganda tizim ma'lumotlarining oshkor bo'lishiga olib kelishi mumkin.
    *   **Xavf darajasi:** Past

## Testlar yetarliligi
*   **Avtomatlashtirilgan frontend testlarining yo'qligi:** Arxitektura va build agentlarida frontend testlari faqat "vizual tekshirish" va "brauzerda qo'lda tekshirish" bilan cheklangan. HTML formasining to'g'ri ishlashi va JavaScript validatsiyasi kabi muhim funksionallikni avtomatlashtirilgan testlar (masalan, Selenium, Cypress) bilan qoplash rejalashtirilmagan.
    *   **Xavf darajasi:** O'rta
*   **Haqiqiy elektron pochta yuborish testlarining yetishmasligi:** Arxitektura agenti "Elektron pochta xizmatining haqiqiy SMTP serveriga ulanib, test xabarini yuborish va uning yetib borishini tasdiqlash (faqat test muhitida)"ni tavsiya qilgan. Biroq, build agenti vazifalarida faqat mock SMTP server yordamida testlash ko'rsatilgan. Haqiqiy SMTP serveri bilan integratsion testlar o'tkazilmasligi elektron pochta xabarlarining real muhitda yetib borishiga ishonchni kamaytiradi.
    *   **Xavf darajasi:** O'rta
*   **Qabul mezonlari uchun testlarning yo'qligi:** Reja agentida belgilangan "Saytning yuklanish vaqti 3 soniyadan oshmasligi kerak" va "Elektron pochta 1 daqiqa ichida yetib borishi kerak" kabi muhim qabul mezonlari uchun test strategiyasida aniq test vazifalari belgilanmagan. Ishlash (performance) testlari yoki end-to-end testlar haqida hech narsa aytilmagan.
    *   **Xavf darajasi:** Yuqori

## Xavfli va noaniq nuqtalar
*   **Byudjet yo'qligi va hosting/resurslar masalasi hal etilmagan:** Reja agentidagi "Byudjet yo'qligi: Loyihani amalga oshirish uchun resurslar (ishlab chiquvchi va hosting) qanday ta'minlanadi?" savoliga javob berilmagan. Texnologiya tanlovi byudjetga mos bo'lsa-da, loyihani joylashtirish (hosting) va uni ishlab chiqish uchun inson resurslari masalasi ochiq qolmoqda. Bu loyihaning amalga oshirilishiga to'sqinlik qilishi mumkin bo'lgan yuqori xavf.
    *   **Xavf darajasi:** Yuqori
*   **Elektron pochta xizmati cheklovlari noaniq:** Reja agenti "Elektron pochta xizmati: Buyurtmalarni yuborish uchun qaysi elektron pochta xizmati (SMTP server) ishlatiladi va uning cheklovlari bormi?" deb so'ragan. `smtplib` moduli tanlangan bo'lsa-da, qaysi tashqi SMTP server (masalan, Gmail, SendGrid) ishlatilishi va uning kunlik yuborish limitlari, spam filtrlari kabi cheklovlari haqida aniq ma'lumot yo'q. Bu elektron pochta xabarlarining yetkazib berilishiga ta'sir qilishi mumkin.
    *   **Xavf darajasi:** O'rta
*   **Guldokoni egasi uchun boshqaruv interfeysining yo'qligi:** Reja agentida "Guldokoni egalariga buyurtma ma'lumotlarini samarali boshqarish imkoniyatini yaratish" maqsad sifatida belgilangan. Ma'lumotlar bazasiga saqlash rejalashtirilgan bo'lsa-da, bu ma'lumotlarni ko'rish, filtrlash yoki boshqarish uchun hech qanday interfeys (admin paneli) mavjud emas. Bu maqsadning 1-versiyada to'liq qoplanmaganligini ko'rsatadi va kelajakda qo'shimcha ish talab qiladi.
    *   **Xavf darajasi:** O'rta

## Release oldidan tekshirish ro'yxati
1.  **Konfiguratsiya xavfsizligi:** `config.py` faylida maxfiy ma'lumotlar (SMTP parollari, Flask `SECRET_KEY`) muhit o'zgaruvchilari orqali yuklanishini ta'minlash va ularni versiya nazorati tizimiga kiritmaslik.
2.  **CSRF himoyasi:** Flask-WTF kabi kutubxonalar yordamida CSRF tokenlari `POST /order` endpointi uchun to'g'ri qo'llanilganligini tekshirish.
3.  **XSS himoyasi:** Backendda kiruvchi ma'lumotlar (ayniqsa `order_details`) XSS hujumlaridan himoyalanganligini (masalan, HTML escape qilish yoki sanitizatsiya) tekshirish.
4.  **Xato boshqaruvi:** Ilovadagi barcha mumkin bo'lgan xatolar (DBga yozish, email yuborish, validatsiya) to'g'ri qayta ishlanishini va foydalanuvchiga ichki tizim ma'lumotlari oshkor etilmasligini ta'minlash.
5.  **Elektron pochta yetkazib berish testlari:** Haqiqiy SMTP serveriga ulanib, test xabarini yuborish va uning muvaffaqiyatli yetib borishini tasdiqlash.
6.  **Qabul mezonlari testlari:** Saytning yuklanish vaqti (3 soniyadan oshmasligi) va elektron pochta yetkazib berish vaqti (1 daqiqa ichida) kabi qabul mezonlari bajarilishini tekshirish uchun ishlash testlarini o'tkazish.
7.  **Hosting va resurslar:** Loyihani joylashtirish uchun hosting, domen va SSL sertifikati kabi resurslar mavjudligini va ularning sozlamalarini tasdiqlash.