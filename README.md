# DB---Denghao-Sun---homework-1

## MongoDB Data Migration Sample

A sample program demonstrating how to migrate data from CSV files and associated PDFs into MongoDB. Developed by Denghao Sun.

## Features

- **CSV to MongoDB Migration**:
  - Script: `MongoDB_Migration_CSV.py`
  - Description: Reads data from CSV files and inserts it into a MongoDB instance. It also stores associated PDF files using GridFS.
  
- **Retrieve PDFs from MongoDB**:
  - Script: `getfile.py`
  - Description: Fetches and saves PDFs from MongoDB back to the filesystem.

## Screenshots

### Running the Commands
<img src="MongoDB/Denghao Sun_command.png" alt="Alt text" width="900"/>

### Comparing Result with Original Data
<img src="MongoDB/Denghao Sun_validation.png" alt="Alt text" width="900"/>

## SQLite Data Migration Sample

A sample program demonstrating how to migrate data from CSV files and associated PDFs into SQLite. Developed by Denghao Sun.

## Features

- **CSV to SQLite Migration**:
  - Script: `SQLite_Migration_CSV.py`
  - Description: Reads data from CSV files and inserts it into a SQLite instance. It also stores associated PDF files as BLOBs.
  
- **Retrieve PDFs from SQLite**:
  - Script: `getfile.py`
  - Description: Fetches and saves PDFs from SQLite back to the filesystem.

## Screenshots

### Running the Commands

<img src="SQLite/Denghao Sun_commands.png" alt="Alt text" width="900"/>

### Comparing Result with Original Data

<img src="SQLite/Denghao Sun_validation.png" alt="Alt text" width="900"/>
