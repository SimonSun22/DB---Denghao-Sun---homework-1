# Author: Denghao Sun
# UID: N14485339
# NetID: ds6963

import sqlite3

def save_pdf_to_file(candidate_id, filename):
    conn = sqlite3.connect('candidates.db')
    cursor = conn.cursor()
    cursor.execute("SELECT Resume FROM candidates WHERE CandidateID=?", (candidate_id,))
    pdf_data = cursor.fetchone()[0]
    
    with open(filename, 'wb') as f:
        f.write(pdf_data)

    conn.close()


save_pdf_to_file(1, 'Denghao Sun_retrieved_resume1.pdf')
save_pdf_to_file(2, 'Denghao Sun_retrieved_resume2.pdf')
