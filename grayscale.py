from PIL import Image

with Image.open("./assets/nature.jpeg") as img:
    extension=img.format.lower()
    grayscale = img.convert("L")
    grayscale.save(f"./dist/grayscale.{extension}", format=extension)

