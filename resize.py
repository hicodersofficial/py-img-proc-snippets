from PIL import Image

with Image.open("./assets/arcane.jpg") as img:
    extension=img.format.lower()
    resized = img.resize(size=(300, 300))
    resized.save(f"./dist/resized.{extension}", format=extension)
