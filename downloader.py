import os
import argparse
from zipfile import ZipFile

from kaggle.api.kaggle_api_extended import KaggleApi


class KaggleDownloader:
    def __init__(self):
        self.api = KaggleApi()
        self.api.authenticate()

    def download(self, dataset: str, download_dir: str = "download"):
        os.makedirs(download_dir, exist_ok=True)

        print(f"Downloading: {dataset}")
        self.api.dataset_download_files(dataset, path=download_dir)
        print("Downloading completed.")

    def extract(
        self, dataset: str, download_dir: str = "download", extract_to: str = "raw_data"
    ):
        zip_file = dataset.split("/")[-1] + ".zip"
        zip_path = os.path.join(download_dir, zip_file)

        print(f"Extracting to: {zip_path}")
        with ZipFile(zip_path, "r") as zip:
            zip.extractall(extract_to)
        print("Extraction complete.")


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Download and extract Kaggle dataset.")
    parser.add_argument(
        "--dataset",
        type=str,
        required=True,
        help="Kaggle dataset ID (e.g. user/dataset-name)",
    )
    parser.add_argument(
        "--download-dir",
        type=str,
        default="download",
        help="Directory to save the zip file",
    )
    parser.add_argument(
        "--extract-to",
        type=str,
        default="raw_data",
        help="Directory to extract dataset",
    )

    args = parser.parse_args()

    downloader = KaggleDownloader()
    downloader.download(args.dataset, args.download_dir)
    downloader.extract(args.dataset, args.download_dir, args.extract_to)

    # python downloader.py --dataset sujaykapadnis/emotion-recognition-dataset
