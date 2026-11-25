## Loyiha skeleti

1.  **`dokon-backend` repozitoriysini yaratish va Django loyihasini sozlash:**
    *   **Modul:** `core`
    *   **Kirish:** Bo'sh Git repozitoriy.
    *   **Chiqish:** `dokon-backend` papkasi ichida Django loyihasi yaratilgan, `settings.py` va `urls.py` fayllari mavjud, asosiy ma'lumotlar bazasi (PostgreSQL) konfiguratsiyasi o'rnatilgan.
    *   **Test:** `python manage.py runserver` buyrug'ini bajarish va loyihaning xatosiz ishga tushishini tekshirish.
2.  **`dokon-frontend` repozitoriysini yaratish va React loyihasini sozlash:**
    *   **Modul:** `src`
    *   **Kirish:** Bo'sh Git repozitoriy.
    *   **Chiqish:** `dokon-frontend` papkasi ichida `create-react-app` yordamida React loyihasi yaratilgan, asosiy `App.js` va `index.js` fayllari mavjud.
    *   **Test:** `npm start` yoki `yarn start` buyrug'ini bajarish va brauzerda asosiy React sahifasining ko'rinishini tekshirish.
3.  **Django ilovalarini yaratish va ro'yxatdan o'tkazish:**
    *   **Modul:** `users`, `products`, `orders`, `sms_notifications`
    *   **Kirish:** `dokon-backend` loyihasi.
    *   **Chiqish:** `users`, `products`, `orders`, `sms_notifications` nomli Django ilovalari yaratilgan (`python manage.py startapp <app_name>`) va `dokon-backend/settings.py` faylidagi `INSTALLED_APPS` ro'yxatiga qo'shilgan.
    *   **Test:** Har bir ilovaning `settings.py` da to'g'ri ro'yxatdan o'tganligini va `python manage.py check` buyrug'ining xatosiz ishlashini tekshirish.

## Modullar bo'yicha vazifalar

1.  **`users` ilovasi uchun asosiy fayl tuzilmasini yaratish:**
    *   **Modul:** `users`
    *   **Kirish:** `users` Django ilovasi.
    *   **Chiqish:** `users/models.py`, `users/serializers.py`, `users/views.py`, `users/urls.py`, `users/admin.py` fayllari yaratilgan.
    *   **Test:** Fayllarning mavjudligini va ilovaning to'g'ri yuklanishini tekshirish.
2.  **`products` ilovasi uchun asosiy fayl tuzilmasini yaratish:**
    *   **Modul:** `products`
    *   **Kirish:** `products` Django ilovasi.
    *   **Chiqish:** `products/models.py`, `products/serializers.py`, `products/views.py`, `products/urls.py`, `products/admin.py` fayllari yaratilgan.
    *   **Test:** Fayllarning mavjudligini va ilovaning to'g'ri yuklanishini tekshirish.
3.  **`orders` ilovasi uchun asosiy fayl tuzilmasini yaratish:**
    *   **Modul:** `orders`
    *   **Kirish:** `orders` Django ilovasi.
    *   **Chiqish:** `orders/models.py`, `orders/serializers.py`, `orders/views.py`, `orders/urls.py`, `orders/admin.py` fayllari yaratilgan.
    *   **Test:** Fayllarning mavjudligini va ilovaning to'g'ri yuklanishini tekshirish.
4.  **`sms_notifications` ilovasi uchun asosiy fayl tuzilmasini yaratish:**
    *   **Modul:** `sms_notifications`
    *   **Kirish:** `sms_notifications` Django ilovasi.
    *   **Chiqish:** `sms_notifications/tasks.py` (Celery vazifalari uchun), `sms_notifications/services.py` (SMS provayder bilan aloqa uchun) fayllari yaratilgan.
    *   **Test:** Fayllarning mavjudligini va ilovaning to'g'ri yuklanishini tekshirish.

## Ma'lumotlar bazasi modeli

1.  **`CustomUser` modelini aniqlash:**
    *   **Modul:** `users`
    *   **Kirish:** Foydalanuvchi autentifikatsiyasi talablari.
    *   **Chiqish:** `users/models.py` da `AbstractUser` dan meros olgan, `email` (unique), `phone_number` (unique, null=True, blank=True), `is_verified` (default=False) maydonlariga ega `CustomUser` modeli yaratilgan.
    *   **Test:** `python manage.py makemigrations users` buyrug'ini bajarish va migratsiya faylining to'g'ri yaratilganligini tekshirish.
