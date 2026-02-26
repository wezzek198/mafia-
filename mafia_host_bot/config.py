import os
import sys
import logging

# ========== ОСНОВНЫЕ НАСТРОЙКИ ==========

# Токен теперь только из переменной окружения!
API_TOKEN = os.environ.get('BOT_TOKEN', '')   # у @BotFather для нового бота!
ADMIN_ID = 1307172745  # Ваш Telegram ID (можно добавить второй: 7294311247)
SKIP_PENDING = False  # Пропустить ожидающие сообщения при старте

# ========== НАСТРОЙКИ ИГРЫ ==========
PLAYERS_COUNT_TO_START = 4  # Минимум игроков для начала
PLAYERS_COUNT_LIMIT = 10    # Максимум игроков
REQUEST_OVERDUE_TIME = 10 * 60  # 10 минут в секундах
WORD_BASE = 'words.txt'  # Файл со словами (в той же папке что и config.py)
DELETE_FROM_EVERYONE = False  # Удалять сообщения у всех или только у игроков

# ========== ВЕБХУКИ (ОТКЛЮЧИТЬ ДЛЯ ПРОСТОГО ЗАПУСКА!) ==========
SET_WEBHOOK = False  # Меняем на False для простого запуска!

# Если SET_WEBHOOK = True, раскомментируйте и настройте:
# SERVER_IP = 'ваш.ip.адрес'
# SERVER_PORT = 8443  # или 443, 88
# SSL_CERT = 'путь/к/cert.pem'
# SSL_PRIV = 'путь/к/private.key'

# ========== ЛОГИРОВАНИЕ ==========
LOGGER_LEVEL = logging.INFO

# ========== ДОПОЛНИТЕЛЬНЫЕ НАСТРОЙКИ ==========
# Путь к базе данных (если используется)
DATABASE_PATH = 'mafia_game.db'

# Язык интерфейса (ru/en)
LANGUAGE = 'ru'

# Время на ход (в секундах)
DAY_TIME = 120    # 2 минуты на дневное обсуждение
NIGHT_TIME = 60   # 1 минута на ночное действие
VOTE_TIME = 30    # 30 секунд на голосование