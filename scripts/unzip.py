import os
from pathlib import Path
from concurrent.futures import ThreadPoolExecutor

BASE_PATH = Path(__file__).parent.parent
INPUT_FOLDER = BASE_PATH / "input"
ZIPS_FOLDER = INPUT_FOLDER / "zips"

def unzip_file(file_path):
    folder_name = zip_file.replace('.zip', '')
    os.system(
        f"unzip {file_path} "
        f"-d {Path(INPUT_FOLDER, folder_name)}"
    )

if __name__ == '__main__':
    with ThreadPoolExecutor() as executor:
        for zip_file in os.listdir(ZIPS_FOLDER):
            file_path = Path(ZIPS_FOLDER, zip_file)
            unzip_file(file_path)
