import check_number as f
from colorama import Fore
from colorama import Style

def rational_number(number:str) -> float:
    '''
    Ввод рационального числа
    '''
    input_data = Fore.BLUE + f'Введите {number} рациональное число: ' + Style.RESET_ALL
    return f.check_float_number(input_data)

def complex_number(number:str) -> complex:
    '''
    Ввод комплексного числа
    '''
    input_d = Fore.GREEN + f'Введите действительную часть {number} числа: ' + Style.RESET_ALL
    input_mn = Fore.GREEN + f'Введите мнимую часть {number} числа: ' + Style.RESET_ALL
    return f.check_int_number(input_d), f.check_int_number(input_mn)

def operation(oper:str) -> str:
    '''
    Ввод операции
    '''
    input_sign = Fore.YELLOW + f'Введите знак операции: (+, -, *, /):{oper}' + Style.RESET_ALL
    return f.check_symbol(input_sign)

def choice_calc(number:str) -> int:
    '''
    Выбор калькулятора
    '''
    print(Fore.YELLOW + 'Для выбора калькулятора рациональных чисел нажмите 1, для комплексных - 2: ' + Style.RESET_ALL)
    return f.check_calc(number)

def output_result(data, res):
    '''
    Вывод результата
    '''
    print(Fore.YELLOW + f"Для этого примера: {data} ответ будет: {res}"  + Style.RESET_ALL)