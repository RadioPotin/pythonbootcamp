import sys, string

cookbook = {
    'sandwich': {
        'ingredients': ["ham", "bread", "cheese", "tomatoes"],
        'meal': "lunch",
        'prep_time': "10 minutes"
        },

    'cake': {
        'ingredients': ["flour", "sugar", "eggs"],
        'meal': "dessert",
        'prep_time': "60 minutes"
        },

    'salad': {
        'ingredients': ["avocado", "arugula", "tomatoes", "spinach"],
        'meal': "lunch",
        'prep_time': "15 minutes"
        }
    }

# Deletion functions

def del_recipe(name_of_recipe):
    if name_of_recipe in cookbook:
        del cookbook[name_of_recipe]

def choose_recipe_deletion():
    cmd = input("Please provide the name of the meal to erase from the Cookbook.")
    del_recipe(cmd.lower())
    return 2

# print_recipe functions

def print_recipe(name_of_recipe):
    print(f'''Recipe for {name_of_recipe}:\n'''
        f'''Ingredients list: {", ".join(cookbook[name_of_recipe]['ingredients'])}.\n'''
        f'''To be eaten for {cookbook[name_of_recipe]['meal']}.\n'''
        f'''Takes {cookbook[name_of_recipe]['prep_time']} of cooking.''')

def reciprint():
    cmd = input("Please enter the recipe's name to get its details:")
    print_recipe(cmd.lower())
    return 3

def print_cookbook():
    i = 1
    for key in cookbook:
        print(f"Recipe {i}: {key}.")
        i += 1
    return 4

# Add functions

def add_recipe(name, ingredients, meal, prep_time):
    if name not in cookbook:
        new = {'ingredients': list(ingredients.split(" ")), 'meal': meal, 'prep_time': prep_time}
        cookbook[name] = new
    else:
        print("There is already a meal called like that in this book !")

def get_new_recipe():
    i = 0
    fields = []
    dialogue_options = {
        0: "Okay, first, what it's name ? ",
        1: "What are the ingredients ? ",
        2: "What kind of meal is it ? ",
        3: "What is the preparation time ? "
        }
    for i in range(0, 4):
        tmp = input(dialogue_options[i])
        fields.append(tmp)
        i += 1
    add_recipe(fields[0].lower(), fields[1], fields[2], fields[3])
    return 1

# Functions container

def command_handling(cmd):
    if (cmd == 0 or cmd > 5):
        print("This option does not exist, please type the corresponding number. To exit, enter 5.")
        return 0
    command_list = [None, get_new_recipe, choose_recipe_deletion, reciprint, print_cookbook]
    command_list[cmd]()

# Menu

def option_menu():
    print("\t\tWelcome to Dario's Cookbook !\n")
    print("Please select an option by typing the corresponding number:")
    print("1: Add a recipe.\n2: Delete a recipe.\n3: Print a recipe.\n4: Print Cookbook.\n5: Quit.")

# Main

def main():
    state = 0
    option_menu()
    while (state is not 5):
        cmd = input()
        if cmd.isdigit() == False:
            command_handling(0)
        elif (cmd == str(5)):
            break
        else:
            state = command_handling(int(cmd))
    print("Thank you ! Bye !\nCookbook closed.")

if __name__ == "__main__":
    main()
