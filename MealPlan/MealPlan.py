
valid_days = tuple('Monday Tuesday Wednesday Thursday Friday Saturday Sunday'.split(' '))

meals_week = {}


def print_menu():
    border = '-' * 50
    print(border)
    for day in meals_week:
        print("{key}: {value}".format(key=day, value=meals_week[day]))
    print(border)


def get_meal_by_day(day):
    try:
        print('On {0}, you will be eating: {1}\n'.format(day, meals_week[day]))
    except KeyError:
        print('{} does not appear in your menu \n'.format(day))


def add_to_menu():
    while True:
        target_day = input('What day do you want to set? \n'
                           '(type "done" to complete list): \n').capitalize()
        if target_day == 'Done':
            print_menu()
            break
        elif target_day not in valid_days:
            print("Sorry, that day doesn't exist")
            return

        print('What do you want to eat on {}?'.format(target_day))
        meal = input()
        meals_week.update({target_day: meal})


def main():
    while True:
        print('Welcome to Meal Planner. What would you like to do? \n \n'
              'Options: "edit menu" to add or update meals in the menu\n'
              '         "view all" to view all the meals of the week\n'
              '         "view day" to view the meal for a single day\n '
              '         "exit" to exit the Meal Planner')
        choice = input()

        if choice == 'edit menu':
            add_to_menu()
        elif choice == 'view all':
            print_menu()
        elif choice == 'view day':
            day = input('What day would you like to view the meal for? ')
            get_meal_by_day(day)
        elif choice == 'exit':
            print('Goodbye!')
            exit()
        else:
            print("I'm afraid I don't understand that response")


if __name__ == '__main__':
    main()



