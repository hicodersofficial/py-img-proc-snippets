from PIL import Image

with Image.open("./assets/earth.jpg") as img:
    with Image.open("./assets/hicoders.png") as logo:
        image = img.convert("RGBA")
        logo_size = int(img.size[0] * .1)
        rbga_logo = logo.convert("RGBA")
        rbga_logo.thumbnail(size=(logo_size, logo_size))
        padding = 10
        img_w, img_h = img.size
        dest = (img_w - (logo_size + padding), img_h - (logo_size + padding))
        image.alpha_composite(im=rbga_logo, dest=dest)
        image.save("./dist/composite.png", format="PNG")
