from collections import OrderedDict
import os
import csv
import re

from postgres import Postgres

db = Postgres(os.environ.get('DATABASE_URL'))

csv_reader = csv.DictReader(open('./data/ParcelCentroids.csv'))

for index, row in enumerate(csv_reader):
    if re.search('^\d+$', row['PVANUM']):
        db.run("INSERT INTO parcels VALUES (%s, %s, %s, %s)", (row['X'], row['Y'], row['ADDRESS'], row['PVANUM']))
    else:
        print row['PVANUM']