2.  **`Category` va `Product` modellarini aniqlash:**
    *   **Modul:** `products`
    *   **Kirish:** Mahsulotlar va kategoriyalar uchun talablar.
    *   **Chiqish:** `products/models.py` da `name` (unique), `slug` (unique) maydonlariga ega `Category` modeli va `name`, `description`, `price`, `stock`, `category` (ForeignKey), `image` (ImageField, optional) maydonlariga ega `Product` modeli yaratilgan.
    *   **Test:** `python manage.py makemigrations products` buyrug'ini bajarish va migratsiya fayllarining to'g'ri yaratilganligini tekshirish.
3.  **`Cart`, `CartItem`, `Order`, `OrderItem` modellarini aniqlash:**
    *   **Modul:** `orders`
    *   **Kirish:** Savat va buyurtma jarayoni talablari.
    *   **Chiqish:** `orders/models.py` da `user` (OneToOneField) ga ega `Cart`, `cart` (ForeignKey), `product` (ForeignKey), `quantity` ga ega `CartItem`, `user` (ForeignKey), `total_price`, `status`, `created_at` ga ega `Order`, `order` (ForeignKey), `product` (ForeignKey), `quantity`, `price` ga ega `OrderItem` modellari yaratilgan.
    *   **Test:** `python manage.py makemigrations orders` buyrug'ini bajarish va migratsiya fayllarining to'g'ri yaratilganligini tekshirish.

## API yaratish

1.  **Autentifikatsiya API endpointlarini implementatsiya qilish:**
    *   **Modul:** `users`, `api`
    *   **Kirish:** `users` ilovasidagi `CustomUser` modeli va `UserSerializer`, DRF Simple JWT konfiguratsiyasi.
    *   **Chiqish:** `users/views.py` da `RegisterView`, `LoginView` (Simple JWT dan foydalanib), `TokenRefreshView` (Simple JWT dan) yaratilgan, `dokon-backend/urls.py` va `users/urls.py` da `POST /api/auth/register/`, `POST /api/auth/login/`, `POST /api/auth/token/refresh/` endpointlari konfiguratsiya qilingan.
    *   **Test:** `pytest` yoki `Django TestCase` yordamida yangi foydalanuvchini ro'yxatdan o'tkazish, tizimga kirish va tokenlarni yangilash API chaqiruvlarini simulyatsiya qilish va javoblarni tekshirish.
2.  **Mahsulotlar va kategoriyalar API endpointlarini implementatsiya qilish:**
    *   **Modul:** `products`, `api`
    *   **Kirish:** `products` ilovasidagi `Category` va `Product` modellari va ularning serializerlari.
    *   **Chiqish:** `products/views.py` da `CategoryViewSet` va `ProductViewSet` (ReadOnlyModelViewSet) yaratilgan, `dokon-backend/urls.py` va `products/urls.py` da `GET /api/products/`, `GET /api/products/{id}/`, `GET /api/categories/` endpointlari konfiguratsiya qilingan.
    *   **Test:** `pytest` yoki `Django TestCase` yordamida mahsulotlar va kategoriyalar ro'yxatini olish, bitta mahsulotni olish API chaqiruvlarini simulyatsiya qilish va javoblarni tekshirish.
3.  **Savat va buyurtmalar API endpointlarini implementatsiya qilish:**
    *   **Modul:** `orders`, `api`
    *   **Kirish:** `orders` ilovasidagi `Cart`, `CartItem`, `Order`, `OrderItem` modellari va ularning serializerlari.
    *   **Chiqish:** `orders/views.py` da `CartViewSet`, `CartItemViewSet`, `OrderViewSet` yaratilgan, `dokon-backend/urls.py` va `orders/urls.py` da `GET /api/cart/`, `POST /api/cart/items/`, `PUT /api/cart/items/{id}/`, `DELETE /api/cart/items/{id}/`, `POST /api/orders/`, `GET /api/orders/`, `GET /api/orders/{id}/` endpointlari konfiguratsiya qilingan.
    *   **Test:** `pytest` yoki `Django TestCase` yordamida savatga mahsulot qo'shish, miqdorini o'zgartirish, buyurtma berish va buyurtmalar ro'yxatini olish API chaqiruvlarini simulyatsiya qilish va javoblarni tekshirish.

