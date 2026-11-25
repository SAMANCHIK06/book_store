## Loyiha skeleti
*   **Vazifa:** `gemini_project` asosiy papkasini va uning ichidagi `backend`, `frontend`, `docs` kabi asosiy subpapkalarni yaratish.
    *   **Modul:** Loyiha ildizi.
    *   **Kirish:** Bo'sh loyiha muhiti.
    *   **Chiqish:** Belgilangan papka tuzilmasi.
    *   **Test:** Fayl tizimida papkalar mavjudligini tekshirish.
*   **Vazifa:** `backend` va `frontend` papkalari uchun Python virtual muhitlarini sozlash va dastlabki `requirements.txt` fayllarini yaratish.
    *   **Modul:** `backend`, `frontend`.
    *   **Kirish:** Bo'sh `backend` va `frontend` papkalari.
    *   **Chiqish:** Har bir papkada `.venv` virtual muhit papkasi va bo'sh `requirements.txt` fayli.
    *   **Test:** Virtual muhitning faollashishini va `pip list` buyrug'i bilan dastlabki paketlar ro'yxatini tekshirish.
*   **Vazifa:** `backend/Dockerfile` va `frontend/Dockerfile` fayllarini yaratish, asosiy Python tasvirlarini belgilash.
    *   **Modul:** `backend`, `frontend`.
    *   **Kirish:** Bo'sh Dockerfile fayllari.
    *   **Chiqish:** Ilovalarni konteynerizatsiya qilish uchun asosiy Dockerfile shablonlari.
    *   **Test:** Fayllar mavjudligini va asosiy sintaksis to'g'riligini tekshirish.

## Modullar bo'yicha vazifalar
*   **Vazifa:** `backend/app/core/security.py` modulida parol heshlash (`bcrypt` yordamida) va JWT tokenlarini yaratish/validatsiya qilish funksiyalarini implementatsiya qilish.
    *   **Modul:** `backend/app/core/security`.
    *   **Kirish:** `plain_password` (str), `username` (str), `user_id` (int), `token` (str).
    *   **Chiqish:** `hashed_password` (str), `access_token` (str), `decoded_token` (dict) yoki `bool` (validatsiya natijasi).
    *   **Test:** Birlik testlari (pytest) yordamida parollarning to'g'ri heshlanishi, JWT tokenlarining yaratilishi va validatsiya qilinishini tekshirish.
*   **Vazifa:** `backend/app/core/ai_service.py` modulida "Haqiqiy AI" modeli bilan o'zaro aloqa qilish (so'rov yuborish va javobni qayta ishlash) logikasini yozish.
    *   **Modul:** `backend/app/core/ai_service`.
    *   **Kirish:** `query_text` (str), AI modelining API kaliti/endpointi.
    *   **Chiqish:** `ai_response_text` (str) va AI modelidan olingan xom javob.
    *   **Test:** Mock AI API yordamida birlik testlari va AI modeliga haqiqiy so'rov yuborish orqali integratsiya testlari.
*   **Vazifa:** `backend/app/core/approval_service.py` modulida AI natijalarini tasdiqlash yoki rad etish ish oqimi mantig'ini, jumladan holatni o'zgartirish va sharhlarni saqlashni implementatsiya qilish.
    *   **Modul:** `backend/app/core/approval_service`.
    *   **Kirish:** `session_id` (int), `user_id` (int), `status` (str - "approved" yoki "rejected"), `comment_or_reason` (str).
    *   **Chiqish:** Yangilangan `Approval` obyekti.
    *   **Test:** Birlik testlari (pytest) yordamida tasdiqlash holatining to'g'ri o'zgarishini va ma'lumotlarning saqlanishini tekshirish.
*   **Vazifa:** `backend/app/core/doc_generator.py` modulida AI sinovlari natijalari va tasdiqlash holatlari asosida avtomatik hujjat (masalan, TXT formatida) yaratish funksiyasini yozish.
    *   **Modul:** `backend/app/core/doc_generator`.
    *   **Kirish:** `AISession` obyekti, `Approval` obyekti.
    *   **Chiqish:** Yaratilgan hujjatning kontenti (str) va uning metama'lumotlari.
    *   **Test:** Mock ma'lumotlar bilan birlik testlari yordamida hujjat kontentining to'g'ri shakllanishini tekshirish.
