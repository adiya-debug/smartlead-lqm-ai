import sqlite3
import os
from config import Config

# Подключение к базе данных
def get_db():
    db_path = Config.DATABASE_URL.replace('sqlite:///', '')
    conn = sqlite3.connect(db_path)
    conn.row_factory = sqlite3.Row
    return conn

# Создание таблицы клиентов (лидов)
def init_db(app):
    conn = get_db()
    conn.execute('''
        CREATE TABLE IF NOT EXISTS leads (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            isim TEXT NOT NULL,
            telefon TEXT NOT NULL,
            mesaj TEXT,
            tarih TIMESTAMP DEFAULT CURRENT_TIMESTAMP
        )
    ''')
    conn.commit()
    conn.close()

# Функция добавления нового клиента
def lead_ekle(isim, telefon, mesaj=""):
    conn = get_db()
    cursor = conn.cursor()
    # Защита от взлома (SQL Injection) с помощью знаков вопроса
    cursor.execute('INSERT INTO leads (isim, telefon, mesaj) VALUES (?, ?, ?)', (isim, telefon, mesaj))
    conn.commit()
    conn.close()

# Функция получения всех клиентов
def tum_leadler():
    conn = get_db()
    leads = conn.execute('SELECT * FROM leads ORDER BY tarih DESC').fetchall()
    conn.close()
    return [dict(lead) for lead in leads]