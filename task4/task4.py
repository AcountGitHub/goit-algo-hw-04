'''
Парсер команд
'''
def parse_input(user_input):
    cmd, *args = user_input.split()
    cmd = cmd.strip().lower()
    return cmd, *args

'''
Функція додавання нового контакту до словника контактів.
Якщо контакт із заданим ім'ям існує, то дані не будуть додані,
а користувач отримає відповідне повідомлення
'''
def add_contact(args, contacts):
    result = "Contact added."
    name, phone = args
    if contacts.get(name) is None:
        contacts[name] = phone
    else:
        result = f"Contact not added because name {name} already exists."
    return result

'''
Функція збереження нового номеру для контакту із заданим ім'ям.
Якщо контакт з заданим ім'ям не існує, то користувач отримає
відповідне повідомлення
'''
def change_contact(args, contacts):
    result = "Contact updated."
    name, phone = args
    if contacts.get(name) is None:
        result = f"Contact with name {name} not found!"
    else:
        contacts[name] = phone
    return result

'''
Функція повертає номер телефону для контакту з заданим ім'ям.
Якщо контакт з заданим ім'ям не існує, то користувач отримає
відповідне повідомлення
'''
def show_phone(name, contacts):
    result = contacts.get(name)
    if result is None:
        result = f"Contact with name {name} not found!"
    return result

'''
Функція повертає рядок з усіма збереженими контактами з номерами телефонів
'''
def show_all(contacts):
    result = "\n---CONTACTS---\n"
    for name in contacts:
        result += f"{name}: {contacts[name]}\n"
    return result

'''
Функція з реалізованою логікою взаємодії з користувачем
'''
def main():
    contacts = {}
    print("Welcome to the assistant bot!")
    while True:
        user_input = input("Enter a command: ")
        command, *args = parse_input(user_input)

        if command in ["close", "exit"]:
            print("Good bye!")
            break

        elif command == "hello":
            print("How can I help you?")

        elif command == "add":
            print(add_contact(args, contacts))

        elif command == "change":
            print(change_contact(args, contacts))

        elif command == "phone":
            print(show_phone(args[0], contacts))
        
        elif command == "all":
            print(show_all(contacts))

        else:
            print("Invalid command.")


if __name__ == "__main__":
    main()