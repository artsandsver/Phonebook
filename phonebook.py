print("Добро пожаловать в приложение Телефонная книга")
print("1. Показать контакт")
print("2. Добавить контакт")
print("3. Переименовать контакт")
print("4. Удалить контакт")
print("5. Очистить контакты")
print("6. Показать только имена контактов")
print("7. Показать только номера контактов")
print("8. Выход")


phones = {
    "Кита": 8915,
    "Федор": 8916,
    "Кирил": 8511,
    "Анна": 8414,
}

def show_contact():
    for name, phone in phones.items():
        print(f"{name} - {phone}")

def add_contacts():
    name = input("Имя контакта: ")
    phone = input("Телефон: ")
    phones[name] = phone
    print("Контакт: ")
    last_name = list(phones.keys())[-1]
    last_phone = list(phones.values())[-1]
    print(f"{last_name} - {last_phone}")
    print("добавлен в телефонную книгу")


def change_number_in_contact():
    name = input("Введите имя контакта, номер которого хотите изменить: ")
    if name in phones:
        new_phone_str = input("Новый телефон: ")
        try:
            new_phone = int(new_phone_str)
            phones[name] = new_phone
            print(f"контакт {name} {new_phone} обновлен")
        except ValueError:
            print("Ошибка: введите номер в числовом формате")
    else:
        print("Контакт не найден")


def delete_contact():
    name = input("Введите имя контакта, который хотите удалить: ")
    if name in phones:
        del phones[name]
        print(f"Контакт {name} успешно удален")
    else:
        print("Контакт не найден")

def show_only_name_contact():
    for name in phones:
        print(name)

def show_only_phone_contact():
    for phone in phones.values():
        print(phone)

def delete_all_contacts():
    phones.clear()
    print("все контакты усешно удалены")

while True:
    action = input("Выберите действие:")

    if action == "1":
        show_contact()


    elif action == "2":
        add_contacts()

    elif action == "3":
        change_number_in_contact()

    elif action == "4":
        delete_contact()

    elif action == "5":
        delete_all_contacts

    elif action == "6":
        show_only_name_contact()

    elif action == "7":
        show_only_phone_contact()

    elif action == "8":
        break

    else:
        print("Команда отсутствует")