from src.module_a_api import fetch_rates
from src.module_b_cache import get_rates
from src.module_c_history import add_to_history, show_history

def convert_currency(amount, from_currency, to_currency, rates):
    """Простая логика конвертации через рубль."""
    if not rates:
        print("Нет данных о курсах. Конвертация невозможна.")
        return None
    
    required_currencies = [from_currency, to_currency]
    for curr in required_currencies:
        if curr not in rates:
            print(f"Валюта '{curr}' не найдена в доступных курсах.")
            return None
    
    amount_in_rub = amount / rates[from_currency]
    result = amount_in_rub * rates[to_currency]
    return result

def main():
    print("--- Конвертер валют с кэшем ---")
    
    rates = get_rates(fetch_rates)
    
    if not rates:
        print("Не удалось загрузить курсы. Завершение работы.")
        return

    print("Доступные валюты: RUB, USD, EUR, GBP, CNY...")
    print("(Используйте международные коды валют)")

    while True:
        print("\nМеню:")
        print("1. Конвертировать валюту")
        print("2. Показать историю конвертаций")
        print("3. Выход")
        
        choice = input("Выберите действие (1/2/3): ").strip()
        
        if choice == '1':
            try:
                amount = float(input("Введите сумму: ").strip())
                from_curr = input("Из какой валюты (код): ").strip().upper()
                to_curr = input("В какую валюту (код): ").strip().upper()
                
                result = convert_currency(amount, from_curr, to_curr, rates)
                if result is not None:
                    print(f"Результат: {amount} {from_curr} = {result:.2f} {to_curr}")
                    # Модуль Софии: сохраняем в историю
                    add_to_history(from_curr, to_curr, amount, result)
            
            except ValueError:
                print("Ошибка: введите корректное число для суммы.")
        
        elif choice == '2':
            show_history()  # Модуль Софии
        
        elif choice == '3':
            print("До свидания!")
            break
        
        else:
            print("Неверный выбор. Пожалуйста, выберите 1, 2 или 3.")

if __name__ == "__main__":
    try:
        import requests
    except ImportError:
        print("Ошибка: Установите библиотеку requests: pip install requests")
    else:
        main()