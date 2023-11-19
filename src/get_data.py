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


import os
import requests

url = 'https://www.research-collection.ethz.ch/bitstream/handle/20.500.11850/383116/rawdata_new.csv?sequence=1&isAllowed=y'
folder_path = 'data/raw'  # Folder path where you want to save the data
file_name = 'data_raw.csv'  # Choose a name for the file where you want to save the data

# Create the folder if it doesn't exist
os.makedirs(folder_path, exist_ok=True)

file_path = os.path.join(folder_path, file_name)

try:
    response = requests.get(url)
    if response.status_code == 200:
        with open(file_path, 'wb') as file:
            file.write(response.content)
        print(f"Data downloaded successfully and saved as '{file_path}'")
    else:
        print(f"Failed to download data. Status code: {response.status_code}")
except requests.RequestException as e:
    print(f"Error downloading data: {e}")
