import os
import re
from datetime import date, datetime


BASE_DIR = os.getcwd()  # указываем текущую дерикторию
COLORS = ('red', 'orange', 'yellow', 'white')


def read_file_and_get_date_and_text(file_name: str) -> (list, list):
    '''Возравщает список дат и текста'''
    path = os.path.join(BASE_DIR, file_name)  # путь к файлу
    rec = re.compile(r'(\d+\.\d+\.\d+)')  # компилируем регулярное выражение
    with open(path, encoding='utf') as f:
        data = f.readlines()
        date_list = [rec.search(value)[0] for value in data]
        text = [rec.split(value)[-1].strip() for value in data]
    return date_list, text


def get_days_time(date_l: list) -> list:
    '''Возвращает количество дней в списке'''
    return [(datetime.strptime('.'.join(day.split('.')[::-1]),
                               '%Y.%m.%d').date() - date.today()).days for day in date_l]


def get_dict_sorted_list(texts: list, days: list) -> dict:
    '''Возвращает отсортированные данные 
    по возрастанию в виде словоря'''
    list_dict = [{'days': days[idx], 'text': text}
                 for idx, text in enumerate(texts)]
    return sorted(list_dict, key=lambda value: value['days'])


def add_color(data: list) -> list:
    '''Добавляет цвет для текста'''
    for element in data:
        if element['days'] < 0:
            element['color'] = COLORS[0]
        elif element['days'] == 0:
            element['color'] = COLORS[1]
        elif element['days'] < 7:
            element['color'] = COLORS[2]
        else:
            element['color'] = COLORS[3]
    return data


def result_text_date(arg: str, day: int) -> str:
    '''Выводит дни в правильном склонении'''
    if arg == 'next':
        args = (f'Остался {day}', f'Осталось {day}')
    else:  # 'prev'
        args = (f'Прошел {day}', f'Прошло {day}')

    if day % 10 == 1 and day != 11:
        return f'{args[0]} день :'
    elif day % 10 in range(2,5) and day // 10 != 1:
        return f'{args[1]} дня :'
    elif day == 0:
        return 'Сегодня :'
    else:
        return f'{args[1]} дней :'


if __name__ == '__main__':
    date_list, texts = (
        read_file_and_get_date_and_text('do.txt')
    )
    days_list = get_days_time(date_list)
    list_dict = get_dict_sorted_list(texts, days_list)
    list_dict = add_color(list_dict)
    print(list_dict)
