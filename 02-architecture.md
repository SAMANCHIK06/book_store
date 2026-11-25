## Texnologiya tanlovi
*   **Frontend (Mini App):** Python afzal qilinganligi sababli, Streamlit ramkasi tanlanadi. U tez rivojlanishni ta'minlaydi, interaktiv UI yaratishga qulay va Python ekotizimiga to'liq mos keladi.
*   **Backend (API):** Python uchun FastAPI ramkasi tanlanadi. U yuqori ishlash, avtomatik API hujjatlari (Swagger UI) va asinxron operatsiyalarni qo'llab-quvvatlashi bilan ajralib turadi, bu esa AI modeli bilan o'zaro aloqa qilishda foydali bo'ladi.
*   **Ma'lumotlar bazasi:** PostgreSQL relatsion ma'lumotlar bazasi tanlanadi. U mustahkamlik, kengaytirilish va murakkab so'rovlarni qo'llab-quvvatlash qobiliyatiga ega bo'lib, foydalanuvchi ma'lumotlari, AI so'rovlari/javoblari, tasdiqlash holatlari va hujjatlar metama'lumotlarini saqlash uchun ideal. SQLAlchemy ORM (Object-Relational Mapper) Python kodidan ma'lumotlar bazasi bilan ishlashni soddalashtiradi.
*   **AI Integratsiyasi:** "Haqiqiy AI" modeli bilan o'zaro aloqa qilish uchun uning rasmiy Python SDK'si yoki RESTful API'si ishlatiladi. Bu AI modelining turiga va provayderiga bog'liq bo'ladi.

## Papkalar va modullar tuzilmasi
```
/gemini_project
├── /backend
│   ├── /app
│   │   ├── main.py                 # FastAPI ilovasining asosiy kirish nuqtasi
│   │   ├── /api                    # API endpointlari uchun routerlar
│   │   │   ├── v1
│   │   │   │   ├── auth.py         # Autentifikatsiya endpointlari (ro'yxatdan o'tish, kirish)
│   │   │   │   ├── ai_interaction.py # AI bilan o'zaro aloqa endpointlari (so'rov yuborish, javob olish)
│   │   │   │   ├── approval.py     # Tasdiqlash mexanizmi endpointlari (tasdiqlash, rad etish, holatni olish)
│   │   │   │   └── documentation.py # Hujjatlar bilan bog'liq endpointlar (ro'yxat, yuklab olish)
│   │   ├── /core                   # Asosiy biznes mantig'i va yordamchi funksiyalar
│   │   │   ├── security.py         # JWT tokenlarini yaratish va validatsiya qilish, parol heshlash
│   │   │   ├── ai_service.py       # AI modeli bilan o'zaro aloqa logikasi va javoblarni qayta ishlash
│   │   │   ├── approval_service.py # Tasdiqlash ish oqimi mantig'i va holatni boshqarish
│   │   │   └── doc_generator.py    # AI sinovlari va tasdiqlashlar asosida hujjatlarni yaratish
│   │   ├── /db                     # Ma'lumotlar bazasi bilan bog'liq modullar
│   │   │   ├── database.py         # Ma'lumotlar bazasi ulanishini sozlash va sessiyalarni boshqarish
│   │   │   ├── models.py           # SQLAlchemy ORM modellarini aniqlash (User, AISession, Approval, Document)
│   │   │   └── crud.py             # Ma'lumotlar bazasi operatsiyalari (Create, Read, Update, Delete)
│   │   └── /schemas                # Pydantic modellar (API so'rovlari va javoblari uchun ma'lumotlar tuzilmalari)
│   │       ├── user.py             # Foydalanuvchi ma'lumotlari sxemalari
│   │       ├── ai_request.py       # AI so'rovi va javobi sxemalari
│   │       ├── approval.py         # Tasdiqlash sxemalari
│   │       └── document.py         # Hujjat sxemalari
│   ├── requirements.txt            # Backend uchun Python bog'liqliklari
│   └── Dockerfile                  # Backend ilovasini konteynerizatsiya qilish uchun
├── /frontend
│   ├── app.py                      # Streamlit Mini App asosiy fayli
│   ├── /components                 # Qayta ishlatiladigan UI komponentlari
│   │   ├── ai_chat_interface.py    # AI bilan matnli o'zaro aloqa komponenti
│   │   ├── approval_workflow.py    # Tasdiqlash tugmalari va holatini ko'rsatish komponenti
│   │   └── document_viewer.py      # Yaratilgan hujjatlarni ko'rish va yuklab olish komponenti
│   ├── /services                   # Backend API bilan o'zaro aloqa qilish uchun xizmatlar
│   │   ├── api_client.py           # Backend API'ga so'rovlar yuborish uchun umumiy mijoz
│   │   └── auth_service.py         # Autentifikatsiya bilan bog'liq funksiyalar (kirish, chiqish, tokenlarni boshqarish)
│   ├── requirements.txt            # Frontend uchun Python bog'liqliklari
│   └── Dockerfile                  # Frontend ilovasini konteynerizatsiya qilish uchun
├── /docs                           # Loyiha hujjatlari va spetsifikatsiyalar
│   ├── architecture.md             # Ushbu arxitektura hujjati
│   └── api_spec.yaml               # OpenAPI spetsifikatsiyasi (FastAPI tomonidan avtomatik yaratiladi)
└── README.md                       # Loyiha haqida umumiy ma'lumot
```

