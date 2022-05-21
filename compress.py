from PIL import Image

with Image.open("./assets/halo.jpg") as img:
    extension = img.format.lower()
    img.save(f"./dist/compressed.{extension}", format=extension, quality=50)

