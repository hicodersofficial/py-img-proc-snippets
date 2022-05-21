from PIL import Image

with Image.open("./assets/arcane.jpg") as img:
    extension=img.format.lower()
    img.thumbnail(size=(400, 400))
    img.save(f"./dist/thumbnail.{extension}", format=extension)
