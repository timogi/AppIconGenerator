# Importing Image class from PIL module
from PIL import Image

# Opens a image in RGB mode
im = Image.open(r"icon.png")

# export sizes
sizes = {1024, 167, 40, 76, 80, 152, 20, 180, 87, 120, 58, 60, 29}

for size in sizes:
    im_temp = im.resize((size, size))
    im_temp.save(fp=f'out/icon_{size}.png', format="png")
