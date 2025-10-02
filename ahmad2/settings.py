from pathlib import Path

# المسار الأساسي للمشروع
BASE_DIR = Path(__file__).resolve().parent.parent

# مفتاح الأمان (غيّره في بيئة الإنتاج)
SECRET_KEY = 'django-insecure-(dodk^8!v(j_9n(c7tuzzqcg2&n(exfj)sk764k&-6u6q6j1c6'

# ⚠️ لا تستخدم التصحيح (DEBUG) في بيئة الإنتاج
DEBUG = True

# hosts المسموح بها
ALLOWED_HOSTS = []


# التطبيقات المثبتة
INSTALLED_APPS = [
    'django.contrib.admin',          # لوحة التحكم
    'django.contrib.auth',           # نظام التوثيق
    'django.contrib.contenttypes',   # إدارة أنواع المحتوى
    'django.contrib.sessions',       # الجلسات
    'django.contrib.messages',       # الرسائل
    'django.contrib.staticfiles',    # الملفات الثابتة (CSS, JS, صور)

    # التطبيقات الخاصة بالمشروع
    'Clients',   # تطبيق العملاء
    'Fleet',     # تطبيق السيارات
    'Booking',   # تطبيق الحجوزات والدفع
]

# الوسائط (Middleware)
MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

# ملف الروابط (urls)
ROOT_URLCONF = 'ahmad2.urls'

# إعدادات القوالب
TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [],      # مسارات القوالب المخصصة (HTML)
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
            ],
        },
    },
]

# واجهة WSGI
WSGI_APPLICATION = 'ahmad2.wsgi.application'


# قاعدة البيانات (SQLite افتراضية)
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'db.sqlite3',
    }
}


# التحقق من كلمات المرور
AUTH_PASSWORD_VALIDATORS = [
    {
        'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator',
    },
]


# الإعدادات الدولية
LANGUAGE_CODE = 'ar'         # لغة المشروع (العربية)
TIME_ZONE = 'Asia/Riyadh'    # المنطقة الزمنية (الرياض)

USE_I18N = True  # دعم الترجمات
USE_TZ = True    # استخدام المنطقة الزمنية


# الملفات الثابتة (CSS, JavaScript, صور)
STATIC_URL = 'static/'

# نوع المفتاح الافتراضي للجداول
DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'
