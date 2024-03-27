def input_error(func):
    def inner(*args, **kwargs):
        try:
            return func(*args, **kwargs)
        except KeyError:
            return "Enter user name."
        except ValueError:
            return "Give me name and phone please."
        except IndexError:
            return "Give me name and phone please."
    return inner

def parse_input(user_input):
    cmd, *args = user_input.split()
    cmd = cmd.strip().lower()
    return cmd, *args

@input_error
def show_contact(contact):
    print(f"Contacts:{contact}")
    return "Done!"

@input_error
def hello():
    return "How can I help you?"

@input_error
def change_contact(args, contacts: dict):
    contacts[args[0]] = args[1]
    return "Contact changed."

@input_error
def get_contact(args, contacts):
    return contacts[args[0]]

@input_error
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
            print(hello())
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
