# This file will download the latest version of the London Fire Brigade data

# we will import it into the main working file as a library

import requests
#pip install patool
import patoolib
import os
import glob
from tqdm import tqdm


def download_data(URL, filename):
    data = requests.get(URL, stream = True)
    total_length = int(data.headers["Content-Length"])
    pbar = tqdm(iterable= None, unit = 'B', unit_scale = True, unit_divisor=1024,
                    total= total_length, colour = 'Blue')
    chunk_size = 1024
    
    if total_length != 0:
        with open(filename , 'wb') as f:
        #pbar.clear()
            for chunk in data.iter_content(chunk_size):
                pbar.update(len(chunk))
                f.write(chunk)
    else:
        print("ERROR: Something went wrong with your download")
    pbar.close()
        
    return filename

data_dir = "LFB-data"

URL = "https://data.london.gov.uk/download/london-fire-brigade-incident-records/f5066d66-c7a3-415f-9629-026fbda61822/LFB%20Incident%20data%20Last%203%20years%20-%20with%20num%20calls.xlsx"
#URL = "https://data.london.gov.uk/download/london-fire-brigade-incident-records/73728cf4-b70e-48e2-9b97-4e4341a2110d/LFB%20Incident%20data%20-%20Datastore%20-%20with%20notional%20cost%20and%20UPRN%20from%20January%202009%20%282%29.zip"


if os.path.exists(data_dir) == False:
    os.mkdir(data_dir)
else:
    pass

os.chdir(data_dir)

# Remove files in the directory
my_files = glob.glob(data_dir)
for files in my_files:
    os.remove(files)

# Download files
print('Starting download ...')
download_data(URL, "lfb-incidents-for-last-3-years.xlsx")
print("\n")
'''
else:
    print('Starting download ...')
    download_data(URL, "archive.zip")    
    print("\n")
    patoolib.extract_archive('archive.zip')
    print("\nExtract complete")

'''