## API endpointlar
*   **Autentifikatsiya:**
    *   `POST /api/v1/auth/register`: Yangi foydalanuvchini ro'yxatdan o'tkazish. Kirish: `username`, `password`. Javob: `user_id`, `username`.
    *   `POST /api/v1/auth/login`: Foydalanuvchi tizimga kirishi va JWT tokenini olishi. Kirish: `username`, `password`. Javob: `access_token`, `token_type`.
*   **AI bilan o'zaro aloqa:**
    *   `POST /api/v1/ai/query`: AI modeliga matnli so'rov yuborish. Kirish: `query_text`. Javob: `session_id`, `ai_response_text`, `timestamp`. (Autentifikatsiya talab qilinadi)
    *   `GET /api/v1/ai/sessions`: Foydalanuvchining barcha AI so'rov sessiyalarini olish. Javob: `List[AISessionSchema]`. (Autentifikatsiya talab qilinadi)
*   **Tasdiqlash mexanizmi:**
    *   `GET /api/v1/approvals`: Barcha tasdiqlash uchun kutilayotgan yoki yakunlangan natijalarni olish. Javob: `List[ApprovalSchema]`. (Autentifikatsiya talab qilinadi)
    *   `POST /api/v1/approvals/{session_id}/approve`: Muayyan AI natijasini tasdiqlash. Kirish: `comment` (ixtiyoriy). Javob: `approval_status`, `timestamp`. (Autentifikatsiya talab qilinadi)
    *   `POST /api/v1/approvals/{session_id}/reject`: Muayyan AI natijasini rad etish. Kirish: `reason` (ixtiyoriy). Javob: `approval_status`, `timestamp`. (Autentifikatsiya talab qilinadi)
*   **Hujjatlar yaratish va boshqarish:**
    *   `GET /api/v1/documents`: Yaratilgan hujjatlar ro'yxatini olish. Javob: `List[DocumentSchema]`. (Autentifikatsiya talab qilinadi)
    *   `GET /api/v1/documents/{document_id}/download`: Muayyan hujjatni yuklab olish. Javob: Fayl (masalan, PDF yoki TXT). (Autentifikatsiya talab qilinadi)

## Autentifikatsiya
*   **Mexanizm:** JWT (JSON Web Tokens) asosidagi tokenli autentifikatsiya qo'llaniladi. Foydalanuvchi tizimga kirganda, server xavfsiz JWT tokenini qaytaradi, bu token keyingi barcha himoyalangan API so'rovlari bilan `Authorization: Bearer <token>` sarlavhasi orqali yuboriladi.
*   **Foydalanuvchi ma'lumotlari:** Foydalanuvchi nomlari (username) va heshlangan parollar PostgreSQL ma'lumotlar bazasida saqlanadi. Parollar `bcrypt` kabi kuchli, bir tomonlama heshlash algoritmlari yordamida heshlanadi va tuz (salt) bilan birga saqlanadi.
*   **Ruxsatlar:** 1-versiya uchun barcha autentifikatsiya qilingan foydalanuvchilar bir xil ruxsatlarga ega bo'ladi. Keyingi versiyalarda "AI sinovchisi", "Mahsulot menejeri" kabi rollar joriy etilishi mumkin, bu esa turli API endpointlariga kirishni cheklash uchun RBAC (Role-Based Access Control) mexanizmini talab qiladi.

