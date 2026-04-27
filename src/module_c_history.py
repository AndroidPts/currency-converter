import json, os
from collections import deque

HISTORY_FILE = "conversion_history.json"
MAX_HISTORY = 5

def load_history():
    if not os.path.exists(HISTORY_FILE):
        return deque(maxlen=MAX_HISTORY)
    try:
        with open(HISTORY_FILE, 'r') as f:
            data = json.load(f)
            return deque(data, maxlen=MAX_HISTORY)
    except (json.JSONDecodeError, IOError):
        return deque(maxlen=MAX_HISTORY)

def save_history(history):
    try:
        with open(HISTORY_FILE, 'w') as f:
            json.dump(list(history), f, indent=4, ensure_ascii=False)
    except IOError as e:
        print(f"Ошибка сохранения истории: {e}")

def add_to_history(from_curr, to_curr, amount, result):
    history = load_history()
    record = f"{amount} {from_curr} -> {result:.2f} {to_curr}"
    history.append(record)
    save_history(history)

def show_history():
    history = load_history()
    if not history:
        print("\nИстория конвертаций пуста.")
        return
    print("\n--- Последние 5 конвертаций ---")
    for i, record in enumerate(history, 1):
        print(f"{i}: {record}")