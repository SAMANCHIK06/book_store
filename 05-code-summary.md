## Yaratilgan fayllar
Ushbu kod skeleti loyihaning asosiy xavfsizlik modulini va uning birlik testlarini o'z ichiga oladi. Bu loyihaning backend qismi uchun foydalanuvchi autentifikatsiyasi va avtorizatsiyasi mexanizmlarini yaratishga asos bo'ladi.

*   `workspace/backend/app/core/security.py`: Parol heshlash va JWT (JSON Web Token) tokenlarini yaratish/validatsiya qilish funksiyalarini o'z ichiga olgan asosiy xavfsizlik moduli.
*   `workspace/backend/tests/unit/test_security.py`: `security.py` modulidagi funksiyalar uchun birlik testlari. Bu testlar parollarning to'g'ri heshlanishi, JWT tokenlarining yaratilishi va validatsiya qilinishini tekshiradi.
*   `workspace/backend/requirements.txt`: Loyiha uchun zarur bo'lgan Python kutubxonalari (passlib, python-jose, pytest) ro'yxati.

## Modul tavsifi
*   **`workspace/backend/app/core/security.py`**:
    Ushbu modul foydalanuvchi autentifikatsiyasi va avtorizatsiyasi uchun asosiy xavfsizlik funksiyalarini taqdim etadi. U `bcrypt` algoritmi yordamida parollarni xavfsiz heshlaydi va `python-jose` kutubxonasi yordamida JWT tokenlarini yaratadi va validatsiya qiladi. Bu tokenlar API so'rovlarini autentifikatsiya qilish va foydalanuvchi sessiyalarini boshqarish uchun ishlatiladi.
    *   `hash_password(password: str) -> str`: Berilgan parolni xavfsiz heshlaydi.
    *   `verify_password(plain_password: str, hashed_password: str) -> bool`: Oddiy parolni heshlangan parol bilan solishtiradi va mos kelishini tekshiradi.
    *   `create_access_token(data: dict, expires_delta: Optional[timedelta] = None) -> str`: Berilgan ma'lumotlar (masalan, foydalanuvchi ID'si, roli) asosida JWT access tokenini yaratadi. Tokenning amal qilish muddati belgilanishi mumkin.
    *   `verify_token(token: str) -> Optional[dict]`: JWT tokenini validatsiya qiladi. Agar token haqiqiy va muddati o'tmagan bo'lsa, uning ichidagi ma'lumotlarni (payload) qaytaradi, aks holda `None` qaytaradi.

## Ishga tushirish
Ushbu skelet faqat xavfsizlik modulini o'z ichiga oladi. Uni ishga tushirish uchun to'liq FastAPI ilovasi (`main.py` kabi) va ulanish nuqtalari (endpoints) kerak bo'ladi. Hozircha faqat testlarni ishga tushirish mumkin.

1.  **Virtual muhit yaratish va faollashtirish:**
    ```bash
    python -m venv .venv
    source .venv/bin/activate  # Linux/macOS
    .venv\Scripts\activate     # Windows
    ```
2.  **Bog'liqliklarni o'rnatish:**
    ```bash
    pip install -r workspace/backend/requirements.txt
    ```

## Test qilish
1.  **Virtual muhitni faollashtiring** (yuqoridagi "Ishga tushirish" bo'limidagi 1-qadamga qarang).
2.  **Bog'liqliklarni o'rnating** (yuqoridagi "Ishga tushirish" bo'limidagi 2-qadamga qarang).
3.  **Testlarni ishga tushirish:**
    ```bash
    pytest workspace/backend/tests/unit/test_security.py
    ```
    Yoki barcha testlarni ishga tushirish uchun (agar ko'proq test fayllari bo'lsa):
    ```bash
    pytest workspace/backend/tests/
    ```

## Keyingi qadamlar
Review agenti tomonidan ta'kidlangan xavfli va noaniq nuqtalarni hisobga olgan holda, keyingi qadamlar quyidagilarni o'z ichiga olishi kerak:

1.  **Foydalanuvchi rollari va ruxsatlarini (RBAC) implementatsiya qilish:** Loyihaning 1-versiyasida ham turli foydalanuvchi turlari (AI sinovchisi, mahsulot menejeri) uchun tegishli ruxsatlarni joriy etish va ularning to'g'ri ishlashini tekshirish. Bu tasdiqlash mexanizmining xavfsizligi va samaradorligi uchun muhim.
2.  **AI modelining aniq turini tanlash va integratsiya qilish:** "Haqiqiy AI" modelining aniq turini tanlash, uning integratsiya tafsilotlarini yakunlash va `backend/app/core/ai_service.py` modulida AI bilan o'zaro aloqa logikasini implementatsiya qilish.
3.  **Ma'lumotlar bazasi modellarini va CRUD operatsiyalarini yaratish:** `backend/app/db/models.py` va `backend/app/db/crud.py` fayllarida ma'lumotlar bazasi modellarini va ularning CRUD operatsiyalarini to'liq implementatsiya qilish.
4.  **FastAPI endpointlarini yaratish:** `backend/app/api/v1/` papkasida barcha kerakli API endpointlarini (`auth.py`, `ai_interaction.py`, `approval.py`, `documentation.py`) yaratish va ularni `security.py` modulidagi autentifikatsiya va avtorizatsiya funksiyalari bilan bog'lash.
5.  **Avtomatlashtirilgan Frontend (UI) testlarini qo'shish:** Streamlit Mini App uchun asosiy funksionallikni qamrab oluvchi avtomatlashtirilgan UI testlarini (masalan, Playwright yoki Selenium yordamida) yozish va ularni CI/CD quvuriga integratsiya qilish.
6.  **Xavfsizlikni kuchaytirish:** DDoS/Brute-force hujumlaridan himoya qilish uchun tezlikni cheklash (rate limiting) mexanizmlarini FastAPI ilovasiga qo'shish.