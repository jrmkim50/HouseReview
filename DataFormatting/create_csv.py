import csv
import pandas as pd

idToRev = {}
with open("reviews1.csv", 'r') as f:
   for line in csv.reader(f):
      if line[0].isnumeric() and len(idToRev) < 190:
         if int(line[0]) in idToRev:
            idToRev[int(line[0])].append(line[5])
         else:
            idToRev[int(line[0])] = [line[5]]
idToLatLong = {}
idToURL = {}
idToNumPeople = {}
idToPrice = {}
with open("listings.csv", 'r') as f:
   for line in csv.reader(f):
      if line[0].isnumeric():
         idToLatLong[int(line[0])] = [float(line[48]), float(line[49])]
         idToURL[int(line[0])] = str(line[1])
         idToNumPeople[int(line[0])] = int(line[53])
         idToPrice[int(line[0])] = float(line[60][1:].replace(',',''))
idToSentiment = {}
with open("IDtoSentiment.csv", "r") as f:
   for line in csv.reader(f):
      if float(line[1]) <= 1:
         idToSentiment[int(line[0])] = float(line[1])
idToDataPrelim = {}
for i in idToSentiment:
   idToDataPrelim[i] = (idToRev[i], idToLatLong[i], idToURL[i], idToNumPeople[i], idToPrice[i], idToSentiment[i])

sep = "[QWERTY123]"
df = pd.DataFrame(columns=["listing_id","reviews","latitude","longitude","url","num_people", "price", "sentiment"])
for i in idToDataPrelim:
   rev, latlong, url, numpeople, price, sentiment = idToDataPrelim[i]
   rev = sep.join(rev)
   lat = latlong[0]
   lng = latlong[1]
   df.loc[len(df)] = [i, rev, lat, lng, url, numpeople, price, sentiment]

df.to_csv("./id_to_data.tsv", sep='\t')



