from PIL import Image
import collections

def rgb_to_hex(rgb):
    return "#{:02x}{:02x}{:02x}".format(rgb[0], rgb[1], rgb[2])

def generate_palette(image_path, num_colors):
    image = Image.open(image_path)
    image.thumbnail((100, 100))
    image = image.convert("RGB")
    pixels = list(image.getdata())
    color_counter = collections.Counter(pixels)
    most_common_colors = color_counter.most_common(num_colors)
    palette = [rgb_to_hex(color[0]) for color in most_common_colors]
    return palette

if __name__ == "__main__":
    input_image_path = "C:/Users/ferdi.saltek/Pictures/1782138.jpg"
    num_colors = 10  # Adjust the number of colors in the palette as needed

    palette = generate_palette(input_image_path, num_colors)

    for color in palette:
        print(color)
