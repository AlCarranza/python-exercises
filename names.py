from PIL import Image
from PIL import ImageFilter

def main():
    # name = input("What's the name: ")

    # file = open("names.txt", "a")
    # file.write(f"{name}\n")
    # file.close()
    with Image.open("loki_drive.png") as img:
        img = img.rotate(10)
        img = img.filter(ImageFilter.BLUR)
        img.save("loki_rotate.png")

main()