## Ma'lumotlar oqimi
*   **Foydalanuvchi -> Frontend (Mini App):** Foydalanuvchi Streamlit Mini App orqali AI'ga matnli so'rov yuboradi, AI javobini ko'rib chiqadi, tasdiqlash tugmalarini bosadi yoki yaratilgan hujjatlar ro'yxatini ko'radi.
*   **Frontend -> Backend (API):** Mini App foydalanuvchi harakatlarini (masalan, AI so'rovi, tasdiqlash) FastAPI Backend API'ga RESTful so'rovlar orqali yuboradi. Har bir himoyalangan so'rovda foydalanuvchining JWT tokeni mavjud bo'ladi.
*   **Backend -> AI modeli:** Backend'dagi `ai_service` moduli kelgan AI so'rovini qayta ishlaydi va "Haqiqiy AI" modelining API'siga yuboradi. AI modelidan javobni oladi, uni qayta ishlaydi va ma'lumotlar bazasiga saqlaydi.
*   **Backend -> Ma'lumotlar bazasi:** Backend foydalanuvchi ma'lumotlari, AI so'rovlari/javoblari, tasdiqlash holatlari va hujjatlar metama'lumotlarini PostgreSQL ma'lumotlar bazasiga yozadi va undan o'qiydi. SQLAlchemy ORM bu operatsiyalarni boshqaradi.
*   **Backend -> Hujjat yaratish:** Tasdiqlash jarayoni yakunlanganda yoki sinov sessiyasi tugagach, `doc_generator` moduli avtomatik ravishda hujjatlarni (masalan, sinov natijalari, tasdiqlash jurnallari) yaratadi. Bu hujjatlar fayl tizimida yoki bulutli saqlashda saqlanadi, ma'lumotlar bazasida esa ularning metama'lumotlari (nomi, turi, joylashuvi) saqlanadi.
*   **Backend -> Frontend:** Backend qayta ishlangan ma'lumotlarni, AI javoblarini, tasdiqlash holatlarini va hujjatlar ro'yxatini JSON formatida Frontend'ga qaytaradi.
*   **Frontend -> Foydalanuvchi:** Mini App Backend'dan olingan ma'lumotlarni foydalanuvchiga qulay va interaktiv tarzda ko'rsatadi, masalan, chat interfeysi, tasdiqlash kartalari yoki hujjatlar ro'yxati.

## Xavfsizlik qoidalari
*   **Ma'lumotlarni shifrlash:** Transportdagi barcha ma'lumotlar HTTPS (TLS/SSL) orqali shifrlanadi, bu mijoz va server o'rtasidagi aloqani himoya qiladi. Ma'lumotlar bazasida sezgir ma'lumotlar (masalan, parollar) heshlangan holda saqlanadi.
*   **Kirishni boshqarish:** JWT tokenlari yordamida API endpointlariga kirishni boshqarish amalga oshiriladi. Faqat autentifikatsiya qilingan va tokeni validatsiya qilingan foydalanuvchilar himoyalangan resurslarga kira oladi. FastAPI'ning `Depends` funksiyasi yordamida har bir himoyalangan endpoint uchun token validatsiyasi majburiy qilinadi.
*   **Kiritishni validatsiya qilish va tozalash:** Barcha foydalanuvchi kiritishlari (input) server tomonida Pydantic sxemalari yordamida qattiq validatsiya qilinadi. Bu SQL Injection, XSS (Cross-Site Scripting) kabi hujumlarning oldini olishga yordam beradi.
*   **AI modeli bilan xavfsiz aloqa:** Agar "Haqiqiy AI" modeli tashqi xizmat bo'lsa, uning API kalitlari yoki boshqa autentifikatsiya mexanizmlari xavfsiz tarzda boshqariladi (masalan, muhit o'zgaruvchilari orqali, kodga qattiq kodlanmaydi) va ularga kirish cheklanadi.
*   **Loglash va monitoring:** Tizimga kirish urinishlari, xato holatlari, muhim tizim voqealari va API so'rovlari loglanadi. Bu xavfsizlik buzilishlarini aniqlash, tahlil qilish va tizimning umumiy holatini kuzatishga yordam beradi.

