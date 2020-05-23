from PIL import Image
import os.path
from os import path
from os import mkdir

def toHex(rgb:tuple):
    return '#%02x%02x%02x' % rgb

def main():
    print("Welcome! This app will print your image with full block (█) symbol in a html file.")
    image_file = input("Image file: ")
    if not path.exists(image_file):
        print("Unable to open file '{}'".format(image_file))
        exit(0)
    output_file = input("Output Filename: ")
    image = Image.open(image_file)
    pix = image.load()
    if output_file[output_file.rfind('.'):].lower() != '.html':
        output_file += ".html"

    try:
        mkdir("outputs")
    except:
        pass
    output_file = "outputs/" + output_file

    old_color = list(pix[0, 0])
    try:
        with open(output_file, 'w', encoding='utf-8') as file:
            file.write("<html><head><style>font{font-size: 1px;}</style><title>" + output_file + "</title></head><body>")
            file.write('<font color = "{}">'.format(toHex(pix[0, 0])))
            for y in range(image.size[1]):
                for x in range(image.size[0]):
                    if tuple(old_color) != pix[x,y]:
                        file.write("</font>")
                        file.write('<font color = "{}">'.format(toHex(pix[x,y])))
                    file.write("█")
                    old_color = list(pix[x, y])
                file.write("<br>")
            file.write("</font></body></html>")
    except:
        print("Cannot create file {}".format(output_file))
        exit(0)
    print()
    print("Saved in {}".format(output_file))
    print("Note: Output file may not look good in Firefox")

if __name__ == '__main__':
    main()
