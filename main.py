from tkinter import Tk, Canvas

from logic_func import (
    read_file_and_get_date_and_text,
    get_days_time, get_dict_corted_list,
    resultate_text_date
)


def root_settings():
    root = Tk()
    root.title('Надо бы, что-то тут написать!')
    root.geometry("950x600")
    root.resizable(width=False, height=False)
    return root

def canva_settings(root):
    conv = Canvas(root, bg='black', width=4000, height=4000)
    conv.create_text(450, 50, text="Мои текущие задачи",
                    justify='center', font="Verdana 28", fill='yellow')
    conv.create_line(250, 70, 650, 70, fill='yellow')
    return conv


def color_message(idx, data_text, text, color):
    conv.create_text(450, 100+idx, text=f'{data_text} {text}',
                    justify='center', font='Verdana 14', fill=f'{color}')

def message_print(conv, days_texts: dict):
    for idx, value in enumerate(days_texts.items()):
        idx *= 30
        if value[0] > 0:
            text_date = resultate_text_date('next', value[0])
        else:
            text_date = resultate_text_date('prev', -value[0])
        if value[0] > 0 and value[0] <= 7:
            color_message(idx, text_date, value[1], 'yellow')
        elif value[0] < 0:
            color_message(idx, text_date, value[1], 'red')
        elif value[0] > 7:
            color_message(idx, text_date, value[1], 'white')
        else:
            color_message(idx, text_date, value[1], 'orange')


if __name__ == '__main__':

    date_list, texts = (
        read_file_and_get_date_and_text('do.txt')
    )
    days_list = get_days_time(date_list)
    days_texts_dict = get_dict_corted_list(texts, days_list)

    root = root_settings()
    conv = canva_settings(root)
    message_print(conv, days_texts_dict)
    conv.pack()
    root.mainloop()
