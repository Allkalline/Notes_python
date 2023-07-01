import console_functions as cf
from console_functions import color_green, color_red


def console():
    while True:
        cf.manager.load_notes()
        cf.print_menu()
        choice = input(color_green("Введите номер нужной функции: "))

        match choice:
            case "1":
                cf.crate()
            case "2":
                cf.read()
            case "3":
                cf.find()
            case "4":
                cf.edit()
            case "5":
                cf.delete()
            case "0":
                break
            case _:
                print(color_red("Попробуйте снова."))