## Interfeys yaratish

1.  **Asosiy UI komponentlarini yaratish:**
    *   **Modul:** `src/components/`
    *   **Kirish:** React komponentlari uchun umumiy dizayn tamoyillari.
    *   **Chiqish:** `Button.js`, `Input.js`, `ProductCard.js`, `CartItem.js` kabi qayta ishlatiladigan React komponentlari yaratilgan.
    *   **Test:** Jest va React Testing Library yordamida har bir komponentning to'g'ri render qilinishini va prop-larni qabul qilishini tekshiruvchi unit testlar yozish.
2.  **Autentifikatsiya sahifalarini yaratish:**
    *   **Modul:** `src/pages/`
    *   **Kirish:** Backend autentifikatsiya API endpointlari.
    *   **Chiqish:** `LoginPage.js` va `RegisterPage.js` sahifalari yaratilgan, ular foydalanuvchi kiritishlarini qabul qiladi va `src/services/auth.js` orqali backend API bilan aloqa qiladi.
    *   **Test:** Foydalanuvchi ma'lumotlarini kiritish, tugmani bosish va API chaqiruvining to'g'ri bajarilishini simulyatsiya qilish uchun integratsiya testlari yozish.
3.  **Mahsulotlar ro'yxati va mahsulot tafsilotlari sahifalarini yaratish:**
    *   **Modul:** `src/pages/`
    *   **Kirish:** Backend mahsulotlar API endpointlari.
    *   **Chiqish:** `ProductListPage.js` (barcha mahsulotlarni ko'rsatish) va `ProductDetailPage.js` (bitta mahsulotning batafsil ma'lumotlari) sahifalari yaratilgan, ular `src/services/products.js` orqali backend API bilan aloqa qiladi.
    *   **Test:** Sahifalarning mahsulot ma'lumotlarini API dan olib, to'g'ri ko'rsatishini tekshirish uchun integratsiya testlari yozish.

## Testlar

1.  **Backend unit testlarini yozish:**
    *   **Modul:** `users`, `products`, `orders`, `sms_notifications`
    *   **Kirish:** Har bir Django ilovasidagi modellar, serializerlar va yordamchi funksiyalar.
    *   **Chiqish:** Har bir modulning `tests.py` faylida model xulq-atvori, serializer validatsiyasi va kichik funksiyalar uchun unit testlar yozilgan.
    *   **Test:** `python manage.py test <app_name>` buyrug'ini bajarish va barcha testlarning muvaffaqiyatli o'tishini tekshirish.
2.  **Frontend unit testlarini yozish:**
    *   **Modul:** `src/components/`, `src/utils/`
    *   **Kirish:** React komponentlari va yordamchi funksiyalar.
    *   **Chiqish:** Har bir komponent va utilit fayli uchun Jest va React Testing Library yordamida unit testlar yozilgan.
    *   **Test:** `npm test` yoki `yarn test` buyrug'ini bajarish va barcha testlarning muvaffaqiyatli o'tishini tekshirish.
3.  **Backend API integratsiya testlarini yozish:**
    *   **Modul:** `api`
    *   **Kirish:** Backend API endpointlari.
    *   **Chiqish:** `api/tests.py` da autentifikatsiya, mahsulotlar, savat va buyurtmalar API endpointlarining ma'lumotlar bazasi bilan to'g'ri ishlashini tekshiruvchi testlar yozilgan.
    *   **Test:** API testlarini bajarish va turli HTTP metodlari (GET, POST, PUT, DELETE) uchun kutilgan javoblarni olishni tekshirish.

## Integratsiya ishlari

1.  **SMS xizmati (Twilio/Vonage) integratsiyasi:**
    *   **Modul:** `sms_notifications`
    *   **Kirish:** Tanlangan SMS provayderning API hujjatlari va API kalitlari.
    *   **Chiqish:** `sms_notifications/services.py` da SMS provayder API bilan aloqa qiluvchi funksiya, `sms_notifications/tasks.py` da bu funksiyani chaqiruvchi Celery vazifasi yaratilgan.
    *   **Test:** Celery vazifasini qo'lda chaqirish va belgilangan telefon raqamiga SMS kelishini tekshirish.
