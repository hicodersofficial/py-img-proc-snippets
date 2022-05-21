from PIL import Image

with Image.open("./assets/dr-strange.jpg") as img:
    extension=img.format.lower()
    rotate= img.rotate(90, expand=1)
    rotate.save(f"./dist/rotated.{extension}", format=extension)
