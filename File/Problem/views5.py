import csv
import numpy as np
from PIL import Image

def main():
    with open("File/Problem/views.csv", "r",encoding="utf-8-sig") as views, open("File/Problem/analysis.csv", "w",encoding="utf-8-sig", newline='') as analysis:
        reader = csv.DictReader(views)
        writer = csv.DictWriter(analysis, fieldnames=reader.fieldnames + ["brightness"])
        writer.writeheader()

        for row in reader:
            row["brightness"] = round(calculate_brightness(f"File/Problem/{row['id']}.jpeg"), 2)
            writer.writerow(row)

def calculate_brightness(filename):
    with Image.open(filename) as image:
        brightness = np.mean(np.array(image.convert("L"))) / 255
    return brightness

main() 