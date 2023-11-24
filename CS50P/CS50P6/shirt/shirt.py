import sys
from PIL import Image, ImageOps

# Check for the correct number of command-line arguments
if len(sys.argv) != 3:
    sys.exit("Too many command-line arguments")

# Extract the input and output file names from command-line arguments
input_file = sys.argv[1]
output_file = sys.argv[2]

# Check if the input and output file names have valid extensions
valid_extensions = (".jpg", ".jpeg", ".png")
if not (input_file.lower().endswith(valid_extensions) and output_file.lower().endswith(valid_extensions)):
    sys.exit("Invalid output")

# Check if the input file exists
try:
    Image.open(input_file)
except FileNotFoundError:
    sys.exit("Input does not exist")

# Open the input image
input_image = Image.open(input_file)

# Open the shirt image
shirt_image = Image.open("shirt.png")

# Resize and crop the input image to match the shirt image size
input_image = ImageOps.fit(input_image, shirt_image.size)

# Overlay the shirt image on the input image
input_image.paste(shirt_image, (0, 0), mask=shirt_image)

# Save the result as the output image
input_image.save(output_file)