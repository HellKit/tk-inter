import os
import re
from datetime import datetime, date, timedelta


BASE_DIR = os.getcwd() # указываем текущую дерикторию
DATA_TODAY = date.today() # указываем текущую дату

def read_file_and_get_date_and_text(file_name: str) -> (list, list):
    '''Возравщаем список дат и текста'''
    path = os.path.join(BASE_DIR, file_name) # путь к файлу
    rec = re.compile(r'(\d+\.\d+\.\d+)') # компилируем регулярное выражение
    with open(path, encoding='utf') as f:
        data = f.readlines() 
        date_list = [rec.search(value)[0] for value in data]
        text = [rec.split(value)[-1].strip() for value in data]
    return date_list, text


def get_days_time(date_l: list) -> list:
    '''Возвращаем количество дней в списке'''
    # Это было создано 06.06.2020
    return [
            0 if ':' in str(year - DATA_TODAY).split()[0] 
            else int(str(year - DATA_TODAY).split()[0]) 
            for year in [date(int(val[2]), int(val[1]), int(val[0])) 
            for val in [value.split('.') for value in date_l]]
        ]
        

def get_dict_sorted_list(texts: list, days: list) -> dict:
    '''Возвращаем отсортированные данные 
    по возрастанию в виде словоря'''
    dict_num_list = {
        days[idx]: text for idx, text in enumerate(texts)
    } # записываем начальные данные в словарь key: value - (key - date, value - text)
    days = sorted(days)
    return {
        days[idx]: dict_num_list[days[idx]] 
        for idx in range(len(dict_num_list))
    }

def result_text_date(arg: str, day: int) -> str:
    '''Выводит дни в правильном склонении'''
    if arg == 'next':
        args = ('Остался', 'Осталось')
    else: # 'prev'
        args = ('Прошел', 'Прошло')
        
    if day % 10 == 1 and day != 11:
        return f'{args[0]} {day} день :'
    elif day % 10 in [2, 3, 4] and day // 10 not in [1]:
        return f'{args[1]} {day} дня :'
    elif day == 0:
        return 'Сегодня :'
    else:
        return f'{args[1]} {day} дней :'

if __name__ == '__main__':
    date_list, texts = (
        read_file_and_get_date_and_text('do.txt')
    )
    # print(date_list.)
    # print(f'{date_list=}\n')
    # print(f'{text=}\n')
    days_list = get_days_time(date_list)
    # print(days_list)
    days_texts = get_dict_sorted_list(texts, days_list)
    print(days_texts)
    