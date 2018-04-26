# Import the necessary packages 

import db_gen
import blast_parser

import os
import sys
import json

# Clears the console
def clear():
    os.system("cls" if os.name == "nt" else "clear")

# Replaces any instances of variable placeholders with the actual variables
# So it's easier to display the configuration values
def check_vars(text, config_params):

    for k in config_params["vals"].keys():
        if k in text:
            text = text.replace(k, config_params["vals"][k])
    return text

# Change a configuration value
def change_config(param):
    global config_params
    clear()

    # Enter the new value based off of which one the user wants to change
    print("Please enter the new " + config_params['config_strs'][param])
    
    # Make sure the user is running Python 3 
    if version < 3:
        config_params["vals"][param] = str(raw_input())
    else:
        config_params["vals"][param] = str(input())

    # Display the configuration menu again now that we are done
    disp_menu("config")

# Display any meny desired
def disp_menu(menu):
    clear()
    global config_params
    global menus
    
    # Get everything pertaining to the menu from the dictionary
    cmds = menus[menu]["commands"]
    opts = menus[menu]["options"]
    title = menus[menu]["title"]
    additional = menus[menu]["additional_lines"]

    # Write out our title and separation bar
    print(title)
    print("=" * 40)

    # Write out the configuration paramaters' current values
    for a in additional:
        print(check_vars(a, config_params))

    print("-" * 40)

    # Print the options for the menu with corresponding numbers
    for i in range(0, len(opts)):
        print("[{}] {}".format(i + 1, opts[i]))

    # Ask the user for input
    print("Please enter the number of the action you would like to perform: ")
    if version < 3:
        act = int(raw_input())
    else:
        act = int(input())
    # Excecutes command based on input
    exec('\n'.join(cmds[act - 1]))

if __name__ == "__main__":
    # Get the python version
    version = sys.version_info[0]

    # Load the data
    with open("./config/menus.json") as data:
        menus = json.load(data)
    with open("./config/params.json") as data:
        config_params = json.load(data)

    # Display the main menu
    disp_menu("main")