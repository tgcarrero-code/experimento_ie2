SESSION_CONFIGS = [
    dict(
        name='justicia_bienestar',
        display_name='Justicia y Bienestar',
        app_sequence=['justicia_bienestar'],
        num_demo_participants=20,
    ),
]

SESSION_CONFIG_DEFAULTS = dict(
    real_world_currency_per_point=1,
    participation_fee=7.50,
)

LANGUAGE_CODE = 'es'
REAL_WORLD_CURRENCY_CODE = 'PEN'
USE_POINTS = False
SECRET_KEY = 'justicia_bienestar_2026_secret_key'
ADMIN_USERNAME = 'admin'
ADMIN_PASSWORD = 'admin123'
DEBUG = True
