# Author: Denghao Sun
# UID: N14485339
# NetID: ds6963

# This is a test script to check if the files are stored properly in the database

from pymongo import MongoClient
import gridfs

# This function reads the corresponding file
# and write a new file with the retrieved one
def retrieve_pdf_from_gridfs(pdf_id, filename):
    pdf_data = fs.get(pdf_id).read()
    with open(filename, "wb") as pdf_file:
        pdf_file.write(pdf_data)

client = MongoClient('mongodb://localhost:27017/')
db = client['candidates']

fs = gridfs.GridFS(db)

candidates = db['candidates_pool'].find()

for candidate in candidates:
    pdf_id = candidate["PDF_GridFS_ID"]
    output_filename = "retrieved_" + candidate["Name"] + ".pdf"
    retrieve_pdf_from_gridfs(pdf_id, output_filename)
    print(f"PDF for Candidate {candidate['CandidateID']} saved as {output_filename}")
