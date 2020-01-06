import os
from decouple import config
from dj_database_url import parse as dburl

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/2.2/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = config('SECRET_KEY')

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = config('DEBUG', default=False, cast=bool)

ALLOWED_HOSTS = ['127.0.0.1', 'e-contas-final.herokuapp.com', '192.168.1.4']

# Application definition
INSTALLED_APPS = [
    'baton',
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'core',
    'baton.autodiscover',
    'bootstrapform',
    'easy_pdf',
]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'econtas.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': ['templates'],
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

WSGI_APPLICATION = 'econtas.wsgi.application'

# Database
# https://docs.djangoproject.com/en/2.2/ref/settings/#databases
default_dburl = 'sqlite:///' + os.path.join(BASE_DIR, 'db.sqlite3')

DATABASES = {'default': config('DATABASE_URL', default=default_dburl, cast=dburl), }

# Password validation
# https://docs.djangoproject.com/en/2.2/ref/settings/#auth-password-validators

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
# https://docs.djangoproject.com/en/2.2/topics/i18n/

LANGUAGE_CODE = 'pt-br'

TIME_ZONE = 'America/Sao_Paulo'

USE_I18N = True

USE_L10N = True

USE_TZ = True

# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/2.2/howto/static-files/

STATIC_URL = '/static/'
STATIC_ROOT = '/static/'
MEDIA_URL = '/media/'
MEDIA_ROOT = '/media/'

STATIC_ROOT = os.path.join(BASE_DIR, 'staticfiles')
STATICFILES_DIRS = [
    os.path.join(BASE_DIR, "static"),
    'static'
]

LOGIN_URL = 'login'
LOGIN_REDIRECT_URL = 'adm'
LOGOUT_REDIRECT_URL = 'index'

# CONFIGURAÇÕES PERSONALIZADAS
DATE_INPUT_FORMATS = ['%d/%m/%Y']

# CONFIGURAÇÕES DO ADM-BATON
BATON = {
    'SITE_HEADER': 'E-Contas',
    'SITE_TITLE': 'E-Contas',
    'INDEX_TITLE': 'E-Contas Administração',
    'SUPPORT_HREF': 'http://e-contas-final.herokuapp.com/econtas/contato',
    'COPYRIGHT': 'copyright © 2019 <a href="http://e-contas-final.herokuapp.com/econtas/contato">E-Contas S.A </a>',
    # noqa
    'POWERED_BY': '<a href="https://github.com/wevertonmatias">Weverton Matias</a>',
    'CONFIRM_UNSAVED_CHANGES': True,
    'SHOW_MULTIPART_UPLOADING': True,
    'ENABLE_IMAGES_PREVIEW': True,
    'MENU': (
        {'type': 'title', 'label': 'main', 'apps': ('auth',)},
        {
            'type': 'app',
            'name': 'auth',
            'label': 'Authentication',
            'icon': 'fa fa-lock',
            'models': (
                {
                    'name': 'user',
                    'label': 'Users'
                },
                {
                    'name': 'group',
                    'label': 'Groups'
                },
            )
        },
        {'type': 'title', 'label': 'Contents', 'apps': ('flatpages',)},
        {'type': 'model', 'label': 'Pages', 'name': 'flatpage', 'app': 'flatpages'},
        {'type': 'free', 'icon': 'fas fa-print', 'label': 'Relatórios',
         'url': 'http://e-contas-final.herokuapp.com/adm/relatorio/'},
        {'type': 'free', 'icon': 'fas fa-chart-pie', 'label': 'Gráfico',
         'url': 'http://e-contas-final.herokuapp.com/adm/grafico/'},
        {'type': 'free', 'icon': 'fas fa-plus-circle', 'label': 'Cadastrar', 'children': [
            {'type': 'model', 'label': 'A Model', 'name': 'mymodelname', 'app': 'myapp', 'icon': 'fa fa-gavel'},
            {'type': 'free', 'label': 'Vendas', 'url': 'http://e-contas-final.herokuapp.com/adm/cadastro/venda/'},
            {'type': 'free', 'label': 'Pagamentos',
             'url': 'http://e-contas-final.herokuapp.com/adm/cadastro/pagamento'},
            {'type': 'free', 'label': 'Empresas', 'url': 'http://e-contas-final.herokuapp.com/adm/cadastro/empresa/'},
            {'type': 'free', 'label': 'Fornecedores',
             'url': 'http://e-contas-final.herokuapp.com/adm/cadastro/fornecedor/'},
            {'type': 'free', 'label': 'Local de Recebimento',
             'url': 'http://e-contas-final.herokuapp.com/adm/cadastro/local_de_recebimento'},
        ]},
        {'type': 'free', 'icon': 'fas fa-edit', 'label': 'Listar/Atualizar/Deletar', 'children': [
            {'type': 'model', 'label': 'A Model', 'name': 'mymodelname', 'app': 'myapp', 'icon': 'fa fa-gavel'},
            {'type': 'free', 'label': 'Vendas', 'url': 'http://e-contas-final.herokuapp.com/adm/lista/venda/'},
            {'type': 'free', 'label': 'Pagamentos', 'url': 'http://e-contas-final.herokuapp.com/adm/lista/pagamento'},
            {'type': 'free', 'label': 'Empresas', 'url': 'http://e-contas-final.herokuapp.com/adm/lista/empresa/'},
            {'type': 'free', 'label': 'Fornecedores',
             'url': 'http://e-contas-final.herokuapp.com/adm/lista/fornecedor/'},
            {'type': 'free', 'label': 'Local de Recebimento',
             'url': 'http://e-contas-final.herokuapp.com/adm/lista/local_recebimento'},
        ]},

    ),
}
