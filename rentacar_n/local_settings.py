ALLOWED_HOSTS = ['*']

SECRET_KEY = '0gix#*m^nlgox^pnw$x*ge++rmowf)p8u3erx5!_nh8_n(9d2t'

DEFAULT_FROM_EMAIL='rent@brainsite.ru'
EMAIL_HOST = 'smtp.yandex.ru'
EMAIL_HOST_PASSWORD = 'RentaCar123'
EMAIL_HOST_USER = 'rent@brainsite.ru'
EMAIL_PORT = '465'
EMAIL_USE_SSL=True


DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': 'renta_n',
        'USER': 'django',
        'PASSWORD': '34t3t545g3f4f3',
        'HOST': 'localhost',
    }
}