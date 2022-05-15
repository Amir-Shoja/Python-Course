import imageio
import os

image = []
for file_name in os.listdir("images"):
    image = imageio.imread(f"image/{file_name}")
    image.append(image)

imageio.mimsave("fun.gif", image)
