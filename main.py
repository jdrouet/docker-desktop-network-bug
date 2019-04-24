import csv
import urllib.request

filename = "image.jpg"
try:
    with open('dataset.csv') as f:
        reader = csv.reader(f)
        for (url,) in reader:
            print(url)
            urllib.request.urlretrieve(url, filename)
except Exception as err:
    print(err)