2.  **Celery va Redis integratsiyasi:**
    *   **Modul:** `core`, `sms_notifications`
    *   **Kirish:** Celery va Redis konfiguratsiyasi talablari.
    *   **Chiqish:** `dokon-backend/settings.py` da Celery brokeri (Redis) va natija bekendi konfiguratsiyasi, Celery ilovasi yaratilgan.
    *   **Test:** Celery ishchisini ishga tushirish (`celery -A dokon_backend worker -l info`) va `sms_notifications` dan biror vazifani yuborib, uning muvaffaqiyatli bajarilishini Celery loglarida tekshirish.
3.  **CORS konfiguratsiyasi:**
    *   **Modul:** `core`
    *   **Kirish:** Frontend domen manzili.
    *   **Chiqish:** `dokon-backend/settings.py` da `django-cors-headers` kutubxonasi yordamida ruxsat etilgan frontend domenlari uchun CORS sozlamalari o'rnatilgan.
    *   **Test:** Frontenddan backend APIga so'rov yuborish va brauzer konsolida CORS xatolarining yo'qligini tekshirish.

## Bajarish ketma-ketligi

1.  **Loyiha skeletini yaratish va asosiy konfiguratsiyalarni o'rnatish:**
    *   **Modul:** `core`, `users`, `products`, `orders`, `sms_notifications`, `src`
    *   **Kirish:** Bo'sh repozitoriylar.
    *   **Chiqish:** Backend va frontend loyihalari yaratilgan, asosiy Django ilovalari va React papkalari tuzilgan, `settings.py` da asosiy sozlamalar (DB, JWT, CORS) o'rnatilgan.
    *   **Test:** Har ikki loyihaning mustaqil ravishda ishga tushishini va asosiy konfiguratsiyalarning to'g'ri ekanligini tekshirish.
2.  **Ma'lumotlar bazasi modellarini aniqlash va migratsiyalarni bajarish:**
    *   **Modul:** `users`, `products`, `orders`
    *   **Kirish:** Foydalanuvchi, mahsulot, savat va buyurtma talablari.
    *   **Chiqish:** Barcha kerakli modellar (CustomUser, Category, Product, Cart, CartItem, Order, OrderItem) yaratilgan, migratsiyalar bajarilgan va ma'lumotlar bazasi tayyor.
    *   **Test:** Django admin panelida har bir model uchun test ma'lumotlarini kiritish va saqlash imkoniyatini tekshirish.
3.  **Backend API endpointlarini yaratish va testlash:**
    *   **Modul:** `api`, `users`, `products`, `orders`
    *   **Kirish:** Aniq belgilangan API endpointlari va ma'lumotlar bazasi modellari.
    *   **Chiqish:** Autentifikatsiya, mahsulotlar, savat va buyurtmalar uchun barcha API endpointlari DRF yordamida implementatsiya qilingan va integratsiya testlari bilan qoplangan.
    *   **Test:** Postman yoki `curl` yordamida har bir API endpointiga so'rov yuborish va kutilgan javoblarni olishni tekshirish.
4.  **Frontend interfeysini yaratish va backend API bilan integratsiya qilish:**
    *   **Modul:** `src/components/`, `src/pages/`, `src/services/`
    *   **Kirish:** Backend API endpointlari.
    *   **Chiqish:** Barcha asosiy sahifalar (Login, Register, ProductList, ProductDetail, Cart, Checkout) yaratilgan, UI komponentlari ishlatilgan va backend API bilan to'g'ri aloqa o'rnatilgan.
    *   **Test:** Brauzerda to'liq foydalanuvchi oqimini (ro'yxatdan o'tishdan buyurtma berishgacha) qo'lda bajarish va xatolarning yo'qligini tekshirish.
5.  **SMS xizmati va asinxron vazifalarni integratsiya qilish:**
    *   **Modul:** `sms_notifications`, `core`
    *   **Kirish:** SMS provayder API kalitlari va Celery/Redis konfiguratsiyasi.
    *   **Chiqish:** SMS yuborish logikasi `sms_notifications` ilovasida implementatsiya qilingan, Celery orqali asinxron tarzda ishlaydi va buyurtma berish jarayoniga integratsiya qilingan.
    *   **Test:** Buyurtma berish jarayonini yakunlash va foydalanuvchining telefon raqamiga tasdiqlash SMSi kelishini tekshirish.