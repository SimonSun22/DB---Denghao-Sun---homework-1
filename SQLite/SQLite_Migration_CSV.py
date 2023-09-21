# Author: Denghao Sun
# UID: N14485339
# NetID: ds6963

import sqlite3
import csv

# This returns in byte format
def insert_pdf_to_db(filepath):
    with open(filepath, 'rb') as f:
        return f.read()

conn = sqlite3.connect('candidates.db')
cursor = conn.cursor()

cursor.execute('''CREATE TABLE IF NOT EXISTS candidates 
                  (CandidateID INTEGER PRIMARY KEY, Name TEXT, Resume BLOB)''')

with open('Denghao Sun_SampleCandidatesPool.csv', 'r') as f:
    reader = csv.reader(f)
    next(reader)
    for row in reader:
        pdf_data = insert_pdf_to_db(row[2])
        cursor.execute("INSERT INTO candidates VALUES (?, ?, ?)", (int(row[0]), row[1], pdf_data))

conn.commit()
conn.close()

print('Migration Good!')
