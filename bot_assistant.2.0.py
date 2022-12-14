from classes import AddressBook, Record


def input_error(func):
    def wrapper(*args, **kwargs):
        try:
            result = func(*args, **kwargs)
            return result
        except KeyError:
            print('Enter user name.')
        except ValueError:
            print('Enter correct type.')
        except IndexError:
            print('Give me name and phone please.')
        except TypeError:
            print('Give me name and phone please.')

    return wrapper


@input_error
def add_new_contact(data):
    name, phone = create_data(data)
    record_add = Record(name.lower())
    record_add.add_phone(phone)
    addressbook.add_record(record_add)
    return f'A new contact name: {name} phone: {phone}, has been added.'


@input_error
def add_new_phone(data):
    name, phone = create_data(data)
    record_add_phone = addressbook.data[name]
    record_add_phone.add_phone(phone)
    return f'A new phone: {phone}, has been added to contact name: {name}.'


@input_error
def change_phone(data):
    name, phone = create_data(data)
    new_phone = data[2]

    record_change = addressbook.data[name]
    if record_change.change_phone(old_phone=phone, new_phone=new_phone) is True:
        return f'A contact name: {name} number: {phone}, has been changed to {new_phone}.'
    else:
        return 'The phone number not exist'


@input_error
def get_contact_number(name):
    name = name[0]
    return f"'name:' {addressbook.data[name].name.value}, 'phone:'{list(map(lambda x: x.value, addressbook.data[name].phones))}"


@input_error
def quit_func():
    return 'Good bye!'


@input_error
def hello_func():
    return "Hello! How can I help you?"


@input_error
def show_all_func():
    return f'All contacts:\n{addressbook.data}'


@input_error
def delete_func(data):
    name, phone = create_data(data)
    record_delete = addressbook.data[name]

    if record_delete.delete_phone(phone) is True:
        return f'Contact name: {name} phone: {phone}, has been deleted.'

    else:
        return 'The phone number not exist'


COMMANDS = {
    'add': add_new_contact,
    'add_phone': add_new_phone,
    'change': change_phone,
    'phone': get_contact_number,
    'hello': hello_func,
    'show all': show_all_func,
    'good bye': quit_func,
    'close': quit_func,
    'exit': quit_func,
    'delete': delete_func
}
commands = ['add', 'add_phone', 'change', 'phone',
            'hello', 'show all', 'good bye', 'close', 'exit', 'delete']


def create_data(data):
    name = data[0]
    phone = data[1]
    if name.isnumeric():
        raise ValueError('Wrong name.')
    if not phone.isnumeric():
        raise ValueError('Wrong phone.')
    return name, phone


def main():

    print('Bot-assistant here...\n("help" - all commands)')

    while True:

        user_input = input('Enter command:\n').lower()

        if user_input == '.':
            break

        elif user_input == 'help':
            print(f"All commands: {commands}.")
            continue

        elif user_input == "":
            continue

        elif user_input in COMMANDS:
            print(COMMANDS[user_input]())
            if COMMANDS[user_input]() == "Good bye!":
                break

        elif user_input.split()[0] in COMMANDS:
            print(COMMANDS[user_input.split()[0]](user_input.split()[1:]))

        else:
            print(
                f"Sorry, i don't know, what is '{user_input}', please, try again.\nAll commands: {commands}")


if __name__ == "__main__":
    addressbook = AddressBook()
    main()