*   **Vazifa:** `backend/app/db/crud.py` modulida `User`, `AISession`, `Approval`, `Document` modellariga oid ma'lumotlar bazasi operatsiyalarini (yaratish, o'qish, yangilash, o'chirish) implementatsiya qilish.
    *   **Modul:** `backend/app/db/crud`.
    *   **Kirish:** Pydantic sxemalari (masalan, `UserCreate`, `AISessionCreate`), ob'ekt ID'lari.
    *   **Chiqish:** Yaratilgan/o'qilgan/yangilangan ORM ob'ektlari yoki `None`.
    *   **Test:** Ma'lumotlar bazasi bilan integratsiya testlari yordamida har bir CRUD operatsiyasining to'g'ri ishlashini tekshirish.

## Ma'lumotlar bazasi modeli
*   **Vazifa:** `backend/app/db/models.py` faylida `User` (username, hashed_password), `AISession` (user_id, query_text, response_text, timestamp), `Approval` (session_id, user_id, status, comment_or_reason, timestamp) va `Document` (session_id, approval_id, name, type, path, timestamp) SQLAlchemy ORM modellarini aniqlash.
    *   **Modul:** `backend/app/db/models`.
    *   **Kirish:** Loyiha talablari va arxitektura hujjati.
    *   **Chiqish:** Ma'lumotlar bazasi jadvallariga mos keladigan Python sinflari.
    *   **Test:** Modellar tuzilishining to'g'riligini va ma'lumotlar bazasi sxemasiga mos kelishini tekshirish uchun birlik testlari.
*   **Vazifa:** Modellar o'rtasidagi munosabatlarni (masalan, `User` va `AISession` o'rtasidagi birga-ko'p munosabat) aniqlash.
    *   **Modul:** `backend/app/db/models`.
    *   **Kirish:** Aniqlangan ORM modellar.
    *   **Chiqish:** `relationship` va `ForeignKey` kabi SQLAlchemy konstruksiyalari yordamida bog'langan modellar.
    *   **Test:** Munosabatlar orqali bog'liq ob'ektlarni yuklash va saqlash orqali integratsiya testlari.
*   **Vazifa:** `backend/app/db/database.py` modulida PostgreSQL ma'lumotlar bazasiga ulanishni sozlash va SQLAlchemy sessiyasini boshqarish.
    *   **Modul:** `backend/app/db/database`.
    *   **Kirish:** Ma'lumotlar bazasi ulanish satri (muhit o'zgaruvchisi orqali).
    *   **Chiqish:** Ma'lumotlar bazasi bilan o'zaro aloqa qilish uchun `SessionLocal` obyekti.
    *   **Test:** Ma'lumotlar bazasiga muvaffaqiyatli ulanishni va sessiya yaratilishini tekshiruvchi integratsiya testi.

## API yaratish
*   **Vazifa:** `backend/app/api/v1/auth.py` da `POST /api/v1/auth/register` (yangi foydalanuvchini ro'yxatdan o'tkazish) va `POST /api/v1/auth/login` (foydalanuvchi tizimga kirishi va JWT tokenini olishi) endpointlarini yaratish.
    *   **Modul:** `backend/app/api/v1/auth`.
    *   **Kirish:** `UserCreate` (username, password) va `UserLogin` (username, password) Pydantic sxemalari.
    *   **Chiqish:** `UserOut` (id, username) yoki `Token` (access_token, token_type) Pydantic sxemalari.
    *   **Test:** Integratsiya testlari (pytest, httpx) yordamida ro'yxatdan o'tish va kirish jarayonlarining to'g'ri ishlashini tekshirish.
