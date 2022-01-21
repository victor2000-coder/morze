# Morse dict
MorseCode = {'A': '.-',
             'B': '-...',
             'C': '-.-.',
             'D': '-..',
             'E': '.',
             'F': '..-.',
             'G': '--.',
             'H': '....',
             'I': '..',
             'J': '.---',
             'K': '-.-',
             'L': '.-..',
             'M': '--',
             'N': '-.',
             'O': '---',
             'P': '.--.',
             'Q': '--.-',
             'R': '.-.',
             'S': '...',
             'T': '-',
             'U': '..-',
             'V': '...-',
             'W': '.--',
             'X': '-..-',
             'Y': '-.--',
             'Z': '--..',
             ' ': '\n',
             }


# return encoded text
def encode_to_morse(text: str) -> str:
  
  # буквы должны быть разделены плобелом. 
  # слова должны быть разделены "\n". 
    return text


# return decoded text
def decode_from_morse(code: str):
  
  # буквы разделены плобелом. 
  # слова разделены "\n". 
    return code


# return True, if all letters are latin
def check_for_latin_encodable(text):
    for ch in text:
        if ch not in MorseCode.keys():
            return False
    return True


# encode and print next user input
def encode_input():
    inp = input("Please, use only latin alphabet!!! I will encode this text: ")
    while check_for_latin_encodable(inp):
        inp = input("\nPlease, use only latin alphabet!!! Try again: ")
    print(encode_to_morse(inp))


# decode and write next user input
def decode_input():
    inp = input("Please, use only dots and dashes, "
                "every word must take one line, "
                "all letters must be separated by space,"
                "End your message by empty string."
                "I will decode this code: ")
    out = inp
    while inp:
        inp = input()
        out += '\n' + inp
    print(decode_from_morse(out))


# commands
EVENTS = {
    'encode': encode_input,
    'decode': decode_input,
    'exit': exit
}


# return next command from input
def get_event():
    inp = input(f"What do you wish? {list(EVENTS.keys())}: ")
    while inp not in EVENTS.keys():
        inp = input(f"\nUnexcepted command: {inp}. Try again: ")
    return EVENTS[inp]


def main():
    while True:
        event = get_event()
        event()


main()
