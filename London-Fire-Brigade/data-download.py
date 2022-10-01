# This file will download the latest version of the London Fire Brigade data

# we will import it into the main working file

import requests
#pip install patool
import patoolib
import os

data_dir = "LFB-data"

URL = "https://data.london.gov.uk/download/london-fire-brigade-incident-records/73728cf4-b70e-48e2-9b97-4e4341a2110d/LFB%20Incident%20data%20-%20Datastore%20-%20with%20notional%20cost%20and%20UPRN%20from%20January%202009%20%282%29.zip"

os.chdir(data_dir)
if (os.path.isdir("archive.zip")) == False:
    data = requests.get(URL, allow_redirects=True)
    open("archive.zip", "wb").write(data.content)
    print("Download Complete\n\nExtracting ...")

# Extract the zip file

    patoolib.extract_archive('archive.zip')
    print("\nExtract complete")
else:
    print("\nFiles Already Extracted")
