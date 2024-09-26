from PIL import Image

def create_linear_gradient_image(width, height, start_color, end_color):

    img = Image.new("RGB", (width, height))
    
    # Generate gradient
    for y in range(height):
        # Calculate the ratio of the current row relative to the total height
        ratio = y / height
        # Interpolate between the start_color and end_color based on the ratio
        r = int(start_color[0] * (1 - ratio) + end_color[0] * ratio)
        g = int(start_color[1] * (1 - ratio) + end_color[1] * ratio)
        b = int(start_color[2] * (1 - ratio) + end_color[2] * ratio)
        
        # Fill the row with the calculated color
        for x in range(width):
            img.putpixel((x, y), (r, g, b))
    
    return img

# Define image size and colors
width, height = 256, 512
start_color = (73, 127, 151)  # Max color
end_color = (0, 0, 0)         # Black

# Create the gradient image
gradient_image = create_linear_gradient_image(width, height, start_color, end_color)

# Save or show the image
gradient_image.show()  # To display the image
gradient_image.save('linear_gradient.png')  # To save the image
