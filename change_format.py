from PIL import Image

with Image.open("./assets/moon-knight.webp") as img:
    img.save("./dist/changed_format.png", format="PNG")

