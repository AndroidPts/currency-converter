        feature/timofey-moduleB-cache
import json
from datetime import datetime, timedelta
import os

CACHE_FILE = "currency_cache.json"
CACHE_DURATION_HOURS = 1

def load_cache():
    """Загружает данные из файла кэша, если он существует и не устарел."""
    if not os.path.exists(CACHE_FILE):
        return None

    try:
        with open(CACHE_FILE, 'r') as f:
            cache = json.load(f)
        # Проверяем, не устарел ли кэш
        timestamp = datetime.fromisoformat(cache['timestamp'])
        if datetime.now() - timestamp > timedelta(hours=CACHE_DURATION_HOURS):
            print("Кэш устарел.")
            return None
        print("Использую данные из кэша.")
        return cache['rates']
    except (json.JSONDecodeError, KeyError, ValueError):
        print("Файл кэша поврежден. Будет загружен заново.")
        return None

def save_cache(rates):
    """Сохраняет курсы валют и текущее время в файл кэша."""
    cache_data = {
        'timestamp': datetime.now().isoformat(),
        'rates': rates
    }
    try:
        with open(CACHE_FILE, 'w') as f:
            json.dump(cache_data, f, indent=4)
        print("Курсы сохранены в кэш.")
    except IOError as e:
        print(f"Ошибка записи кэша: {e}")

def get_rates(api_fetch_function):
    """
    Основная функция: пытается загрузить из кэша.
    Если не удалось, вызывает функцию из Модуля А.
    """
    rates = load_cache()
    if rates is None:
        print("Загружаю свежие курсы через API...")
        rates = api_fetch_function()
        if rates:
            save_cache(rates)
    return rates
import json
from datetime import datetime, timedelta
import os

CACHE_FILE = "currency_cache.json"
CACHE_DURATION_HOURS = 1

def load_cache():
    """Загружает данные из файла кэша, если он существует и не устарел."""
    if not os.path.exists(CACHE_FILE):
        return None

    try:
        with open(CACHE_FILE, 'r') as f:
            cache = json.load(f)
        # Проверяем, не устарел ли кэш
        timestamp = datetime.fromisoformat(cache['timestamp'])
        if datetime.now() - timestamp > timedelta(hours=CACHE_DURATION_HOURS):
            print("Кэш устарел.")
            return None
        print("Использую данные из кэша.")
        return cache['rates']
    except (json.JSONDecodeError, KeyError, ValueError):
        print("Файл кэша поврежден. Будет загружен заново.")
        return None

def save_cache(rates):
    """Сохраняет курсы валют и текущее время в файл кэша."""
    cache_data = {
        'timestamp': datetime.now().isoformat(),
        'rates': rates
    }
    try:
        with open(CACHE_FILE, 'w') as f:
            json.dump(cache_data, f, indent=4)
        print("Курсы сохранены в кэш.")
    except IOError as e:
        print(f"Ошибка записи кэша: {e}")

def get_rates(api_fetch_function):
    """
    Основная функция: пытается загрузить из кэша.
    Если не удалось, вызывает функцию из Модуля А.
    """
    rates = load_cache()
    if rates is None:
        print("Загружаю свежие курсы через API...")
        rates = api_fetch_function()
        if rates:
            save_cache(rates)
    return rates
        main
    