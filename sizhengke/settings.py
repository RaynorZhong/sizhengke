"""
Django settings for sizhengke project.

Generated by 'django-admin startproject' using Django 3.2.6.

For more information on this file, see
https://docs.djangoproject.com/en/3.2/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/3.2/ref/settings/
"""

from pathlib import Path
from decouple import config

# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/3.2/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'django-insecure-aj_c8(^@-s$#x(7)$zhoxijx1e7q$0s@66s61dgoihhwjh9e^_'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = config('DEBUG', default=False, cast=bool)

ALLOWED_HOSTS = ['*']


# Application definition

INSTALLED_APPS = [
    'cqmu',
    'simplepro',
    'simpleui',
    'import_export',
    'django_static_jquery3',
    'django_secure_password_input',
    'django_simple_tags',
    'captcha',
    'django_admin_safe_login',
    'multi_captcha_admin',
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'django.contrib.sitemaps',
    'debug_toolbar'
]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
    # DebugTool
    'debug_toolbar.middleware.DebugToolbarMiddleware',
    # 加入simplepro的中间件
    'simplepro.middlewares.SimpleMiddleware'
]

ROOT_URLCONF = 'sizhengke.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [BASE_DIR / 'templates'],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
            ],
        },
    },
]

WSGI_APPLICATION = 'sizhengke.wsgi.application'


# Database
# https://docs.djangoproject.com/en/3.2/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': config('DB_NAME'),
        'USER': config('DB_USER'),
        'PASSWORD': config('DB_PASSWORD', default=''),
        'HOST': config('DB_HOST'),
        'PORT': '3306',
    }
}

# Password validation
# https://docs.djangoproject.com/en/3.2/ref/settings/#auth-password-validators

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


# Internationalization
# https://docs.djangoproject.com/en/3.2/topics/i18n/

LANGUAGE_CODE = 'zh-hans'

TIME_ZONE = 'Asia/Chongqing'

USE_I18N = True

USE_L10N = True

USE_TZ = False


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/3.2/howto/static-files/

STATIC_URL = '/static/'
STATIC_ROOT = config('STATIC_ROOT', default='/root/sizhengke/static/')

STATICFILES_DIRS = [
    BASE_DIR / "static",
    ]

# Media files

MEDIA_URL = '/media/'
MEDIA_ROOT = config('MEDIA_ROOT', default='/root/sizhengke/media/')

# 配置simpleui静态文件离线模式 不填该项或者为False的时候，默认从第三方的cdn获取
SIMPLEUI_STATIC_OFFLINE = True

# Default primary key field type
# https://docs.djangoproject.com/en/3.2/ref/settings/#default-auto-field

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'

# DebugTool Settings

INTERNAL_IPS = [
    '127.0.0.1',
]

# SimplePro 版权信息
SIMPLEPRO_INFO = False
# 配置Simple Pro是否显示首页的图标，默认为True，显示图表，False不显示
SIMPLEPRO_CHART_DISPLAY = False
SIMPLEUI_LOGO = '../../static/sizhengke/banner.png'

# COS Settings
COS_SECRET_ID = config('COS_SECRET_ID', None)
COS_SECRET_KEY = config('COS_SECRET_KEY', None)
COS_REGION = config('COS_REGION', None)
COS_BUCKET = config('COS_BUCKET', None)

# Count Of Page
COP = config('COP', default=10, cast=int)

# Auth
LOGIN_REDIRECT_URL = '/index'
LOGIN_URL = '/admin/login/'
LOGOUT_REDIRECT_URL = '/'

# SESSION
# 7200秒后失效(2小时)
SESSION_COOKIE_AGE = 7200

# 初始密码
INIT_PASSWORD = config('INIT_PASSWORD')

# 验证码配置
MULTI_CAPTCHA_ADMIN = {
    'engine': 'simple-captcha',
}
# 验证码图片大小
CAPTCHA_IMAGE_SIZE = (78, 35)
# 字符个数
CAPTCHA_LENGTH = 4
# 超时
CAPTCHA_TIMEOUT = 10