#! python3
# bulletPointAdder.py - Adds Wikipedia bullet points to the start
# of each line of text on the clipboard.

import pyperclip

text = pyperclip.paste()

# TO DO: Separate lines and add stars

print(text)