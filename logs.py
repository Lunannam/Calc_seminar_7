from datetime import datetime as dt

def logger(data, result):
    """
    Записывает время операции, саму операцию и её результат
    """
    time = dt.now().strftime('%m.%d.%Y - %H:%M')
    with open('log.csv', 'a') as file:
        file.write(f'{time}: {data} = {result}\n')