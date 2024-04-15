from datetime import datetime, timedelta


class Field:
    pass


class Name(Field):
    def __init__(self, value):
        self.value = value


class Phone(Field):
    def __init__(self, value):
        if not value.isdigit() or len(value) != 10:
            raise ValueError("Invalid phone number format. Use 10 digits.")
        self.value = value


class Birthday(Field):
    def __init__(self, value):
        try:
            self.value = datetime.strptime(value, "%d.%m.%Y")
        except ValueError:
            raise ValueError("Invalid date format. Use DD.MM.YYYY")


class Record:
    def __init__(self, name):
        self.name = Name(name)
        self.phones = []
        self.birthday = None

    def add_phone(self, phone):
        self.phones.append(Phone(phone))

    def add_birthday(self, birthday):
        self.birthday = Birthday(birthday)


class AddressBook:
    def __init__(self):
        self.records = []

    def add_record(self, record):
        self.records.append(record)

    def find(self, name):
        for record in self.records:
            if record.name.value == name:
                return record
        return None

    def get_upcoming_birthdays(self):
        upcoming_birthdays = []
        today = datetime.today()
        next_week = today + timedelta(days=7)
        for record in self.records:
            if record.birthday and today <= record.birthday.value < next_week:
                upcoming_birthdays.append((record.name.value, record.birthday.value.strftime("%d.%m.%Y")))
        return upcoming_birthdays


def add_birthday(args, book):
    name, birthday = args
    record = book.find(name)
    if record:
        record.add_birthday(birthday)
        return f"Birthday added for {name}."
    else:
        return f"Contact {name} not found."


def show_birthday(args, book):
    name = args[0]
    record = book.find(name)
    if record and record.birthday:
        return f"{name}'s birthday: {record.birthday.value.strftime('%d.%m.%Y')}"
    elif record:
        return f"{name} has no birthday set."
    else:
        return f"Contact {name} not found."


def birthdays(args, book):
    upcoming_birthdays = book.get_upcoming_birthdays()
    if upcoming_birthdays:
        return "\n".join([f"{name}'s birthday on {date}" for name, date in upcoming_birthdays])
    else:
        return "No upcoming birthdays."


def input_error(func):
    def wrapper(args, book):
        try:
            return func(args, book)
        except Exception as e:
            return str(e)

    return wrapper


def add_contact(args, book):
    name, phone = args
    record = book.find(name)
    if record:
        record.add_phone(phone)
        return f"Phone number added for {name}."
    else:
        record = Record(name)
        record.add_phone(phone)
        book.add_record(record)
        return f"New contact {name} added with phone number {phone}."


def change_phone(args, book):
    name, new_phone = args
    record = book.find(name)
    if record:
        record.phones = [Phone(new_phone)]
        return f"Phone number changed for {name}."
    else:
        return f"Contact {name} not found."


def show_phone(args, book):
    name = args[0]
    record = book.find(name)
    if record:
        phones = ', '.join([phone.value for phone in record.phones])
        return f"Phone numbers for {name}: {phones}."
    else:
        return f"Contact {name} not found."


def show_all(book):
    if book.records:
        all_contacts = "\n".join(
            [f"{record.name.value}: {', '.join([phone.value for phone in record.phones])}" for record in book.records])
        return f"All contacts:\n{all_contacts}"
    else:
        return "Address book is empty."


def main():
    book = AddressBook()
    print("Welcome to the assistant bot!")
    while True:
        user_input = input("Enter a command: ")
        command, *args = user_input.split()

        if command in ["close", "exit"]:
            print("Good bye!")
            break

        elif command == "hello":
            print("How can I help you?")

        elif command == "add":
            print(add_contact(args, book))

        elif command == "change":
            print(change_phone(args, book))

        elif command == "phone":
            print(show_phone(args, book))

        elif command == "all":
            print(show_all(book))

        elif command == "add-birthday":
            print(add_birthday(args, book))

        elif command == "show-birthday":
            print(show_birthday(args, book))

        elif command == "birthdays":
            print(birthdays(args, book))

        else:
            print("Invalid command.")


if __name__ == "__main__":
    main()
