import datetime
from note_manager import NoteManager

manager = NoteManager()


def print_menu():
    print("\033[3m\033[35mЗАМЕТКИ")
    print("1. Создать заметку")
    print("2. Показать все заметки")
    print("3. Найти заметку по id")
    print("4. Редактировать заметку")
    print("5. Удалить заметку")
    print("0. Выход\033[0m")


def color_green(text):
    color_text = f'\033[32m{text}\033[0m'
    return color_text


def color_red(text):
    color_text = f'\033[3;31m{text}\033[0m'
    return color_text


def crate():
    title = input(color_green("Введите заголовок заметки: "))
    content = input(color_green("Введите тело заметки: "))
    manager.create_note(title, content)


def read():
    manager.read_notes()



def find():
    try:
        note_id = int(input(color_green("Введите номер заметки: ")))
        note = manager.get_note_by_id(note_id)
        if note:
            print(("\033[34mЗаметка:\033[0m"))
            print((note))
        else:
            print(color_red("Заметка не найдена."))
    except ValueError:
        print(color_red("Введенный идентификатор должен быть числом"))


def delete():
    try:
        note_id = int(input(color_green("Введите номер заметки: ")))
        manager.delete_note(note_id)
    except ValueError:
        print(color_red("Введенный идентификатор должен быть числом"))


def edit():
    try:
        note_id = int(input(color_green("Введите номер заметки: ")))
        new_title = input(color_green("Введите новый заголовок заметки: "))
        new_content = input(color_green("Введите новое тело заметки: "))
        manager.edit_note(note_id, new_title, new_content)
    except ValueError:
        print(color_red("Введенный идентификатор должен быть числом"))