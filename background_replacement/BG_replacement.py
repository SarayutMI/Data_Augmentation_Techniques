from rembg import remove
from PIL import Image
import os
import random  # <-- Add this line

input_path = "./input_dir/"
bg_path = "./backgrounds_dir/"
output_path = "output_dir/"

os.makedirs(output_path, exist_ok=True)

for file in os.listdir(input_path):
    if file.endswith(".jpg") or file.endswith(".png") or file.endswith(".JPG"):
        # ตัด background
        img = Image.open(os.path.join(input_path, file))
        fg = remove(img)
        print("Process ---> ",file)
        # เลือก background สุ่ม
        bg_file = os.path.join(bg_path, random.choice(os.listdir(bg_path)))
        bg = Image.open(bg_file).resize(fg.size)

        # รวม foreground + background
        bg.paste(fg, (0,0), fg)
        bg.save(os.path.join(output_path, file))

print("The Process is sucessfully : Background Replacment")
