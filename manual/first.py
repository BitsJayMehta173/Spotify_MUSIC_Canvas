from PIL import Image

def image_to_hashmap(image_path):
    # Open the image
    img = Image.open(image_path)
    # Convert the image to RGB mode (if it's not already)
    img = img.convert('RGB')
    
    # Get image size
    width, height = img.size
    
    # Create a dictionary to store pixel coordinates and their RGB values
    pixel_map = {}
    
    # Iterate through each pixel
    for x in range(width):
        for y in range(height):
            # Get the RGB value of the pixel
            rgb = img.getpixel((x, y))
            # Add to the hashmap with the pixel's coordinates as the key
            pixel_map[(x, y)] = rgb
            
    return pixel_map

# Example usage
image_path = 'pp.jpeg'
pixel_hashmap = image_to_hashmap(image_path)

# Print first 10 pixel mappings
print({k: pixel_hashmap[k] for k in list(pixel_hashmap)[:10]})
