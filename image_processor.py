import os
import random
import argparse

from PIL import Image
from tqdm import tqdm

from utils import read_dirs, read_files


class ImageProcessor:
    def __init__(self, read_from: str, write_to: str, seed: int = 0):
        random.seed(seed)
        self.raw_data_path = read_from

        self.gray_data_path = os.path.join(write_to, "gray_data")
        self.color_data_path = os.path.join(write_to, "color_data")
        self.create_directories()

        self.dir_labels = ["Angry", "Happy", "Neutral", "Sad", "Surprise"]
        self.label_dict = dict()
        for idx, label in enumerate(self.dir_labels):
            self.label_dict[label] = idx

        self.image_size = (48, 48)
        self.image_limit = 1000

    def create_directories(self):
        os.makedirs(self.gray_data_path, exist_ok=True)
        os.makedirs(self.color_data_path, exist_ok=True)

    def run(self):
        print("Starting dataset preprocessing...\n")

        dirs = read_dirs(self.raw_data_path, self.dir_labels)
        for label, dir_path in dirs:
            print(f"Label: {label}")
            files = read_files(dir_path, [".jpg", ".jpeg", ".png"])
            random.shuffle(files)
            self.process_images(files[: self.image_limit], label)

        print("\nAll classes processed and saved.")

    def read_image(self, path: str, grayscale: bool = True):
        image = Image.open(path)
        if grayscale:
            image = image.convert("L")
        image = image.resize(self.image_size)

        return image

    def generate_name(self, label_id: int, count: int):
        return f"{label_id:02d}_{count:04d}.jpg"

    def save_image(self, image: Image.Image, path: str, filename: str):
        file_path = os.path.join(path, filename)
        image.save(file_path)

    def process_images(self, files: list, label: str):
        label_id = self.label_dict[label]
        for idx, file in tqdm(
            enumerate(files), desc=f"{label:10s}", unit="img", total=self.image_limit
        ):
            filename = self.generate_name(label_id, idx)

            gray_image = self.read_image(file)
            self.save_image(gray_image, self.gray_data_path, filename)

            color_image = self.read_image(file, grayscale=False)
            self.save_image(color_image, self.color_data_path, filename)


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Preprocess emotion dataset images.")
    parser.add_argument(
        "--read-from", type=str, default="raw_data/dataset", help="Path to raw dataset"
    )
    parser.add_argument(
        "--write-to",
        type=str,
        default="dataset",
        help="Directory to save processed images",
    )
    parser.add_argument(
        "--seed", type=int, default=0, help="Random seed for reproducibility"
    )

    args = parser.parse_args()

    processor = ImageProcessor(
        read_from=args.read_from, write_to=args.write_to, seed=args.seed
    )
    processor.run()