*   **Vazifa:** `backend/app/api/v1/ai_interaction.py` da `POST /api/v1/ai/query` (AI modeliga matnli so'rov yuborish) va `GET /api/v1/ai/sessions` (foydalanuvchining barcha AI so'rov sessiyalarini olish) endpointlarini yaratish.
    *   **Modul:** `backend/app/api/v1/ai_interaction`.
    *   **Kirish:** `AIQueryRequest` (query_text) Pydantic sxemasi, JWT token.
    *   **Chiqish:** `AISessionResponse` (session_id, ai_response_text, timestamp) yoki `List[AISessionSchema]` Pydantic sxemasi.
    *   **Test:** Integratsiya testlari (pytest, httpx) yordamida AI bilan o'zaro aloqa va sessiya boshqaruvini tekshirish, autentifikatsiya talablarini qondirish.
*   **Vazifa:** `backend/app/api/v1/approval.py` da `GET /api/v1/approvals` (barcha tasdiqlash natijalarini olish), `POST /api/v1/approvals/{session_id}/approve` (AI natijasini tasdiqlash) va `POST /api/v1/approvals/{session_id}/reject` (AI natijasini rad etish) endpointlarini yaratish.
    *   **Modul:** `backend/app/api/v1/approval`.
    *   **Kirish:** `session_id` (int), `ApprovalRequest` (comment/reason) Pydantic sxemasi, JWT token.
    *   **Chiqish:** `List[ApprovalSchema]` yoki `ApprovalStatusResponse` (approval_status, timestamp) Pydantic sxemasi.
    *   **Test:** Integratsiya testlari (pytest, httpx) yordamida tasdiqlash ish oqimini va holat o'zgarishini tekshirish.
