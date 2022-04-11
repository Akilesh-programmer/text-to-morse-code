# Importing the morse code dictionary
from morse_code_dictionary import MORSE_CODE_DICT

# Class for text to morse code and morse code to text conversion
class MorseCodeConverter():
    def __init__(self):
        self.morse_code_dict = MORSE_CODE_DICT
    
    # Function to convert text to morse code
    def text_to_morse(self, text):
        morse_code = ''
        text = text.upper()
        for char in text:
            morse_code += self.morse_code_dict[char] + ' '
        return morse_code

    # Function to convert morse code to text
    def morse_to_text(self, morse_code):
        text = ''
        morse_code = morse_code.split(' ')
        for char in morse_code:
            for key, value in self.morse_code_dict.items():
                if value == char:
                    text += key
        return text
