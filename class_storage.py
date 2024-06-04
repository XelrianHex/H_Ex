from class_attempt import Player


def ask_for_input(question):
    answer = input(question)
    return answer.strip()  # strip any user created white space.


def main():

    # Store our users
    users = []

    # Collect the user info
    name = ask_for_input(question="name?")
    lvl = 10

    # Create our user object
    char = Player(name=name, lvl=lvl)
    # accessing the id property
    print(char.name)
    print(char.lvl)

    users.append(char)


if xel in main.users:
    print("it's there")


if __name__ == '__main__':
    main()
