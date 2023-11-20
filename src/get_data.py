# import os
# import wget

# # data from https://www.sciencedirect.com/science/article/pii/S2352340920303048

# # Download the zipped dataset
# url = 'https://md-datasets-cache-zipfiles-prod.s3.eu-west-1.amazonaws.com/yshdbyj6zy-1.zip'
# zip_name = "data.zip"
# wget.download(url, zip_name)

# # Unzip it and standardize the .csv filename
# import zipfile
# with zipfile.ZipFile(zip_name,"r") as zip_ref:
#     zip_ref.filelist[0].filename = 'data_raw.csv'
#     zip_ref.extract(zip_ref.filelist[0])

# os.remove(zip_name)
import requests
import logging
import os
import time

# Set up logging configuration
logging.basicConfig(level=logging.DEBUG,
                    format='%(asctime)s - %(levelname)s - %(message)s')

# Create a file handler
file_handler = logging.FileHandler('download_log.log')
file_handler.setLevel(logging.DEBUG)
file_handler.setFormatter(logging.Formatter('%(asctime)s - %(levelname)s - %(message)s'))

# Create a console handler
console_handler = logging.StreamHandler()
console_handler.setLevel(logging.INFO)
console_handler.setFormatter(logging.Formatter('%(levelname)s - %(message)s'))

# Add handlers to the logger
logger = logging.getLogger('')
logger.addHandler(file_handler)
logger.addHandler(console_handler)

url = 'https://www.research-collection.ethz.ch/bitstream/handle/20.500.11850/383116/rawdata_new.csv?sequence=1&isAllowed=y'
folder_path = 'data/raw'
file_name = 'data_raw.csv'

# Create the folder if it doesn't exist
os.makedirs(folder_path, exist_ok=True)
file_path = os.path.join(folder_path, file_name)

try:
    response = requests.get(url)
    if response.status_code == 200:
        with open(file_path, 'wb') as file:
            file.write(response.content)
        logger.info(f"Data downloaded successfully and saved as '{file_path}'")
        print(f"Data downloaded successfully and saved as '{file_path}'")
    else:
        logger.error(f"Failed to download data. Status code: {response.status_code}")
        print(f"Failed to download data. Status code: {response.status_code}")

    # Add a delay before making the next request
    time.sleep(5)  # Sleep for 5 seconds (adjust the duration as needed)
except requests.RequestException as e:
    logger.exception(f"Error downloading data: {e}")
    print(f"Error downloading data: {e}")
