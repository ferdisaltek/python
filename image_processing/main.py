from PIL import Image
import collections

def generate_palette(image_path, num_colors):
    # Open the image
    image = Image.open(image_path)
    
    # Resize the image to a small size for faster processing (optional)
    image.thumbnail((100, 100))
    
    # Convert the image to the RGB mode (if not already)
    image = image.convert("RGB")
    
    # Get the image's pixel data
    pixels = list(image.getdata())
    
    # Count the occurrences of each color in the image
    color_counter = collections.Counter(pixels)
    
    # Get the most common colors (top 'num_colors' colors)
    most_common_colors = color_counter.most_common(num_colors)
    
    # Extract the RGB values of the most common colors
    palette = [color[0] for color in most_common_colors]
    
    return palette

def save_palette_as_image(palette, output_path):
    # Create a new image with the palette colors
    palette_image = Image.new("RGB", (len(palette), 100))
    palette_image.putdata(palette)
    
    # Save the palette image
    palette_image.save(output_path)

if __name__ == "__main__":
    input_image_path = "C:/Users/ferdi.saltek/Pictures/1782138.jpg"
    output_palette_path = "color_palette.jpg"
    num_colors = 10  # Adjust the number of colors in the palette as needed

    palette = generate_palette(input_image_path, num_colors)
    save_palette_as_image(palette, output_palette_path)

