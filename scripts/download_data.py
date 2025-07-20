from kaggle.api.kaggle_api_extended import KaggleApi
import os
import zipfile

def download_titanic():
    try:
        print("Starting Kaggle API...")
        api = KaggleApi()
        api.authenticate()
        print("Authentication successful!")

        print("Downloading Titanic dataset...")
        # Download the zip file to data/raw/titanic.zip
        zip_path = 'data/raw/titanic.zip'
        api.competition_download_files('titanic', path='data/raw', force=True)

        # Find the downloaded zip file (the API downloads with .zip extension)
        # It may download as 'titanic.zip' or with original competition file names zipped.

        # Unzip all zip files in data/raw
        for file in os.listdir('data/raw'):
            if file.endswith('.zip'):
                file_path = os.path.join('data/raw', file)
                print(f"Unzipping {file_path} ...")
                with zipfile.ZipFile(file_path, 'r') as zip_ref:
                    zip_ref.extractall('data/raw')
                print(f"Removing zip file {file_path} ...")
                os.remove(file_path)

        files = os.listdir('data/raw')
        print("Files in data/raw after download and unzip:", files)
        print("Download complete.")

    except Exception as e:
        print("Error during download:", e)

if __name__ == "__main__":
    download_titanic()
