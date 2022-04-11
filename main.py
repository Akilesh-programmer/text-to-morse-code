# Importing the MorseCodeConverter class
from converter import MorseCodeConverter

# Art works for printing.
morse_code_art = '''  __  __                                  ____               _             ____                                         _                 
 |  \/  |   ___    _ __   ___    ___     / ___|   ___     __| |   ___     / ___|   ___    _ __   __   __   ___   _ __  | |_    ___   _ __ 
 | |\/| |  / _ \  | '__| / __|  / _ \   | |      / _ \   / _` |  / _ \   | |      / _ \  | '_ \  \ \ / /  / _ \ | '__| | __|  / _ \ | '__|
 | |  | | | (_) | | |    \__ \ |  __/   | |___  | (_) | | (_| | |  __/   | |___  | (_) | | | | |  \ V /  |  __/ | |    | |_  |  __/ | |   
 |_|  |_|  \___/  |_|    |___/  \___|    \____|  \___/   \__,_|  \___|    \____|  \___/  |_| |_|   \_/    \___| |_|     \__|  \___| |_|   
                                                                                                                                          '''
thank_you_art = '''  _____   _                       _       __   __                
 |_   _| | |__     __ _   _ __   | | __   \ \ / /   ___    _   _ 
   | |   | '_ \   / _` | | '_ \  | |/ /    \ V /   / _ \  | | | |
   | |   | | | | | (_| | | | | | |   <      | |   | (_) | | |_| |
   |_|   |_| |_|  \__,_| |_| |_| |_|\_\     |_|    \___/   \__,_|
                                                                 '''
# Creating the boolean variable to run the while loop.
go_on = True

while go_on:
    # Welcome note
    print("Welcome to morse code converter!")
    print(morse_code_art)

    # Asking the user for input
    print("Please enter your choice:")
    print("1. Text to morse code")
    print("2. Morse code to text")
    print("3. Exit")

    choice = input("Your choice (type the number) : ")

    # We are using the below thing or else if the user types something other than number then it will give an error.
    try:
        choice = int(choice)
    except:
        pass

    if choice == 1:
        # Asking the user for input
        text = input("Please enter your text: ")

        # Creating an instance of the MorseCodeConverter class
        morse_code_converter = MorseCodeConverter()

        # Calling the text_to_morse function
        morse_code = morse_code_converter.text_to_morse(text)

        # Printing the morse code
        print("Your morse code is: " + morse_code)
    
    elif choice == 2:
        # Asking the user for input
        morse_code = input("Please enter your morse code: ")

        # Creating an instance of the MorseCodeConverter class
        morse_code_converter = MorseCodeConverter()

        # Calling the morse_to_text function
        text = morse_code_converter.morse_to_text(morse_code)

        # Printing the text
        print("Your text is: " + text)

    elif choice == 3:
        # Exiting the program
        go_on = False
        print("Thank you for using the morse code converter!")
        print(thank_you_art)
    else:
        print("Invalid choice! Please choose the right one.")
