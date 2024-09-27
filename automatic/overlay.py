from PIL import Image
from collections import Counter

def image_to_hashmap(image_path):

    img = Image.open(image_path)
    
    img = img.convert('RGB')
    
    width, height = img.size
    
    pixel_list = []
    
    for x in range(width):
        for y in range(height):
            rgb = img.getpixel((x, y))
            pixel_list.append(rgb)
    
    # Count the occurrence of each color
    color_count = Counter(pixel_list)
    
    # Get the color with the highest occurrence
    most_common_color = color_count.most_common(1)[0][0]
    
    return most_common_color

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

def overlay_image(background, overlay, position):
    # Paste the overlay image onto the background image at the given position
    background.paste(overlay, position, overlay if overlay.mode == 'RGBA' else None)
    return background

# Find the highest occurrence color in the image
image_path = 'pp.jpeg'  # Replace with your image path
highest_occurrence_color = image_to_hashmap(image_path)
print(f"Highest occurrence color: {highest_occurrence_color}")

#Create a gradient image from the highest occurrence color to black
width, height = 512, 1024  # Set the desired width and height
start_color = highest_occurrence_color  # Use the most common color as the start color
end_color = (0, 0, 0)  # Black as the end color

# Create the gradient image
gradient_image = create_linear_gradient_image(width, height, start_color, end_color)

# Overlay the original image at 20% of the gradient height
overlay_image_obj = Image.open(image_path)

# Resize overlay image if it's too large
overlay_image_obj.thumbnail((width // 2, height // 2))  # Resize to fit within half the gradient size

# Calculate the position to overlay the image at 20% of the gradient height
overlay_width, overlay_height = overlay_image_obj.size
position = ((width - overlay_width) // 2, int(height * 0.2))  # 20% from the top

# Overlay the image at the calculated position
final_image = overlay_image(gradient_image, overlay_image_obj, position)

# Save or show the final image
final_image.show()  # To display the image
final_image.save('final_image_with_overlay_at_20_percent.png')  # To save the image
