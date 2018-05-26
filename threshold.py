import PIL.Image as pim

filename = input("Enter a filename: ")
threshold = int(input("Enter a threshold: "))

original = pim.open(filename)
bwimage = pim.new('1', (original.width, original.height))

for x in range(original.width):
    for y in range(original.height):
        pixel = original.getpixel((x, y))
        
        if pixel >= threshold:
            bwimage.putpixel((x, y), 1)
        else:
            bwimage.putpixel((x, y), 0)

bwimage.save('output.png')
