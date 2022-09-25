from ctypes import Union


x = 0
y = 0

def init_compl(ad, am, bd, bm):
    global x
    global y
    x = complex(ad, am)
    y = complex(bd, bm)

def init_ratio(a,b):
    global x
    global y
    x = float(round(a,5))
    y = float(round(b,5))

def sum():
    return x + y

def sub():
    return x - y

def mult():
    return x * y

def div():
    return x / y

def check_dev_null(denominator_r: float, denominator_mn: float, sign: str)-> bool:
    '''
    Функция проверяет деление на 0
    '''
    if denominator_r == 0 and denominator_mn == 0 and sign == '/':
        return True
        # data_log = msg_compl(first_r, first_mn, second_r, second_mn, sign)
        # logs.logger(data_log, "Деление на 0 невозможно!")
        exit()
