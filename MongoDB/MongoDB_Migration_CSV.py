# Author: Denghao Sun

import pandas as pd
from pymongo import MongoClient
import gridfs

def store_pdf_in_gridfs(filename):
    with open(filename, 'rb') as pdf_file:
        pdf_store_id = fs.put(pdf_file, filename=filename)
    return pdf_store_id

client = MongoClient('mongodb://localhost:27017/')
db = client['candidates']
experiments_collection = db['candidates_pool']

fs = gridfs.GridFS(db)

data_df = pd.read_csv('SampleCandidatesPool.csv')

# Inserting CSV data and associated PDF links to MongoDB
for index, row in data_df.iterrows():
    pdf_filename = row['Resume_Link']
    pdf_id = store_pdf_in_gridfs(pdf_filename)
    experiment_data = {
        "CandidateID": row["CandidateID"],
        "Name": row["Name"],
        "PDF_GridFS_ID": pdf_id
    }
    experiments_collection.insert_one(experiment_data)

print("Files saved!")
