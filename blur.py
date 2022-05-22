from PIL import Image, ImageFilter

with Image.open("./assets/eternals.jpg") as img:
    blur = img.filter(filter=ImageFilter.GaussianBlur(radius=6))
    blur.save("./dist/blurred.png", format="PNG")
