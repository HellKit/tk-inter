from tkinter import Tk, Canvas
from logic_func import (
    read_file_and_get_date_and_text,
    get_dict_sorted_list, result_text_date,
    add_color
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
    canva = Canvas(root, bg='black', width=900, height=600)
    canva.create_text(450, 50, text='Мои текущие задачи',
                      font='Verdana 28', fill='yellow')
    canva.create_line(250, 70, 650, 70, fill='yellow')
    return canva


def message_print(canva, days_texts: list):
    '''Главная функция по выводу в интерфейс приложения'''
    for idx, element in enumerate(days_texts):
        if element['days'] > 0:
            text_date = result_text_date('next', element['days'])
        else:
            text_date = result_text_date('prev', -element['days'])
        canva.create_text(150, 100+idx*30, text=f"{text_date} {element['text']}",
                          anchor='w', font='Verdana 14', fill=f"{element['color']}")


if __name__ == '__main__':
    root = root_settings()
    canva = canvas_settings(root)

    days_list, texts = (
        read_file_and_get_date_and_text('do.txt')
    )
    list_dict = get_dict_sorted_list(texts, days_list)
    list_dict = add_color(list_dict)
    message_print(canva, list_dict)

    canva.pack()
    root.mainloop()
