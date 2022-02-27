import PIL.Image
import os
from config import *


class Image:

    def __init__(self, name):
        self.path = os.path.join("input", name)
        self.image = self.load()
        self.string = self.convert()

    def load(self):
        with PIL.Image.open(self.path) as image:
            image.getpixel((0, 0))
            new_height = round(image.height * WIDTH * (8/21) / image.width)
            return image.resize((WIDTH, new_height))

    def convert(self):
        string = ""
        for y in range(self.image.height):
            line = ""
            for x in range(self.image.width):
                pixel = self.image.getpixel((x, y))
                value = sum(pixel) // len(pixel)
                index = value * len(ASCII) // 256
                line += ASCII[index]
            string += line + "\n"
        return string

    def write(self):
        with open(os.path.join("output", f"{IMAGE_NAME[:-4]}.txt"), "w", encoding="utf-8") as file:
            file.write(self.string)

    def __repr__(self):
        return self.string


if __name__ == '__main__':
    img = Image(IMAGE_NAME)
    img.write()
    print(img)