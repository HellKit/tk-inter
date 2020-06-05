from tkinter import Tk, Canvas


def root_settings(root):
    root.title('Надо бы, что-то тут написать!')
    root.geometry("700x800")
    root.resizable(width=False, height=False)

def canva_settings(conv, root):
    conv.create_text(350, 50, text="Мои текущие задачи",
                    justify='center', font="Verdana 28", fill='yellow')
    conv.create_line(150, 70, 550, 70, fill='yellow')

def message_print(conv):
    for i in range(10):
        i *= 30
        conv.create_text(150, 100+i, text='Привет молодой человек',
                        justify='center', font='Verdana 15', fill='yellow')


if __name__ == '__main__':
    root = Tk()
    root_settings(root)
    conv = Canvas(root, bg='black', width=4000, height=4000)
    canva_settings(conv, root)
    message_print(conv)
    conv.pack()
    root.mainloop()
