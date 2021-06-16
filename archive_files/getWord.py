import csv
import pathlib
import os
import pandas as pd
import numpy as np
from io import StringIO

pd.set_option('display.max_rows', None)
pd.set_option('display.max_columns', None)
pd.set_option('display.max_colwidth', None)

words = []
with open('wordUmkb.csv', 'r') as f:
    load_file = csv.reader(f)
    for row in load_file:
        words.append(row[0].replace(';', ' ').split()[0])

with open('wordsUmkb.csv', mode='w', encoding='utf-8') as file:
    file_writer = csv.writer(file, delimiter=',')
    file_writer.writerow(words)