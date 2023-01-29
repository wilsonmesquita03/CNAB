import ipdb
from datetime import date, time

def get_type(type_num):
    types = [
        'Débito', 
        'Boleto', 
        'Financiamento', 
        'Crédito', 
        'Recebimento Empréstimo',
        'Vendas',
        'Recebimento TED',
        'Recebimento DOC',
        'Aluguel'
    ]

    return types[int(type_num) - 1]

def get_nature(type_num):
    exit = [2,3,9]

    if int(type_num) in exit:
        return 'exit'
    else:
        return 'entrance'

def get_date(date_str):
    year = int(date_str[0:4])
    month = int(date_str[4:6])
    day = int(date_str[6:8])
    
    new_date = date(year, month, day)

    return str(new_date)

def get_value(value_str):
    value_num = int(value_str)

    return value_num / 100.00   

def get_hour(value_str):
    hour = int(value_str[0:2])
    minute = int(value_str[2:4])
    seconds = int(value_str[4:6])

    new_time = time(hour, minute, seconds)

    return str(new_time)