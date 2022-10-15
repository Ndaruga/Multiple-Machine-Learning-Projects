# The London Fire Brigade
LFB is the largest fire and emergency response team in the United Kingdom. Serving a larger part of London.

Any incident that is reported to this department is recorded and data updated on a public domain once in a fortnight.

### The data.
The <a href = "https://data.london.gov.uk/dataset/london-fire-brigade-incident-records" target = "_blank">LFB dataset</a> is available for public use.

At the time of writing this file, the data contained in a CSV file has a shape of 1048575 rows and 39 columns which is likely to increase in the future as incidences occur on daily basis.

### Folder structure
Below is the folder structure of the London fire brigade project.<br>
![image](https://user-images.githubusercontent.com/68260816/194726990-5335c921-c33c-474c-9c96-e537edad2d63.png)
<br>

#### Download_data.py
This file is responsible for fetching the LFB data from the Uk gov data website, creating a data folder and extracting the zip archive.<br>
We use patool library to extract the zip archive.<br>
We have used a the taqaddum (tqdm for short) library to show download progress.

#### LFB-analysis.ipynb
This is the main file where we do everything from analysis to dimentionality reduction to clustering.

## Execution
In the LFB-analysis.ipynb file, We start by importing the necessary libraries.

We go further to import the download_data.py file. This will help download and extract data.
![image](https://user-images.githubusercontent.com/68260816/194727520-abe2aead-36d7-45ea-b964-c1682f80c271.png)

As shown above the file is imported as a module and downloads the data.


