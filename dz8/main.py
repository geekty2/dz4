import pickle
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

def save_data(book, filename="addressbook.pkl"):
    with open(filename, "wb") as f:
        pickle.dump(book, f)

def load_data(filename="addressbook.pkl"):
    try:
        with open(filename, "rb") as f:
            return pickle.load(f)
    except FileNotFoundError:
        return AddressBook()

def main():
    book = load_data()

    save_data(book)
if __name__ == "__main__":
    main()
