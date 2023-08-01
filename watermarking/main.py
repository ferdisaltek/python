import tkinter as tk
from tkinter import filedialog
from PIL import Image, ImageDraw, ImageFont

def open_image():
    file_path = filedialog.askopenfilename(filetypes=[("Image files", "*.png;*.jpg;*.jpeg;*.gif;*.bmp")])
    if file_path:
        original_image = Image.open(file_path)
        return original_image
    return None

def add_watermark():
    original_image = open_image()
    if original_image:
        watermark_text = watermark_text_entry.get()
        watermark_position = (int(watermark_x_entry.get()), int(watermark_y_entry.get()))

        watermark_image = Image.new("RGBA", original_image.size, (255, 255, 255, 0))
        draw = ImageDraw.Draw(watermark_image)
        font = ImageFont.truetype("arial.ttf", 40)  # You can specify the font and size here

        draw.text(watermark_position, watermark_text, font=font, fill=(255, 255, 255, 128))
        watermarked_image = Image.alpha_composite(original_image.convert("RGBA"), watermark_image)

        save_path = filedialog.asksaveasfilename(defaultextension=".png", filetypes=[("PNG files", "*.png")])
        if save_path:
            watermarked_image.save(save_path)

# Create the main application window
app = tk.Tk()
app.title("Image Watermark App")

# Create GUI elements
open_button = tk.Button(app, text="Open Image", command=open_image)
open_button.pack()

watermark_text_label = tk.Label(app, text="Watermark Text:")
watermark_text_label.pack()

watermark_text_entry = tk.Entry(app)
watermark_text_entry.pack()

watermark_x_label = tk.Label(app, text="X position:")
watermark_x_label.pack()

watermark_x_entry = tk.Entry(app)
watermark_x_entry.pack()

watermark_y_label = tk.Label(app, text="Y position:")
watermark_y_label.pack()

watermark_y_entry = tk.Entry(app)
watermark_y_entry.pack()

add_watermark_button = tk.Button(app, text="Add Watermark", command=add_watermark)
add_watermark_button.pack()

app.mainloop()

