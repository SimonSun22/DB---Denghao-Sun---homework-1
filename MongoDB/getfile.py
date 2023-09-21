# Author: Denghao Sun

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
db = client['lab_experiments']

fs = gridfs.GridFS(db)

experiments = db['experiments'].find()

for experiment in experiments:
    pdf_id = experiment["PDF_GridFS_ID"]
    output_filename = "retrieved_" + experiment["Description"].replace(" ", "_") + ".pdf"
    retrieve_pdf_from_gridfs(pdf_id, output_filename)
    print(f"PDF for Experiment {experiment['ExperimentID']} saved as {output_filename}")
