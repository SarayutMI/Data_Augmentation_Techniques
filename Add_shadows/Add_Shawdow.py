from PIL import Image, ImageEnhance
import os
import random

input_path = "./input_dir/"
shadow_path = "./shadow_textures/"  # ใส่ไฟล์เงาที่เตรียมเอง
output_path = "./shadow_images_output/"
os.makedirs(output_path, exist_ok=True)

# Process all images
for file in os.listdir(input_path):
    if file.lower().endswith((".jpg", ".png")):
        print(f"Processing {file}...")
        img = Image.open(os.path.join(input_path, file)).convert("RGBA")

        # เลือกเงาสุ่มจากโฟลเดอร์
        shadow_file = os.path.join(shadow_path, random.choice(os.listdir(shadow_path)))
        shadow = Image.open(shadow_file).convert("RGBA")

        # ปรับขนาดเงาให้เท่าภาพ
        shadow = shadow.resize(img.size)

        # ลดความเข้มของเงา
        enhancer = ImageEnhance.Brightness(shadow)
        shadow = enhancer.enhance(0.5)  # ค่าตั้งแต่ 0–1, <1 ทำให้เงาอ่อนลง

        # ซ้อนเงา
        combined = Image.alpha_composite(img, shadow)

        # บันทึก
        combined.convert("RGB").save(os.path.join(output_path, file))

print("All images processed ✅")
