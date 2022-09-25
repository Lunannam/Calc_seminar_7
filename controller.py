import calculator as calcul
import ui
import logs


def msg_compl(first_r, first_mn, second_r, second_mn, sign):
    '''
    Функция получает данные и формирует строку из них
    '''
    if first_mn >= 0:
        data_log = '(' + str(first_r) + ' + ' + str(first_mn) + 'j' + ')' + ' ' + sign + ' ' + '(' + str(second_r)
    elif first_mn < 0:
        data_log = '(' + str(first_r) + ' + (' + str(first_mn) + 'j)' + ')' + ' ' + sign + ' ' + '(' + str(second_r)
    if second_mn >= 0:
        data_log += ' + ' + str(second_mn) + 'j' + ')'
    if second_mn < 0:
        data_log += ' + (' + str(second_mn) + 'j)' + ')'
    return data_log


def button_click():
    '''
    Функция запрашивает данные, решает и выводит
    '''
    name = ui.choice_calc('')
    if name == 1:
        first_r = ui.rational_number(1)
        sign = ui.operation('Введите знак операции: (+, -, *, /): ')
        second_r = ui.rational_number(2)
        second_mn = 0
        calcul.init_ratio(first_r, second_r)
        data_log = '' + str(first_r) + ' ' + sign + ' ' + str(second_r)
    elif name == 2:
        first_r, first_mn = ui.complex_number(1)
        sign = ui.operation('Введите знак операции: (+, -, *, /): ')
        second_r, second_mn = ui.complex_number(2)
        calcul.init_compl(first_r, first_mn, second_r, second_mn)
        data_log = msg_compl(first_r, first_mn, second_r, second_mn, sign)
    if calcul.check_dev_null(second_r, second_mn, sign) == True:
        result = 'Деление на 0 невозможно!'
        print(result)
    else:
        if sign == '+':
            result = calcul.sum()
        if sign == '-':
            result = calcul.sub()
        if sign == '*':
            result = calcul.mult()
        if sign == '/':
            result = calcul.div()
        # data_log = '' + str(first_r) + ' ' + sign + ' ' + str(second_r)
        # print(f"Для этого примера: {data_log} ответ будет: {result}")
        # logs.logger(data_log, result)
    # elif name == 2:
    #     first_r = ui.complex_number('Введите действительную часть первого числа: ')
    #     first_mn = ui.complex_number('Введите мнимую часть первого числа: ')
    #     sign = ui.operation('Введите знак операции: (+, -, *, /): ')
    #     second_r = ui.complex_number('Введите действительную часть второго числа: ')
    #     second_mn = ui.complex_number('Введите мнимую часть второго числа: ')
    #     calcul.init_compl(first_r, first_mn, second_r, second_mn)

        # result = calcul.check_dev_null(second_r, second_mn, sign)
        # if result == 'Деление на 0 невозможно!':
        #     print(result)
        # else:
        #     if sign == '+':
        #         result = calcul.sum()
        #     if sign == '-':
        #         result = calcul.sub()
        #     if sign == '*':
        #         result = calcul.mult()
        #     if sign == '/':
        #         # if second_r == 0 and second_mn == 0:
        #         #     result = 'Деление на 0 невозможно!'
        #         #     print('Деление на 0 невозможно!')
        #         #     data_log = msg_compl(first_r, first_mn, second_r, second_mn, sign)
        #         #     logs.logger(data_log, result)
        #         #     exit()
        #         # else:
        #         result = calcul.div()

        # data_log = msg_compl(first_r, first_mn, second_r, second_mn, sign)
    ui.output_result(data_log, result)
    logs.logger(data_log, result)