## Test strategiyasi
*   **Birlik testlari (Unit Tests):** Har bir alohida funksiya, metod va kichik modul uchun testlar yoziladi. Masalan, `security.py` dagi parol heshlash funksiyalari, `crud.py` dagi ma'lumotlar bazasi operatsiyalari, `ai_service.py` dagi AI javobini qayta ishlash logikasi. `pytest` ramkasidan foydalaniladi.
*   **Integratsiya testlari (Integration Tests):** Turli modullar va xizmatlar o'zaro qanday ishlashini tekshirish. Bu Backend API endpointlarining ma'lumotlar bazasi bilan, Backend'ning AI modeli bilan va Frontend'ning Backend API bilan to'g'ri aloqa qilishini tekshiradi. `pytest` va `httpx` (yoki `requests`) kutubxonalari yordamida API testlari yoziladi.
*   **Foydalanuvchi interfeysi testlari (UI Tests):** Frontend (Mini App) komponentlarining to'g'ri ko'rsatilishini, foydalanuvchi o'zaro aloqalarini va umumiy foydalanuvchi tajribasini tekshirish. Streamlit uchun to'g'ridan-to'g'ri UI testlari murakkab bo'lishi mumkin, shuning uchun dastlabki versiyada vizual tekshiruvlar va asosiy funksionallikni qo'lda tekshirishga e'tibor qaratiladi. Keyingi versiyalarda Playwright yoki Selenium kabi vositalar yordamida avtomatlashtirilgan testlar qo'shilishi mumkin.

## Deploy uchun talablar
*   **Konteynerizatsiya:** Ilova komponentlari (Frontend va Backend) Docker konteynerlariga joylashtiriladi. Bu har bir komponent uchun izolyatsiya qilingan va bir xil ish muhitini ta'minlaydi, "mening mashinamda ishlaydi" muammosini bartaraf etadi.
*   **Orkestratsiya:** 1-versiya uchun Docker Compose yordamida Frontend, Backend va PostgreSQL ma'lumotlar bazasi konteynerlarini birgalikda boshqarish. Bu mahalliy rivojlanish va oddiy deploy uchun qulay yechim. Kengaytirilish talab qilinsa, Kubernetes kabi orkestratsiya vositalariga o'tish mumkin.
*   **Muhit o'zgaruvchilari:** Konfiguratsiya ma'lumotlari (masalan, ma'lumotlar bazasi ulanish satrlari, AI API kalitlari, JWT sirlari) muhit o'zgaruvchilari orqali boshqariladi. Bu sezgir ma'lumotlarni koddan ajratish va xavfsiz saqlash imkonini beradi.
*   **CI/CD quvuri:** Avtomatlashtirilgan integratsiya va deploy (CI/CD) quvurini o'rnatish (masalan, GitHub Actions yoki GitLab CI/CD). Bu kod o'zgarishlari kiritilganda avtomatik testlash, Docker tasvirlarini yaratish va ularni deploy qilishni ta'minlaydi, rivojlanish jarayonini tezlashtiradi va xatolarni kamaytiradi.
*   **Monitoring va loglash:** Ilova ishlashini kuzatish va xatolarni aniqlash uchun monitoring va loglash tizimlari integratsiya qilinadi. Konteyner loglari markazlashtirilgan log boshqaruv tizimiga (masalan, ELK Stack yoki Grafana Loki) yuboriladi. Prometheus va Grafana yordamida tizim metrikalari (CPU, RAM, tarmoq, API javob vaqtlari) kuzatiladi.