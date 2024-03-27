def parse_input(user_input):
    cmd, *args = user_input.split()
    cmd = cmd.strip().lower()
    return cmd, *args


def show_contact(contact):
    print(f"Contacts:{contact}")
    return "Done!"


def hello():
    return "How can I help you?"


def change_contact(args, contacts: dict):
    contacts[args[0]] = args[1]
    return "Contact changed."


def get_contact(args, contacts):
    return contacts[args[0]]


def add_contact(args, contacts):
    name, phone = args
    contacts[name] = phone
    return "Contact added."


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
        elif command == "show":  # all
            print(show_contact(contacts))
        elif command == "phone":
            print(get_contact(args, contacts))
        elif command == "change":
            print(change_contact(args, contacts))
        else:
            print("Invalid command.")


if __name__ == "__main__":
    main()
