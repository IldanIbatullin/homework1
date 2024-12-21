import os
from functools import wraps

def log(filename=None):
    """
    Декоратор для логирования работы функции.
    Если filename задан, логи записываются в файл.
    Если filename не задан, логи выводятся в консоль.
    При возникновении ошибки логируется сообщение об ошибке и входные параметры функции.
    """
    def wrapper(func):
        @wraps(func)
        def inner(*args, **kwargs):
            try:
                result = func(*args, **kwargs)
                message = f"{func.__name__} ok"
            except Exception as e:
                message = f"{func.__name__} error: {e}. Inputs: {args}, {kwargs}"

            if filename:
                os.makedirs(os.path.dirname(filename), exist_ok=True)
                with open(filename, "a", encoding="utf-8") as file:
                    file.write(message + "\n")
            else:
                print(message)

            return result

        return inner

    return wrapper
