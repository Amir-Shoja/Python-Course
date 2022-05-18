from os import listdir
from imageio import imread, mimsave

images = []
image = listdir("New")
for name in image:
    images.append(imread("New/" + name))

mimsave("fun.gif", images)
