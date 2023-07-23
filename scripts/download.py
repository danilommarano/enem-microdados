import os
import requests
from bs4 import BeautifulSoup
from pathlib import Path
from concurrent.futures import ThreadPoolExecutor

BASE_PATH = Path(__file__).parent.parent

def download_zip_file(url, folder):
    try:
        os.system(
            "wget "
            f"-P {Path(BASE_PATH, folder)} "
            "--no-check-certificate "
            f"{url} "
        )
    except Exception as e:
        print(f"Error occurred while downloading: {e}")

url = "https://www.gov.br/inep/pt-br/acesso-a-informacao/dados-abertos/microdados/enem"

response = requests.get(url)

if response.status_code == 200:
    soup = BeautifulSoup(response.content, "html.parser")
    links = soup.find_all("a", class_="external-link")
    zips = [link.get("href") for link in links]

    with ThreadPoolExecutor() as executor:
        for zip_url in zips:
            executor.submit(download_zip_file, zip_url, folder='input/zips')

