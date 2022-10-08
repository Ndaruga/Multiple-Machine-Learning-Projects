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
<br>

#### Download_data.py
This file is responsible for fetching the LFB data and extracting it.
We use patool library to extract the zip archive.

#### LFB-analysis.ipynb
This is the main file where we do everything from analysis to dimentionality reduction to clustering.

## Execution




