import sys
import random
import pyfiglet

def generate_random_font():
    fonts = pyfiglet.FigletFont.getFonts()
    return random.choice(fonts)

if len(sys.argv) == 1:
    font = generate_random_font()
elif len(sys.argv) == 3 and sys.argv[1] in ['-f', '--font']:
    font = sys.argv[2]
else:
    print("Invalid usage")
    sys.exit(1)

text = input(" ")

figlet_text = pyfiglet.Figlet(font=font)
output = figlet_text.renderText(text)

print(output)