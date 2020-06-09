from tkinter import Tk, Canvas

from logic_func import (
    read_file_and_get_date_and_text,
    get_days_time, get_dict_sorted_list,
    result_text_date
)


def root_settings():
    '''Создаем root Tk'''
    root = Tk()
    root.title('Надо бы, что-то тут написать!')
    root.geometry('900x600')
    root.resizable(width=False, height=False)
    return root


def canvas_settings(root):
    '''Создаем Canvas settings'''
    canva = Canvas(root, bg='black', width=1920, height=1080)
    canva.create_text(450, 50, text='Мои текущие задачи',
                    font='Verdana 28', fill='yellow')
    canva.create_line(250, 70, 650, 70, fill='yellow')
    return canva


def settings_message(idx: int, data_text: str, text: str, color: str):
    '''Для смены цветов и отображения текста'''
    canva.create_text(450, 100+idx, text=f'{data_text} {text}',
                    font='Verdana 14', fill=f'{color}')


def message_print(canva, days_texts: dict):
    '''Главная функция по выводу в интерфейс приложения'''
    for idx, value in enumerate(days_texts.items()):
        idx *= 30
        if value[0] > 0:
            text_date = result_text_date('next', value[0])
        else:
            text_date = result_text_date('prev', -value[0])
        if value[0] > 0 and value[0] <= 7:
            settings_message(idx, text_date, value[1], 'yellow')
        elif value[0] < 0:
            settings_message(idx, text_date, value[1], 'red')
        elif value[0] > 7:
            settings_message(idx, text_date, value[1], 'white')
        else:
            settings_message(idx, text_date, value[1], 'orange')


if __name__ == '__main__':
    root = root_settings()
    canva = canvas_settings(root)
    
    date_list, texts = (
        read_file_and_get_date_and_text('do.txt')
    )
    days_list = get_days_time(date_list)
    days_texts_dict = get_dict_sorted_list(texts, days_list)
    message_print(canva, days_texts_dict)

    canva.pack()
    root.mainloop()
