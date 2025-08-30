from PIL import Image
from colorsys import rgb_to_hsv, hsv_to_rgb
import os
import random

input_folder = "./input_dir/"
output_folder = "./output_dir/"

os.makedirs(output_folder, exist_ok=True)

def dark_green_with_warm_tones(img):
    img = img.convert("RGB")
    pixels = img.load()

    for i in range(img.width):
        for j in range(img.height):
            r, g, b = pixels[i, j]

            # Convert RGB to HSV
            h, s, v = rgb_to_hsv(r/255, g/255, b/255)

            # Base dark green: hue ~120° (0.33), reduce brightness
            h = 0.33  # green
            v = v * 0.4 + 0.2  # darken green

            # Add small random yellow/orange highlights
            if random.random() < 0.05:  # 5% of pixels
                h = random.uniform(0.08, 0.12)  # yellow/orange hue
                v = min(1.0, v + 0.3)           # brighten
                s = min(1.0, s + 0.3)           # saturate

            r_new, g_new, b_new = hsv_to_rgb(h, s, v)
            pixels[i, j] = (int(r_new*255), int(g_new*255), int(b_new*255))

    return img

# Process all images in folder
for file in os.listdir(input_folder):
    print("Processing -----> ",file)
    if file.lower().endswith((".jpg", ".png")):
        img_path = os.path.join(input_folder, file)
        img = Image.open(img_path)

        new_img = dark_green_with_warm_tones(img)

        new_img.save(os.path.join(output_folder, file))

print("Processing complete!")