*   **Vazifa:** `backend/app/api/v1/documentation.py` da `GET /api/v1/documents` (yaratilgan hujjatlar ro'yxatini olish) va `GET /api/v1/documents/{document_id}/download` (muayyan hujjatni yuklab olish) endpointlarini yaratish.
    *   **Modul:** `backend/app/api/v1/documentation`.
    *   **Kirish:** `document_id` (int), JWT token.
    *   **Chiqish:** `List[DocumentSchema]` Pydantic sxemasi yoki fayl kontenti.
    *   **Test:** Integratsiya testlari (pytest, httpx) yordamida hujjatlar ro'yxati va yuklab olish funksiyasini tekshirish.

## Interfeys yaratish
*   **Vazifa:** `frontend/app.py` da asosiy Streamlit ilovasini sozlash, foydalanuvchi autentifikatsiyasi (ro'yxatdan o'tish va kirish) sahifalarini yaratish.
    *   **Modul:** `frontend/app`.
    *   **Kirish:** Foydalanuvchi kiritishlari (username, password).
    *   **Chiqish:** Kirish va ro'yxatdan o'tish shakllari, autentifikatsiya holatini ko'rsatish.
    *   **Test:** Qo'lda tekshirish va autentifikatsiya jarayonining to'g'ri ishlashini sinash.
*   **Vazifa:** `frontend/components/ai_chat_interface.py` da AI bilan matnli o'zaro aloqa qilish uchun interaktiv chat interfeysi komponentini yaratish.
    *   **Modul:** `frontend/components/ai_chat_interface`.
    *   **Kirish:** Matn kiritish maydoni, yuborish tugmasi, AI javoblarini ko'rsatish maydoni.
    *   **Chiqish:** Foydalanuvchi so'rovlarini yuborish va AI javoblarini ko'rsatish imkoniyatiga ega UI.
    *   **Test:** Qo'lda tekshirish, turli so'rovlar bilan sinash va javoblarning to'g'ri ko'rsatilishini tekshirish.
*   **Vazifa:** `frontend/components/approval_workflow.py` da AI tomonidan yaratilgan natijalarni ko'rib chiqish, "Tasdiqlash" va "Rad etish" tugmalari hamda tasdiqlash holatini ko'rsatish komponentini yaratish.
    *   **Modul:** `frontend/components/approval_workflow`.
    *   **Kirish:** AI javobi, tasdiqlash holati.
    *   **Chiqish:** Tasdiqlash tugmalari va natijaning joriy holatini aks ettiruvchi UI.
    *   **Test:** Qo'lda tekshirish, tasdiqlash va rad etish jarayonlarini sinash, holat o'zgarishining to'g'ri aks etishini tekshirish.
*   **Vazifa:** `frontend/components/document_viewer.py` da yaratilgan hujjatlar ro'yxatini ko'rsatish va ularni yuklab olish imkoniyatini beruvchi komponentni yaratish.
    *   **Modul:** `frontend/components/document_viewer`.
    *   **Kirish:** Hujjatlar ro'yxati (nomi, sanasi), yuklab olish tugmasi.
    *   **Chiqish:** Hujjatlar ro'yxati va har bir hujjatni yuklab olish uchun interaktiv elementlar.
    *   **Test:** Qo'lda tekshirish, hujjatlar ro'yxatining to'g'ri ko'rsatilishini va yuklab olish funksiyasining ishlashini sinash.

## Testlar
*   **Vazifa:** `backend/tests/unit` papkasida `core/security.py`, `core/ai_service.py` (mock bilan), `core/approval_service.py` va `core/doc_generator.py` modullari uchun birlik testlarini yozish.
    *   **Modul:** `backend/tests/unit`.
    *   **Kirish:** Har bir modulning alohida funksiyalari va metodlari.
    *   **Chiqish:** Test natijalari (o'tgan/o'tmagan) va kod qamrovi hisoboti.
    *   **Test:** `pytest` ramkasi yordamida testlarni bajarish.
*   **Vazifa:** `backend/tests/integration` papkasida barcha FastAPI API endpointlari uchun integratsiya testlarini yozish, ma'lumotlar bazasi va AI xizmati (mock yoki test muhitida) bilan o'zaro aloqani tekshirish.
    *   **Modul:** `backend/tests/integration`.
    *   **Kirish:** FastAPI ilovasi, test ma'lumotlar bazasi, mock AI xizmati.
    *   **Chiqish:** API endpointlarining to'g'ri ishlashini tasdiqlovchi test natijalari.
    *   **Test:** `pytest` va `httpx` (yoki `requests`) kutubxonalari yordamida API so'rovlarini simulyatsiya qilish.
*   **Vazifa:** Frontend (Streamlit Mini App) uchun asosiy funksionallikni (autentifikatsiya, AI bilan o'zaro aloqa, tasdiqlash, hujjatlarni ko'rish) qo'lda tekshirish bo'yicha test ssenariylarini yaratish va bajarish.
    *   **Modul:** `frontend`.
    *   **Kirish:** Ishlayotgan Streamlit Mini App.
    *   **Chiqish:** Foydalanuvchi talablariga muvofiqligini tasdiqlovchi test hisoboti (qo'lda).
    *   **Test:** Vizual tekshiruvlar va foydalanuvchi o'zaro aloqalarini sinash.

## Integratsiya ishlari
*   **Vazifa:** Backend'ni "Haqiqiy AI" modeli bilan integratsiya qilish, uning rasmiy Python SDK'si yoki RESTful API'si orqali so'rovlar yuborish va javoblarni qayta ishlash.
    *   **Modul:** `backend/app/core/ai_service`.
    *   **Kirish:** AI modelining API kalitlari, SDK o'rnatish.
    *   **Chiqish:** AI modeliga muvaffaqiyatli so'rov yuborish va javob olish.
    *   **Test:** AI modeliga haqiqiy so'rovlar yuborish orqali integratsiya testlari.
*   **Vazifa:** `docker-compose.yml` faylini yaratish va Frontend, Backend, PostgreSQL ma'lumotlar bazasi konteynerlarini birgalikda boshqarish uchun sozlash.
    *   **Modul:** Loyiha ildizi.
    *   **Kirish:** Frontend va Backend Dockerfile'lari, PostgreSQL konfiguratsiyasi.
    *   **Chiqish:** Barcha xizmatlarni birgalikda ishga tushirish, to'xtatish va boshqarish imkoniyati.
    *   **Test:** `docker-compose up --build` buyrug'i bilan barcha konteynerlarning muvaffaqiyatli ishga tushishini va o'zaro aloqa qilishini tekshirish.
*   **Vazifa:** CI/CD quvurini (masalan, GitHub Actions) loyihaga qo'shish, avtomatik testlash, Docker tasvirlarini yaratish va ularni deploy qilish uchun dastlabki bosqichlarni sozlash.
    *   **Modul:** `.github/workflows` (yoki shunga o'xshash).
    *   **Kirish:** Kod bazasi, Dockerfile'lar.
    *   **Chiqish:** Kod o'zgarishlari kiritilganda avtomatik testlash va Docker tasvirlarini yaratish jarayoni.
    *   **Test:** Kodni o'zgartirish va push qilish orqali CI/CD quvurining ishga tushishini va belgilangan bosqichlarni muvaffaqiyatli bajarishini tekshirish.

## Bajarish ketma-ketligi
*   **Vazifa:** Loyiha skeletini yaratish, virtual muhitlarni sozlash va asosiy `requirements.txt` fayllarini to'ldirish.
    *   **Kirish:** Loyiha talablari va arxitektura hujjati.
    *   **Chiqish:** Ishga tayyor loyiha papkasi tuzilmasi va asosiy bog'liqliklar o'rnatilgan muhitlar.
    *   **Test:** Papka tuzilmasi va muhit sozlamalarini tekshirish.
*   **Vazifa:** Ma'lumotlar bazasi modellarini (`models.py`) aniqlash, ulanishni (`database.py`) sozlash va asosiy CRUD operatsiyalarini (`crud.py`) implementatsiya qilish.
    *   **Kirish:** Ma'lumotlar bazasi sxemasi.
    *   **Chiqish:** Ishlaydigan ORM modellar va ma'lumotlar bazasi bilan o'zaro aloqa funksiyalari.
    *   **Test:** Ma'lumotlar bazasi modullari uchun birlik va integratsiya testlari.
*   **Vazifa:** Backend API endpointlarini (`api/v1/*`) yaratish, ularni ma'lumotlar bazasi modullari va `core` xizmatlari bilan bog'lash.
    *   **Kirish:** API spetsifikatsiyasi, ma'lumotlar bazasi modullari, `core` xizmatlari.
    *   **Chiqish:** To'liq ishlaydigan RESTful API, autentifikatsiya va AI bilan o'zaro aloqa funksiyalari bilan.
    *   **Test:** Backend API uchun integratsiya testlari.
*   **Vazifa:** Frontend Mini App interfeysini (`app.py`, `components/*`) ishlab chiqish va Backend API bilan integratsiya qilish (`services/*`).
    *   **Kirish:** UI/UX dizayni, Backend API.
    *   **Chiqish:** Foydalanuvchilar bilan interaktiv Mini App, barcha asosiy funksiyalar (AI chat, tasdiqlash, hujjatlar) mavjud.
    *   **Test:** Frontend uchun qo'lda tekshirish va asosiy UI testlari.
*   **Vazifa:** Barcha modullar uchun birlik va integratsiya testlarini yozish va bajarish, aniqlangan xatolarni tuzatish.
    *   **Kirish:** Ishlab chiqilgan kod.
    *   **Chiqish:** Test hisobotlari, xatolarni tuzatish natijasida barqaror kod bazasi.
    *   **Test:** Test quvurini ishga tushirish va barcha testlarning muvaffaqiyatli o'tishini ta'minlash.
*   **Vazifa:** Docker konteynerlarini yaratish va `docker-compose` yordamida loyihani mahalliy muhitda ishga tushirish.
    *   **Kirish:** Ishlaydigan Frontend va Backend ilovalari.
    *   **Chiqish:** Konteynerlashtirilgan va ishga tushirilgan loyiha.
    *   **Test:** `docker-compose up` buyrug'ining muvaffaqiyatini tekshirish va ilovaning to'g'ri ishlashini sinash.
*   **Vazifa:** CI/CD quvurini sozlash va avtomatlashtirilgan testlash hamda deploy jarayonini yo'lga qo'yish.
    *   **Kirish:** Konteynerlashtirilgan ilova.
    *   **Chiqish:** Avtomatlashtirilgan testlash va deploy jarayoni.
    *   **Test:** Kod o'zgarishlari bilan quvurning ishga tushishini va belgilangan bosqichlarni muvaffaqiyatli bajarishini tekshirish.