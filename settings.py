from os import environ

SESSION_CONFIGS = [
     dict(
         name='control',
         display_name="Mercados duales: control",
         num_demo_participants=6,
         app_sequence=['control']
     ),
     dict(
         name='information',
         display_name="Mercados duales: tratamiento info-relativa",
         num_demo_participants=6,
         app_sequence=['information']
     ),
     dict(
         name='icl',
         display_name="Mercados duales: icl",
         num_demo_participants=6,
         app_sequence=['information','icl','questions'] 
     ),
]

# if you set a property in SESSION_CONFIG_DEFAULTS, it will be inherited by all configs
# in SESSION_CONFIGS, except those that explicitly override it.
# the session config can be accessed from methods in your apps as self.session.config,
# e.g. self.session.config['participation_fee']

SESSION_CONFIG_DEFAULTS = dict(
    real_world_currency_per_point=1.00, participation_fee=0.00, doc=""
)

# ISO-639 code
# for example: de, fr, ja, ko, zh-hans
LANGUAGE_CODE = 'es'

# e.g. EUR, GBP, CNY, JPY
REAL_WORLD_CURRENCY_CODE = 'USD'
USE_POINTS = False

ROOMS = []

ADMIN_USERNAME = 'admin'
# for security, best to set admin password in an environment variable
ADMIN_PASSWORD = environ.get('OTREE_ADMIN_PASSWORD')

DEMO_PAGE_INTRO_HTML = """ """

SECRET_KEY = 'rv!@_k&5rjif=kog&iqzko+_m!9%h0com$ep$mud43bj**uc*f'

# if an app is included in SESSION_CONFIGS, you don't need to list it here
INSTALLED_APPS = ['otree', 'django_user_agents', 'numpy']

STATIC_URL = '/static/'

MIDDLEWARE_CLASSES = (
    # other middlewares...
    'django_user_agents.middleware.UserAgentMiddleware',
)
