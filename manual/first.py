from PIL import Image

def image_to_hashmap(image_path):

    img = Image.open(image_path)

    img = img.convert('RGB')
    

    width, height = img.size
    
    # Create a dictionary to store pixel coordinates and their RGB values
    pixel_map = {}
    

    for x in range(width):
        for y in range(height):

            rgb = img.getpixel((x, y))
            # Add to the hashmap with the pixel's coordinates as the key
            pixel_map[(x, y)] = rgb
            
    return pixel_map

image_path = 'pp.jpeg'
pixel_hashmap = image_to_hashmap(image_path)

# first 10 pixel mappings
print({k: pixel_hashmap[k] for k in list(pixel_hashmap)[:10]})
