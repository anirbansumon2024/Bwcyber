import os

os.system("pip install pillow")


from PIL import Image, ImageDraw, ImageFont

# Create an image
width, height = 800, 200
image = Image.new('RGB', (width, height), color=(255, 255, 255))  # White background
draw = ImageDraw.Draw(image)

# Choose a font and size
font = ImageFont.truetype('path/to/your/font.ttf', 100)  # Replace with your font path

# Define text and position
text = "Awesome Font!"
text_position = (50, 50)

# Add text to image
draw.text(text_position, text, font=font, fill=(255, 0, 0))  # Red color

# Save or show the image
image.show()
image.save('awesome_font_image.png')
