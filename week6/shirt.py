import sys
from PIL import Image, ImageOps

argc = len(sys.argv)
argv = sys.argv

if argc < 3:
    print("Too few command-line arguments")
    sys.exit(1)
elif argc > 3:
    print("Too many command-line arguments")
    sys.exit(1)

read_file_format = argv[1].rstrip().split(".")[1]
write_file_format = argv[2].rstrip().split(".")[1]
expected_extension = ["jpg", "jpeg", "png"]

if read_file_format not in expected_extension or write_file_format not in expected_extension:
    print("Invalid input")
    sys.exit(1)

if read_file_format != write_file_format:
    print("Input and output have different extensions")
    sys.exit(1)

input_file = argv[1]
output_file = argv[2]

try:
    input_image = Image.open(input_file)
    shirt_image = Image.open("shirt.png")
    fitted_image = ImageOps.fit(input_image, shirt_image.size)
    fitted_image.paste(shirt_image, (0, 0), shirt_image)
    fitted_image.save(output_file)
except FileNotFoundError:
    print("File not found")
    sys.exit(1)
