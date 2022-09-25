import check_number as f

def rational_number(number:str) -> float:
    '''
    Ввод рационального числа
    '''
    return f.check_float_number(number)

def complex_number(number:str) -> complex:
    '''
    Ввод комплексного числа
    '''
    return f.check_int_number(number)

def operation(oper:str) -> str:
    '''
    Ввод операции
    '''
    return f.check_symbol(oper)

def choice_calc(number:str) -> int:
    '''
    Выбор калькулятора
    '''
    return f.check_calc(number)
