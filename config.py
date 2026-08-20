import os
from dotenv import load_dotenv

load_dotenv()

class Config:
    SECRET_KEY = os.environ.get('SECRET_KEY', 'lqm-secret-key-2026')
    DATABASE_URL = os.environ.get('DATABASE_URL', 'lqm_leads.db')
    GROQ_API_KEY = os.environ.get('GROQ_API_KEY', '')
    AI_PROVIDER = os.environ.get('AI_PROVIDER', 'groq')
    DEBUG = False

    # Инструкция для ИИ
    BUSINESS_CONTEXT = """Sen LQM. Cosmetics markasinin güler yüzlü, uzman yapay zekâ güzellik danişmanisin.
LQM.; Türk kahvesi, gül lokumu, demli çay, nar ve Antep fistiğindan ilham alan vegan, cruelty-free ve yapişmayan dudak parlaticilari üretir.
Müşterilere Türkçe olarak samimi tavsiyeler ver. Onlari sipariş veya bilgi almak için iletişim formunu doldurmaya yönlendir."""

class DevelopmentConfig(Config):
    DEBUG = True

class ProductionConfig(Config):
    DEBUG = False

# Словарь конфигураций, который искал Python:
config_dict = {
    'development': DevelopmentConfig,
    'production': ProductionConfig,
    'default': DevelopmentConfig
}