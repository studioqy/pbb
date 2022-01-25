'''
Week 8 Assignment Green Background
Opens two images, removes the green pixels from one and overlays it on the
other, simulating a green-screened effect
Nov 7 2020
'''

from PIL import Image

print("Please include the file type for all of your responses (Ex .jpg, .png)")
# Try field.jpg as background and cat.jpg as green screened image
# The images must be in the same directory as this file
b_img = input("What background image would you like to use? ")
g_img = input("What image on a green screen would you like to use? ")
final_img = input("What name would you like to save the new image as? ")

background_img = Image.open(b_img)
green_img = Image.open(g_img)

background_img.show()
green_img.show()

background_width, background_height = background_img.size
green_width, green_height = green_img.size
background_pixels = background_img.load()
green_pixels = green_img.load()

x = 1
y = 1
for y in range(0, green_height):
    for x in range(0, green_width):
        r, g, b = green_pixels[x, y]
        br, bg, bb = background_pixels[x, y]
        if g < 140 and r < 50 and b < 140:
            green_pixels[x, y] = (br, bg, bb)
        else:
            pass
        x += 1
    y += 1


green_img.show()
green_img.save(final_img)
